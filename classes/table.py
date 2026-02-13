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

class Table:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.seats = [Seat() for _ in range(capacity)]
        
    def has_free_spot(self):
        for seat in self.seats:
            if seat.free:
                return True
        return False
    
    def assign_seat(self, name):
        for seat in self.seats:
            if seat.free:
                seat.set_occupant(name)
                return True
        return False
    
    def left_capacity (self):
        count = 0
        for seat in self.seats:
            if seat.free:
                count += 1
        return count
    

