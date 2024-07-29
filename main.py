from GeneratePassword import GeneratePassword
from AdminData import AdminData
gp = GeneratePassword()
db = AdminData()
    
def Menu():
    print("\n\n------------ Select oprion ------------")
    print("- [1] Add password")
    print("- [2] Search Password")
    print("- [3] List passwords")
    print("- [4] Update name")
    print("- [5] Delete password")
    
    option = int(input("Enter option: "))
     
    print("\n")
     
    if option == 1:
        name = input("Enter name's password: ")
        letgth = int(input("Enter password's legth: "))
        
        if letgth != 0:
            password = gp.CustomLegth(letgth)
            db.addPassword(password, name)
 
    elif option == 2:
        path = input("Enter password name: ")
        ps = db.Read(path)
        print(f"- {ps}")
             
    elif option == 3:
        db.readAll()
        
    elif option == 4:
        path = input("Enter password name: ")
        new_password = int(input("Enter new password's legth: "))
        
        if new_password != 0:
            new_password = gp.CustomLegth(new_password)
        
        db.update(path, new_password)
        print("Update sucessful")
        
    elif option == 5:
        path = input("Enter password name: ")
        db.delete(path)
        print("Delete sucessful")
        
while True:
    try:      
        Menu()
    except KeyboardInterrupt:
        print("\n\n------------ Goodbye ------------")
        break