# import random     #library for random number generation
# random_integer =random.randint(1, 10)  #generates a random integer between 1 and 10 and1,10 
# print(random_integer)  


# import my_module
# #module  i separeate page called my_module i import it and i can yuse it in this page
# print(my_module.pi)  #accessing the variable pi from my_module 


# import random  
# random_float = random.random()  #generates a random float between 0.0 and 1.0 not one
# print(random_float)

# import random
# random_float=random.random()*5
# print(random_float)  #generates a random float between 0.0 and 5.0 

# love_score=random.randint(1, 100)  #generates a random integer between 1 and 100
# print(f"Your love score is {love_score}")  #prints the love score in a


# #heads and tail using random it has 2 possibilities 0or 1 assign t,h for each and (1,0) not possable
# import random
# random_side=random.randint(0,1)
# if random_side==1:
#     print("heads")
# else:
#     print("tails")    





#askpythone

# #offset and appending item to list -1 last one 0 the first 
# x=["a", "b", "c"] 
# print(x)
# x[0]="z"
# print(x) #changes the first item to z
# x.append("d")
# print(x)  #adds d to the end of the list
# x.extend(["e", "f"])  #adds e and f to the end of the list
# print(x)  #prints the list with e and f added
# x.insert(1, "y")  #inserts y at index 1
# print(x)  #prints the list with y inserted at index 1
# x.clear()  #clears the list
# print(x)  #prints the empty list




# #every atm in a bowel and pick one at random and that pays
# import random
# names = input("Give me everybody's names, separated by a comma. ")
# names_list = names.split(", ")  #splits the names by comma and space thislike liste  sepate all the inputin list
# print(names_list)
#  #the long way
# paying=random.randint(0,len(names_list)-1)  #picks a random index from the list
# print(f"{names_list[paying]} is going to buy the meal today!")  #

# # #the short and easy way
# # paying=random.choice(names_list )  #picks a random name from the list
# # print(f"{paying} is going to buy the meal today!")  #prints the name


#index errors 
 #out of range error

# #nested list 
# fruits = ["apple", "banana", "cherry"]
# vegetables = ["carrot", "broccoli", "spinach"]
# food = [fruits, vegetables]  #creates a nested list with fruits and vegetables
# print(food)  #prints the nested list


# #treasure map
# row1= ["a", "⬜️g", "⬜️k"]
# row2= ["⬜d", "⬜️e", "⬜️g"]   
# row3= ["⬜️h", "⬜i", "⬜️j"]
# map = [row1, row2, row3]  #creates a nested list with
# print(f"{row1}\n{row2}\n{row3}")  #prints the nested list    
# position = input("Where do you want to put the treasure? (col,row) ")
# # split=position.split(",")  #splits the input by comma
# # print(split)
# x=int(position[0])   
# y=int(position[1]) 
# map[y-1][x-1]="x"
# print(map) 




#rock paper scissors 
user=input("Enter your choice (rock, paper, scissors): ").lower()  #takes input from the user and converts it to lowercase
import random  #imports the random module
choices = ["rock", "paper", "scissors"]  #creates a list of choices
computer_choice=random.choice(choices)
print(f"Computer chose: {computer_choice}")  #prints the computer's choice
if user==computer_choice:
    print("It's a draw!")  #if the user's choice is the same as the computer's choice, it's a draw
elif user=="rock"and computer_choice=="scissors":
 print("you win")
elif user=="paper"and computer_choice=="rock":
 print("you win")
elif user=="scissor"and computer_choice=="paper":
 print("you win")
else:
  print("you loss") 