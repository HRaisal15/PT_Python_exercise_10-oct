# Program to generate a random number between 0 and 100

# importing the random module
import random

num = random.randint(0,100)

# output username
print("Hi.. My name is Mr. Laptop, I have chosen an interger between 1-100. Can you guess what it is? ")

#first score 100
score = 100

while True:
    bil = int(input("Enter your guess number : "))

    #show the message based on number
    if (bil < num):
        print("Sorry, your guess number is too low")
        score = score - 5
    elif (bil > num):
        print("Sorry, your guess number is too high")
        score = score - 5
    elif (bil == num):
        print ("Yes, you are right. The Number is ",num,". Congratulations!")
        break

print("Your score is ",score,)

# say goodbye
print("OK.. see you later")
