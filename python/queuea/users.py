import os


# functions
def mainMenu():
    print(":::Main menu:::")
    print("[1] Register a new user")
    print("[2] List all user")
    print("[3] Search user")
    print("[4] Delete user")
    print("[5] Update user")
    print("[6] Show active users")
    print("[7] Show inactive user")
    print("[8] Exit")

   
# Main
while True:
    os.system('clear')
    mainMenu()
    opt= input("Press any option [1-8]: ")
    match opt:
        case '1':
            os.system('clear')
            print(":::Register form:::")
            id= input("Ident.number: ")
            firstname=input("Firstname: ")
            lastname=input("Lastname: ")
            mobile.phone=input("Mobile phone: ")
            email=input("E-mail: ") 
            gender=input("Gender[M/F/O]: ")
            ids.append(id)
            firstnames.appends(firstname)


            statuses.appends(True)

            created_at.append(date.today())
            print ("User has been created successfully !!")
            any_key= input("Press any key to back to Main Meny")
        case '2':
            print(":::List all registered users:::")

#option 3
        case '3':
            os.system('clear')
            
            print("Search User ::: \n")
            id_user= input("Enter identification number to search: ")

            i = 0
            j = 0
            while i< len(ids):
                  if id.user==ids[i]:
                      j+=1
                i+=1
            if j > 0:
                print(f"Ident users: {ids [i]}")
                print(f"Full name: {firstname [i]} {lastname [i]}")
                print(f"Mobile phone: {mobile_phone [i]}")
                # complete here all fields
            else:
                print("Identification number not found")
            
            key = input("Press any key")
            any_Key = input("Press any key")
        case '8':
            print("")

            any_key = input("Press any key")
            break
        case _:
                