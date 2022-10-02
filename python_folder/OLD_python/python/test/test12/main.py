#This is a test file.
#By Santino .J. Tomasi
#Version alpha 5(exp)-2-

#values = ["1","+","1","+","2"]

"""
    while True:

        if i<x:
            if x==1:
                ans.append(values[i])
                print(ans[0])
                break

            if x>=5:

                
                #Layer 1
                if values[i] == "*":
                    if values[i+2] == "*":
                        ans.append(int(values[i-1])*int(values[i+1])*int(values[i+3]))
                        i+=6
                    else:
                        ans.append(int(values[i-1])*int(values[i+1]))
                        print(ans)

            i+=1
            
        print(ans)
    """


def file_test():

    values = []
    reval = []
    l1ans = []
    l2ans = []
    fans = []


    i = 0
    z = 0

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

               #1+2*3

    while True:
        x = len(values)
        l = len(l1ans) 
        

        if i<x:
            print(fans)
            print(l1ans)
            
            

            if values[i] == "*":
                
                if values[i+2] == "*":
                    
                    if z == 0:
                        l1ans.append(int(values[i-1])*int(values[i+1]))
                        z=1
                        
                    
                    elif z==1:
                        l1ans.append(int(l1ans[l-1])*int(values[i+1]))
                        print(l1ans)

                elif z==1:
                    fans.append(int(l1ans[l-1])*int(values[i+1]))
                    z=0
                    print(fans)

            if values[i] == "/":
                
                if values[i+2] == "/":
                    
                    if z == 0:
                        l1ans.append(int(values[i-1])/int(values[i+1]))
                        z=1
                        
                    
                    elif z==1:
                        l1ans.append(int(l1ans[l-1])/int(values[i+1]))
                        print(l1ans)

                elif z==1:
                    fans.append(int(l1ans[l-1])/int(values[i+1]))
                    z=0
                    print(fans)

                

                        
                
        i+=1

        

    
            


def main():
    file_test()

if __name__ == "__main__":
    main()