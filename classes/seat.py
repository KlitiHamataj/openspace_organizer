class Seat:
    def __init__(self, free = True, occupant = ""):
        self.free = free
        self.occupant = occupant

    def set_occupant(self, name):
        if self.free:
            self.occupant = name
            self.free = False
            
    def remove_occupant(self):
        previous_occupant = self.occupant
        self.occupant = " "        
        self.free = True
        return previous_occupant