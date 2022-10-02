#Random program.
#By Santino .J. Tomasi



def ask_user_name():
    print("Please enter user name")
    user=input('')
    print("Hello",user,"Welcome to CALCULATOR")
    calculator()



def calculator():
    while True:
        print("Please chose oporation either,add,sub,mul,or div")
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
            

        if oporation=='off':
            print("Thank you for using CALCULATOR")
            onoff()


def onoff():
    while True:
        print("Please type start if you would like to start CALCULATOR")
        on=input('')
        if on==('start'):
            calculator()
            

if 1==1:
    ask_user_name()