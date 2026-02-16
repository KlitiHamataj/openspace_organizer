from classes.openspace import Openspace
from utils.file_loader import load_colleagues

def main():
    print("\nLoading colleagues from Excel file...")
    colleagues = load_colleagues()
    print(f"\nLoaded {len(colleagues)} colleagues")
    
    number_of_tables = 6
    seats_per_table = 4
    
    #  Create the openspace
    print(f"\nCreating openspace with {number_of_tables} tables, {seats_per_table} seats each...")
    openspace = Openspace(number_of_tables, seats_per_table)
    print(f"\nTotal capacity: {openspace.total_capacity()} seats")
    
    
    # Organize colleagues into tables
    print(f"\nOrganizing {len(colleagues)} colleagues...")
    success = openspace.organize(colleagues)
    
    
    # Display the results
    if success:
        print("\nSEATING ARRANGEMENT")
        openspace.display()
    else:
        print("\nFailed to organize colleagues. Please add more tables.")
        

if __name__ == "__main__":
    main()
    