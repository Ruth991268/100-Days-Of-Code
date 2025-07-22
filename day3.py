#if/else 
#if condition:
#do this
#else:
#do this

# print("welcome to the rollercoaster!")
# height=int (input("what is your height in cm?"))
# if height>=120:
#     print("you can ride the rollercoaster!")
# else:
#     print("sorry, you are not tall enough to ride the rollercoaster.")      





# #check if even or odd
# number=int(input("enter a number"))
# if number % 2 ==0:
#     print("this is an even number")
# else:
#     print("this is an odd number")    




#nested if/else
#if condition:
  #if condition:
    #do this
   #else:
     #do this
#else:
 #do this



# #exerise foucus on each postion of if ,print,rlse 
# number=int(input("enter a number"))
# if number >=120:
#     print("you can ride the rollercoaster!")
#     age=int(input("enter a age"))
#     if age>5:
#      print("u pay 5$")
#     elif age>12:
#      print("u pay 10$")
#     else:
#      print("u pay 15$")    

# else:
#     print("you cant ride the rollercoaster")    






# #exercise bmi calculator but have range

# print("welcome to the bmi calculator")
# height=float(input("enter your height in meters:"))
# weight= float(input("enter your weighr in kg:"))
# bmi=round(weight/(height**2))
# print(f"your bmi is {bmi}")
# if bmi<18.5:
#     print("you are underweight")
# elif bmi<25:
#     print("you have a normal weight")
# elif bmi<30:
#     print("you are overweight") 
# elif bmi<35:
#     print("you are obese")
# else:
#     print("you are clinically obese")          
 
 

# #exercise leap year
# print("welcome to the leap year calculator")
# year=int(input("enter a year:"))
# if year %4==0:
#    if year%100==0:
#        if year%400==0:
#           print("its a leap year")
#        else:   
#          print("its a not leap year")
#    else:   
#        print("its a  leap year")
        
# else:
#   print("its not a leap year")



# #multiple if statements The first checks their each at the same time And we created another if statement that checks if they want an image or not. To show that. It should be indated in the same line so that they are equally positive statements.
# number=int(input("enter a height"))
# bill=0
# if number >=120:
#     print("you can ride the rollercoaster!")
#     age=int(input("enter a age"))
#     if age<10:
#      bill=5 
#      print("child tickets 5$")
#     elif age<16:
#      bill=10
#      print("youth  10$")
    
#     else: 
#      print("adult pay 15$")
#      bill=15    
#     photo=input("do you want a pic? Y or N ")
#     if photo=="y" :
#        bill+=3
#     print(f"you can  ride the rollercoaster and your total bill is {bill}")
    
# else:
#     print(f"you cant ride the rollercoaster ")    




# exericse pizza ordering

# print("hey welcone to pyton pizza delivery ")
# size=input("do you want large , medium or samll pizza say l,m,s")
# pepperoni=input("do you want pepperpni yes y and no n")
# chesse=input("do you want an extra chesse yes y and no n")
# bill=0
# if size=="s":
#     bill+=15
# elif size=="m":
#     bill+=20
# elif size=="ll":
#     bill+=25
# print(bill)    
# if pepperoni=="y":
#     if size=="s":
#      bill+=2
#     elif size=="m":
#      bill+=3
#     elif size=="l":
#      bill+=3    
# if chesse=="y":
#     bill+=1
#     print(f"you have orderd succfuly {bill} ")      

#mutiple condtion in the same line here is where logical operation comes in 


       
# number=int(input("enter a height"))
# bill=0
# if number >=120:
#     print("you can ride the rollercoaster!")
#     age=int(input("enter a age"))
#     if age<10:
#      bill=5 
#      print("child tickets 5$")
#     elif age<16:
#      bill=10
#      print("youth  10$")
#     elif age<55 and age>45:
#       print("free") 
#     else: 
#      print("adult pay 15$")
#      bill=15    
#     photo=input("do you want a pic? Y or N ")
#     if photo=="y" :
#        bill+=3
#     print(f"you can  ride the rollercoaster and your total bill is {bill}")
    
# else:
#     print(f"you cant ride the rollercoaster ")    



# # exerise love calaulator
# print("welcome to the love calculator")
# name1= input("enter your name\n")
# name2= (input("enter your their\n"))
# combine=name1+name2
# combine_lower=combine.lower()

# t=combine_lower.count("t")
# r=combine_lower.count("r")
# u=combine_lower.count("u")
# e=combine_lower.count("e")
# true=t+r+u+e
# l=combine_lower.count("l")
# o=combine_lower.count("o")
# u=combine_lower.count("v")
# e=combine_lower.count("e")
# love=l+o+u+e
# score=str(true)+str(love)
# print(score) 


print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

choice1 = input("You're at a crossroad. Where do you want to go? Type 'left' or 'right': ").lower()
if choice1 == "left":
    choice2 = input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across: ").lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ").lower()
        if choice3 == "red":
            print("It's a room full of fire. Game Over.")
        elif choice3 == "yellow":
            print("You found the treasure! You Win!")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You got attacked by an angry trout. Game Over.")