# fruits =["apple","peach","pear"]
# for x in fruits:
#     print(x)
#     print(x+"pie")
#     print(fruits)
# print(fruits)    


#exersise 2 ava height 
#method one the easy one
# student_height = input("inter your name").split(",")
# for n in range(0, len(student_height)):
#     student_height[n] = int(student_height[n])
# print(len(student_height))
# print(sum(student_height))
# print(round(sum(student_height)/len(student_height)))


# student_height=(input("enter the list of height in your class").split(","))
# print(student_height)
# for n in range(0,len(student_height)):
#     student_height[n]=int(student_height[n])
# print(student_height)
# total=0 
# #total 
# for height in student_height:
#      total+=height
# print(total)
# #ava using for  
# avarge=round(total/len(student_height))
# print(avarge)
# #using for loop to find length length     
# number_of_students=0
# for students in student_height:
#      number_of_students+=1 
# print(number_of_students)    




# #max(student_score)
# #max using 
# student_score=input("enter list for your exam score").split(",")
# for n in range(0,len(student_score)):
#     student_score[n]=int(student_score[n])
# print(student_score)
# highest_score=0   
# for c  in student_score:
#     if c>=highest_score:
#         highest_score=c
#     else:
#         highest_score
# print(highest_score)         




##for loop indpendent on list -range
## for number in range(a,b):
##not including b            


# for number in range(1,10):
#     print(number)
#increase in any amt 
# for number in range(1,11,3):
#     print(number)





# #sum of numbers form 1,100
# x=0
# for number in range(1,101):
#     x+=number
# print(x)    


# #sumof even number1-100
# #method 1
# x=0
# for number in range(0,101,2):
#     x+=number
# print(x)   
# #method 2 
# y=0
# for number in range(0,101):
#     if number%2==0:
#         y+=number
# print(y)   
# 
# 
#      
#       #exerise div 3,5 and both game
# for number in range (0,101):
#     if  number%3==0 and number%5==0:
#         print("fizznuzz")
#     elif number%5==0:
#         print("buzz")
#     elif number%3==0 :
#         print("fizz")
#     else:
#         print(number)    







# import random

# print("Welcome to Password Generator")

# # Get user input for password characteristics
# user_letters = int(input("How many letters would you like in your password? "))
# user_symbols = int(input("How many symbols would you like? "))
# user_numbers = int(input("How many numbers would you like? "))

# # Define possible characters
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# # Initialize the password variable
# password = ""

# # Generate random letters
# for letter in range(user_letters):
#     random_letter = random.choice(letters)
#     password += random_letter  # Add the random letter to the password

# # Generate random symbols
# for symbol in range(user_symbols):
#     random_symbol = random.choice(symbols)
#     password += random_symbol  # Add the random symbol to the password

# # Generate random numbers
# for number in range(user_numbers):
#     random_number = random.choice(numbers)
#     password += random_number  # Add the random number to the password

# # Print the generated password
# print(f"Your password is: {password}")

# So for this one, we wanted to shuffle it. So in order to shuffle it, we needed to create a list. So how do we create a list fom differnt input we need to  Apende 


import random
print("there there welcome to password genetor ")
user_letters=int(input(" enter the number  letter"))
user_symbols=int(input("enter the number of   symbol"))
user_numbers=int(input("enter the number of numbers you want to have"))
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
password=[]
for n in range(1, user_numbers+1):
    random_number=random.choice(numbers)
    password.append(random_number)
for u in range(1, user_symbols+1):
    random_symbol=random.choice(symbols)
    password.append(random_symbol)
for nm in range(1, user_letters+1):
    random_letter=random.choice(letters)      
    password.append(random_letter)
random.shuffle(password)
print(password)   
final="" 
for n in password:
    final+=n
print(final)    