import random as r

count = 1


def main():
    num = gen_rand_num()

    c = 1

    while c <= 10:
        try:
            guess = int(input("ans : "))
            c += 1
            verdict = user_guess_checker(guess, num)
            if not verdict:
                small_big_checker(guess, num)
                attempt_counter(verdict)
            else:
                attempt_counter(verdict)
                break

        except ValueError:
            print("please enter an actual number")


def gen_rand_num():
    return r.randint(1, 100)


def user_guess_checker(num: int, ans: int):
    if num == ans:
        return True
    else:
        return False


def attempt_counter(verdict: bool):
    global count

    if verdict:
        if count == 1:
            print(f"you have guessed the number in {count} attempt!")
        else:
            print(f"you have guessed the number in {count} attempts!")
    else:
        if count != 10:
            print(f"you have {10 - count} attempts remaining")
            count += 1
        else:
            print("\noutta lives game over!")


def small_big_checker(guess: int, ans: int):
    global count
    if count != 10:
        if guess > ans:
            print("too big")
        else:
            print("too small")


main()