import json

class Hotel:
    def __init__(self, args={}):
        self.hotel_photos = []
        self.id = args.get('id')
        self.location_id = args.get('location_id')
        self.name = args.get('name', '')
        self.description = args.get('description', '')
        self.perks = args.get('perks', '')
        self.affiliate_link = args.get('affiliate_link', '')
        self.identifier = args.get('identifier', '')


    def photos_to_JSON(self):
        return json.dumps(
            self.hotel_photos,
            default=lambda o: o.__dict__,
            indent=4
        )