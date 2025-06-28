class Hotel:
    def __init__(self, args={}):
        self.hotel_photos = []
        self.id = args['id']
        self.name = args['name']
        self.description = args['description']
        self.perks = args['perks']
        self.affiliate_link = args['affiliate_link']

    