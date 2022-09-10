
#A program made to edit and read a txt file
#Version Beta
#By Santino .J. Tomasi
#Date 5/8/2022

import pygame

def edit_file():
    while True:
        keyin = input(' ')
        f = open("a.txt","a+")
        f.write(keyin)
        if pygame.K_ESCAPE:
            exit()

def exit():
    exitin = input(" ")
    print("Hello, if you would like to go back to the program please type wow")
    if exitin == "wow":
        edit_file()

def main():
    edit_file()

if __name__ == "__main__":
    main()

