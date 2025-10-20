def hurricane_classifier():
    s = input("Please input the wind speed as an integer:\n> ")
    if 74 > int(s) > 0:
        print("This is a Tropical Storm")
    elif 96 > int(s) > 74:
        print("This is a Category 1 Hurricane")
    elif 111 > int(s) > 96:
        print("This is a Category 2 Hurricane")
    elif 130 > int(s) > 111:
        print("This is a Category 3 Hurricane")
    elif 157 > int(s) > 130:
        print("This is a Category 4 Hurricane")
    elif int(s) >= 157:
        print("This is a Category 5 Hurricane")
    else:
        print("This is not Valid")

hurricane_classifier()






