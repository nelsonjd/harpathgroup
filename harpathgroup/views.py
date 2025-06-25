from flask import Flask, render_template
from . import app
from .db_runner import query_db
from .models.hotel import Hotel
from .models.hotel_photo import HotelPhoto
from .models.location import Location

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/locations")
def locations():
    return render_template(
        "locations.html",
    )

@app.route("/locations/")
@app.route("/locations/<identifier>")
def locations_show(identifier=None):
    location_row = query_db("""
        SELECT * from locations
        WHERE identifier = ?
    """, [identifier], True)

    if location_row is None: 
        return 'No location has this identifier.'

    location = Location({
        'id': location_row['id'],
        'city': location_row['city'],
        'description': location_row['description'],
        'identifier': location_row['identifier']
    })
    
    rows = query_db("""
        SELECT * from hotels
            INNER JOIN hotel_photos hp on hotels.id = hp.hotel_id
        WHERE location_id = ?
        ORDER by hotel_id ASC;
    """, [location.id])

    if rows is None: 
        return 'No hotels are available at this location.'
    
    hotels = {}

    for row in rows:
        hotel_id = row['hotel_id']
        hotel = hotels.get(hotel_id)
        if hotel is None:
            hotel = Hotel({'id': row['hotel_id'], 
                        'name': row['name'], 
                        'description': row['description'], 
                        'perks': row['perks']
            })
        hotel.hotel_photos.append(
            HotelPhoto({
                'width_t': row['width_t'],
                'height_t': row['height_t'],
                'src_t': row['src_t'],
                'width': row['width'],
                'height': row['height'],
                'src': row['src'],
            })
        )
        hotels[hotel_id] = hotel
    
    return render_template(
        "locations_show.html",
        hotels=hotels,
        location=location
    )
