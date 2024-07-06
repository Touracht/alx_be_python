#
def perform_operation(num1, num2, operation):
    """Calls for a function and
      give output based on the chosen one"""
    if operation == "add":
       sum = num1 + num2       
       return sum
    
    if operation == "subtract":
        difference = num1 - num2
        return difference
    if  operation == "multiply":
        product = num1 * num2
        return product
    if operation == "divide":
        quotient = num1 / num2
        if num1 / 0 == 0:
            print("Cannot divide by 0!")
        
        return quotient     
#