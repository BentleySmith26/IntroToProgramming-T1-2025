def sigmapassword():
    password = input("Password:\n> ")
    pin = input("Pin:\n> ")
    if password == "Ueidj934Jie9" and pin == "1231":
        print("Access Granted") 
        Q1 = input("What is your favorite food?\n> ")

        if Q1 == "pineapple pizza":
            print("Security answer correct!")
            Q2 = input("What is your dog's nickname?\n> ")
            if Q2 == "goose":
               print("Welcome to the computer")
            else:
              print("Access Denied")
              sigmapassword()
        else:
            print("Access Denied")
            sigmapassword()
    else:
        print("Access Denied")
        sigmapassword()

sigmapassword()
   

