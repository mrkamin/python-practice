numbers = [10, 20,20,30,40,50]

unique = []

for number in numbers:
    if number not in unique:
        unique.append(number)

print(unique)