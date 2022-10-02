
#This is a experiment program that changes.
#By Santino .J. Tomasi
#Version NO VERSION
#Date 5/8/2022





def wow():
    try:
        equation = ' '
        ein = input(' ')
        if ein == "off":
            print("bye")
            exit()
        equation = equation+ein
        out = "print("+equation+")"
        exec(out)
        wow()
    except ZeroDivisionError:
        print("The answer is infinite.")
        wow()
    except (SyntaxError,NameError):
        print("Sorry you did not input a equation.")
        wow()

def main():
    wow()

if __name__ == "__main__":
    main()