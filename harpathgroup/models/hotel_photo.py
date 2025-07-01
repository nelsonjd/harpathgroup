class HotelPhoto:
    def __init__(self, args={}):
        self.width_t = args.get('width_t', '')
        self.height_t = args.get('height_t', '')
        self.src_t = args.get('src_t', '')
        self.width = args.get('width', '')
        self.height = args.get('height', '')
        self.src = args.get('src', '')