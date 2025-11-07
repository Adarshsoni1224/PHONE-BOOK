contacts = []
next_choice=0
def add_contact():
        name = input("Enter the name: ")
        email = input("Enter the email id: ")
        number = input("Enter the number: ")
        contact = [name, email, number] 
        contacts.append(contact) 
        print("Contact added successfully!")
        print(contacts)
        show_contacts(contact)
def show_contacts (x):
    print("name:",x[0])
    print("email:",x[1])
    print("number:",x[2])
def show_all_contacts():
    for i in contacts:
        show_contacts(i)
def search_contact(x):
     name = input("Enter name to search: ")
     for i in contacts:
            if name in i :
                show_contacts(i) 
               break
     else:
          print("Contact not found.")
def update_contact():

    print("Update Contact function not yet implemented.")

def delete_contact():
    print("Delete Contact function not yet implemented.")

# Main menu loop
while True:
    print("\n--- Phone Book Menu ---")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Show_all_Contacts")
    print("4. Update Contact Number")
    print("5. Delete Contact")
    next_choice=True
    choice = input("Enter your choice (1 to 5): ")
    if choice == '1':
        add_contact()
    elif choice == '2':
        search_contact()
    elif choice=="3":
        show_all_contacts()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
        break
    else:
        print("Invalid choice. Please try again.")

    next_choice=input("Enter Y to add other item or n key to stop")
    if next_choice=="Y"or next_choice=="Y":
        next_choice==True
    else:
        next_choice==False
    