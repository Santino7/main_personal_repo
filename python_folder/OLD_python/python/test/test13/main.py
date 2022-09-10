#This is a Expression Calculator.
#By Santino .J. Tomasi
#Version 1: Base line expression math completed.
#Version 2

#This is the function that the calculator is in.
def ExpCal():

    #This is the array which will hold the equation.
    array = []

    #Displays the message in the double quotes to the terminal.
    print("Please enter equation one at a time, e to end equation.")

    #The input loop which stops when e is entered into the terminal.
    while True:
        #Takes input from the terminal.
        user_in = input()
        #Checks to see if the user inputted e.
        if user_in == "e":
            #Displays the message in double quotes to the terminal and does not use an new line.
            print("Your answer is ",end="")
            #Stops the loop.
            break

        try:
            #Converts the input to a float.
            array.append(float(user_in))
        
        #If the user input is not a float it checks to see if it is a operator.
        except:
            if user_in == "*":
                array.append(user_in)
            elif user_in == "/":
                array.append(user_in)
            elif user_in == "+":
                array.append(user_in)
            elif user_in == "-":
                array.append(user_in)

            #If it is not a number and is not a valid operator that it restarts.
            else:
                print("WRONG")
                



    #Math loop that does the math operations to get the answers.
    while True:
        #The increment value.
        i=0

        #The length of the array.
        x=len(array)

        #Checking value to see what to run in the program.
        v=0

        #Multiplication loop and division loop.
        while i<x:
            #Updates the value of x.
            x=len(array)

            if v == 0:
                #Checks to see if current value is a multiplication symbol.
                if array[i] == "*":
                    ans = float(array[i-1])*float(array[i+1]) 
                    array[i-1] = ans
                    del array[i+1]
                    del array[i]
                    v=1

            if v == 0:
                #Checks to see if current value is a division symbol.
                if array[i] == "/":
                    ans = float(array[i-1])/float(array[i+1]) 
                    array[i-1] = ans
                    del array[i+1]
                    del array[i]
                    v=1
            
            if v==0:
                i+=1
            if v==1:
                i=0
                v=0
        
        #Resets i for next loop.
        i=0

        #Addition and subtraction loop.
        while i<x:

            #Updates the value of x.
            x=len(array)

            if v == 0:
                #Checks to see if current value is a addition symbol.
                if array[i] == "+":
                    ans = float(array[i-1])+float(array[i+1]) 
                    array[i-1] = ans
                    del array[i+1]
                    del array[i]
                    v=1

            if v == 0:
                #Checks to see if current value is a subtraction symbol.
                if array[i] == "-":
                    ans = float(array[i-1])-float(array[i+1]) 
                    array[i-1] = ans
                    del array[i+1]
                    del array[i]
                    v=1
            
            if v==0:
                i+=1
            if v==1:
                i=0
                v=0
        
        #Displays last value in array to the screen.
        print(array)
        #Stops the loop.
        break

#Main if statement.
if __name__ == "__main__":
    #Calls ExpCal function.
    ExpCal()