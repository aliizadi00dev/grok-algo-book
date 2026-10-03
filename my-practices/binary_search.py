# Guess correct number program
import time


def num_checker(num: int):
    print("Number:", num)

    # time.sleep(1)
    if num < given_num:
        print("too low")
        return -1
    elif num > given_num:
        print("too high")
        return 1
    else:
        print("correct!")
        return 0


def num_guesser():
    # ## Old solotion
    # for i in range(max_num):
    #     num_checker(i)

    # ## Old solution: doesn't work at all
    global given_num, max_num, min_num
    # mid = int((min_num + max_num) / 2)
    # while True:
    #     result = num_checker(mid)
    #
    #     if result == 0:
    #         # correct
    #         break
    #     elif result == -1:
    #         # too low
    #         min_num = mid
    #         mid = int(((min_num + max_num) / 2))
    #         print(f"max_num: {max_num} -- mid:{mid}")
    #     else:
    #         # too high
    #         max_num = mid
    #         mid = int(max_num - ((min_num + max_num) / 2))
    #         print(f"max_num: {max_num} -- mid:{mid}")
    steps = 1
    while min_num <= max_num:
        mid = int((min_num + max_num) / 2)
        result = num_checker(mid)

        if result == 0:
            # correct number
            break
        elif result == -1:
            # too low
            min_num = mid + 1
        else:
            # too high
            max_num = mid - 1

        steps = steps + 1
    print(f"steps: {steps}")


if __name__ == "__main__":
    given_num = 29
    max_num = 100
    min_num = 0
    num_guesser()
