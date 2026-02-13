import random
from classes.table import Table

class Openspace:
    def __init__(self, number_of_tables: int, seats_per_table: int):
        self.number_of_tables = number_of_tables
        self.tables = [Table(seats_per_table) for _ in range(number_of_tables)]
        
    def total_capacity(self):
        total = 0
        for table in self.tables:   
            total += table.capacity
        return total    
            
    def organize (self, names):
        
        if len(names) > self.total_capacity():  # check for enough seats
            print(f"Error: Not enough seats! Need {len(names)}, have {self.total_capacity()}")
            return False 
        
        for name in names:
            available_tables = []
            for i, table in enumerate(self.tables):  # list of available tables
                if table.has_free_spot():
                    available_tables.append(i)
            
            if available_tables:
                table_index = random.choice(available_tables)  # pick randomly from tables with free place
                self.tables[table_index].assign_seat(name)
        
        return True
                

    def display(self):   # display tables and their occupants
        for i, table in enumerate(self.tables, 1):
            print(f"\nTable {i} (Capacity: {table.capacity}, Free spots: {table.left_capacity()}):")
            
            occupied_seats = []
            
            for seat in table.seats:
                if not seat.free:
                    occupied_seats.append(seat.occupant)
        
            if occupied_seats:
                for occupant in occupied_seats:
                    print(f"  - {occupant}")
        else:
            print("  (Empty)")
    
        print(f"\nTotal tables: {self.number_of_tables}")
        
    # create method add_person(self, name):
    
    def add_person(self, name):
        #loop through tables
        #if table has free spots
        #assign seat to person  
        # return true
        # else print a message
        # return false
        for table in self.tables:
            if table.has_free_spot():
                table.assign_seat(name)
                return True
        print("We have no more free seats available. consider adding more tables")
        return False
    
    def add_table(self, capacity):
        #create a new table with capacity
        #add it to self.tables list
        #increment by 1 self.number_of_tables
        #print confirmation message with new total capacity
        table = Table(capacity)
        self.tables.append(table)
        self.number_of_tables += 1
        print(f"Added table with capacity {capacity}. Total capacity: {self.total_capacity()}")
    