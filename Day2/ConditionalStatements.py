# Conditional statements
# if, if...else, elif

#----------------------------------------
# Example1: Eligible for vote

# age = int(input("Enter your age:"))
# if age >= 18:
#     print("Eligible to vote")
# else:
#     print("Not eligible to vote")
#----------------------------------------
# Example2: Using direct boolean values

# if False:
#     print("True condition")
# else:
#     print("False condition")
#----------------------------------------
# Example3: Using direct boolean values

# if 0:
#     print("one")
# else:
#     print("Not one")
#----------------------------------------
#Example 4: Find if the number is even or odd

# Num=11
# if Num%2 == 0:
#     print("Even number:")
# else:
#     print("Odd number")
#----------------------------------------
# Example 5: even odd for input value

# Num = int(input("Enter a number:"))
# if Num%2 == 0:
#     print("Even number")
# else:
#     print("Odd number")
#----------------------------------------
# Example 6: Write the code in single line (TERNARY Operator)
# num=15
# print("Even number") if num%2 == 0 else print("Odd number")
#----------------------------------------

# Example 7: Multiple statements in single line
# num = 5
# {print("Hello"),print("Python")} if num>=10 else {print("Hi"), print("Java")}
#----------------------------------------

# Ex 8: Elif statement for multiple conditions

WeekNum = int(input("Enter the week number:"))
if WeekNum == 1:
    print("Sunday")
elif WeekNum == 2:
    print("Monday")
elif WeekNum == 3:
    print("Wednesday")
elif WeekNum == 4:
    print("Thursday")
elif WeekNum == 5:
    print("Friday")
elif WeekNum == 6:
    print("Saturday")
else:
    print("Invalid week number")
