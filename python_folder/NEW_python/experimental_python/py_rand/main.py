#This is a random python file for on the spot test.
#Any good things that happen in this file will be sent to another file to be stored.
#By Santino .J. Tomasi
#Date when file was made: Oct 9,2022 

def main():  

    while True:

        a = ["!","!"]
        
        if a[0] == "!" and a[1] == "!":
            a[0] = "@"

        elif a[0] == "@" and a[1] == "!":
            a[0] = "!"
            a[1] = "@"
            print("hi")



        print(a)

if __name__ == "__main__":
    main()
