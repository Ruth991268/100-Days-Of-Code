# programming_dictinary={
#     "bug": "An error in a program that prevents the program from running as expected.",
#     "function": "A block of code that only runs when it is called.",    
#     "loop": "The action of doing something over and over again.",
#     123:"1233"
# }
# print(programming_dictinary["loop"])

# print(programming_dictinary[123])
# programming_dictinary["jh"]="the action of lala"
# print(programming_dictinary)
# #programming_dictinary={}   wappinf all items in a dictionary
# programming_dictinary["bug"]="A moth in your computer"
# print(programming_dictinary)
# for x in programming_dictinary:
#     print(x) # out put bug,function,loop,123 dispay the keys
#     print(programming_dictinary[x])  # display the values 
#     #as it loops it display key then value key vale..  


# #exersis
# student_scores={
#     "Harry":81, 
#      "Ron":78,
#      "Hermione":99, 
#      "Draco":74,
#      "Neville":62}
# student_grades={}
# for student in student_scores:
#       score= student_scores[student]
#       if score>90:
#           student_scores[student]="Outstanding"
#       elif score>80:
#           student_scores[student]="Exceeds Expectations"
#       elif score>70:
#           student_scores[student]="Acceptable"
#       else:
#           student_scores[student]="Fail"
# print(student_scores)

#         # #Nesting
# capitals={
#     "France":"Paris", 
#     "Germany":"Berlin"}
# travel_log={
#     "france":["paris","lille"],
#     "germany":["Berlin","Hamburg"],
# }
# travel_logg={
#  "France":{"cities_visited":["paris","lille"],
#            "total_visits":12}, 
# "germany":{"france":["paris","lille"], "total_visits":5}},
# tevell={ 
# {"country":"France",
#  "cities_visited":["paris","lille"],
#  "total_visits":12},
# {"country":"Germany","cities_visited":["Berlin","Hamburg"],"total_visits":5}}

# tevell=[
# {"country":"France",
#  "cities_visited":["paris","lille"],
#  "total_visits":12},
# {"country":"Germany","cities_visited":["Berlin","Hamburg"],"total_visits":5}]

# travel_log={
#     "france":["paris","lille"],
#     "germany":["Berlin","Hamburg"],
# }
# travel_logg={
#  "France":{"cities_visited":["paris","lille"],
#            "total_visits":12}, 
# "germany":{"france":["paris","lille"], "total_visits":5}}, 
# travel_lo=[
#     {"country":"russua",
#      "tottal_visted":2,
# "city_visted":["moscow","st petersburg"]},
# },
# ]

#exercise 
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

x = {}  # This will store all bids with name as key

name = input("Enter your name: ")
bid_prise = int(input("Enter your bid price: "))
x[name] = bid_prise  # Save first bidder

other_bidders = input("Are there any other bidders? Type 'yes' or 'no': ").lower()

while other_bidders == "yes":
    clear_console()  # Clear screen before next bidder enters
    name = input("Enter your name: ")
    bid_prise = int(input("Enter your bid price: "))
    x[name] = bid_prise  # Add next bidder
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no': ").lower()

# Find the highest bid and winner
highest_bid = 0
winner = ""

for bidder in x:
    if x[bidder] > highest_bid:
        highest_bid = x[bidder]
        winner = bidder

print(f"\nThe winner is {winner} with a bid of ${highest_bid}.")

