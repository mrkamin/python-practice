message = input(">")

words = message.split(" ")

emojis = {
    ":)": "Happy emoje",
    ":(" :  "sad emojy"
}
output = ""
for word in words:
   output += emojis.get(word, word) + " "
print(output)