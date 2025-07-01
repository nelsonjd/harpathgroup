class Location:
    def __init__(self, args={}):
        self.id = args.get('id')
        self.identifier = args.get('identifier', '')
        self.city = args.get('city', '')
        self.description = args.get('description', '')
        self.region = args.get('region', '')

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