# count down program
def countdown(i):
    print(i)
    if i <= 0:  # Base Case
        return
    else:  # Recursive Case
        countdown(i-1)


countdown(100)
