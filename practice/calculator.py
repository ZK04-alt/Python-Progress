def main():
    n1 = input('first number: ')
    if not n1.isnumeric() or n1 == '':
        n1 = input('enter correct first number: ')
        
        
    n2 = input('second number: ')
    if not n2.isnumeric() or n2 == '':
        n2 = input('enter correct second number: ')
        
    char = input('select one of the following operators: \n+ \n- \n* \n/\n\n')
    
    n1 = int(n1)
    n2 = int(n2)
    
    match char:
        case "+":
            print(n1 + n2)
        case "-":
            print(n1 - n2)
        case "*":
            print(n1 * n2)
        case "/":
            if n1 or n2 == 0:
                print('division by zero not possible')
            print(n1 / n2)
        case _:
            print('invalid operator')
            
main()