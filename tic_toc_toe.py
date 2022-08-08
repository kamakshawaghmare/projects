def sum(a,b,c):
    return a+b+c

def printbord(xpoint,zpoint):
    zero="x" if xpoint[0] else("0" if zpoint[0] else 0)
    one="x" if xpoint[1] else("0" if zpoint[1] else 1)
    two="x" if xpoint[2] else("0" if zpoint[2] else 2)
    three="x" if xpoint[3] else("0" if zpoint[3] else 3)
    four="x" if xpoint[4] else("0" if zpoint[4] else 4)
    five="x" if xpoint[5] else("0" if zpoint[5] else 5)
    six="x" if xpoint[6] else("0" if zpoint[6] else 6)
    seven="x" if xpoint[7] else("0" if zpoint[7] else 7)
    eight="x" if xpoint[8] else("0" if zpoint[8] else 8)
    print(f"{zero} | {one} | {two} ")
    print(f"--|---|---")
    print(f"{three} | {four} | {five} ")
    print(f"--|---|---")
    print(f"{six} | {seven} | {eight} ")
    print(f"--|---|---")

def checkwin(xpoint,zpoint):
    wins=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in wins:
        if (sum(xpoint[win[0]],xpoint[win[1]],xpoint[win[2]])==3):
            print("x won the match")
            return 1
        if (sum(zpoint[win[0]],zpoint[win[1]],zpoint[win[2]])==3):
            print("0 won the match")
            return 0
    return -1

xpoint=[0,0,0,0,0,0,0,0,0]
zpoint=[0,0,0,0,0,0,0,0,0]
turn=1  #1 for x and 0 for 0
print("welcome to Tic Tac Toe")
while (True):
    printbord(xpoint,zpoint)
    if (turn==1):
        print("x's chance")
        value=int(input("please enter a value:"))
        xpoint[value]=1
    else:
        print("0's chance")
        value=int(input("please enter a value"))
        zpoint[value]=1
    cwin=checkwin(xpoint,zpoint)
    if (cwin != -1):
        print("match over")
        break
    turn=1-turn

