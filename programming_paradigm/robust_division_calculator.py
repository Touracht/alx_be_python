def safe_divide(numerator, denominator):
    division = float(numerator) / float(denominator)

    try:
        if division:
            print(f"The result of the division is {division:.1f}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    
    try:
        if division:
            print(f"{numerator} / {denominator} is {division:.1f}")
    except ValueError:
        print("Error: Please enter numeric values only.")
                  
