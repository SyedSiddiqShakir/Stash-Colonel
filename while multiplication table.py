num = int(input("Enter a number to see its application number"))
multi = int(input("Enter the amount of time you want it to multiply"))
startnum = 1
i = 1
while i <= multi:
    startnum = num * i
    print(startnum)
    i = i + 1