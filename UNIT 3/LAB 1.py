contacts = []

while True:
    print("\n--- CONTACT BOOK ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Update Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")

        contact = {
            "name": name,
            "phone": phone,
            "email": email
        }

        contacts.append(contact)
        print("Contact added successfully.")

    elif choice == "2":
        if len(contacts) == 0:
            print("No contacts available.")
        else:
            print("\n--- ALL CONTACTS ---")
            for contact in contacts:
                print("Name:", contact["name"])
                print("Phone:", contact["phone"])
                print("Email:", contact["email"])
                print("-------------------")

    elif choice == "3":
        search_name = input("Enter name to search: ")
        found = False

        for contact in contacts:
            if contact["name"].lower() == search_name.lower():
                print("\nContact Found")
                print("Name:", contact["name"])
                print("Phone:", contact["phone"])
                print("Email:", contact["email"])
                found = True
                break

        if not found:
            print("Contact not found.")

    elif choice == "4":
        delete_name = input("Enter name to delete: ")
        found = False

        for contact in contacts:
            if contact["name"].lower() == delete_name.lower():
                contacts.remove(contact)
                print("Contact deleted successfully.")
                found = True
                break

        if not found:
            print("Contact not found.")

    elif choice == "5":
        update_name = input("Enter name of contact to update: ")
        found = False

        for contact in contacts:
            if contact["name"].lower() == update_name.lower():
                print("\n--- UPDATE CONTACT ---")
                new_name = input(
                    "Enter new name (press Enter to keep old name): "
                )
                new_phone = input(
                    "Enter new phone number (press Enter to keep old number): "
                )
                new_email = input(
                    "Enter new email (press Enter to keep old email): "
                )

                if new_name != "":
                    contact["name"] = new_name
                if new_phone != "":
                    contact["phone"] = new_phone
                if new_email != "":
                    contact["email"] = new_email

                print("Contact updated successfully.")
                found = True
                break

        if not found:
            print("Contact not found.")

    elif choice == "6":
        print("Exiting Contact Book...")
        break

    else:
        print("Invalid choice.")