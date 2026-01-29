small_num = None
i = 0
while True:

    if i < 2:
        number = int(input("enter a number: "))

        if small_num is None or number <= small_num:
            small_num = number
            i = 0
            continue
        else:
            i = i + 1

    else:
        break
print("i found a sequence of 3 numbers bigger than the other")
