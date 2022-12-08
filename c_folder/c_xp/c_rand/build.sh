#!/bin/bash

#By Santino J. Tomasi
#This is a little bash script used for compiling and running c code.
#Only works if the exe file and .c file names are both "main".

clear

gcc -o main main.c

./main
