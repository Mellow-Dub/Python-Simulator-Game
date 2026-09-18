#Day 2 begins

print ("You wake up in your bed and turned around to look at the clock and it's says 9:30 Am \n")
print ("You stand up feeling tired and went to the kitchen to get a cup of coffee")
print ("You made yourself a cup of coffee and drank it but it feels weird. But you didn't care and went to your bedroom to change clothes.")

print (" While you was changing you heard a knock at the door. \n")
choice = input("You decide if you want answer it of leave it \n")

if choice == "Answer it" or choice == "Yes" or choice == "yes" or choice == "answer it":
    print ("You went to the door and answered it and it was no one. Probably kids ding dong ditching \n")
elif choice == "Leave it" or choice == "leave it":
    print ("You was to lazy and mind your own busniess \n")
else:
    while choice not in ["Answer it" , "answer it" , "Yes" , "yes" , "Leave it" , "leave it"]:
        print ("Dude what are you doing? Think! \n")
        choice = input("You decided to ignore does options but you are forced todo so \n")

import time

print ("After that you went a walk to your friend place to meet up and have a talk. It might take 10 Minutes so you let time pass by. \n")
time.sleep(5)

Minutes = 10
for i in range (10):
    Minutes -= 1
    print ("Walking... Minutes: " , Minutes)
    time.sleep(3)

print ("You have reached to your destination and knock at your friends house \n")
time.sleep(2)

for i in range(3):
    print ("Knock...")
    time.sleep(3)

print ("You waited...")
print ("Then you heard a noise in the house \n")
choice_2 = input("Should you wait or say something?")

if choice_2 == "Wait" or choice_2 == "wait":
    print(" you waited and he open the door")
elif choice_2 == "Say something" or choice_2 == "say something":
    print("You said that is there someone there and weirdly no one responded back. Then the door opens at your friend apologise for not responding back.")
else:
    while choice_2 not in ["Wait" , "wait" , "Say something" , "say something"]:
        print ("There's no options rather these soyou have to pick one")
        choice_2 = input("You have to pick another option")

print ("Hey so what should we do today?")
choice_3 = input("Choose either Calculator, Diary, Play or Go for a walk \n ")

#Calculator

if choice_3 == "Calculator":
    number_1 = float(input("What number should you pick? \n"))
    number_2 = float(input ("Now what number should the second number be? \n"))
    operator = input ("Now choose your operator! \n")

    if operator == "+" or operator == "Plus":
        print (number_1 + number_2)
    elif operator == "-" or operator == "Minus":
        print (number_1 - number_2)
    elif operator == "/" or operator =="Divide":
        print (number_1 / number_2)
    elif operator == "*" or operator == "Multiply":
        print (number_1 * number_2)
    elif operator == "**" or operator == "Powers":
        print (number_1 ** number_2)
    elif operator == "%" or operator == "Remainder":
        print (number_1 % number_2)
    else:
        while operator not in ["+" , "-" , "/" , "*" , "**" , "%" , "Plus" , "Minus" , "Divide" , "Multiply" , "Powers" , "Remainder"]:
         print ("That's not a operator in a Simple Calculator, try a diffrent one")
        operator = input ("Pick another operator \n")

#Diary

elif choice_3 == "Diary":    
    print ("Write something")
    Diary = input()

#Play

elif choice_3 == "Play":
    print ("You and your friend decided to play basketball and have fun \n")

#Walk

elif choice_3 == "Walk" or choice_3 == "Go for a walk":
    print ("You and your friend walked for 20 Min, it was a bit boring but still had fun \n")

else:
    while choice_3 not in ["Calculator" , "Diary" , "Play" , "Walk"]:
        print ("um there are no other choice than this")
        choice_3 = input ("Please select a diffrent option")

print ("Well that was fun, let's go to the Las Vegas tomorrow got it? \n")
print ("You nod and went straight back home to rest.")

#Day 2 Finished