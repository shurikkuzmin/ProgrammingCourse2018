import random
y=random.randint(1,20)
guessed = False
for attempt in range(5):
    print("enter number")
    x=int(input())
    if x==y:
        guessed = True
        break
    elif x<y:
        print("too small")
    else:
        print("too big")                    

if not guessed:
    print("Looser")
else:
    print("Congrats!")