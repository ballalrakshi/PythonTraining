# input from the console is considered as String
# num1 = input("Enter 1st number:") #1
# num2 = input("Enter 2ndd number:") #2
# print(type(num1)) # <class 'str'>
# print(type(num2)) # <class 'str'>
# print(num1+num2) # 12

#Approach1
# Approach to convert input to num so that it will be considered as number
# num1 = int(input("Enter 1st number:")) #1
# num2 = int(input("Enter 2ndd number:")) #2
# print(type(num1))  #int
# print(type(num2)) #int
# print(num1+num2) #3

#Approach2 for integers
#Approach convert into int while calculating and printing the result
num1 = input("Enter 1st number:") #1
num2 = input("Enter 2ndd number:") #2
print(type(num1)) # <class 'str'>
print(type(num2)) # <class 'str'>
print(int(num1)+int(num2)) # 3

#Approach3 for decimals(float)
#Approach convert into int while calculating and printing the result
num1 = input("Enter 1st number:") #1
num2 = input("Enter 2ndd number:") #2
print(type(num1)) # <class 'str'>
print(type(num2)) # <class 'str'>
print(float(num1)+int(num2)) # 3