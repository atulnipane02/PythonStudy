def rFib(num):
    if num == 0:
        return 0
    elif num == 1 or num == 2:
        return 1
    else:
        return rFib(num-1) + rFib(num-2)


print(rFib(4))
