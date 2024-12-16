# s = "welcome"
# s = 'welcome'
# s = str('welcome')
# s = str("string")

#Creating empty string variables
# name = ""
# name = ''
# name = str()

#mutable - can NOT change the value of the variable
# immutable - can change the value of variable

# str="welcome"
# print(str+" to Python")    # welcome to Python
# print(str*4) # welcomewelcomewelcomewelcome

# Slicing operators []
#-----------------------
# str="welcome"
#
# print(str[1:3])   #el
# print(str[:6])    #welcom
# print(str[2:])    #lcome
#
# print(str[1:-1])  #elcom


# ASCII
#----------------
# print(ord('A'))    #65
# print(chr(65))    #A

# ex4.	In and Not In operators ----returns true or false
#------------------------------
# s = "welcome"
# print("come" in s)    #-----true
# print("lome" in s)    #-------false
#
# print("come" not in s)    #-----false
# print("lome" not in s)    #-------true

# string comparison
#   == != > >= < <=
# Day 3    https://www.youtube.com/watch?v=9CJhkEje9e8   1.34.30 mins
#
# s = "welcome3"
# print(s.isalnum())   #true
# print(s.isalpha())     #false
# print("welcome".isalpha())

#Reverse string

# s= "welcome"
# rev_str = ""
# for i in s:    #l
#     rev_str= i+rev_str #emoclew
# print("reversed string is: ", rev_str)

#Method2:
s = "welcome"
rev_str = s[::-1]            # s[0:7:-1]
print(rev_str)     #emoclew