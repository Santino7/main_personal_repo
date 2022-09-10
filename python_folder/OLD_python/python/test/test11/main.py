#This is a test file.
#By Santino .J. Tomasi
#Version alpha 5

#values = ["1","+","1","+","2"]

def file_test():

    values = []
    ans = []

    while True:
        user_in = input()
        if user_in == "e":
            break
        try:
            values.append(int(user_in))
        except ValueError:
            if user_in == "+":
                values.append(user_in)

            elif user_in == "*":
                values.append(user_in)

            elif user_in == "/":
                values.append(user_in)

            elif user_in == "-":
                values.append(user_in)
            
            else:
                print("You failed.")
                exit()

                """
                7+1/4-2*2*2
                7+0.25-2*2
                7+0.25-4
                7.25-4
                3.25
                """
                
            
      
    i = 0
    x = len(values)

    while True:
        l = len(ans)

        if x==1:
            ans.append(int(values[0]))
            print(ans[0])
            break

        if x==3:

            if i<=2:
                if i==2:
                    print(ans[l-1])
                    break
                if i<x:
                    if values[i] == "+":
                        ans.append(int(values[i-1])+int(values[i+1]))
                    if values[i] == "-":
                        ans.append(int(values[i-1])-int(values[i+1]))
                    if values[i] == "*":
                        ans.append(int(values[i-1])*int(values[i+1]))
                    if values[i] == "/":
                        ans.append(int(values[i-1])/int(values[i+1]))

        if x>3:

            if i+1 == x:
                print(ans[l-1])
                break

            if i>2:
                if values[i] == "+":
                    ans.append(ans[l-1]+int(values[i+1]))
                if values[i] == "-":
                    ans.append(ans[l-1]-int(values[i+1]))
                if values[i] == "*":
                    ans.append(ans[l-1]*int(values[i+1]))
                if values[i] == "/":
                    ans.append(ans[l-1]/int(values[i+1]))
                
            if i<=2:
                if i<x:
                    if values[i] == "+":
                        ans.append(int(values[i-1])+int(values[i+1]))
                    if values[i] == "-":
                        ans.append(int(values[i-1])-int(values[i+1]))
                    if values[i] == "*":
                        ans.append(int(values[i-1])*int(values[i+1]))
                    if values[i] == "/":
                        ans.append(int(values[i-1])/int(values[i+1]))
            
        i+=1

def main():
    file_test()


if __name__ == "__main__":
    main()