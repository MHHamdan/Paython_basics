user_input = input("Enter some text: ")
print("""Use .replace() to convert the text entered by the user into leetspeak
by making the following changes to lowercase letters:""")

result = user_input.replace('a', '4')
result = result.replace('b', '8')
result = result.replace('e', '3')
result = result.replace('l', '1')
result = result.replace('o', '0')
result = result.replace('s', '5')
result = result.replace('t', '7')


print(result)
