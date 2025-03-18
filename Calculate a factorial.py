num = int(input("Enter the integer you want a factorial of: "))

if num < 0:
    print("Please enter a non-negative integer.")
else:
    factorial = 1

    for i in range(1, num + 1):
        factorial *= i

    print(f"The factorial of {num} is: {factorial}") 
