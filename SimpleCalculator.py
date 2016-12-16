'''
 Author      : DORIAN JAVA BROWN
 Version     : N/A
 Copyright   : All Rights Reserve; You may use, distribute and modify this code.
 Description : This is a simple calculator that can add, subtract, multiply and divide using functions 
 '''



'''functions definitions'''

# addition function
def add(x, y):
   return x + y

# subtraction function
def subtract(x, y):
   return x - y

# multiplication function
def multiply(x, y):
   return x * y

# divison function
def divide(x, y):
   return x / y

# operation selection from the user
print("\t\tSelect operation:")
print("==============================================")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")


print('Please type in the math operation you would like to complete:')
print('-------------------------------------------------------------')
print('+ for addition')
print('- for subtraction')
print('* for multiplication')
print('/ for division')
print('\n\n')

choice = input("Enter choice(1/2/3/4):")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("Invalid input")