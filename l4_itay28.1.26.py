count_positive = 0
count_negative = 0
sum_positive = 0
high_number = None
while True:
    number = int(input("please input a number: "))
    if number == 0:
        continue
    if number < 0:
        count_negative += 1
        continue

    count_positive += 1
    sum_positive += number
    if high_number == None or high_number < number:
        high_number = number
    if number % 7 == 0:
        break
print("the sum of the positive number is:",sum_positive)
print ("the count of the positive numver is:",count_positive)
print ("the count of the negative numver is",count_negative)
print("the sum of the high number is:",high_number)
