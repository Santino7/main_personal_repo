#This is a THING and I have no idea!

#By Santino .J. Tomasi

def p(word,esc):
    if esc == "!":
        print(word)

    if esc != "!":
        print(word,end="")

def main():
    print("->",end="")
    u_in = input()

    l = (len(u_in)-1)

    if u_in[0] == "(" and u_in[l] == ")": 

    else:
        print("Error")

if __name__ == "__main__":
    main()
