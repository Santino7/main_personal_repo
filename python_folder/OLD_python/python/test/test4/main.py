#This is a test file.
#By Santinon .J. Tomasi


class new_class:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def add(self):
        self.ans = self.x+self.y
        return self.ans


def learn_stuff():
    user_in1 = input()
    user_in1 = int(user_in1)
    user_in2 = input()
    user_in2 = int(user_in2)
    use = new_class(user_in1,user_in2)
    use.add()
    print(use.ans)

def main():
    learn_stuff()

if __name__ == "__main__":
    main()