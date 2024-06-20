numbers =[]

for i in range(10):
    number = int(input("enter numbers:  "))
    numbers.append(number)

even =[]
odd =[]


for n in range(10):
    if numbers[i] % 2 == 0:
        odd.append(numbers[i])
else:
    even.append(numbers[i])

print("kenti:  ", odd )
print("luwi:  ", even)