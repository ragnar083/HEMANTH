# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XkRPa8lY1xN0PpU93LOoeHvsjDFTTjqF
"""

#INITIALIZING AN EMPTY DICTIONARY
contact = {}
#DEFINING A FUCTION TO DISPLAY CONTACTS
def display_contact():
    name = input("Enter the name of the contact you want to display: ")
    if name in contact:
        contact_info = contact[name]
        print("Contact Information:")
        print(f"Name: {name}")
        print(f"Email: {contact_info['email']}")
        print(f"Phone: {contact_info['phone']}")
    else:
        print(f"{name} not found in the contact list.")
#INTERACTING WITH THE USER
while True:
  choice = int(input("1.Add new contact\n 2.Search contact\n 3.Display contact\n 4.Edit contact\n 5.Delete contact\n 6.Exit\n ENTER YOUR CHOICE "))
  if choice==1: #ADDING CONTACTS
       name = input("Enter the name of the contact: ")
       email = input("Enter the email address: ")
       phone = input("Enter the phone number: ")
       contact[name] = {'email': email, 'phone': phone}
       print(f"Contact for {name} added successfully.")

  elif choice ==2: #SEARCH CONTACT
      search_name = input("enter the contact name")
      if search_name in contact:
        print(search_name,"1.Person's contact number is\n 2.Person's email id is ",contact[search_name])
      else:
          print("NAME IS NOT FOUND IN THE CONTACT BOOK")
  elif choice==3:#DISPLAY CONTACT
            if not contact:
              print ("empty contact book")
            else:
                display_contact()
  elif choice==4:# EDIT CONTACT
                  edit_contact = input("Enter the contact to be edited ")
                  if edit_contact in contact:
                    phone = input("enter the mobile number ")
                    email = input("enter email id ")
                    contact[edit_contact]=phone
                    contact[edit_contact]=email
                    print ("Contact updated")
                    display_contact()
                  else :
                      print("Name is not found on the contact book")
  elif choice ==5:#DELETING CONTACT
                        del_contact =input("Enter the contact to be deleted")
                        if del_contact in contact:
                          confirm = input("Do you want to delete this contact")
                        if confirm=="y" or confirm== "Y":
                          contact.pop(del_contact)
                          display_contact()
                        else:
                            print("Name is not found in the contact book")
#TO EXIT THE PROGRAM.
  else:
    break