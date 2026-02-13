from classes.openspace import Openspace
from utils.file_loader import load_colleagues

def main():
    print("Loading colleagues from Excel file...")
    colleagues = load_colleagues()
    print(f"Loaded {len(colleagues)} colleagues")
    
    number_of_tables = 6
    seats_per_table = 4
    
    #  Create the openspace
    print(f"\nCreating openspace with {number_of_tables} tables, {seats_per_table} seats each...")
    openspace = Openspace(number_of_tables, seats_per_table)
    print(f"Total capacity: {openspace.total_capacity()} seats")
    
    # Organize colleagues into tables
    print(f"\nOrganizing {len(colleagues)} colleagues...")
    success = openspace.organize(colleagues)
    
    # Display the results
    if success:
        print("SEATING ARRANGEMENT")
        openspace.display()
    else:
        print("\nFailed to organize colleagues. Please add more tables.")
        
def test_features():
    print("TESTING ADD_TABLE AND ADD_COLLEAGUE")
    
    # Setup: Create small openspace
    print("\n1. Creating openspace with 2 tables, 3 seats each...")
    openspace = Openspace(2, 3)
    print(f"   Initial tables: {openspace.number_of_tables}")
    print(f"   Initial capacity: {openspace.total_capacity()}")
    openspace.display()
    
    # Test add_table
    print("\n2. Testing add_table()...")
    print("   Adding a table with 4 seats...")
    openspace.add_table(4)
    print(f"   Tables after adding: {openspace.number_of_tables}")
    print(f"   Capacity after adding: {openspace.total_capacity()}")
    openspace.display()
    
    # Organize initial colleagues
    print("\n3. Organizing initial colleagues...")
    test_colleagues = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']
    openspace.organize(test_colleagues)
    print(f"   Organized {len(test_colleagues)} colleagues")
    openspace.display()

if __name__ == "__main__":
    main()       
