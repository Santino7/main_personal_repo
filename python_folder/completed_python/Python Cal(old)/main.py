#Calculator program.
#By Santino .J. Tomasi
#Version 1.2
#Date 5/6/2022







#Function that asks username saves said username and runs calcultor function.
def ask_user_name():
    print("Please enter user name")
    user=input('')
    if user == 'johncar':
        print("Hello Santino and welcome to your program!")
        calculator()
    users = """      
    """,user
    f = open("user_names.txt","a")
    f.writelines(users)
    f.close()
    print("Hello",user,"Welcome to CALCULATOR")
    calculator()


#The calculator function.
def calculator():
    while True:
        print("Please chose oporation either,add,sub,mul,div, off, or list")
        oporation=input('')

        if oporation=='add':

            print("Please enter a number")
            answer1=input('')
            try:
                num1=float(answer1)
            except ValueError:
                print("That is not a number.")
                calculator()
            print("Next number please")
            answer2=input('')
            try:
                num2=float(answer2)
            except ValueError:
                print("That is not a number.")
                calculator()
            answer3=num1+num2
            print("This is your answer")
            print(answer3)

        if oporation=='sub':

            print("Please enter a number")
            answer1=input('')
            try:
                num1=float(answer1)
            except ValueError:
                print("That is not a number.")
                calculator()
            print("Next number please")
            answer2=input('')
            try:
                num2=float(answer2)
            except ValueError:
                print("That is not a number.")
                calculator()
            answer3=num1-num2
            print("This is your answer")
            print(answer3)
            

        if oporation=='mul':

            print("Please enter a number")
            answer1=input('')
            try:
                num1=float(answer1)
            except ValueError:
                print("That is not a number.")
                calculator()
            print("Next number please")
            answer2=input('')
            try:
                num2=float(answer2)
            except ValueError:
                print("That is not a number.")
                calculator()
            answer3=num1*num2
            print("This is your answer")
            print(answer3)
            

        if oporation=='div':

            print("Please enter a number")
            answer1=input('')
            try:
                num1=float(answer1)
            except ValueError:
                print("That is not a number.")
                calculator()
            print("Next number please")
            answer2=input('')
            try:
                num2=float(answer2)
            except ValueError:
                print("That is not a number.")
                calculator()
            try:
                answer3=num1/num2
            except ZeroDivisionError:
                print("The answer is infinite")
                calculator()
            print("This is your answer")
            print(answer3)

        if oporation== 'list':
            f = open("user_names.txt", "r")
            print(f.read())

        if oporation=='off':
            print("Thank you for using CALCULATOR")
            onoff()
        
        if oporation=='superoff':
            print("wow you found super off, by now.")
            veryoff()

#A experiment function
def veryoff():
    print("bye")

#Puts the program into a loop of waiting for user input.
def onoff():
    while True:
        print("Please type start if you would like to start CALCULATOR")
        on=input('')
        if on==('start'):
            calculator()
            
#The main statement that starts the whole program.
if __name__ == "__main__":
    ask_user_name()