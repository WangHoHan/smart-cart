class Plant:
    def __init__(self, name, state):
        self.name = name
        self.state = state
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_state(self):
        return self.state
    def set_state(self, state):
        self.state = state