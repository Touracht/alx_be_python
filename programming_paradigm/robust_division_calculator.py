def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        division = numerator / denominator
        return division
        
    except ZeroDivisionError:
        print(f"Error: Cannot divide by zero.")
        
    except ValueError:
        print("Error: Please enter numeric values only.")

