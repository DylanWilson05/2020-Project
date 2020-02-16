#Random Lottery Number Generator by Dylan Wilson


#Imports the Random Library used for generating random integers.
import random


#Defines the function "lottery_numbers"
def lottery_numbers():
    #Creates 7 Numbers between 1 and 49
    num1 = random.randint(1, 49)
    num2 = random.randint(1, 49)
    num3 = random.randint(1, 49)
    num4 = random.randint(1, 49)
    num5 = random.randint(1, 49)
    num6 = random.randint(1, 10)
    num7 = random.randint(1, 10)
    #Prints out all of the numbers into a readable format.
    print(num1, num2, num3, num4, num5, num6, num7,)


#Calls the "lottery_numbers" function
lottery_numbers()

