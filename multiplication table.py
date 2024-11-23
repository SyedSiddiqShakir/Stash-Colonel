print  ("Enter any number of your choice")
print("I will print the multiplicaiton table for it till x10")

mult = 1
num = int(input())

for table in range(1, 10, 1):
    mult = mult + 1
    nnum = num * mult
    print(nnum)