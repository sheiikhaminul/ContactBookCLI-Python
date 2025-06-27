def add_contact(contacts):
    try:
        name = input("Enter Name: ").strip()
        email = input("Enter Email: ").strip()
        phone = input("Enter Phone Number: ").strip()
        if not phone.isdigit():
            raise ValueError("The phone number must be an integer.")
        address = input("Enter Address: ").strip()

        for contact in contacts:
            if contact['phone'] == phone:
                print("This phone number is already assigned to a contact.")
                return

        contact = {'name': name, 'email': email, 'phone': phone, 'address': address}
        contacts.append(contact)
        print("Contact added successfully!")
    except ValueError as e:
        print("Error:", e)
