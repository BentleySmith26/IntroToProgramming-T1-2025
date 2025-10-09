def tally_score():
    q1 = input("what is 5 + 10?(number form)\n> ")
    q2 = input("what is 5 * 5?(number form)\n> ")
    q3  =input("what is my birthday? (Ex: xx/xx/xxxx)\n> ")
    q4 =input("what is your credit card number?(number form)\n> ")
    q5 =input("what is my dog's nickname?(word form)\n> ")
    q6 =input("first 10 digits of pi?(don't forget the decimal)\n> ")
    q7 =input("how many bones does a human have?(number form)\n> ")
    q8 =input("what is the sqrt of infinity? (put full word form)\n> ")
    q9 =input("what is 67-67?(number form)\n> ")
    q10 =input("what is 3+64?(number form)\n> ")
    score = 0
    if q1 == "15":
        score = score + 1
    if q2 == "25":
        score = score + 1
    if q3 == "03/11/2008":
        score = score + 1
    if q4 == "1234":
        score = score + 1
    if q5 == "goose":
        score = score + 1
    if q6 == "3.141592653":
        score = score + 1
    if q7 == "206":
        score = score + 1
    if q8 == "infinity":
        score = score + 1
    if q9 == "0":
        score = score + 1
    if q10 == "67":
        score = score + 1

    print(score)
tally_score()








