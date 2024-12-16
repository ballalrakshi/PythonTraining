def find_largest(number1, number2):
    if number1 > number2:
        return number1
    else:
        return number2


Number1 = float(input("Enter the 1st number: "))
Number2 = float(input("Enter the 2nd number: "))
if Number1 == Number2:
    print("Numbers are equal")
else:
    result = find_largest(Number1, Number2)
    print(f"{result} is the largest number")
