def main():
    num = int(input('enter number to check: '))
    check_3 = divmod(num, 3)
    check_3 = check_3[1]
  
    check_5 = divmod(num, 5)
    check_5 = check_5[1]

   
    if check_3 == 0 and check_5 == 0:
        print(f'{num} is a multiple of both 3 and 5')
    elif check_3 == 0 and check_5 != 0:
        print(f'{num} is a multiple of 3')
        
    elif check_3 != 0 and check_5 == 0:
        print(f'{num} is a multiple of 5')
    else:
        print(f'{num} is a multiple of neither')
        
    
        
    

    
    
    
    
    
    
    
    
main()