def power(base, exponent=2): # exponent defaults to 2
    """Calculates base to the power of exponent"""
    # Check to ensure base and exponent are valid
    result = base ** exponent
    return result


# Main
print(f"10 squared is {power(base=10)}") # 100
print(f"2 cubed is {power(2, 3)}") # 8
