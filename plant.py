class Plant:
    def __init__(self, current_state, maximum_state):
        self.current_state = current_state
        self.maximum_state = maximum_state
    def get_current_state(self):
        return self.current_state
    def set_current_state(self, current_state):
        self.current_state = current_state
    def get_maximum_state(self):
        return self.maximum_state
    def set_maximum_state(self, maximum_state):
        self.maximum_state = maximum_state