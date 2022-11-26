#By  Santino .J. Tomasi
#This is tic-tac-toe in python.

#Also ... FUNNY   \/([(.)]0[(')])\/ 



#Imports the os module. 
import os



#-----------WINNING AND FAILING SCREENS---------
                                               #
#This prints when player x has won.            #
def p_x_win():                                 #
    print("PLAYER X WON THE BATTLE!")          #
    print("     \     /")                      #
    print(" /\([\'] [\'])/\ ")                 #
    print("       \/")                         #
    print("wow player x is so COOL!")          #
    quit()                                     #
                                               #
                                               #
#This prints when player x has failed or lost. #
def p_x_fail():                                #
    print("PLAYER X  FAILS!")                  #
    print("      |")                           #
    print("      \/")                          #
    print("\/([(.)]_[(.)])\/")                 #
    print("     |     |")                      #
    print("  ___|_____|__")                    #
                                               #
                                               # 
#This prints when player o has won.            #
def p_o_win():                                 #
    print("PLAYER O WON THE BATTLE!")          #
    print("     \     /")                      #
    print(" /\([\'] [\'])/\ ")                 #
    print("       \/")                         #
    print("wow player o is so COOL!")          #
    quit()                                     #
                                               #
                                               #
#This prints when player x has failed or lost. #
def p_o_fail():                                #
    print("PLAYER O  FAILS!")                  #
    print("      |")                           #
    print("      \/")                          #
    print("\/([(.)]_[(.)])\/")                 #
    print("     |     |")                      #
    print("  ___|_____|__")                    #
                                               #
#-----------------------------------------------








#Sets all of the possible location letters to the correct values.
a="A" #1                                                        #
b="B" #2                                                        #
c="C" #3                                                        # 
d="D" #4                                                        #
e="E" #5                                                        #
f="F" #6                                                        #
g="G" #7                                                        #
h="H" #8                                                        #
i="I" #9                                                        #
#----------------------------------------------------------------


#The setup function that sets the game up for what you want.
#eg. who goes first x or o and are you playing against the computer.
def setup():
    global t,s
    
    #Clears the terminal screen.
    if os.name == "posix":
        s=1
    else:
        s=0
        
    #Sets t or the go *t*hrough value to x.
    #This is used to figure out which players turn it is.
    clear_screen()
    print("Who goes first X or O?")
    print(":",end="")
    t = input()
    t = t.lower()
    
    if t == "q":
        clear_screen()
        print("You didn't even try the game =(")
        quit()
    
    elif t != "x" and t != "o":
        print(t + " is not a correct letter.")
        setup()
        
        
        
def clear_screen():
    #Clears the terminal screen.
    if s==1:
        os.system("clear")
    elif s==0:
        os.system("cls")
        
def print_board():
    
    global board
    
    #For loop that prints each array in board.
    #I chose the letter q for the loop randomly.
    for q in board:
        print(q)

#Defines the game function.
def end_screen_func():
    
    global board
    
    clear_screen()
    
    
    board = [[a,b,c],
             [d,e,f],
             [g,h,i]
             ]
    
    #a,b,c
    if board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X":
        p_o_fail()
        
    #a,d,g
    elif board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X":
        p_o_fail()
        
    #g,h,i
    elif board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X":
        p_o_fail()
            
    #c,f,i
    elif board[2][2] == "X" and board[1][2] == "X" and board[0][2] == "X":
        p_o_fail()
            
    #d,e,f
    elif board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X":
        p_o_fail()
            
    #b,e,h
    elif board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X":
        p_o_fail()
            
    #a,e,i
    elif board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
        p_o_fail()
            
    #c,e,g
    elif board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X":
        p_o_fail()
        
        
        
        
        
    #a,b,c
    elif board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O":
        p_x_fail()
        
    #a,d,g
    elif board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O":
        p_x_fail()
        
    #g,h,i
    elif board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O":
        p_x_fail()
            
    #c,f,i
    elif board[2][2] == "O" and board[1][2] == "O" and board[0][2] == "O":
        p_x_fail()
            
    #d,e,f
    elif board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O":
        p_x_fail()
            
    #b,e,h
    elif board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O":
        p_x_fail()
            
    #a,e,i
    elif board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
        p_x_fail()
            
    #c,e,g
    elif board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O":
        p_x_fail()
            
    print_board()
        
    #a,b,c
    if board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X":
        p_x_win()
            
    #a,d,g
    elif board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X":
        p_x_win()
            
    #g,h,i
    elif board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X":
        p_x_win()
            
    #i,f,c
    elif board[2][2] == "X" and board[1][2] == "X" and board[0][2] == "X":
        p_x_win()
            
    #b,e,h
    elif board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X":
        p_x_win()
            
    #a,e,i
    elif board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
        p_x_win()
            
    #c,e,g
    elif board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X":
        p_x_win()
            
            
            
            
    #a,b,c
    elif board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O":
        p_o_win()
        
    #a,d,g
    elif board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O":
        p_o_win()
        
    #g,h,i
    elif board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O":
        p_o_win()
            
    #c,f,i
    elif board[2][2] == "O" and board[1][2] == "O" and board[0][2] == "O":
        p_o_win()
            
    #d,e,f
    elif board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O":
        p_o_win()
            
    #b,e,h
    elif board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O":
        p_o_win()
            
    #a,e,i
    elif board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
        p_o_win()
            
    #c,e,g
    elif board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O":
        p_o_win()
       
       
       
       
def player_turn():
    
    global t,a,b,c,d,e,f,g,h,i
    
    #Checks to see if it is player x turn.
    if t=="x":
        #Prints without starting a newline.
        print("Choose x:",end="")
        x = input()
            
        #Makes x uppercase,
        x = x.upper()
        
        if x=="Q":
            clear_screen()
            print("Goodbye see you next time =)")
            quit()
            
        elif x == "O" or x == "X":
            clear_screen()
            print(x+" not a correct letter.")
            print_board()
            player_turn()
            
        #Many checks that are used to figure out what letter player x gave.
        #Each check sets the letter player x gave to the letter X.
        elif x==a:
            a="X"
        elif x==b:
            b="X"
        elif x==c:
            c="X"
        elif x==d:
            d="X"
        elif x==e:
            e="X"
        elif x==f:
            f="X"
        elif x==g:
            g="X"
        elif x==h:
            h="X"
        elif x==i:
            i="X"
        else:
            #Prints FAIL if player x did not enter a correct letter.
            print("{FAIL}")
            
        #Sets t to o so that next turn is player o turn.
        t="o"
        
    #Elif that checks if it is player o turn.
    elif t=="o":
        #Prints without a newline.
        print("Choose o:",end="")
        o = input()
            
        #Makes o uppercase.
        o = o.upper()
        
        if o=="Q":
            clear_screen()
            print("Goodbye see you next time =)")
            quit()
            
        
        elif o == "O" or o == "X":
            clear_screen()
            print(o+" not a correct letter.")
            print_board()
            player_turn()
            
        #Many checks that are used to figure out what letter player o gave.
        #Each check sets the letter player o gave to the letter O.
        elif o==a:
            a="O"
        elif o==b:
            b="O"
        elif o==c:
            c="O"
        elif o==d:
            d="O"
        elif o==e:
            e="O"
        elif o==f:
            f="O"
        elif o==g:
            g="O"
        elif o==h:
            h="O"
        elif o==i:
            i="O"
        else:
            #Prints FAIL if player o did not enter a correct letter.
            print("{FAIL}")
            
        #Sets t to o so that next turn is player x turn.
        t="x"
            
def game():
    setup()
    while True:
        end_screen_func()
        player_turn()
        

#Defines the main function.
def main():
    #Calls the game function.
    game()

#If statment that checks if this current file name that the program is in is main.
if __name__ == "__main__":
    #Calls that main function. 
    main()
