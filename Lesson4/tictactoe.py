import random


def drawField(field): 
    print(field[0],"|",field[1],"|",field[2])
    print("-","+","-","+","-")
    print(field[3],"|",field[4],"|",field[5])
    print("-","+","-","+","-")
    print(field[6],"|",field[7],"|",field[8])
field=[" "," "," "," "," "," "," "," "," "]
token = "X"
for attempt in range(4):
    print("Hi, in which row do you want to put your item?")
    i = int(input())
    print("In which column do you want to put your item?")
    j = int(input())  
    index = (i-1)*3 + j-1
    field[index] = token
    if token == "X":
        token= "O"
    else:
        token = "X"
    drawField(field)
