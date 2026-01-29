red = '\033[31m'
while True:
    lower = int(input("enter lower number: "))
    higher = int(input("enter higher number: "))

    if higher <= lower:
        continue

    if higher > lower:
        break
for x in range(lower, higher + 1):
    print(red,x, end = " ")