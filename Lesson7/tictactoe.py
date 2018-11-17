import random


def drawField(field): 
    print(field[0],"|",field[1],"|",field[2])
    print("-","+","-","+","-")
    print(field[3],"|",field[4],"|",field[5])
    print("-","+","-","+","-")
    print(field[6],"|",field[7],"|",field[8])
    
def checkWin(field,token):
    field[0]==token
    if field[0]==token and field[1]==token and field[2]==token:
        return True    
    if field[3]==token and field[4]==token and field[5]==token:  
        return True
    if field[6]==token and field[7]==token and field[8]==token:
        return True
    if field[0]==token and field[3]==token and field[6]==token:
        return True
    if field[1]==token and field[4]==token and field[7]==token:
        return True
    if field[2]==token and field[5]==token and field[8]==token:
        return True
    if field[0]==token and field[4]==token and field[8]==token:
        return True
    if field[2]==token and field[4]==token and field[6]==token:
        return True
    return False
def playComputer(field):
    free=[ ]
    for i in range(9):
        if field[i]==" ":
            free.append(i)
    for i in free:
        field2=field.copy()
        field2[i]="O"
        if checkWin(field2,"O")==True:
            return i
    for i in free:
        field2=field.copy()
        field2[i]="X"
        if checkWin(field2,"X")==True:
            return i
    
    randomIndex= random.randint(0,len(free)-1)
    return free[randomIndex]

    
field=[" "," "," "," "," "," "," "," "," "]
token = "X"
for attempt in range(9):
    if token=="O":
        print("Computer turn: ")
        index=playComputer(field)
    else: 
        while True:
            print("Hi, in which row do you want to put your item?")
            i = int(input())
            print("In which column do you want to put your item?")
            j = int(input())  
            index = (i-1)*3 + j-1
            if field[index] == " ":
                break
        
    field[index] = token
    drawField(field)
    checkWin(field,token)
    if checkWin(field,token)==True:
        print(token, " win!")
        break
    if token == "X":
        token= "O"
    else:
        token = "X"