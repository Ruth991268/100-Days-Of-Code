# enemies=1
# def increase_elemies():
#     enemies=2
#     print(f"enemies {enemies}")
# increase_elemies()
# print({enemies})  # out putenemies 2  {1}  
 


#  #localscope 

# def drink_portion():
#     potion_strenth=2
#     print(potion_strenth)
# drink_portion()
# print(potion_strenth)  #eror only acssed in only in function


# #globalscope
# player_health=10
# def drink_portion():
#     potion_strenth=2
#     print(potion_strenth)
# drink_portion()
# print(player_health)



# # guessing game mine 
import random
print("welcome to the number guessing game\n")
print("i am thinking of a number 1and 100")
level=input("type 'easy' or hard ").lower()
target=random.randint(1,100)
y=10 
z=5  

if  level=="easy" :
  number=int(input("guess the number"))

  for x in range(10):
     y-=1
     print(f"you have {y} try left")
     if number>target:
       print("to high")
     elif number<target:
       print("too low ") 
     else:
       print("correct congra")  
     number=int(input("guess the number")) 
elif  level=="hard" :
  z-=1
  print(f"you have {z} try left")
  number=int(input("guess the number"))
  for x in range(5):
     print(f"you have {x-10} try left")
     if number>target:
       print("to high")
     elif number<target:
       print("too low ") 
     else:
       print("correct congraution")  
       break
     number=int(input("guess the number"))   

       
      
     


#method 2  vid
# import random
# def check_answer(guess, answer, turns):
#     """Check guess and return updated turns."""
#     if guess > answer:
#         print("Too high")
#         return turns - 1
#     elif guess < answer:
#         print("Too low")
#         return turns - 1
#     else:
#         print(f"Correct, congratulations! The number was {answer}.")
#         return 0  # End game on correct guess

# def set_difficulty():
#     level = input("Choose a difficulty (type 'easy' or 'hard'): ").lower()
#     if level == "easy":
#         return easylevel
#     return hardlevel  # Default to hard for any other input

# # Constants
# easylevel = 10
# hardlevel = 5

# while True:  # Replay loop
    
#     print("Welcome to the Number Guessing Game!\n")
#     print("I'm thinking of a number between 1 and 100")
    
#     answer = random.randint(1, 100)
#     turns = set_difficulty()
#     print(f"You have {turns} attempts.")

#     # Main game loop
#     while turns > 0:
#         # Validate input with while loop
#         valid = False
#         while not valid:
#             guess_str = input("Make a guess: ")
#             if guess_str.isdigit():
#                 guess = int(guess_str)
#                 if 1 <= guess <= 100:
#                     valid = True
#                 else:
#                     print("Please enter a number between 1 and 100.")
#             else:
#                 print("Invalid input. Please enter a number.")
        
#         turns = check_answer(guess, answer, turns)
#         if turns > 0 and guess != answer:
#             print(f"You have {turns} attempts left.")
#         elif guess == answer:
#             break
    
#     if turns == 0 and guess != answer:
#         print(f"Game over! You ran out of attempts. The number was {answer}.")

#     # Ask to replay
#     replay = input("Play again? Type 'y' or 'n': ").lower()
#     if replay != 'y':
#         print("Thanks for playing!")
#         break