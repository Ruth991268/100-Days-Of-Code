# def greet():
    
#     print("Hello, World!")
# greet()

# def greet(some):
    
#     print(f"Hello, World! {some}")
# greet("Python is great") 
# # some is the parameter and "Python is great" is the argument


# #function with more than one input
# def fr(name, location):
    
#     print(f"Hello, {name} from {location}!")
# fr("jack bauer","usa")    
# #the order we give the arguments matters, so we have to give the name first and then the location, otherwise it will not work as expected.
# # we can also give the arguments in any order by using the parameter name, like this:

# print(f"Hello, {name} from {location}!")




# # exersise how much paint required to paint a wall
# import math
# coverage=int(input("enter coverage")) # coverage of one can of paint in square meters
# width=int(input("enter the width of your wall"))
# height=int(input("enter the hight  your wall"))

# def paint(width,height,coverage):
#     number_of_can=math.ceil((width*height)/coverage) 
#     print (f"you will need {number_of_can}")
# paint(width,height,coverage)  





# #2 way
# import math
# coverage=int(input("enter coverage")) # coverage of one can of paint in square meters
# width=int(input("enter the width of your wall"))
# height=int(input("enter the hight  your wall"))

# def paint(width,height,coverage):
#     number_of_can=math.ceil((width*height)/coverage) 
#     return number_of_can
# number_of_can=paint(width,height,coverage)  

# print (f"you will need {number_of_can}")






# #prime number checker 
# n=int(input("enter a number to check if it is prime or not: "))
# def prime(n):
#     is_prime=True 
#     for i in range(2,n):
#      if n%i==0:
#            is_prime=False
#     if is_prime:
#         print(f"{n} is a prime number")
#     else:
#          print(f"{n} is not  prime number")
 # prime(n)         


# project Caesar cipher
# #simple one
# alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
#           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n")) 
# def encrypt(text,shift):    
#     l=text[shift:]+ text[:shift]
#     print(f"The encoded text is {l}")
# encrypt(text,shift)   
# 
# 
# 
#  
# alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
#           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
#           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n")) 
# def encrypt(textother,shiftother):
#     cipher_text=""    
#     for letter in textother: 
#         position=alphabet.index(letter)
#         new_position=(position+shiftother)
#         new_letter=alphabet[new_position]
#         cipher_text+=new_letter
#     print(f"The encoded text is {cipher_text}")        
 

# def decrypt(chipher_text,shiftother):
#       plain_text=""
#       for letter in chipher_text: 
#         position=alphabet.index(letter)
#         new_position=(position- shiftother)
#         new_letter=alphabet[new_position]
#         plain_text+=new_letter
#       print(f"The decoded text is {plain_text}") 

# if direction=="encode":   
#    encrypt(textother=text,shiftother=shift)    
# elif direction=="decode":
#    decrypt(chipher_text=text,shiftother=shift) 
# else:
#     print("invalid input")     


from art import logo 
print(logo)
alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
          'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
          'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
should_continue = True
while should_continue:
 direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
 textother= input("Type your message:\n").lower()
 shiftother = int(input("Type the shift number:\n")) 
 shiftother=shiftother % 26  # to handle shifts greater than 26

	
 def encrypt(textother,shiftother):
    cipher_text=""    
    for letter in textother: 
    #   numbers and symbole is the if statmeny
      if letter in alphabet:
         position=alphabet.index(letter)
         if direction=='encode':
           new_position = (position + shiftother)
         else:
          new_position = (position + shiftother)
        
         cipher_text+=alphabet[new_position]  
      else:
           cipher_text+=letter       
    print(f"The encoded text is {cipher_text}")
 encrypt(textother,shiftother) 
 result=input("Do you want to continue? Type 'yes' or 'no': ").lower()
 if result == 'no':
		should_continue = False
		print("Goodbye!") 
   

