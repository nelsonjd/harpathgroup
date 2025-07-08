import json

class HotelPhoto:
    def __init__(self, args={}):
        self.id = args.get('width', None)
        self.width_t = args.get('width_t', '')
        self.height_t = args.get('height_t', '')
        self.src_t = args.get('src_t', '')
        self.width = args.get('width', '')
        self.height = args.get('height', '')
        self.src = args.get('src', '')


    def toJSON(self):
        return json.dumps(
            self,
            default=lambda o: o.__dict__,
            indent=4
        )