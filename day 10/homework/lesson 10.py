# მომხმარებელს შემოატანინეთ ორი ბულიან ტიპის მნიშვნელობა(true, false), 
#შემდეგ კი დაბეჭდეთ ერკანზე ეს მნიშვნელობები     
#შედარებული ერთმანეთზე, ამისთვის გამოიყენეთ ლოგიკური ოპერატორები (and და or)

knows_programing = bool(input("do you know programing?: "))
#pls enter incorrect info
is_over_18 = bool(input("are you an adult: "))

print(knows_programing and is_over_18)
print(knows_programing or is_over_18)