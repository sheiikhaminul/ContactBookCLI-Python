from contacts import load_contacts, save_contacts
from add import add_contact
from view import view_contacts
from delete import delete_contact
from search import search_contacts

def menu():
    contacts = load_contacts()
    while True:
        print("\n--- Contact Book Management System ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Delete Contact")
        print("4. Search Contacts")
        print("5. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            delete_contact(contacts)
        elif choice == '4':
            search_contacts(contacts)
        elif choice == '5':
            save_contacts(contacts)
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    menu()
