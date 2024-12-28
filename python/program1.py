def calc(num1,num2):
    add = 0
    multiply = 0
    add = num1 + num2
    multiply = num1 * num2
    if multiply > 1000:
        return add
    else:
        return multiply
num1 = int(input("What's your first number? "))
num2 = int(input("What's your second number? "))
answer = calc(num1,num2)
print(f"The answer is {answer}")
