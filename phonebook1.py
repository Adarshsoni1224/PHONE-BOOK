print("WELCOME TO MY PHONEBOOK")
Master_list=[["Bhoomika","bhumi@gmail.com","3243223546445"],["Adarsh","soniji@gmail.com","3124325635787866"],["Rajvi","ajmeraji@gmail.com","074353645636"]]
def add_contact():
    name= input("enter contact name:")
    email= input("enter contact email:")
    phone= input("enter contact phone:")
    entry=[name,email,phone]
    Master_list.append(entry)
    print("contact added successfully!")
    print(Master_list)
    show_contact(entry)

def show_contact(x):
    print("====================")
    print("name:",x[0])
    print("email:",x[1])
    print("contact:",x[2])
    print("====================")

def search_contact():
    search_term = input("Enter Search Term : ")
    for i in Master_list :
        if search_term  in i : 
            show_contact(i)
            break
    else : 
        print("Contact Not found")

def show_all_contact():
    for i in Master_list:
        show_contact(i)


def update_contact() :
    search_term = input("Enter Search Term : ")
    current_contact = None
    for i in Master_list :
        if search_term  in i : 
            print("Current Contact")
            show_contact(i)
            current_contact = i
            break
    else : 
        print("Contact Not found") 

    change_item = input("Enter 1 to Change Name\nEnter 2 to Change Email\nEnter 3 to change Contact Number\nEnter a valid Choice : ")
    change_value = input("Enter value to be updated : ")

    if  change_item == "1" :
        current_contact[0] = change_value   
    elif change_item == "2" :
        current_contact[1] = change_value
    elif change_item == "3" :
        current_contact[2] = change_value

    print("Updated Contact")
    show_contact(current_contact)

def delete_contact():
    search_term=input("Enter to delete contact :")
    for i in Master_list :
        if search_term in i:
            Master_list.remove(i)
            print("successfully deleted contact:")
choice2 = True
while choice2 :
    choice=int(input("press 1 for add contact\npress 2 for search contact\npress 3 for show contact\npress 4 for update contact\npress 5 for delete contact\nenter a valid choice:"))
    if choice == 1:
        add_contact()
    elif choice == 2:
        search_contact()
    elif choice == 3:
        show_all_contact()
    elif choice == 4:
        update_contact()
    elif choice == 5:
        delete_contact()
    else:
        print("Invalid Choice")

    next_choice = input("Enter y to continue and n to stop : ")
    if next_choice == "n"or next_choice == "N":
        choice2 = False