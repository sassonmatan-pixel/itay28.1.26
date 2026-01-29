count = 0
count16 = 0
yellow = '\033[33m'
white = '\033[97m'
while True:
    if count < 10:
        age = int(input("enter age: "))
        if not age >= 12:
            print("please enter a older age")
            continue
        if age <= 18 and age >= 12:
            count += 1
            if age > 16:
                count16 += 1
    else:
        break
    if age > 18:
        print("its older age for teen group")
        continue
print(white,"the valid age is" ,yellow  , count)
print(white,"the player is older then",yellow,count16)

