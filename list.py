numbers = [7, 2, 5, 2, 2]
for x_count in numbers:
    print("x" * x_count)

numbers = 10
for number in range(numbers):
    print(number)
items = ["gold", 'plastic', 'selver']

for item in items:
    print(item)

numbers = [1,2,3,4,5,6,7,10]
for number in numbers:
    print(number)

max = numbers[0]

for number in numbers:
    if max < number:
        max = number
print(max)
