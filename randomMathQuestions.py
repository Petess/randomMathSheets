#!/usr/bin/python3

from random import * 

def GenerateSingleDigits(numberToGenerate):
    symbols = ['+','-','*','/']

    for j in range(0,numberToGenerate):
        
        operation = symbols[randint(0,3)]

        if ( operation == '/' ):
            int1 = randint(1,9)
            int2 = randint(1,9)
            result = int1 * int2
            print(str(result) + operation + str(int1) + " =    " ,
                end='')
        else: 
            print(str(randint(1,9)) + operation + str(randint(1,9)) + " =    " ,
                end='')

if __name__ == "__main__":
    GenerateSingleDigits(100) 
