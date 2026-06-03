def main():
    choice = input('select one of the following programs: \n1.calculator \n2.even-odd checker \n3.grade calculator \n')
    match choice:
        
        case '1':
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
                    
        case '2':
            num = int(input('enter number to be checked: '))
            quo_rem = divmod(num, 2)
            if quo_rem[1] == 0:
                print('even')
            else:
                print('odd')
        
        case '3':
            marks = int(input('enter student marks: '))
    
            if marks >= 90:
                print('A')
            elif marks < 90 and marks >= 80:
                print('B')
            elif marks < 80 and marks >= 70:
                print('C')
            elif marks < 70 and marks >= 60:
                print('D')
            else:
                print('F')
            
    
main()