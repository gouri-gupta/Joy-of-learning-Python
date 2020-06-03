#Code with altogether 79 lines excluding the commented statement

'''Step 1: Write a function that can print out a board. Set up your board as a list, where each index 1-9 corresponds with a
number on a number pad, so you get a 3 by 3 board representation.'''
print("This is the following TIC-TAC-TOE board on which we are going to play our game.")
print("So,let's get started!!!")
board=["#"," "," "," "," "," "," "," "," "," "]
def fun(board):
    for i in range(1,10,3):
        print(board[i]+"|"+board[i+1]+"|"+board[i+2])
        if (i==7):
            break
        print("-----")
fun(board)
board=["#","1","2","3","4","5","6","7","8","9"]
print("Here is the numpad sequence dispalyed for your convienience")
fun(board)
board=["#"," "," "," "," "," "," "," "," "," "]




'''Step 2: Write a function that can take in a player input and assign their marker as 'X' or 'O'. Think about using 
while loops to continually ask until you get a correct answer.'''
def assign():
    marker=""
    while (marker!="X" or marker!="O"):
        marker=input("The player 1 wants which marker 'X' or 'O' ?").upper()
        if (marker=="X"):
            return "X","O"
        elif (marker=="O") :
            return "O","X"
print("\n"*2)
x,y=assign()
print("Please note that, the player 1 is assigned the marker",x,"and the second player is assigned the marker",y)





''''Step 4: Write a function that takes in a board and a mark (X or O) and then checks to see if that mark has won.
'''
def winner(board):
    flag=0
    for i in range(1,10,3):
        if (board[i]==board[i+1] and board[i+1]==board[i+2]):
            z=board[i]
            if (x==z):
                flag=1
                break
            elif (y==z):
                flag=2
                break
    for j in range(1,4):
        if (board[j]==board[j+3] and board[j+3]==board[j+6]):
            z=board[j]
            if (x == z):
                flag = 1
                break
            elif (y == z):
                flag = 2
                break
    if (board[1]==board[5] and board[5]==board[9]):
        z=board[1]
        if (x==z):
            flag=1
            return flag
        elif (y==z):
            flag=2
            return flag
    if (board[3]==board[5] and board[5]==board[7]):
        z=board[3]
        if (x==z):
            flag=1
            return flag
        elif (y==z):
            flag=2
            return flag
    return flag





'''
Step 3: Write a function that takes in the board list object, a marker ('X' or 'O'), and 
a desired position (number 1-9) and assigns it to the board.
'''
i=1
while (i<=9):
    if (i%2!=0):
        n=int(input("Player 1 enter your desired position of tick:"))
        board[n]=x
        fun(board)
        s=winner(board)
        if (s==1):
            print("Congo!!! Player 1 with symbol",x,"is the winner")
            break
    else:
        n=int(input("Player 2 enter your desired position of tick:"))
        board[n]=y
        fun(board)
        s=winner(board)
        if (s == 2):
            print("Congo!!! Player 2 with symbol", y, "is the winner")
            break
    i+=1
if (s==0):
    print("There is a draw")
