from classes.seat import Seat

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
    
tables = [Table(4) for _ in range(6)]