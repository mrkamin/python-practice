phone = input("Phone:")

digit_mapping = {
    '1' : 'One',
    '2' : 'Two',
    '3' : 'Three',
    '4' : 'Four',
    '5' : 'Five',
    '6' : 'Six',
    '7' : 'seven',
    '8' : 'eight',
    '9' : 'nine'
}
output = ""
for ch in phone:
    output += digit_mapping.get(ch, "!") + " "

print(output)