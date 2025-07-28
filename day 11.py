# import random
# x=input("do you want to play blackjack ?Type 'y' or 'n'").lower()
# your_card=random.randint(1, 11)
# computer_card=random.randint(1,11)
# def closest(your_card,computer_card,k):
#     if abs(your_card - k) < abs(computer_card - k) :
#         if(your_card<=21):
#           return "You win!"
#     elif abs(your_card - k) > abs(computer_card - k):
#           if(your_card<=21):
#             return "Computer wins!"
#     else:
#         return "It's a draw!"
# k=21
# while True:
#     x=input("do you want to play again ?Type 'y' or 'n'").lower()
#     if x == "n":
#         print("Thanks for playing!")
#         break
#     elif x == "y":
#         your_card = random.randint(1, 11)
#         computer_card = random.randint(1, 11)
#     else:
#         print("Invalid input. Please type 'y' or 'n'.")
#         continue
# print(f"Your card is {your_card} and computer's card is {computer_card}")
# x=closest(your_card, computer_card, k)
# print(x)
import random
def deal_card (): 
 """return random card"""
 cards=[11,2,3,4,5,6,7,8,9,10,10,10,10] 
 card=cards.random.choice(card)
 return card
user_card=[]
computer_card=[]
for _ in range(2): 
   new_card=deal_card()
   user_card.append(new_card)
   computer_card.append(new_card)
def calculate_score(cards):
   if sum (cards)==21 and len(cards)==2:
       return 0 
       return sum(cards) 
   
