import os
import time
# count down program
# def countdown(i):
#     print(i)
#     if i <= 0:  # Base Case
#         return
#     else:  # Recursive Case
#         countdown(i-1)
#
#
# countdown(100)

PID = os.getpid()
print(PID)

time.sleep(10)


def fact(x):
    time.sleep(2)
    if x == 1:
        return 1
    else:
        print(f"=> fact >> else >> value of x: {x}")
        result = x * fact(x-1)
        print(f"=> fact >> x * fact(x-1) = {result}")
        return result


fact(5)
