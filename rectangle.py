def calculate_rectangle_area(width, height):
    # The context of 'width' and 'height' (inside parentheses after a 'def')
    # defines them as parameters.
    """Calculates the area of a rectangle"""
    # 1. Calculate the area
    area = width * height
    # 2. Return the result
    return area


# Main
# rect_area stores the value returned from calculate_rectangle_area()
print(calculate_rectangle_area(5, 10))
print(calculate_rectangle_area(12, 7))
