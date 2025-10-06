
item = input("item input here:\n> ")
price = input("Price input here\n> ")
rate = 0.06875



def calculate_tax(item, price, rate):
    print(f"The amount of tax on a {str(item)} is ${float(price) * rate}.")

calculate_tax(item, price, rate)



def add_five_numbers(one, two, three, four, five):
    print(one+two+three+four+five)

add_five_numbers(67, 41, 69, 98, 34)

first = input("first\n> ")
last = input("last\n> ")
def full_name(first, last):
    print(f" Your name is: {first}, {last}.")

full_name(first, last)


def area_calculator(length, width):
    print(length*width)

area_calculator(6, 7)
area_calculator(28, 7)
area_calculator(4, 13)


def word_smash(word1, word2):
    print(str(word1) + str(word2))

word_smash("one", "two")
word_smash("1", "two")
word_smash("one", "2")


def echo(copy, times):
    print(str(copy)*(times))

echo("ball", 5)

def happy_birthday(name):
    print(f"Happy Birthday to You, Happy Birthday to You, Happy Birthday Dear {name}, Happy Birthday to You!")

happy_birthday("sigma boy")