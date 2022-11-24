#This is a random file that I have made for no real reason.
#This does nothing important at all just so I could write some python code.
#By S.J.T
#( Date of first edit: Nov 9, 2022 : Time: 19:59 )


#The check column function which checks each index of the array.
#It takes to arguments 1: character 1, 2: character 2, 3: The array that will be checked.
def check_col(c1,c2,a):

    #i or Index is the current index the function is on.
    i = 0

    #z or siZe is the size of the array or how long it is. 
    z = len(a)

    #The main while true loop that checks the array.
    while True:
    
        #Prints the array to the screen.
        print(a)

        #This if statment is used to see if the current index value is equal too character 1.
        if a[i] == c1:
            #If the if statment is true then that index value will be set to character 2.
            a[i] = c2
    
        #If the if statment is not true then the index value will be set to character 1.
        else:
            a[i] = c1
        
        #If the index is less than the size minus 1(which is the furthest index value) then i is now one greater.
        if i < z-1:
            i+=1

        #If the if statment is not true then i is set to the smallest index of 0.
        else:
            i=0


#This is the main function that calls other functions.
def main():

    #A call to the check_col function.
    check_col("@","!",["!","!","!"])
        

#This if statment runs the main function if the file is named "main".
if __name__ == "__main__":
    main()
