def calculator():
    while True:
        ques = input("Enter following Numbers to perform respective tasks.\n1.Addition      2.Subtraction\n3.Multiplication         4.Division.\n   5.To terminate the program.\n")
        if ques == '5':
            return
        a = int(input("Enter first Number:"))
        b = int(input("Enter second Number:"))
        if ques =='1':
            print(Addition(a,b))
        elif ques == '2':
            print(subtraction(a,b))
        elif ques=='3':
            print(multiplication(a,b))
        elif ques =='4':
            print(division(a,b))
def Addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    return a/b
calculator()