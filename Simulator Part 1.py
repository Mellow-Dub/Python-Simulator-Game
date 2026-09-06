#Sign up Simulator Part 1

print ("Hello and Welcome to my website! please sign up \n")
username = input ("Please enter your username \n")
password = input ("Please enter your password \n")

print ("Alright what do you want to do first? Maybe Youtube or Paint? \n")
choice = input()


if choice == "Youtube" or choice == "youtube":
    print ("You are watching a cat dance \n")

elif choice == "Paint" or choice == "paint":
    print ("You are drawing a circle \n")

else:
    while choice not in ["Youtube" , "youtube" , "paint" , "Paint"]:
        print ("That's not an option you silly! \n")
        choice = input ("Choose another word \n")

print ("Great! That was fun, but there are still more to do! \n")
print ("Huh, your hungry? i got food at home! look in my fridge \n")
choice_2 = input("Now choose, Soup or Burger? \n")

if choice_2 == "Soup" or choice_2 == "soup":
    print ("Huh i though you will pick the burger but whatever. Atleast your healthy!\n")
elif choice_2 == "Burger" or choice_2 == "burger":
    print ("Quite unhealthy but atleast your not hungry! \n")
else:
    while choice_2 not in ["Soup" , "soup" , "burger" , "Burger"]:
        print ("There are no other food rather than these two. Pick another food! \n")
        choice_2 = input ("Choose another food \n")

print ("Huh, is getting dark outside. We see eachother tomorrow alright? bye! \n")
print ("You decided to go back home and rest. \n")

print ("That's it! This is the ending! Bye! \n")
print ("Day 1 is Finished")

#Day 1 Finished
