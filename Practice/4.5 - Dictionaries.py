bentleys_faves = {
    "video game": "Peak",
    "food": "pasta",
    "color": "Purple",
    "city": "Albertville",
    "class": "Ap stats"
}

print(bentleys_faves["video game"])

#add a new entry
bentleys_faves["fortnite"] = "Battlepass"

#modify an entry
bentleys_faves["color"] = "yellow"

#remove an entry
bentleys_faves.pop("city")

#looping through a dictionary
for key, value in bentleys_faves.items():
    print(f'{key}: {str(value)}')


print(bentleys_faves.keys())
print(bentleys_faves.values())
print(bentleys_faves.items())
bentleys_faves.clear()
print(bentleys_faves)