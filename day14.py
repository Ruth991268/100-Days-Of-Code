# import random
# from  game_data import data
# random_person1=random.choice(data)
# random_person2=random.choice(data)
# follower1=random_person1['follower_count']
# follower2=random_person2['follower_count']
# score=0
# while score>=0:
#  print(f"compare the follower of {random_person1['name']}{random_person1['description']} vs {random_person2['name']}{random_person2['description']}")

#  choice=int(input("which one has more follower text 1 for the first person and 2 for the second person"))
#  random_person1=random.choice(data)
#  random_person2=random.choice(data)
#  if follower1>=follower2 and choice==1:
#    print("you are correct")
#    score+=1
#    print(score)
#  elif follower2>=follower1 and choice==2:
#    print("you are correct")
#    score+=1  
#    print(score)
#  else:
#    print(f"you are incorrect ")
#    score-=1   
#    print(score) 

import random
from game_data import data
from welcome import x
score = 0
total = 0

print(x)

while score >= 0:
    random_person1 = random.choice(data)
    random_person2 = random.choice(data)
    while random_person1 == random_person2:
        random_person2 = random.choice(data)
    follower1 = random_person1['follower_count']
    follower2 = random_person2['follower_count']
    
    print(f"compare the follower of {random_person1['name']}{random_person1['description']} vs {random_person2['name']}{random_person2['description']}")

    choice = int(input("Which one has more followers? Type 1 for the first person and 2 for the second person: "))

    if follower1 >= follower2 and choice == 1:
        print("You are correct!")
        score += 1
        total += 1
        print(f"Score: {score}")
    elif follower2 >= follower1 and choice == 2:
        print("You are correct!")
        score += 1
        total += 1
        print(f"Score: {score}")
    else:
        print("You are incorrect.")
        score = -1
        print(f"Total correct answers: {total}")
