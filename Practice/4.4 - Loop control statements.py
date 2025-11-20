import random
number = 0
for i in range(1, 21):
    print(i)
    if i >= 15:
        break

print("\n---------------------------------------------------------\n")

for i in range(1, 31):
    if i % 2 == 0:
        continue
    print(i)

print("\n---------------------------------------------------------\n")

for i in range(1, 100):
    pass #print only even numbers

print("\n---------------------------------------------------------\n")

for i in range(10, 0, -1):
    if i == 5:
        continue
    print(i)

print("\n---------------------------------------------------------\n")

x = [random.randint(-10, 10) for i in range(11)]
total = 0
for i in x:
    if i <= 0:
        print(f'Negative Number "{i}" Stopped The Sum')
        print(f'Total: {total}')
        break
    print(i)
    total += i
        