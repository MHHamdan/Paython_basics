string1 = 'Mohammed'
string2 = 'Hamdan'


full_name = string1 + ' ' + string2

print(full_name)

print(full_name[0:3])
print(full_name[:5])

print(full_name[9:])

print('empty string')
empty_string = ""
non_empty_string = " "
non_empty_string1 = "   "

print(len(empty_string))

print(len(non_empty_string))
print(len(non_empty_string1))


word = 'goal'
print(word)
#word[0] = 'f'
word = 'f'+word[1:]
print(word)

print('#1 Create a string and print its length using len().')
string = 'Programming is fun'
print(len(string))

print('#2 Create two strings, concatenate them, and print the resulting string.')
string2 = 'Belive it or not!'

result12 = string + ' ' + string2
print(result12)

print('#3 Create two strings, use concatenation to add a space between them, and print the result.')
string1 = 'For'
string2 = 'fun'
concat = string1 + ' '+ string2
print(concat)


print('Print the string "zing" by using slice notation to specify the correct range of characters in the string "bazinga".'
      )

string = 'bazinga'
print(string[2:-1])


name = ' MoHa MMe D '
print(name)
print(name.lower())
print(name.upper())
print(len(name))


print("""There are three string methods that you can use to remove whitespace 
from a string:""")
print(name.rstrip())
print(len(name))
print(name.lstrip())
print(len(name))
name = '   MoHa MMe D   '
print(len(name))
print(name.strip())
print(len(name))

print("""Determine If a String Starts or Ends With a
Particular String: using .strartswith() or .endswith() """)

startship = 'Enterpise'
print(startship, "starts with en", startship.startswith('en'), """starts
with """, startship.startswith('En'), """ Also it ends
with """, startship.endswith('rise'))

name = 'Mohammed'
print(name.lower())

print(name)
name = name.lower()
print(name)

print("""Write a program that converts the following strings to lowercase:
"Animals", "Badger", "Honey Bee", "Honey Badger". Print each lowercase
string on a separate line.""")

print(" Animals".lower(), "\n Badger".lower(), "\n Honey Bee".lower(), "\n Honey Badger".lower())


print("""Repeat exercise 1, but convert each string to uppercase instead of
lowercase.""")
print(" Animals".upper(), "\n Badger".upper(), "\n Honey Bee".upper(), "\n Honey Badger".upper())


print("""Write a program that removes whitespace from the following
strings:
string1 = " Filet Mignon"
string2 = "Brisket "
string3 = " Cheeseburger "
Print out the strings with the whitespace removed.""")
print('Answerss:')
string1 = " Filet Mignon"
string2 = "Brisket "
string3 = " Cheeseburger "

print(string1.lstrip())
print(string2.rstrip())
print(string3.strip())

print("""5. Using the same four strings from exercise 4, write a program that
uses string methods to alter each string so that .startswith("be")
returns True for all of them.""")
string1 = 'be'+string1
string2 = 'be'+string2
string3 = 'be'+string3
print(string1.startswith('be'))
print(string2.startswith('be'))
print(string3.startswith('be'))


prompt= "please enter your name here >>> "
name = input(prompt)
print("Your name is " + name)

response = input("Enter your name in only a Captile letter: ")
print(response + "Is your input a capital letters " + response)
must_capital = response.upper()
print("WE CONVERTED YOU INPUT TO A CAPITAL LETTER "+ must_capital)

print("""Write a program that takes input from the user and displays that
input back.""")
input1 = input("Enter your input")
print("your input is "+input1)

print("""Write a program that takes input from the user and displays the
input in lowercase.""")
input1 = input("Enter your input")
print("your input is "+input1)
print("your input should be in a lower case "+input1.lower())


print("""Write a program that takes input from the user and displays the
number of characters in the input.""")
input1 = input("Enter your input to comute the number of caracherters")
print("your input is "+input1)
print("your input length is ")
print(len(input1.lower()))
