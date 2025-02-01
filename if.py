weight = int(input('Weigth: '))
unit = input('(L)bs or (K)g: ')

if unit.upper() == "L":
    converted = weight * 0.45
    print(converted)
else:
    converted = weight / 0.45
    print(converted)