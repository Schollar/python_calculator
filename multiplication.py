# Function that loops over the list provided and multiplies the list elements
def multiply_numbers(list):
    result = list[0]
    for i in range(1, len(list)):
        result = result * list[i]

    print(result)
