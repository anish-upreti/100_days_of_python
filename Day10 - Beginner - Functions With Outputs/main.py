import art

# calculator

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def divide(n1, n2):
  return n1 / n2

def multiply(n1, n2):
  return n1 * n2

# dictionary
operations = {
  "+": add,
  "-": subtract,
  "/": divide,
  "*": multiply
}

def calculator():
  print(art.logo)
  num1 = float(input("Enter the first number: "))
  # looping through the dictionary
  for operator in operations:
    print(operator)
  should_continue = True
  
  while should_continue:
    operation_symbol = input("Select an operator: ")
    num2 = float(input("Enter the next number: "))
    
    calculator_func = operations[operation_symbol]
    result = calculator_func(num1,num2)
  
    print(f"{num1} {operation_symbol} {num2} = {result}")
  
    decision = input(f"Type 'yes' to continue calculation with {result} and 'no' to restart calculation: ")
    if decision == "yes":
      num1 = result
    else:
      should_continue = False
      calculator()

calculator()