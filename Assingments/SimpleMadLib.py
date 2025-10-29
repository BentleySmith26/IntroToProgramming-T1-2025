
#Base madlib
#One time in {Noun_Place} There was a person named {Name}.
#and at around {Time}, there was a wild {Noun_thing} raging through {First - Noun_Place}.
#Thankfully a {Adjective} {Noun_Animal} came to Save the day!
#as the {Adjective} Battle came to the end, a plot twist arose and the real winner was a {Adjective} {Noun_Animal}
#Everybody Cheered as the {second - Noun_Animal} came back from {Noun_place}
#as the {adjective} day finished everybody sat back and enjoyed a nice glass of {noun_thing}

noun_p1 = input("Please give a noun that is a place\n> ")
name = input("Please give a name\n> ")
time = input("Please give a time\n> ")
noun_t1 = input("Please give a noun that is a thing\n> ")
adjective1 = input("Please give a adjective\n> ")
noun_a1 = input("please give a noun that is an animal\n> ")
adjective2 = input("Please give another adjective\n> ")
adjective3 = input("Please give another adjective\n> ")
noun_a2 = input("Please give another animal\n> ")
noun_p2 = input("Please give another noun that is a place\n> ")
adjective4 = input("Please give another adjective\n> ")
noun_t2 = input("Please give another noun which is a thing\n> ")

def mad_lib(np1, name, time, nt1, adj1, na1, adj2, adj3, na2, np2, adj4, nt2):
    print(f"One time in {np1} There was a person named {name}. And at around {time}, there was a wild {nt1} raging through {np1}. Thankfully a {adj1} {na1} came to save the day! as the {adj2} Battle came to the end, a plot twist arose and the real winner was a {adj3} {na2}. Everybody Cheered as the {na2} came back from {np2}. as the {adj4} day finished everybody sat back and enjoyed a nice glass of {nt2}.")



