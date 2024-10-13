#!/usr/bin/env python3

def admin_login(username, password):
    # Admin credentials
    password = "12345"
    
    # Check if the username is either "admin" or "ADMIN"
    if (username == "admin" or username == "ADMIN") and password == "12345":
        print("Access granted")
    else:
        print("Access denied")
        
# Call the function with the arguments
admin_login("ADMIN", "12345")

def hows_the_weather(temperature):
    if temperature <=40  :
        print("It's brisk out there!")
    elif 40 < temperature <=65  :
        print("It's a little chilly out there!")
    elif (temperature >=85 ) :
        print("It's too dang hot out there!")
    else :
        print("Perfect")
        
hows_the_weather(55)

def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0 :
        print('FizzBuzz')
    elif num % 3 == 0 :
        print('Fizz')
    elif  num % 5 == 0 :
        print('Buzz')
    else:
        print(num)
        
fizzbuzz(9)
fizzbuzz(10)
fizzbuzz(4)

def calculator(operation, num1, num2):
    
    num1 = float(num1)
    num2 = float(num2)
    
    if operation == "+":
        print( num1 + num2)
    elif operation == "-":
        print( num1 - num2)
    elif operation == "*":
        print( num1 * num2)
    elif operation == "/":
        if num2 != 0:  # Avoid division by zero
            print(num1 / num2)
        else:
            print("Error: Division by zero!")
    else:
        print(" Error: Invalid operation!")

calculator("+", "30", "5")
calculator("-", "30", "5")
calculator("*", "30", "5")
calculator("/", "30", "5")
calculator("hello", "30", "5")
