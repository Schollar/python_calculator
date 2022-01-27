import addition
import division
import multiplication
import subtraction


# Function that takes in the user_selection(input) and the users choice of numbers(list)
# and then calls the appropriate calculate function
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


# Function that gets the users input on what math function to be done
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

# Function that takes in user input numbers and adds them to a list to be passed along to the calculate function


def get_calc(num):
    try:
        number = input("Please atleast 2 numbers, type 'stop' to end: ")
        if(number == 'stop'):
            # Checks to make sure the list has atleast 2 numbers
            if(len(user_input_list) < 2):
                print('You need atleast two numbers!')
            else:
                calculator(num, user_input_list)
        else:
            num_float = float(number)
            user_input_list.append(num_float)
            get_calc(num)
    except:
        print('Something went wrong! Try again')


user_input_list = []
get_user_input()
