def safe_divide(numerator, denominator):
    division = float(numerator / denominator)

    try:
        if division:
            print(f"The result of the division is {division:.2f}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    
    try:
        if division:
            print(f"{numerator} / {denominator} is {division:.2f}")
    except ValueError:
        print("Error: Please enter numeric values only.")
                  
