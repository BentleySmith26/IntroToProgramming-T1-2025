print("in this Text Adventure, all 'Y or N' questions are to be  inputed as a lowercase y or lowercase n, this is simpily for convenience purposes.")
def start_adventure():
    
    print("You stare at the great door in front of you")
    print("do you:")
    print("1. return to the village to ask the people for assistance")
    print("2. join the caravan inviting you into their group")
    print("3. give a call to your friend to come help you out")
    print("4. wait for 20 minutes")

    choice = input("> ")

    if choice == "1":
        return_to_village()
    elif choice == "2":
        caravan() # not finished
    elif choice == "3":
        call_friend() # not finished
    elif choice == "4":
        wait()

def wait():# Waiting path
    print("you wait for 20 minutes and nothing happens")
    print("wait some more?")
    print("Y or N")
    waiting1 = input("> ")
    if waiting1 == "y":
        wait1()
    elif waiting1 == "n":
        start_adventure()
    else:
        print("invalid input, Please use lowercase letters")
        wait()
def wait1():
    print("you wait for 20 minutes and nothing happens")
    print("wait some more?")
    print("Y or N")
    waiting2 = input("> ")
    if waiting2 == "y":
        wait2()
    elif waiting2 == "n":
        start_adventure()
    else:
        print("invalid input, Please use lowercase letters")
        wait1()
def wait2():
    print("you wait for 20 minutes and SOMETHING HAPPENS")
    print(" The door opens and your patience has seemed to pay off!")
    print("would you like to step inside?")
    print("Y or N")
    waiting3 = input("> ")
    if waiting3 == "y":
        door_opens()
    elif waiting3 == "n":
        loser()
    else:
        print("invalid input, Please use lowercase letters")
        wait2()
def loser():
    print("game over, you're a loser for not continuing on")
def door_opens_waiting():
    print("you slowly decide to step inside.")
    print("inside you see a massive pile of gold")
    print("do you:")
    print("1. take the gold")
    print("2. report the gold to the local village")
    print("3. commit a scrooge McDuck into the pile of gold")
    
    choice = input("> ")

    if choice == "1":
        greed()
    elif choice == "2":
        secret1()
    elif choice == "3":
        death()
def greed():
    print("you decide to take the gold, out of the gold pops out a tiny goblin\n the goblin says:\n'wow, I can't believe you came here alone as a greedy person to take all of this gold alone... I CAST THUNDER'")
    death()
def secret1():
    print("You return back to the village and report the gold, the town builds a statue of you in rememberence of your effect on them, you shall forever be remembered\nYou got: secret ending 1")

def return_to_village(): # not finished
    print("you return to the village\ndo you:\n1. talk to the creepy old guy\n2. enter the mayor's office\n3. go to the adventurer's guild to recruit a team\n4. jump in the well for fun")
    choice = input("> ")
    if choice == "1":
        old_man()
    elif choice == "2":
        mayor_office()
    elif choice == "3":
        adv_guild()
    elif choice == "4":
        death()
    else:
        print("Invalid input")
        return_to_village()
def old_man(): # Old man path finsihed
    print("you go to speak to the old man sitting on the shady city street\nOld man:\n'oh yes, young adventurer, what brings you here to our humble village? are you here about that door I pressume? well I just so happen to know how to open this door. would you care to hear my story?\nY or N")
    choice = input("> ")
    if choice == "y":
        listen()
    elif choice == "n":
        print("you leave the old man behind as he vanishes into the darkness")
        village_no_old()
    else:
        print("invalid input, Please use lowercase letters")
        old_man()
def listen():
    print("you decide to listen to the old man.\n'ah yes, so my story is so, I was a young man once and I gathered a big group of adventurers and was ready to start my marvelous adventure\nour journey lasted long and vasted accross the lands far and wide, as we did continue on though we did end up not finding the key, but we found this scroll")
    print("you open up a scroll and find a map to a nearby cave just 10 miles from the village")
    print("Old man:\nI suggest you go pickup a horse before you go on your journey for the key to that big door just so you can have your feet fairly rested for what may lie inside the door\nalso if the horse seller gives you any trouble just say the lost adventurer sent you")
    print("the old man suddenly vanishes leaving you stunned\nyou should probably go and get that horse for your journy ahead\nenter Y to continue")
    choice = input("> ")
    if choice == "y":
        horses()
    else:
        print("invalid input")
        listen()
def horses():
    print("you walk into the old horse place and see the seller\nHorse seller:\n'Heya bud, what kind of stalion you looking for? also our horses can be quite pricey, you sure you got the funds?'")
    print("what do you say?")
    print("1. the lost adventurer sent me\n2. I have no money sorry\n3. attempt to steal the horse\n4. return to the town square")
    choice = input("> ")
    if choice == "1":
        horse_text()
    elif choice == "2":
        print("Horse seller:\n'Get out of my shop and never come back!'\nthe horse seller sends you back to the town square")
        village_no_old()
    elif choice == "3":
        print("you try and steal the horse and the Horse seller pulls out a magical rifle to put an end to you")
        print("to simpily put it, you die because of your poor choice, maybe you'll succeed in another life.\nRestart?\nY or N")
        choice = input("> ")
        if choice == "y":
            start_adventure()
        elif choice == "n":
            print("Thank you for playing my text adventure project")
        else:
            print("invalid input, Please use lowercase letters")
    elif choice == "4":
        print("you decide that this is not worth your time")
        village_no_old()
    else:
        print("invalid input")
        horses()
def horse_text():
    print("Horse Seller:\n 'Ah, so I see you have met him, very few actually get to meet this legend, he is an old friend of mine and if he really did send you I'm sure you're the right person to get past that forsaken door.'")
    print("The Horse Seller proceeds to give you his most valliant horse")
    print("Horse Seller:\nThis is Job the Horse, don't judge the name please adventurer. Now go on your journy to go find the secret of the locked door!")
    print("Enter Y to continue")
    choice = input("> ")
    if choice == "y":
        path_to_cave()
    else:
        print("invalid input")
        horse_text()
def path_to_cave():
    print("you decide to set off on your stallion Job and go to the cave, you know the journey might be difficult but-\nWait what?\nSome how you were able to get to the cave with no issues, what a pleasent surprise!")
    print("Enter Y to continue")
    choice = input("> ")
    if choice == "y":
        cave()
    else:
        print("invalid input")
        path_to_cave()
def cave():
    print("you decide to enter the cave and see what's inside. you notice it's quite dim in the cave so you decide to light the cave with the torch you brought along with you.\nas you light the torch you see a swarm of bats heading towards you\nWhat do you do?")
    print("1. Wave around your torch mindlessly\n2. take out your sword and prepare to unalive the bats\n3. surrender to the bats and accept your fate\n4. decide that that's the end of your journey and leave the cave leaving the secrets of the door behind.")
    choice = input("> ")
    if choice == "1":
        print("As you mindlessly swing your torch around the bats atually swarm away from you letting you live another day")
        key()
    elif choice == "2":
        print("you take out your blade and slice the tiny beasts to shreds with relitive ease.")
        key()
    elif choice == "3":
        death()
    elif choice == "4":
        loser()
    else:
        print("invalid input")
        cave()
def key():
        print("after the bats, you decide to continue on in the cave.\nas you turn the next corner you see a chest on the ground, while it could be a little dangerous you decide to open it anyway.\nThankfully this chest was just normal and contained quite an odd shaped key, maybe this opens the massive door?")
        print("Enter Y to continue")
        choice = input("> ")
        if choice == "y":
            door()
        else:
            print("invalid input")
            key()
def door():
    print("you travel to the door and see the grandness before you.\nYou walk up slowly and insert the key and turn it.\n The door opens...")
    print("Enter Y to continue")
    choice = input("> ")
    if choice == "y":
            door_opens_oldman()
    else:
        print("invalid input")
        door()
def door_opens_oldman():
    print("you slowly step inside and see the massive pile of gold before you. you step forward to claim your prize.\nall of a sudden a dragon made of gold appears from the pile.\nWhat do you do?")
    print("1. do a crazy series of flips and tricks to confuse the dragon then strike it.\n2. Take out your trusty bow and aim for the small eyes of the enlarged beast.\n3. Stare at the dragon as you slowly accept defeat.\n4. Zexkq qeb pbzobq qbuq ql Bifjfkxqb qeb ybxpq...")
    choice = input("> ")
    if choice == "1":
        death()
    elif choice == "2":
        print("you aim for the eye's of the dragon and you hit it's eye dead on. the beast struggles but falls to your expertly placed shot.\nYou may now claim the gold and do whatever you would like with it")
        print("Congradulations!\nYou Got: Old man ending")
    elif choice == "3":
        death()
    elif choice == "4":
        print("le eliv pmfofqp colj xylsb, F zljjxka vlr ql pqofhb altk vlro ifdeqkfkd xka bka qefp clb fk jv txv...")
        print("suddenly a thunderbolt strikes down and instantly ends the beast, you have won and may now collect the tresure, although the nearby village may have some questions about your new power...")
        print("Congradulations!\nYou Got: Secret ending 2")
def village_no_old():
    print("you decide return to the village\ndo you:\n1. enter the mayor's office\n2. go to the adventurer's guild to recruit a team\n3. jump in the well for fun")
    choice = input("> ")
    if choice == "1":
        mayor_office()
    elif choice == "2":
        adv_guild()
    elif choice == "3":
        death() 
    else:
        print("Invalid input")
        village_no_old()
def mayor_office(): # Mayor path finished
    print("You walk into the Mayor's office and see many many distracting things.\nYou're smart enough to ignore this and instead just head straight for the big man himself, The Mayor")
    print("Mayor:\nHello there adventurer, I see the you're new here and I hope you enjoy your stay, is there anything that you need from me?")
    print("What do you ask for?\n1. access to the village secrets\n2. What the old man is doing on the street corner\n3. ask about the door\n4. attempt to kill the Mayor")
    choice = input("> ")
    if choice == "1":
        print("Mayor:\n'H-HELL NAW'")
        print("The Mayor kicks you out of the village and you are left to just ponder at the door for eternity")
        limbo()
    elif choice == "2":
        print("Mayor:\n'Oh yes, the old man, he is an odd fella. He has been here for quite some time now, he always just sits there scaring everyone off if they come near, quite odd wouldn't you say?")
        mayor_ask()
    elif choice == "3":
        print("Mayor:\n'Oh yes! the door. That door has been there for generations and only one group has ever come close to revealing it's secrets. Perchance do you think that you're going to be the next to open the door?")
        print("You:\n'Yes indeed Mayor'")
        print("Mayor:\n'Ah alright then adventurer, I shall send you on your way to the door, I heard that the mysterious chant is decrypted on this scroll. If you can decode it all I ask is that you bring some of the treasure to our village.")
        print("Enter Y to continue")
        choice2 = input("> ")
        if choice2 == "y":
            decode()
        else:
            print("invalid input")
            mayor_choice3()
    elif choice == "4":
        print("you lunge at the mayor with a dagger in hand and lower a devistating blow, I have no Idea why you would do that but the gods have decided to let you have another chance at life anyways")
        start_adventure()
    else:
        print("invalid input")
        mayor_ask()
def mayor_ask():
    print("What do you ask for?\n1. access to the village secrets\n2. What the old man is doing on the street corner\n3. ask about the door\n4. attempt to kill the Mayor")
    choice = input("> ")
    if choice == "1":
        print("Mayor:\n'H-HELL NAW'")
        print("The Mayor kicks you out of the village and you are left to just ponder at the door for eternity")
        limbo()
    elif choice == "2":
        print("Mayor:\n'Oh yes, the old man, he is an odd fella. He has been here for quite some time now, he always just sits there scaring everyone off if they come near, quite odd wouldn't you say?")
        mayor_ask()
    elif choice == "3":
        print("Mayor:\n'Oh yes! the door. That door has been there for generations and only one group has ever come close to revealing it's secrets. Perchance do you think that you're going to be the next to open the door?")
        print("You:\n'Yes indeed Mayor'")
        print("Mayor:\n'Ah alright then adventurer, I shall send you on your way to the door, I heard that the mysterious chant is decrypted on this scroll. If you can decode it all I ask is that you bring some of the treasure to our village.")
        print("Enter Y to continue")
        choice2 = input("> ")
        if choice2 == "y":
            decode()
        else:
            print("invalid input")
            mayor_choice3()
    elif choice == "4":
        print("you lunge at the mayor with a dagger in hand and lower a devistating blow, I have no Idea why you would do that but the gods have decided to let you have another chance at life anyways")
        start_adventure()
    else:
        print("invalid input")
        mayor_ask()
def mayor_choice3():
    print("Mayor:\n'Oh yes! the door. That door has been there for generations and only one group has ever come close to revealing it's secrets. Perchance do you think that you're going to be the next to open the door?")
    print("You:\n'Yes indeed Mayor'")
    print("Mayor:\n'Ah alright then adventurer, I shall send you on your way to the door, I heard that the mysterious chant is decrypted on this scroll. If you can decode it all I ask is that you bring some of the treasure to our village.")
    print("Enter Y to continue")
    choice2 = input("> ")
    if choice2 == "y":
        decode()
    else:
        print("invalid input")
        mayor_choice3()
def limbo():
    print("Pondering is A very Steady and Swift Way to send your thoughts Outword and Right Down to the point... (hint, type Help if you are stuck)")
    choice = input("> ")
    if choice.lower() == "password":
        secret2()
    elif choice.lower() == "help":
        print("Look at the uppercase letters...")
        limbo()
    else:
        limbo()
def secret2():
    print("Congrats on making it out of this limbo! you deserve this secret ending!\nYou Got: Secret Ending 2")
def decode():
    print("you stare at the scroll wondering how to decode this, all you see is the words 'ABRIR PUERTA'\nWhat could this possibly mean?")
    choice = input("> ")
    if choice.lower() == "open door":
        door_decode()
    else:
        print("Maybe if you translate this code you can continue...")
        decode()
def door_decode():
    print("You successfully decode the scroll and you hear the door open in the distance, as you get there you are able to walk inside and find the mass amounts of treasure\nWhat do you do?")
    print("1. Take all of the gold for yourself\n2. Bring the gold back to the village like you promised to the Mayor\n3. close the door back up for the secret to be forever hidden with you")
    choice = input("> ")
    if choice == "1":
        greed()
    elif choice == "2":
        print("the gold is to be safe with the village and they end up celebrating you with a huge festival, but mysteriously the old man is missing...")
        print("Congrats! You Got: Mayor's office ending")
    elif choice == "3":
        print("you decide to close the door and leave the mystery for someone else to discover")
        print("Congrats! You Got: Secret Ending 3")
    else:
        print("invalid input")
        door_decode()
def adv_guild(): # not finished
    print("you decide to head to the adventurers guild to get a team to help you out")
    print("you see three groups, the Vikings, the Dwarfs, and the Humans, which do you choose?\n1. Vikings\n2. Dwarfs\n3. Humans")
    choice = input("> ")
    if choice == "1":
        print("you have chosen the Vikings, but they are not very nice people and they gang up on you to rob you although a little too rough...")
        death()
    elif choice == "2":
        print("you chose the Dwarfs, they are small but come with great power")
        dwarf()
    elif choice == "3":
        print("You go with the most basic choice, your own kind. all around handy and just a great group of people to go with")
        human()
    else:
        print("invalid input")
        adv_guild()
def dwarf():
    print("you set off towards the door to use your new team to break it down")
    print("as you stand infront of the door your new dwarf buddies stand there and ponder while they try and think of a solution.")
    print("What do you do?\n1. Use the power of friendship and break down the door\n2. send in your dwarfs to start digging under the door\n3. give up and cry in a corner")
    choice = input("> ")
    if choice == "1":
        print("you charge at the door with your new dwarf buddies swiftly, although you fail to realize that you're between all of the dwarfs and they end up crushing you.")
        death()
    elif choice == "2":
        print("you send in your new strong team to dig under the door, they dig hastily and they end up getting a nice perfect tunnel through")
        dwarf_2()
    elif choice == "3":
        print("you give up like a baby and you sit in the corner and cry")
        print("congrats? you got: baby ending")
    else:
        print("invalid input")
        dwarf()
def dwarf_2():
    print("you stand inside the door's room that it was hiding. you and your team spot a massive pile of gold")
    print("Do you:\n1. Split the gold among your new teammates and part ways and enjoy your new lives\n2. Try and steal all the gold for yourself before the Dwarfs get any\n3. let your new friends enjoy the gold all to themselves")
    choice = input("> ")
    if choice == "1":
        print("you successfully split the gold with your allies and live a nice life")
        print("Congrats! You Got: Normal Dwarf ending")
    elif choice == "2":
        print("you attempt to steal all of the gold forgetting that you're going against all the dwarfs you hired")
        print("The dwarfs all quickly lunge at you and beat you to death")
        death()
    elif choice == "3":
        print("you let all of your new friend enjoy they're new stash of gold, you feel good about yourself.")
        print("Congrats! You Got: Dwarf good ending :)")
    else:
        print("invalid input")
        dwarf_2()
def human():
    print("you choose the humans to team up with and get inside the door, a nice all around choice.")
    print("you now stand before the door with your team of wonderful pals you have gotten to know quite well along the trip over")
    print("how do you open the door?\n1. throw rocks at the door until it opens\n2. Use the power of friendship and pile drive your way into the door\n3. ponder at the door until it opens\n4. Give up and live your life with your new friends")
    choice = input("")
    








def death():
    print("to simpily put it, you die because of your poor choice, maybe you'll succeed in another life.\nRestart?\nY or N")
    choice = input("> ")
    if choice == "y":
        start_adventure()
    elif choice == "n":
        print("Thank you for playing my text adventure project")
    else:
        print("invalid input, Please use lowercase letters")
        death()










start_adventure()