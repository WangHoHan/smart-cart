class Fringe: #kolejka zawierająca akcje oraz pola do odwiedzenia
    def __init__(self, fringe):
        self.fringe = fringe
    def get_fringe(self):
        return self.fringe
    def set_fringe(self, fringe):
        self.fringe = fringe