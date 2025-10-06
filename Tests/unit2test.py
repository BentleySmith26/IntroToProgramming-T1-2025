#1 (15 points)

word_1 = input("Please submit your first word:\n> ")
word_2 = input("Please submit your second word:\n> ")
word_3 = input("Please sumbit your thrid word:\n> ")

print(word_1 + " " + word_2 + " " + word_3 + ".") 


#2 (7 points)

def add_three(x, y, z):
    print(x + y + z)

x = float(input("Please insert the first number:\n> "))
y = float(input("Please insert the second number:\n> "))
z = float(input("Please insert the third number:\n>  "))

add_three(x, y, z)

#3 (3 points)

def data_three():
    word_4 = input("Please give me a word:\n> ")
    integer_1 = int(input("Please give me a Integer:\n> "))
    float_1 = float(input("Please give me a float:\n "))
    print(f"{integer_1 + float_1}{word_4}")

data_three()