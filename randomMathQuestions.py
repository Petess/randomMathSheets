#!/usr/bin/python3

from random import * 

def GenerateSingleDigits(numberToGenerate):
    symbols = ['+','-','*']

    for j in range(0,numberToGenerate):
        
        print(str(randint(1,9)) + symbols[randint(0,2)] + str(randint(1,9)) + " =    " ,
              end='')

if __name__ == "__main__":
    GenerateSingleDigits(100) 
