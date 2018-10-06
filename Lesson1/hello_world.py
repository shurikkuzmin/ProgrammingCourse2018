print("Greetings! What's your name?")
name = input()
print("What time is it right now (time)? (24 hour format)")
time = input()
int_hour = int(hour)

if int_hour > 24 or int_hour < 0:
    print ("You're stupid!")
    exit()
if int_hour >= 6 and int_hour < 11:
    print("Good morning, " + name + "!")
elif int_hour >= 11 and int_hour < 14:
    print("Good day, " + name + "!")
elif int_hour >= 14 and int_hour < 17:
    print("Good afternoon, " + name + "!") 
elif int_hour >= 17 and int_hour < 21:
    print("Good evening, " + name + "!")
else:
    print("Good night, " + name + "!")

