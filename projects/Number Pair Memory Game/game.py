import random

NUM_PAIRS = 3


def main():
    num_list = create_list(NUM_PAIRS)  # created list with pairs
    random.shuffle(num_list)  # shuffling that list
    star_list = create_star_list(
        NUM_PAIRS
    )  # created an encrypted list with same length

    while "*" in star_list:
        print(star_list)
        # get valid indices from user
        indices = get_indices(star_list)
        index = get_valid_index(indices, star_list)
        index1, index2 = index

        # play game

        check_pairs(int(index1), int(index2), star_list, num_list)

    print(star_list)
    print("Congratulations! You won!")


def create_list(NUM_PAIRS):
    num_list = []
    for x in range(NUM_PAIRS):
        for i in range(2):
            num_list.append(x)

    return num_list


def create_star_list(NUM_PAIRS):
    star_list = []
    for i in range(NUM_PAIRS * 2):
        star_list.append("*")
    return star_list


def get_valid_index(indices, star_list):
    flag = False
    while not flag:

        flag1 = False

        while not flag1:
            index1 = input("Enter an index: ")
            if index1.isalpha():
                print("Not a number. Try again")
            elif int(index1) not in indices:
                print("Invalid index. Try again.")
            elif star_list[int(index1)] != "*":
                print("This number has already been matched. Try again.")
            else:
                flag1 = True

        flag2 = False
        while not flag2:
            index2 = input("Enter an index: ")
            if index2.isalpha():
                print("Not a number. Try again.")
            elif int(index1) == int(index2):
                print("You entered the same index twice. Try again.")
            elif int(index2) not in indices:
                print("Invalid index. Try again.")
            elif star_list[int(index2)] != "*":
                print("This number has already been matched. Try again.")
            else:
                flag2 = True

        if flag1 and flag2:
            flag = True

    return index1, index2


def get_indices(star_list):
    indices = []
    for i in range(len(star_list)):
        indices.append(i)
    return indices


def clear_terminal():
    for i in range(20):
        print("\n")


def check_pairs(index1, index2, star_list, num_list):

    if num_list[index1] != num_list[index2]:
        print(f"Value at index {index1} is {num_list[index1]}")
        print(f"Value at index {index2} is {num_list[index2]}")
        print("No match. Try again.")
        continuation = input("Press Enter to continue... ")
        clear_terminal()
    else:
        star_list[index1] = num_list[index1]
        star_list[index2] = num_list[index2]

        print("Match!")
        clear_terminal()


if __name__ == "__main__":
    main()
