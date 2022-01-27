import addition
import division
import multiplication
import subtraction


def calculator(input, list):
    if(input == 1):
        addition.add_numbers(list)
    elif(input == 2):
        subtraction.subtract_numbers(list)
    elif(input == 3):
        multiplication.multiply_numbers(list)
    elif(input == 4):
        division.divide_numbers(list)
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
            get_calc(user_float)
        else:
            print('You must pick a valid selection!')
    except ValueError:
        print('You must input a number!')

# Wrap this with a try catch


def get_calc(num):
    number = input("Please atleast 2 numbers, type 'stop' to end: ")
    if(number == 'stop'):
        if(len(user_input_list) < 2):
            print('You need atleast two numbers!')
        else:
            calculator(num, user_input_list)
    else:
        num_float = float(number)
        user_input_list.append(num_float)
        get_calc(num)


user_input_list = []
get_user_input()
