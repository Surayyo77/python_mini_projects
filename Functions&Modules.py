# Mini Calculator 

def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the second number: "))
print("1. add\n2. subtract\n3. multiply\n4. divide")
option = int(input("Choose one operation (1-4): "))
if option==1:
    print("Result: ",add(first_num,second_num))
elif option==2:
    print("Result: ",subtract(first_num,second_num))
elif option==3:
    print("Result: ",multiply(first_num,second_num))
elif option==4:
    print("Result: ",divide(first_num,second_num))
else:
    print("Invalid option!")