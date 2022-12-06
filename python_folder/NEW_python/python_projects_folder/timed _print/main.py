#This is a test file.
#By Santino .J. Tomasi


import time



def weird_string():
    words1 = ["Hi ","there ","how ","goes ","it?"]
    wait_time = 0.08
    wait_increase = 0
    
    i=0
    x=len(words1)

    print("Please enter text speed, nothing below zero.")
    user_in = input()

    user_in = float(user_in)
    
    if user_in < 0:
        print("This is not a value above zero,you failed ")
        weird_string()

    if user_in > wait_time:
        wait_increase=user_in

    if user_in == 'down':
        wait_increase=0.1

    if user_in == 'up':
        wait_increase=0.06

    wait_increase=user_in


    while i<x:
        i+=1
        time.sleep(wait_time+wait_increase)
        print(words1[i-1],end="")


def main():
    weird_string()


if __name__ == "__main__":
    main()