
#PYTHON FUNDAMENTALS

#Write Python code that prints your name, student number and email address
# print("Seetha V")
# print("32")
# print("seetha917@gmail.com")

# Write Python code that prints your name, student number and email address using escape sequences.
# print("Seetha V\n32\nseetha917@gmail.com")

# Write Python code that add, subtract, multiply and divide the two numbers. You can use the two numbers 14 and 7.
# x=14
# y=7
# print(x,"+",y,"=",x+y)
# print(x,"*",y,"=",x*y)
# print(x,"-",y,"=",x-y)
# print(x,"/",y,"=",x//y)

# Write Python code that displays the numbers from 1 to 5 as steps.
# for i in range(1,6):
#     print(i)

# Write Python code that outputs the following sentence (including the quotation marks and line break) to the screen:
# An example runs of the program: "SDK" stands for "Software Development Kit", whereas "IDE" stands for "Integrated Development Environment".
# print('\"SDK\" stands for \"Software Development Kit\", whereas\n\"IDE\" stands for \"Integrated Development Environment\" ')

#Practice and check the output
# print("python is an \"awesome\" language.")
# print("python\n\t2023")
# print('I\'m from Entri.\b')
# print("\65")
# print("\x65")
# print("Entri", "2023", sep="\n")
# print("Entri", "2023", sep="\b")
# print("Entri", "2023", sep="*", end="\b\b\b\b")

#Define the variables below. Print the types of each variable.
#What is the sum of your variables? (Hint: use a type conversion function.) What datatype is the sum? num=23 textnum="57" decimal=98.3
# num=23
# textnum="57"
# decimal=98.3
#
# print("TYPE OF NUM IS",type(num))
# print("TYPE OF TEXTSUM IS",type(textnum))
# print("TYPE OF DECIMAL IS",type(decimal))
#
# sum = num + int(textnum) + decimal
# print("SUM=",sum)
# print("TYPE OF SUM IS",type(sum))

# calculate the number of minutes in a year using variables for each unit of time. print a statement that describes what your code does also.
# Create three variables to store no of days in a year, minute in a hour, hours in a day, then calculate the total minutes in a year and
# print the values (hint) total number of minutes in an year =No.of days in an year * Hours in a day * Minutes in an hour
# Variables for time units
# no_of_days_in_year = 365
# hours_in_a_day = 24
# minutes_in_a_hour = 60
#
# total_minutes_in_an_year = no_of_days_in_year * hours_in_a_day * minutes_in_a_hour
#
# print("This code calculates the total number of minutes in a year.")
# print("Total minutes in a year:", total_minutes_in_an_year,"minutes")

#Write Python code that asks the user to enter his/her name and then output/prints his/her name with a greeting.
#An example runs of the program: Please enter you name: Tony Hi Tony, welcome to Python programming :)
# Ask the user to enter their name

# user_name = input("Please enter your name: ")
# print(f"Hi {user_name}, Welcome to Python programming :)")

#CONDITIONAL AND LOOPING STATEMENTS

# A certain cinema currently sells tickets for a full price of 6 pounds,
# but always sells tickets for half price to people who are less than 16 years old, and
# for a third of the price for people who are 60 years old or more.
# An example run of the program (numbers in bold are typed in by the user) Enter your age: 63 Your ticket costs £2

# age = int(input("Enter your age:"))
# if age < 16:
#     print("Your ticket price is £3 ")
# elif age >=60:
#     print("Your ticket price is £2 ")
# else:
#     print("Your ticket price is £6")

# age = int(input("Enter your age:"))
# full_price=6
# if age < 16:
#     price_reduction = full_price // 2
# elif age >= 60:
#     price_reduction = full_price // 3
# else:
#     price_reduction = full_price
# print(f"Your ticket price is £{price_reduction}")

#Write a Python program to receive 3 numbers from the user and print the greatest among them.

# x = int(input("Enter first number: "))
# y = int(input("Enter second number: "))
# z = int(input("Enter third number: "))
# if x > y and x > z:
#     print("The greatest number is ",x)
# elif y > x and y > z:
#     print("The greatest number is ",y)
# else:
#     print("The greatest number is ",z)

#Find the factorial of a given number using loops(note the number is received from the user)

# num = int(input("Enter a number: "))
# f = 1
# for i in range(1, num + 1):
#     f = f * i
# print(f"The factorial of {num} is {f}")

#Reverse a number using while loop

# n = int(input("Enter a number : "))
# r = 0
# while n > 0:
#     d = n % 10
#     r = r * 10 + d
#     n = n // 10
# print(f"The reversed number is:{r}")

#Finding the multiples of a number using loop

# num = int(input("Enter a number: "))
# count = int(input("How many multiples do you want to see? "))
#
# for i in range(1, count + 1):
#     multiple = num * i
#     print(multiple," ",end='')

#Write a program to print the inputted value as it is and break the loop if the value is 'done'.
# Example run of the program :hello there hello there :finished finished :done Done

# while True:
#     word = input("Enter a value (type 'done' to finish): ")
#     print(word)
#     if word == 'done' or word == 'Done' or word == 'DONE':
#         break

# Write a program that prints the numbers from 1 to 20.
# But for multiples of three print "Fizz" instead of the number and for the multiple of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz"

# for i in range(1, 21):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i," ",end='')

# Write a program to print the following pattern:
#  5 4 3 2 1
#  4 3 2 1
#  3 2 1
#  2 1
#  1

# n = 5
# for i in range(n, 0, -1):
#     for j in range(i, 0, -1):
#         print(j, end=' ')
#     print()

# DATA STRUCTURES

# List
# Q1. Create a list of 5 random numbers and print the list.
# import random
# r_num= [random.randint(1, 100) for _ in range(5)]
# print(r_num,type(r_num))

# Q2. Insert 3 new values to the list and print the updated list.
# import random
# r_num= [random.randint(1, 100) for _ in range(5)]
# print("Original List",r_num)
# new_values = [random.randint(1, 100) for _ in range(3)]
# r_num.extend(new_values)
# print("Updated List",r_num)

# Q3. Try to use a for loop to print each element in the list.
# import random
# r_num= [random.randint(1, 100) for _ in range(5)]
# print("Original List",r_num)
# new_values = [random.randint(1, 100) for _ in range(3)]
# r_num.extend(new_values)
# print("Updated List",r_num)
# for i in r_num:
#     print(i)

# Dictionary
# Q1. Create a dictionary with keys 'name', 'age', and 'address' and values 'John', 25, and 'New York' respectively.

# user = {
#     'name': 'John',
#     'age': 25,
#     'address': 'New York'
# }
# print(user)

# Q2. Add a new key-value pair to the dictionary created in Q1 with key 'phone' and value '1234567890'.
# user['phone'] = '1234567890'
# print(user)

# Set
# Q1.Create a set with values 1, 2, 3, 4, and 5.
# set = {1, 2, 3, 4, 5}
# print("SET=",set,"\n","TYPE=",type(set))

# Q2.Add the value 6 to the set created in Q1.
# set.add(6)
# print(set)

# Q3.Remove the value 3 from the set created in Q1.
# set.remove(3)
# print(set)

# Tuple
# Q1. Create a tuple with values 1, 2, 3, and 4
# tuple = (1, 2, 3, 4)
# print("TUPLE=",tuple,"\n","TYPE=",type(tuple))

# Q2. Print the length of the tuple created in Q1.
# print("LENGTH=",len(tuple))

# PYTHON FUNCTIONS

# What does the len() function do in Python?
# The `len()` function in Python returns the number of items in an object, such as strings, lists, tuples, dictionaries, and sets.
# It returns an integer representing the size or length of these data structures.

# Write a code example using len() to find the length of a list.
# list = [10, 20, 30, 40, 50]
# print("LIST:",list)
# print("Length of the list:", len(list))

# Write a Python function greet(name) that takes a person's name as input and prints "Hello, [name]!"
# def greet(name):
#     print(f"Hello, {name}!")

# user_name=str(input("Enter a Name: "))
# greet(user_name)

# Write a Python function find_maximum(numbers) that takes a list of integers and
# returns the maximum value without using the built-in max() function.
# Use a loop to iterate through the list and compare values.

# def find_maximum(numbers):
#     if not numbers:
#         return None
#     maximum = numbers[0]
#     for i in numbers:
#         if i > maximum:
#             maximum = i
#
#     return maximum
#
# numbers_list = [14, 29, 51, 8, 30]
# print(numbers_list)
# print("Maximum value:", find_maximum(numbers_list))

# Explain the difference between local and global variables in a Python function.
# Local Variables
#     Scope: Defined inside a function; accessible only within that function.
#     Lifetime: Exists only during the function's execution.
#     Example:
#
# def my_function():
#     local_var = 10  # Local variable
#     print(local_var)
#
# my_function()  # This will print 10
#     print(local_var)  # This will raise an error,  local_var is not accessible here
#
# Global Variables
#     Scope: Defined outside any function; accessible throughout the entire program.
#     Lifetime: Exists for the duration of the program.
#     Example:
#
# global_var = 20  # Global variable
#
# def my_function():
#     print(global_var)  # Accessing the global variable
#
# my_function()  # This will print 20
# print(global_var)  # This will also print 20

# Write a program where a global variable and a local variable have the same name and show how Python differentiates between them.
# value = 10 # Global variable
# def my_function():
#
#     value = 5 # Local variable with the same name
#     print("Inside the function, local value:", value)
#
# my_function()
# print("Outside the function, global value:", value)

# Create a function calculate_area(length, width=5) that calculates the area of a rectangle.
# If only the length is provided, the function should assume the width is 5.
# Show how the function behaves when called with and without the width argument.
#
# def calculate_area(length, width=5):
#     area = length * width
#     return area
#
# area_with_width = calculate_area(10, 3)
# print("Area with length and width:", area_with_width)
#
# area_with_default_width = calculate_area(10)
# print("Area with length and default width 5:", area_with_default_width)

# FILE AND EXCEPTIONAL HANDLING
# Exercise 1: (score : 1)Write a Python program to read a file and display its contents
#
# file1=open("C:\\Users\\SIXCOUSER\\Desktop\\DSML\\Python\\ASSIGNMENTS\\Assignment 5\\sample.txt",'r')
# print(file1.read())
#
# Exercise 2: (score : 1) Write a Python program to copy the contents of one file to another file
#
# source_filename = input("Please enter the source filename: ")
# destination_filename = input("Please enter the destination filename: ")
#
# try:
#     source_file =  open(source_filename, 'r')
#     destination_file = open(destination_filename, 'w')
#     contents = source_file.read()
#     destination_file.write(contents)
#     print("Contents copied successfully!")
# except FileNotFoundError:
#     print(f"Error: The file '{source_filename}' was not found.")
# except IOError as e:
#     print(f"An I/O error occurred: {e}")
# except Exception as e:
#     print(f"An unexpected error occurred: {e}")
# source_file.close()
# destination_file.close()
#
# Exercise 3: (score : 2) Write a Python program to read the content of a file and count the total number of words in that file.
#
# filename = input("Please enter the filename to read: ")
# try:
#     # Open the file in read mode
#     file = open(filename, 'r')
#     content = file.read()
#     print(content)
#     words = content.split()
#     word_count = len(words)
#
#     print(f"The total number of words in the file is: {word_count}")
#
# except FileNotFoundError:
#     print(f"Error: The file '{filename}' was not found.")
# except IOError as e:
#     print(f"An I/O error occurred: {e}")
# except Exception as e:
#     print(f"An unexpected error occurred: {e}")
#
# Exercise 4: (score : 1) Write a Python program that prompts the user to input a string and converts it to an integer.
# Use try-except blocks to handle any exceptions that might occur
#
# user_input = input("Please enter a number: ")
# print("Type of string before converting: ",type(user_input))
# try:
#     converted_to_integer = int(user_input)
#     print(f"The converted integer is: {converted_to_integer}")
#     print("Type of string after converting: ",type(converted_to_integer))
# except ValueError:
#     print("Error: The input is not a valid integer.")
#
#
# Exercise 5: (score : 1) Write a Python program that prompts the user to input a list of integers and
# raises an exception if any of the integers in the list are negative.
#
# user_input = input("Please enter a list of integers separated by spaces: ")
# try:
#     integer_list = [int(num) for num in user_input.split()]
#     for num in integer_list:
#         if num < 0:
#             raise ValueError(f"Negative integer found: {num}")
#
#     print("All integers are non-negative.")
# except ValueError as e:
#     print(f"Error: {e}")
#
#
# Exercise 6: (score : 2) Write a Python program that prompts the user to input a list of integers and computes the average of those integers.
# Use try-except blocks to handle any exceptions that might occur.
# use the finally clause to print a message indicating that the program has finished running.
#
# user_input = input("Please enter a list of integers separated by spaces: ")
#
# try:
#     integer_list = [int(num) for num in user_input.split()]
#     average = sum(integer_list) / len(integer_list)
#     print(f"The average of the entered integers is: {average}")
#
# except ValueError as e:
#     print(f"Error: {e}")
# except ZeroDivisionError:
#     print("Error: Cannot calculate the average of an empty list.")
# except Exception as e:
#     print(f"An unexpected error occurred: {e}")
# finally:
#     print("Program has finished running.")
#
# Exercise 7 : (score : 2) Write a Python program that prompts the user to input a filename and writes a string to that file.
# Use try-except blocks to handle any exceptions that might occur and print a welcome message if there is no exception occurred.
#
# filename = input("Please enter the filename to write to: ")
# content = "Hello, This is a sample string written to the file."
# try:
#     with open(filename, 'w') as file:
#         file.write(content)
#     print("Welcome! The string has been successfully written to the file.")
# except Exception as e:
#     print(f"An error occurred: {e}")

#OOPS CONCEPT
#Question 1: (5 Marks) Build a program to manage a university('s course catalog.
# You want to define a base class Course that has the following properties:
# course_code: a string representing the course code (e.g., "CS101") c
# ourse_name: a string representing the course name (e.g., "Introduction to Computer Science")
# credit_hours: an integer representing the credit hours for the course (e.g., 3)
# You also want to define two subclasses CoreCourse and ElectiveCourse, which inherit from the Course class.
# CoreCourse should have an additional property required_for_major which is a boolean representing
# whether the course is required for a particular major.
# ElectiveCourse should have an additional property elective_type which is a string representing the type of elective
# (e.g., "general", "technical", "liberal arts"). )

# class Course:
#     def __init__(self, course_code, course_name, credit_hours):
#         self.course_code = course_code
#         self.course_name = course_name
#         self.credit_hours = credit_hours

# class CoreCourse(Course):
#     def __init__(self, course_code, course_name, credit_hours, required_for_major):
#         Course.__init__(self, course_code, course_name, credit_hours)
#         self.required_for_major = required_for_major

# class ElectiveCourse(Course):
#     def __init__(self, course_code, course_name, credit_hours, elective_type):
#         Course.__init__(self, course_code, course_name, credit_hours)
#         self.elective_type = elective_type

# core_course1 = CoreCourse("CS101", "Introduction to Computer Science", 3, True)
# print(f"\nCore Course: {core_course1.course_code} - {core_course1.course_name}")
# print(f"Credit Hours: {core_course1.credit_hours}")
# print(f"Required for Major: {'Yes' if core_course1.required_for_major else 'No'}")

# elective_course1 = ElectiveCourse("MATH201", "Calculus", 4, "technical")
# print(f"\nElective Course: {elective_course1.course_code} - {elective_course1.course_name}")
# print(f"Credit Hours: {elective_course1.credit_hours}")
# print(f"Elective Type: {elective_course1.elective_type}")


#Question 2: (5 Marks) Create a Python module named employee that contains a class Employee with attributes
# name, salary and methods get_name() and get_salary().
#Write a program to use this module to create an object of the Employee class and display its name and salary.

# import employee
# emp = employee.Employee("Seetha V", 50000)
# print("Employee Name: ", emp.get_name())
# print("Employee Salary: ", emp.get_salary())










