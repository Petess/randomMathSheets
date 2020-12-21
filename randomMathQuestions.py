#!/usr/bin/python3

from random import * 


def GenerateSingleDigits(numberToGenerate):
    for j in range(0,numberToGenerate):
        print(str(randint(1,9)) + " + " + str(randint(1,9)) + " =    " ,
              end='')

if __name__ == "__main__":
    GenerateSingleDigits(100) 
