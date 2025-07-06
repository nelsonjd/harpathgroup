from flask import render_template, request, redirect, url_for, abort
from . import app
from .db_runner import query_db, get_con
from .models.location import Location
from .models.hotel import Hotel
from .models.hotel_photo import HotelPhoto


@app.get("/admin/locations")
def admin_index():
    location_rows = query_db("""
        SELECT * from locations;
    """)

    if location_rows is None: 
        return 'No location has this identifier.'
    
    locations = []

    for row in location_rows:
        location = Location({
            'id': row['id'],
            'city': row['city'],
            'description': row['description'],
            'identifier': row['identifier'],
            'region': row['region']
        })
        locations.append(location)

    return render_template("admin_locations.html", locations=locations)


@app.route("/admin/locations/new")
def admin_locations_new():
    regions = Location.all_regions()

    action_url = '/admin/locations'

    location = Location()
    
    return render_template("admin_locations_form.html", regions=regions, action_url=action_url, location=location)


@app.route('/admin/locations/<id>')
def admin_locations_edit(id=None):
    row = query_db("""
        SELECT * from locations
        WHERE id = ?;
    """, [id], True)

    if row is None:
        return abort(404)

    location = Location(
        {
            "id": row["id"],
            "city": row["city"],
            "description": row["description"],
            "identifier": row["identifier"],
            "region": row['region']
        }
    )

    regions = Location.all_regions()

    action_url = f"/admin/locations/{location.id}"

    return render_template('admin_locations_form.html', location=location, regions=regions, action_url=action_url)


@app.post("/admin/locations")
def admin_locations_create():
    region = request.form['region']
    city = request.form['city']
    identifier = request.form['identifier']
    description = request.form['description']

    if not (region and city and identifier and description):
        return 'please retry, one of the items was blank.'
    
    con = get_con()
    
    con.execute("""
        INSERT into locations (city, description, identifier, region)
        VALUES (?, ?, ?, ?)
    """, [city, description, identifier, region])

    con.commit()
    con.close()

    return redirect(url_for('admin_index'))


@app.post('/admin/locations/<id>')
def admin_locations_update(id=None):
    row = query_db("""
        SELECT * from locations
        WHERE id = ?;
    """, [id], True)


    if (row is None):
        return abort(404)
    
    region = request.form['region']
    city = request.form['city']
    identifier = request.form['identifier']
    description = request.form['description']

    if not (region and city and identifier and description):
        return 'please retry, one of the items was blank.'
    
    con = get_con()
    
    con.execute("""
        UPDATE locations 
        SET city = ?, 
            description = ?, 
            identifier = ?, 
            region = ?
        WHERE id = ?
    """, [city, description, identifier, region, id])

    con.commit()
    con.close()

    return redirect(url_for('admin_index'))


@app.get('/admin/hotels/locations/<id>')
def admin_hotels_index(id=None):
    rows = query_db("""
        SELECT * from hotels
        WHERE location_id = ?
    """, [id])

    if (rows is None):
        return abort(404)

    hotels = []

    for row in rows:
        hotels.append(
            Hotel(
                {
                    "id": row["id"],
                    "name": row["name"],
                    "description": row["description"],
                    "perks": row["perks"],
                    "affiliate_link": row["affiliate_link"],
                    "location_id": row["location_id"],
                }
            )
        )

    location_id = int(id)

    return render_template("admin_hotels.html", hotels=hotels, location_id=location_id)


@app.route("/admin/hotels/new")
def admin_hotels_new():
    action = 'new'

    location_id = int(request.args.get('location_id'))

    hotel = Hotel({ 'location_id': location_id })
    
    return render_template("admin_hotels_form.html", action=action, hotel=hotel)


@app.post("/admin/hotels")
def admin_hotels_create():
    name = request.form['name']
    description = request.form['description']
    perks = request.form['perks']
    location_id = request.form['location_id']
    affiliate_link = request.form['affiliate_link']
    
    con = get_con()
    cur = con.cursor()
    
    cur.execute("""
        INSERT into hotels (name, description, perks, location_id, affiliate_link)
        VALUES (?, ?, ?, ?, ?)
    """, [name, description, perks, location_id, affiliate_link])

    con.commit()

    hotel_id = cur.lastrowid

    index = 0
    keys = ['src_t', 'width_t', 'height_t', 'src', 'width', 'height']
    while (all(key in request.form for key in transfomed_keys(keys, index))):
        cur.execute("""
            INSERT into hotel_photos (src_t, width_t, height_t, src, width, height, hotel_id)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, [request.form[key] for key in transfomed_keys(keys, index)] + [hotel_id])

        con.commit()

        index += 1

    return redirect(url_for('admin_hotels_index', id=location_id))


def transfomed_keys(keys, index):
    return [(key + '_' + str(index)) for key in keys]
