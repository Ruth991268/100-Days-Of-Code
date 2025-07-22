# print ("hello"[0]) # Output: h subscript
# print(123+456)
# #lagre numbers in  python 123,456,666 is treated as 123_456_666
# print(123_456_666) # Output: 123456666
# print(type(123)) # Output: <class 'int'> check the type of the variable

# number=len(input("what is your name"))
# number=str(number) # convert int to string
# print(type(number)) # Output: <class 'str'> check the type of the variable
# print("your name has " + number + " characters") # Output: your name has 4 characters 
# #the main idea is to convert the int to string so that we can concatenate it with the string 
# print(str(123)+str(456)) # Output: 123456
          

# #exercise  input a nuber and ad the digits together
# number=input("type a two digit number: ")
# print(type(number)) # Output: <class 'str'> check the type of the variable
# first_digits=number[0]
# second_digits=number[1]
# print(int(first_digits)+int(second_digits))



# #math operations
# print(3*3) # Output: 9
# print(3/3) # Output: 1
# print(type(3/3)) # Output: float
# print(2**3) # Output: 8 power 
# #PEMDAS Parentheses exponent multiplication division addition substruction.
# # print(3*3+3/3-3) # Output: 7.0
# # print(3*(3+3)/3-3) # Output: 3.0

# #bmi calculator
# height =input("enter your  height in meter:")
# weight =input("enter your weight in kg:")
# bmi=int(weight)/float(height)**2
# print(bmi)

# #data mainupulation
# print(8/3) # Output: 2.6666666666666665
# print(round(8/3)) # Output: 3 round to the nearest integer
# print(round(8/3,2)) # Output: 2.67 round to 2 decimal places 
# print(type(8//3)) # Output: 2 floor division its data type int even if we use divison and its is rounded the main idea is //
# x=20//2
# print(x) # Output: 2.5
# x/=2 # Output: 2.5
# print(x) # Output: 1.25
# print(type(x)) # Output: <class 'float'>    
# #  #f-string
# score=0 
# height=1.8
# isWinning=True  
# print(f"your score is {score}, your height is {height}, you are winning is {isWinning}") # Output: your score is 0, your height is 1.8, you are winning is True


# #exercise
# #days , weeks , monyth left to live  if we live upto 90 years old

# age =input("what is your current age?")

# age_left=90-int(age)
# print(age_left)
# days_left=age_left*365 
# week_left=age_left*52
# month_left=age_left*12
# print(f"you have {days_left} days, {week_left} weeks, and {month_left} months left to live if you live upto 90 years old") # Output: you have 29200 days, 416 weeks, and 96 months left to live if you live upto 90 years old What we did here is that, instead of concatenating each one, we just write it in the. A. Form, so it is easy.
 
 #exercise tip calculator
print("Welcome to the tip calculator!")
total=float(input("total bill: $"))
tip=int(input("what percent tip would you like to give ?10,12,15"))
number_of_people=int(input("how many people to split the bill?"))
money=total+(total*tip/100)
indiv=money/number_of_people
indiv=round(indiv,2) # round to 2 decimal places
print(f"each person is paying {indiv}")
