from helper import get_valid_input
from management import Management
from rental import Rental
    
def print_intro():
    print("Welcome to the Ada Video Store interface!")

def print_top_menu():
    print("Please choose from the following menu options:")
    print("To manage customers, type 1")
    print("To manage videos, type 2")
    print("To manage rentals, type 3")
    print("To quit, type 4")

MANAGE_CUSTOMERS = 1
MANAGE_VIDEOS = 2
MANAGE_RENTALS = 3
QUIT = 4

rental = Rental()
management = Management()

def main():
    while(True):
        print_intro()
        print_top_menu()
        choice = get_valid_input(int, range(1,5))
        if choice == QUIT:
            break
        elif choice == MANAGE_RENTALS:
            rental.menu()
        elif choice == MANAGE_CUSTOMERS or choice == MANAGE_VIDEOS:
            management.menu(choice)

    print("Goodbye!")


if __name__ == "__main__":
    main()