import random

def fortuneteller():
    Q1 = input("Lucky number\n> ")
    Q2 = input("How many years into the future would you like to see?\n> ")
    Q3 = input("What is the Mystical Multiplier you would like?\n> ")
    Q4 = input("What is the amount of time you spend oh your phone per week\n> ")
    Q5 = input("Another funny number for fun\n> ")
    try:
        a = int(Q1) + int(Q2) * int(Q3) / int(Q4) ** int(Q5)
        random.seed(a)
        fortune = ["You die",  #1
                "Free Money",  #2
                "World domination",  #3
                "No more fortnite",  #4
                "sigma skibidi", "HAHA",  #5
                "LOL",  #6
                "#RUNNING OUT OF IDEAS!!!",  #7
                "Fortune 8 hehe",  #8
                "Fortune 8 but like 1 higher",  #9
                "Fortune 67 haha funni :3"  #10
                                            ]
        print(random.choice(fortune))
    except:
        print("Uh Oh! should have used only integers!")
        fortuneteller()
    


fortuneteller()



