print("WELCOME TO MY PHONEBOOK")
#Adding a contact to phonebook.
def add_contact():
    name= input("Enter contact name:")
    email= input("Enter contact email:")
    phone= input("Enter contact phone:")
    contact_entry="{},{},{}\n".format(name,email,phone)
    file=open("sample2.txt","a")
    file.write(contact_entry)
    file.close()

#Search contact that added.
def search_contact():
    file=open("sample2.txt","r")
    #Master_data=file.read()
    Master_data=file.readlines()
    file.close()
    #print(Master_data)
    #print(type(Master_data))
    search_term = input("Enter Search Term : ")
    for k in Master_data :
        if search_term in k : 
            print(k)
            show_contact(k)
            break  
    else :
        print("Contact Not Found")

#Show all save contact.
def show_contact(x) : 
    #print("Original Term : ",x)
    x = x.replace("\n","")
    #print("Replaced Term : ",x)
    contact_split = x.split(",")
    #print(contact_split)
    print("====================")
    print("Name : ",contact_split[0])
    print("Email : ",contact_split[1])
    print("Phone : ",contact_split[2])
    print("====================")

def show_all_contact():
    file=open("sample2.txt","r")
    Master_data=file.readlines()
    file.close()
    for i in Master_data :
        show_contact(i)

#Update contact.
def update_contact():
    file=open("sample2.txt","r")
    #Master_data=file.read()
    Master_data=file.readlines()
    file.close()
    #print(Master_data)
    #print(type(Master_data))
    search_term = input("Enter Search Term : ")
    for k in Master_data :
        if search_term in k : 
            print(k)
            current_contact = k
            show_contact(k)
            break  
    else :
        print("Contact Not Found")

    print("Current Contact : ",current_contact)
    current_contact2 = current_contact.replace("\n","")
    current_contact_data = current_contact2.split(",")

    print(current_contact_data)

    choice2 = int(input("Enter 1 to change Name\nEnter 2 to change Email\nEnter 3 to change Contact\nEnter a Valid Choice :  "))
    change_term = input("Enter Term : ")
    if choice2 == 1 :
        current_contact_data[0] = change_term
    elif choice2 == 2 :
        current_contact_data[1] = change_term
    elif choice2 == 3 : 
        current_contact_data[2] = change_term
    else :
        print("Invalid Choice")
    print(current_contact_data)
    print(Master_data)

    updated_contact_entry = "{},{},{}\n".format(current_contact_data[0],current_contact_data[1],current_contact_data[2])
    current_index = Master_data.index(current_contact)

    Master_data[current_index] = updated_contact_entry

    print(Master_data)

    file = open("sample2.txt","w")
    for i in Master_data :
        file.write(i)
    file.close()

    print("Contact Updated Successfully")

#Delete contact.
def delete_contact():
    pass

choice=int(input("press 1 for add contact\npress 2 for search contact\npress 3 for show all contact\npress 4 for update contact\npress 5 for delete contact\nenter a valid choice:"))
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