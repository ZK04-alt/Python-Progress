def main():
    choice = input('choose one converter \n1.Celsius to Fahrenheit \n2.Fahrenheit to Celsius \n\nchoice: ')
    if choice != '1' and choice != '2':
        choice = input('choose one converter \n1.Celsius to Fahrenheit \n2.Fahrenheit to Celsius \n\nchoice: ')
    
    match choice:
        case '1':
            cel = input('input temperature in celsius to convert : ')
            if cel != '' and cel.isnumeric():
                print(f'{(int(cel)*2)+30}°F')
            else:
                cel = input('enter valid temp: ')
                print(f'{(int(cel)*2)+30}°F')
            
        
        case '2':
            far = input('input temperature in fahrenheit to convert : ')
            if far != '' and far.isnumeric():
                print(f'{(int(far)-30)/2}°C')
            else:
                far = input('enter valid temp: ')
                print(f'{(int(far)-30)/2}°C')
            
                     
main()