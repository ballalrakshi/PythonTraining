# Function to check the number is positive, negative or zero

def check_num(num):
    if num > 0:
        return "positive"
    elif num < 0:
        return "negative"
    else:
        return "zero"

Number = float(input("Enter a number: "))
result = check_num(Number)
print(f"Number is {result}.")