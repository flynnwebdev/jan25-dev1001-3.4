def analyze_numbers(number_list):
    """
    Takes a list of numbers and returns a dictionary containing
    the sum, average and max value from the list.

    Args:
        number_list: The list of numbers (int/float) to analyze

    Returns:
        dict: A dictionary with 'sum', 'average' and 'max' values
    """
    # TODO: Check to ensure list is not empty and contains only numbers
    # Calculate the sum
    total_sum = sum(number_list)
    # Calculate average
    # average = total_sum / len(number_list)
    # Calculate maximum value
    # max_val = max(number_list)
    # Return the values in a dict
    # This statement is first creating the dict, then returning it
    return {
        'sum': total_sum,
        'average': total_sum / len(number_list),
        'max': max(number_list)
    }


# List - group of indexed values, eg. [2, 4, 8, 10]
# Dict - group of key/value pairs, eg. {foo: 'bar', qty: 20}

# Main
my_numbers = [10, 20, 5, 15]
print(analyze_numbers(my_numbers))
