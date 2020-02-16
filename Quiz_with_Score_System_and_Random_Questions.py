#Python Math Quiz with Score System and Randomized Questions by Dylan Wilson



#Imported Libraries
import random



#User Data
username = input("Enter a username: ")


#Defining the Quiz Function
def quiz():

    #Sets the score and the level vaules to 0
    score = 0
    levelNumber = 0


    #Generates 2 Random Numbers between 1 and 100
    num1q1 = random.randint(1, 100)
    num2q1 = random.randint(1, 100)
    #Outputs the Question
    print("What is", num1q1, "+", num2q1, "?")
    #Creates a user input for the user to enter the answer using an integer data type
    userinputQ1 = int(input(" "))
    #If the answer is correct
    if userinputQ1 == num1q1 + num2q1:
        #Outputs "Correct Answer" to the user
        print("Correct Answer!")
        #Add 1 to the score
        score = score + 1
        #If the user enters an incorrect answer, also prints out the correct answer
    else:
        print("Incorrect Answer! The Correct answer was", num1q1 + num2q1)


    #Generates 2 Random Numbers between 1 and 100
    num1q2 = random.randint(1,100)
    num2q2 = random.randint(1,100)
    #Outputs the Question
    print("What is", num1q2, "+", num2q2, "?")
    #Creates a user input for the user to enter the answer using an integer data type
    userinputQ2 = int(input(" "))
    #If the answer is correct
    if userinputQ1 == num1q2 + num2q2:
        #Outputs "Correct Answer" to the user
        print("Correct Answer!")
        #Add 1 to the score
        score = score + 1
    else:
        #If the user enters an incorrect answer, also prints out the correct answer
        print("Incorrect Answer! The Correct answer was", num1q2 + num2q2)

    #Generates 2 Random Numbers between 1 and 100
    num1q3 = random.randint(1, 100)
    num2q3 = random.randint(1, 100)
    #Outputs the Question
    print("What is", num1q3, "+", num2q3, "?")
    #Creates a user input for the user to enter the answer using an integer data type
    userinputQ3 = int(input(" "))
    #If the answer is correct
    if userinputQ1 == num1q3 + num2q3:
        #Outputs "Correct Answer" to the user
        print("Correct Answer!")
        #Add 1 to the score
        score = score + 1
    #If the user enters an incorrect answer, also prints out the correct answer
    else:
        print("Incorrect Answer! The Correct answer was", num1q3 + num2q3)


    #Printing out the final score
    print("Your final score is", score)

#Calling the Quiz Function
quiz()
