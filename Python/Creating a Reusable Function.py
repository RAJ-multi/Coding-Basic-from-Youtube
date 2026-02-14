def emoji_converter(message):
    return message.replace(":)", "😀").replace(":(", "😞")


input_message = input("Enter your message: ")
result = emoji_converter(input_message)
print("Converted message:", result)

# altrnatively, using a dictionary for more emojis
def emoji_converter_v2(message):
    emojis = {":)": "😊",
              ":(": "😞"}
    output = ""
    for word in message.split():
        output += emojis.get(word, word) + " "
    return output.strip()

messsage = input("Enter your message: ")
result = emoji_converter_v2(messsage)
print("Converted message:", result)