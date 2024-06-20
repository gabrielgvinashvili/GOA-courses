numbers =[]

more = []
less = []

for n in range(10):
    number = int(input("shemoitane ricxvi:  "))
    numbers.append(number)

greater_than_100 = []
less_than_100 = []

for number in numbers:
    if number > 100:
        greater_than_100.append(number)
else:
    less_than_100.append(number)

print("100 ze meti ricxvi:  ", greater_than_100)
print("100 ze naklebi ricxvi:  ", less_than_100)