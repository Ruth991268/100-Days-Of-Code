# word_list=["python", "java", "javascript", "hangman", "programming", "developer", "computer", "science", "algorithm", "function"]

# import random
# word=random.choice(word_list)
# print(word)
# guess=input("guess a letter:").lower()
# for c in range(0, len(word)):
#     if  guess in word:
#       print("correct")
#     else:
#       print("incorrect")    
word_list=["python", "java", "javascript", "hangman", "programming", "developer", "computer", "science", "algorithm", "function"]

import random
word=random.choice(word_list)
print(word)
display=[]
for i in range(len(word)):
   display+='_'
print(display)
# for i in word:
#     display+="_"
# print(display) 
while "_"in display:
     guess=input("guess a letter:").lower()
     for position in range(len(word)):
      letter=word[position]
      if letter==guess:
       display[position]=letter
     print(display)       
       
