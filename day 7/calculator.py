def addition(num1,num2):
    return num1+num2

def subtraction(num1,num2):
    return num1-num2

def division(num1,num2):
    return num1/num2

def multiplication(num1,num2):
    return num1*num2

counter=True
while counter==True:
    print(f'Enter any two numbers:')
    num1=input()
    num2=input()
    print(f'Please enter the preferred operation to be conducted:') 
    print("1. Addition")
    print("2. Subtraction")
    print("3. Division")
    print("4. Multiplication")
    choice=input()

    num1=float(num1)
    num2=float(num2)

    if (choice=='1'):
        print(f'The sum of {num1} and {num2} is {addition(num1,num2)}')

    elif (choice=='2'):
        print(f'The difference of {num1} and {num2} is {subtraction(num1,num2)}')

    elif (choice=='3'):
        print(f'The division of {num1} and {num2} is {division(num1,num2)}')

    elif (choice=='4'):
        print(f'The product of {num1} and {num2} is {multiplication(num1,num2)}')
    else:
        print("invalid entry")
    cont=input("Do you want to continue calculations? Y/N: ")
    # print(cont)
    if (cont=='Y' or cont=='y'):
        # print("I'm here")
        counter==True
    else:
        counter=False