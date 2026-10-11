def get_num(prompt):

    while True:

        user_input= input(prompt) 

        try:
            return float(user_input)
        except ValueError:
            print ("Invalid input. Please input valid number.")

num1= get_num ("Enter first number: ")
num2= get_num ("Enter second number: ")

valid_ops= ["add", "subtract", "multiply", "division"] 
while True:
    user_ops= input ( "Enter the operation to perform [add/subtract/multiply/division]:" ).lower() 

    if user_ops in valid_ops:
        break
    else:
        print ("INVALID OPERATION. please enter from the following [add,substract,multiply,division]")

if user_ops == "add":
    result = num1+num2
elif user_ops == "subtract":
    result = num1-num2
elif user_ops == "multiply":
    result = num1*num2
elif user_ops == "division":
    if num2!=0:
        result = num1/num2
    else:
        print("Invaild second number. Please enter valid")

print(f'the result of {user_ops}ing of {num1} and {num2} is {result}')