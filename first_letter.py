password = input('Tell me your password ')
check_first_letter = password[0]
print('The first letter you entered was: ',password[0].upper())

num = input("Enter a number to be doubled: ")
doubled_num = float(num) * 2
print("Your entered number is ", num + " its doubled is ")
print(doubled_num)
print("Your entered number is ", num + " its doubled is "+str(doubled_num))


total_pancakes = 10
pancakes_eaten = 5

print("Only " + str(total_pancakes - pancakes_eaten) + "pancakes left.")


print("""Create a string containing an integer, then convert that string into
an actual integer object using int(). Test that your new object is
a number by multiplying it by another number and displaying the
result.""")

string1 = '123'
print(string1)
print(2 * int(string1))

print("""Repeat the previous exercise, but use a floating-point number and
float().""")
string1 = '123.2'
print(string1)
print(2 * float(string1))

print("""Create a string object and an integer object, then display them side
by side with a single print statement using str().""")

string = "Your salary will be " + str(5000) + " Dollar"
print(string)

print("Streamline Your Print Statements ")
name = "Zaphod"
heads = 2
arms = 4
output = name + " has " + str(heads) + " heads and " + str(arms) + " arms"
print(output)

output_fstring = f"{name} has {heads} heads and {arms} arms"
print(output_fstring)

print("""You can also insert Python expressions between the curly braces. The
expressions are replaced with their result in the string:""")
n , m = 3  , 4
print(f"{n} times {m} is {n*m}")

x, y = 2, 6
print(f"{x} times {y} is {x*y}")

#print(format"{x} subract {y} is {x-y}")
print("{} subtract {} is {}".format(x,y,x-y))

print(f"{x} +  {y}  = {x+y} >>>> This format according to Python3 and higher")
print("{} + {} = {} This format is for Python2 lower".format(x,y,x+y))




print("""Create a float object named weight with the value 0.2, and create
a string object named animal with the value "newt". Then use these
objects to print the following string using only string concatenation:
0.2 kg is the weight of the newt.""")

weight = 0.2
animal = "nwet"
print(str(weight) + " kg is the weight of the newt.")

print("""Display the same string by using .format() and empty {} placeholders.""")

print("{} kg is the weight of the {}.".format(weight, animal))

print("3. Display the same string using an f-string.")
print(f"{weight} kg is the weight of the {animal}.")


print("""One of the most useful string methods is .find(). As its name implies,
this method allows you to find the location of one string in another
string—commonly referred to as a substring.""")
phrase = "the surprise is in here somewhere surprise 5142192291"
result = phrase.find("surprise")
print(result)

no_in_phrase = phrase.find("mhammed")
print(no_in_phrase)
print("""If a substring appears more than once in a string, then .find() returns
the index of only the first appearance, starting from the beginning of
the string:""")
result = phrase.find("surprise")
print(result)

result = phrase.find("4")
print(result)

print("""strings have a .replace() method that replaces
each instance of a substring with another string.""")

my_story = "I'm telling you the truth; nothing but the truth!"
print(my_story)
result = my_story.replace("the truth", 'lies')
print(result)

text = "some of the stuff"
print(text)
new_text = text.replace('some', 'all')
print(new_text)
new_text = new_text.replace('staff', 'things')
print(new_text)

print("""1. In one line of code, display the result of trying to .find() the substring
"a" in the string "AAA". The result should be -1.""")

print("AAA".find("a"))


print("""Replace every occurrence of the character "s" with "x" in the string
"Somebody said something to Samantha.""")
string = "Somebody said something to Samantha."
print(string)
string_result = string.replace("s", "x")

print("""Write a program that accepts user input with input() and displays
the result of trying to .find() a particular letter in that input.""")
x = input("Enter your input:  ")
results = x.find(x[0])
print(f"{x[0]} is the first letter of the input {x}.")
print("{} is the last letter of the input {}.".format(x[-1],x))
print("check if the letter f  is in the input :")
 



      

