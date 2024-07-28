from GeneratePassword import GeneratePassword
gp = GeneratePassword()

while True:
    letgth = int(input("Enter password's legth: "))
    
    if letgth != 0:
        password = gp.CustomLegth(letgth)
        
        print(password)
    else:
        break

