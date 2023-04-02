#This is an expression calculator that runs in the terminal.
#Version 3
#By Santino J. Tomasi


#Imports os to clear screen.
import os

#Imports graphics module tkinter.
import tkinter as tk


#List that holds all input.
exp_list = []


def input_function():

    global exp_list

    display_in_terminal("start")
    
    #Takes user input and removes all whitespaces.
    user_in = input().replace(" ","")

    #Sets increment value to 0.
    inc = 0 
    
    #The length of the string provided by the user input.
    length = len(user_in)

    #A variable that is used to find the index of the first\front digit in a number.
    front = None
    
    while inc < length:
        
        try:
            
            #Checks to see if current index value is a "." so that the program allows "." for decimals.
            if user_in[inc] != ".":
                
                int(user_in[inc])
            
            #Checks if front has been set to "None" yet, essentialy meaning has the program found the first\front digit of the current number.
            if front == None:
                
                front = inc
            
            #Checks to see if the program has reached the end of the expression.
            if inc+1 == length:
                
                exp_list.append(user_in[front:inc+1])
                
                break
                
            inc += 1
        
        #Checks current index value since it was not an it in order to avoid errors.
        except ValueError:

            #Checks to see if a proper value is used for current index.
            if user_in[inc] != "+" and user_in[inc] != "-" and user_in[inc] != "*" and user_in[inc] != "/":

                display_in_terminal("bad_value")

            exp_list.append(user_in[front:inc])
            
            exp_list.append(user_in[inc])

            front = None
            
            inc += 1


#This is the function that takes the input and calculates the output.
def ExpCal():

    global exp_list

    #Math loop that does the math operations to get the output.
    while True:

        #The increment value.
        inc = 0

        #The length of the list.
        length = len(exp_list)

        #Checking value to see what to run in the program.
        check = 0

        #Multiplication loop and division loop.
        while inc < length:

            #Updates the value of length.
            length = len(exp_list)

            if check == 0:

                #Checks to see if current value is a multiplication symbol.
                if exp_list[inc] == "*":

                    ans = float(exp_list[inc-1]) * float(exp_list[inc+1]) 

                    exp_list[inc-1] = ans

                    del exp_list[inc+1]

                    del exp_list[inc]

                    check = 1

            if check == 0:

                #Checks to see if current value is a division symbol.
                if exp_list[inc] == "/":

                    if exp_list[inc+1] == "0":

                        display_in_terminal("division 0 error")

                    ans = float(exp_list[inc-1]) / float(exp_list[inc+1]) 

                    exp_list[inc-1] = ans

                    del exp_list[inc+1]

                    del exp_list[inc]

                    check = 1
            
            if check == 0:

                inc += 1

            if check == 1:

                inc = 0

                check = 0
        
        #Resets inc for next loop.
        inc = 0

        #Addition and subtraction loop.
        while inc < length:

            #Updates the value of length.
            length = len(exp_list)

            if check == 0:

                #Checks to see if current value is a addition symbol.
                if exp_list[inc] == "+":

                    ans = float(exp_list[inc-1]) + float(exp_list[inc+1]) 

                    exp_list[inc-1] = ans

                    del exp_list[inc+1]

                    del exp_list[inc]

                    check = 1

            if check == 0:

                #Checks to see if current value is a subtraction symbol.
                if exp_list[inc] == "-":

                    ans = float(exp_list[inc-1])-float(exp_list[inc+1]) 

                    exp_list[inc-1] = ans

                    del exp_list[inc+1]

                    del exp_list[inc]

                    check = 1
            
            if check == 0:

                inc += 1

            if check == 1:

                inc = 0

                check = 0

        #Stops the loop.
        break


#Function that displays output.
def display_in_terminal(terminal_display_option):

    #Runs clear or cls command for respective os.
    os.system("cls") if os.name == "nt" else os.system("clear")

    #Prints if there is a bad value.
    if terminal_display_option == "bad_value":

        print("You entered a false value.")

        quit()

    #Prints if there is a division of 0 error.
    elif terminal_display_option == "division 0 error":

        print("Listen do not try and divide a number by 0.")

        quit()

    #Prints at start of program.
    elif terminal_display_option == "start":

        print("[Santino's expression calculator version 3]")

    #Prints at end of program.
    elif terminal_display_option == None: 
        
        print(exp_list)

        quit()


def display_graphically():

    window = tk.Tk()

    window.title("Expression Calculator")

    window.iconbitmap(r".\cal_icon.ico")

    one_button = tk.Button(window,text="1",width=10,).grid(row=2,column=1) #1

    two_button = tk.Button(window,text="2",width=10,).grid(row=2,column=2) #2

    three_button = tk.Button(window,text="3",width=10,).grid(row=2,column=3) #3

    four_button = tk.Button(window,text="4",width=10,).grid(row=3,column=1) #4

    five_button = tk.Button(window,text="5",width=10,).grid(row=3,column=2) #5

    six_button = tk.Button(window,text="6",width=10,).grid(row=3,column=3) #6

    seven_button = tk.Button(window,text="7",width=10,).grid(row=4,column=1) #7

    eight_button = tk.Button(window,text="8",width=10,).grid(row=4,column=2) #8

    nine_button = tk.Button(window,text="9",width=10,).grid(row=4,column=3) #9

    zero_button = tk.Button(window,text="0",width=10,).grid(row=1,column=1) #0

    decimal_button = tk.Button(window,text=".",width=10,).grid(row=5,column=2) #. decimal

    clear_button = tk.Button(window,text="clear",width=10,).grid(row=5,column=1) #Clear

    divide_button = tk.Button(window,text="'/.",width=10,).grid(row=5,column=4) #Divide

    mul_button = tk.Button(window,text="x",width=10,).grid(row=4,column=4) #Multiplication

    add_button = tk.Button(window,text="+",width=10,).grid(row=2,column=4) #Addition

    subtract_button = tk.Button(window,text="-",width=10,).grid(row=3,column=4) #Subtract

    equal_button = tk.Button(window,text="=",width=10,).grid(row=1,column=4) #equal

    delete_button = tk.Button(window,text="del",width=10,).grid(row=5,column=3) #delete

    window.mainloop()


#The main function that runs everyting in order.
def main():

    print("1 for graphical interface or 0 for terminal interface:",end="")

    graph_or_no = input()

    if graph_or_no == "0":

        input_function()

        ExpCal()

        display_in_terminal(None)

    elif graph_or_no == "1":
        
        display_graphically()


#Main if statment. 
if __name__ == "__main__":

    main()