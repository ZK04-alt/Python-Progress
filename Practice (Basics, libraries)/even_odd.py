def main():
    num = int(input('enter number to be checked: '))
    quo_rem = divmod(num, 2)
    if quo_rem[1] == 0:
        print('even')
    else:
        print('odd')
        
main()
