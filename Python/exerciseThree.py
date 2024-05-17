#Exercise: Calculate the Factorial of a Number
#1. Define a function called `calculate_factorial` that takes in one parameter, `number`.
#2. Inside the function, write code to calculate the factorial of the given number.
#3. The factorial of a number is the product of all positive integers less than or equal to that number. 
#For example, the factorial of 5 is 5 * 4 * 3 * 2 * 1 = 120.
def calce_faulatctorial(numb):
    result = 1
    for i in range(1, numb + 1):
        result *= i
    return result



def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example usage:
number = 5
print("Factorial of", number, "is", calce_faulatctorial(number))
