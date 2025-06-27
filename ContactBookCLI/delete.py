def delete_contact(contacts):
    phone = input("Enter the phone number of the contact to delete: ").strip()
    for contact in contacts:
        if contact['phone'] == phone:
            contacts.remove(contact)
            print("Contact deleted successfully!")
            return
    print("Contact not found.")
