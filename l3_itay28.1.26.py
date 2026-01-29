number = int(input("please input a number: "))
i = 1
z = 0
while True:
    if number <= 1:
        print("number isn't prime")
        break

    i += 1
    if number % i == 0:
        z += 1
        if number == i and z == 1:
            print("number is prime")
            break

        else:
            print("number is not prime")
            break
