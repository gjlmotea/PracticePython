from module import Calculator

a = input("請輸入a的值:\n")
b = input("請輸入b的值:\n")
op = input("請輸入要做的運算(+ - * /):\n")

operation = Calculator(a, b, op)

print(operation.result)
