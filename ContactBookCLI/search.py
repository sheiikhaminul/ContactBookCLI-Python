def search_contacts(contacts):
    keyword = input("Enter keyword to search (name, email, phone, address): ").lower()
    results = [c for c in contacts if keyword in c['name'].lower() or keyword in c['email'].lower() or keyword in c['phone'] or keyword in c['address'].lower()]
    if results:
        print("\nSearch Results:")
        for contact in results:
            print(f"Name: {contact['name']}, Email: {contact['email']}, Phone: {contact['phone']}, Address: {contact['address']}")
    else:
        print("No matching contacts found.")
