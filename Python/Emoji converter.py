message = input("> ")
word = message.split(" ")
emojis = {":)": "😊",
          ":(": "😞"}
for word in word:
    output = emojis.get(word, word) + " "
print(output)