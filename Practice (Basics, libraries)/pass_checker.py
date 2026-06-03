def main():

    check = False  # initializing check with false so that loop runs until password passes all requirements

    # running all checks with the functions

    while not check:
        pword = input("password: ").strip()
        e_check = empty_checker(pword)
        if e_check:
            len_check = len_checker(pword)
            case_check = lcase_checker(pword)
            case_check = ucase_checker(pword)
            dig_check = digit_checker(pword)
            alp_check = alpha_checker(pword)
            sym_check = sym_checker(pword)

            if len_check and case_check and dig_check and alp_check and sym_check:
                print("password set!")
                check = True


def empty_checker(pword: str):
    if pword == "":
        print("enter a password, do not leave blank")
        return False
    else:
        return True


def len_checker(pword: str):
    if len(pword) >= 8:
        return True
    else:
        print("password is too short")
        return False


def lcase_checker(pword: str):
    if pword.islower():
        print("include at least one upper case letter")
        return False
    else:
        return True


def ucase_checker(pword: str):
    if pword.isupper():
        print("include at least one lower case letter")
        return False
    else:
        return True


def digit_checker(pword: str):
    if pword.isalpha():
        print("include at least one number")
        return False
    else:
        return True


def alpha_checker(pword: str):
    if pword.isnumeric():
        print("include at least two alphabets, one lower case and one upper case")
        return False
    else:
        return True


def sym_checker(pword: str):
    if pword.isalnum():
        print("include at least one symbol")
        return False
    else:
        return True


main()
