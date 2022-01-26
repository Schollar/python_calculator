import addition
import division
import multiplication
import subtraction


def calculator(input, arg1, arg2):
    if(input == 1):
        addition.add_numbers(arg1, arg2)
    elif(input == 2):
        subtraction.subtract_numbers(arg1, arg2)
    elif(input == 3):
        multiplication.multiply_numbers(arg1, arg2)
    elif(input == 4):
        if(arg1, arg2 == 0):
            print("Sorry you cannot divide by zero!")
        else:
            division.divide_numbers(arg1, arg2)
    else:
        print("Sorry not a valid choice")


def get_user_input():
    try:
        print('Please select from the following options')
        print('1.Addition')
        print('2.Subtraction')
        print('3.Multiplication')
        print('4.Division')
        user_choice = input("Please enter your selection: ")
        user_float = float(user_choice)
        if(user_float >= 1 and user_float <= 4):
            first_number = input("Please enter first number: ")
            first_num_float = float(first_number)
            second_number = input("Please enter your second number: ")
            second_num_float = float(second_number)
            calculator(user_float, first_num_float, second_num_float)
        else:
            print('You must pick a valid selection!')
    except ValueError:
        print('You must input a number!')


get_user_input()
