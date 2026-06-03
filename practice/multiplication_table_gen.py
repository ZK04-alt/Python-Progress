def main():
    choice = True
    while choice:

        while True:
            try:
                table, ran = take_inputs()
                break
            except TypeError:
                pass

        try:
            start, end = splitter(ran)
            check = validator(start, end)
            if not check:
                raise ArithmeticError
            table_gen(table, start, end)

        except ArithmeticError:
            print("starting value in range cannot be greater than ending")

        except TypeError:
            pass

        except UnboundLocalError:
            pass

        ans = input("Generate another table? y or n: ").lower()
        if ans == "n":
            choice = False


def take_inputs():
    try:
        table = int(input("What number's table do you want to generate? ").strip())
        if table == 0:
            raise ValueError
        ran = input(
            "Give range for the table in the following format; starting number,ending number: "
        ).strip()
        if ran == "":
            ran = "1,10"
    except ValueError:
        print("Please enter a non zero number.")

    try:
        return table, ran
    except UnboundLocalError:
        pass


def validator(start: int, end: int):
    if start > end:
        return False
    else:
        return True


def splitter(t_range: str):
    try:
        start, end = t_range.split(",")
    except ValueError:
        print("Range entered does not contain commas.")
    try:
        start, end = int(start), int(end)
        return start, end
    except ValueError:
        print("Enter numbers only.")
    except UnboundLocalError:
        pass


def table_gen(table: int, start: int, end: int):
    end += 1
    for i in range(start, end):
        print(f"{table} x {i} = {table*i}")


main()
