# Function that loops over the list provided and divides the list elements

def divide_numbers(list):
    result = list[0]
    for i in range(1, len(list)):
        result = result / list[i]

    print(result)
