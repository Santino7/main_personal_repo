#This is a test file.
#By Santino .J. Tomasi




def function1():
    array1 = [[[1,2],
              [3,4]],
              [[5,6],
               [7,8]]]

    print("Please choose x,y,z to read values")
    x_in = int(input())
    y_in = int(input())
    z_in = int(input())

    print(array1[x_in][y_in][z_in])

def main():
    function1()


if __name__ == "__main__":
    main()