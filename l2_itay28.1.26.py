products = 0
i = 0
while True:
    product = int(input("choose products: "))
    products += product
    i += 1
    if products >= 1000:
        print("he buy {} products".format(i))
        print("the total prise is", products)
        break
