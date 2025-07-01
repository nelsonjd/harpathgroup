class Location:
    def __init__(self, args={}):
        self.id = args['id']
        self.identifier = args['identifier']
        self.city = args['city']
        self.description = args['description']
        self.region = args['region']

    @staticmethod
    def all_regions():
        return [
            ('abruzzo', 'Abruzzo'),
            ('basilicata', 'Basilicata'),
            ('calabria', 'Calabria'),
            ('campania', 'Campania'),
            ('emilia-romagna', 'Emilia-Romagna'),
            ('friuli-venezia-giulia', 'Friuli-Venezia Giulia'),
            ('lazio', 'Lazio'),
            ('liguria', 'Liguria'),
            ('lombardia', 'Lombardia'),
            ('marche', 'Marche'),
            ('molise', 'Molise'),
            ('piemonte', 'Piemonte'),
            ('puglia', 'Puglia'),
            ('sardegna', 'Sardegna'),
            ('sicilia', 'Sicilia'),
            ('trentino-alto-adige', 'Trentino-Alto Adige'),
            ('toscana', 'Toscana'),
            ('umbria', 'Umbria'),
            ('veneto', 'Veneto'),
            ("valle-d-aosta", "Valle d'Aosta"),
        ]