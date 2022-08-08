print(type(1))

num = 23
print(type(num))

print(type(int(num)))

print(1000000)
print(1_000_000)
print(10000001000000100000010000001000000100000010000001000000)



print("floating \n numbers are: ")
print(type(1.0))

num = 23.
print(type(num))

print(type(float(num)))

print(1000000.)
print(1_000_000.)
print(10000001000000100000010000001000000100000010000001000000.)

print("""To write a float literal in E-notation, type a number followed by the
letter e and then another number. Python takes the number to the
left of the e and multiplies by 10 raised to the power of the number
after the e. So 1e6 is equivalent to 1×10⁶.""")

print("""E-notation is short for exponential notation. You may have
seen this notation used by calculators to represent numbers
that are too big to fit on their screen.""")

print(200000000000000000.0)
print("""The float 200000000000000000.0 gets displayed as 2e+17. The + sign indicates
that the exponent 17 is a positive number. You can also use
negative numbers as the exponent:""")

print(1e-4)
print("""The literal 1e-4 is interpreted as 10 raised to the power -4, which is
1/10000 or, equivalently, 0.0001.""")

print("""Unlike integers, floats do have a maximum size. The maximum
floating-point number depends on your system, but something like
2e400 ought to be well beyond most machines’ capabilities. 2e400 is 2×10⁴⁰⁰, which is far more than the total number of atoms in the
universe!
When you reach the maximum floating-point number, Python returns
a special float value inf:""")

print(2e299)

n = 2e100
print(type(n), n)
n = -2e100
print(type(n), n)


print("""Write a script that creates the two variables, num1 and num2. Both
num1 and num2 should be assigned the integer literal 25,000,000,
one written with underscored and one without. Print num1 and num2
on two separate lines.""")

num1, num2 = 25000000, 25_000_000
print(num1, "\n", num2)


print("""Write a script that assigns the floating-point literal 175000.0 to the
variable num using exponential notation, and then prints num in the
interactive window.""")
num = 175e3
print(num)

print("""Write a script that assigns the floating-point literal -100000.0 to the
variable num using exponential notation, and then prints num in the
interactive window.""")
num = -10e5
print(num)

print("""3. In IDLE’s interactive window, try and find the smallest exponent N
so that 2e<N>, where <N> is replaced with your number, returns inf.""")
N = int(input("Enter your Number: "))
result = 2e333
print(result)

print("""PEP 8 recommends separating both operands from an operator
with a space.
Python can evaluate 1+1 just fine, but 1 + 1 is the preferred format
because it’s generally considered easier to read. This rule
of thumb applies to all of the operators in this section.""")
x, y = 9 , 5
print(f"{x} + {y} = {x+y}.")
print("{} - {} = {}".format(x,y,x- (-y)))

print("{} * {} = {}".format(x,y,x * (y)))

print(f"{x} / {y} = {x/y}")

print("{} / {} = {}".format(x,y, int(x/y)))


print("""The // operator first divides the number on the left by the number on
the right and then rounds down to an integer. This might not give the
value you expect when one of the numbers is negative.
For example, -3 // 2 returns -2. First, -3 is divided by 2 to get -1.5.
Then -1.5 is rounded down to -2. On the other hand, 3 // 2 returns 1
Another thing the above example illustrates is that // returns a
floating-point number if one of the operands is a float. This is why 9
// 3 returns the integer 3 and 5.0 // 2 returns the float 2.0.""")

print("{} // {} = {}".format(y , x , y//x))
print(f"{y} // {x} = {y//x}")


print("You can raise a number to a power using the ** operator:")
print(2 ** 3)
print(2 * 1.5)

print(2 ** -1)
print(100 ** -4)

print("""The % operator, or the modulus, returns the remainder of dividing
the left operand by the right operand:
3 divides 5 once with a remainder of 2, so 5 % 3 is 2. Similarly, 7 divides
20 twice with a remainder of 6.
In the last example, 16 is divisible by 8, so 16 % 8 is 0. Any time the
number to the left of % is divisible by the number to the right, the result""")
print(5%3)
print(20%7)
print(16 % 4)

print(1 % 3 )
print(44 % 333 )

print("""These potentially shocking results are really quite well defined. To calculate
the remainder r of dividing a number x by a number y, Python
uses the equation r = x - (y * (x // y)).
For example, to find 5 % -3, first find (5 // -3). Since 5 / -3 is about
-1.67, 5 // -3 is -2. Now multiply that by -3 to get 6. Finally, subtract
6 from 5 to get -1.""")

print(" 5 % -3 = " + str(5 % -3))
print(" - 1 % -2  = " + str(-1 % -2))
print("-3 % -2 = " + str(-3 % -2))


print("""The *, /, //, and % operators all have equal precedence, or priority,
in an expression, and each of these has a higher precedence than the +
and - operators. This is why 2*3 - 1 returns 5 and not 4. 2*3 is evaluated
first, because * has higher precedence than the - operator.""")


print("Exponent to print the first number raised toa the poer of the second number" )
base = float(input("Enter a float number as a base: "))
exponent = int(input("Enter an integer number as an exponent: "))

print(f"{base} to the power of {exponent} = {base ** exponent}")

print("Exponent to print the first number raised toa the poer of the second number" )
base = input("Enter a float number as a base: ")
base = float(base)
exponent = input("Enter an integer number as an exponent: ")
exponent = int(exponent)
print(f"{base} to the power of {exponent} = {base ** exponent}")

print("""Python has a few built-in functions you can use to work with numbers.
In this section, you’ll learn about three of the most common ones:
1. round(), for rounding numbers to some number of decimal places
2. abs(), for getting the absolute value of a number
3. pow(), for raising a number to some power""")

print(round(2.3))
print(round(2.7))
print(round(2.5))
print(round(3.5))
print(round(4.5))
print(round(5.5))
print(round(6.5))

print("""You can round a number to a given number of decimal places by passing
a second argument to round():""")
print(round(3.14149867, 3))
print(round(3.14149867, 2))
print(round(3.14149867, 4))

print("""The absolute value of a number n is just n if n is positive, and -n
if n is negative. For example, the absolute value of 3 is 3, while the
absolute value of -5 is 5.""")
print(abs(-3))
print(abs(3))

print(pow(2,3))
print(pow(2, -2))

print("""So, what’s the difference between ** and pow()? The pow() function
accepts an optional third argument that computes the first number
raised to the power of the second number and then takes the modulo
with respect to the third number.""")
x,y,z = 2,3,2
print(pow(x,y, z))
print(f"{(x ** y) % z}")

print("""The .is_integer() method can be useful for validating user input. For
example, if you are writing an app for a shopping cart for a store that
sells pizzas, you will want to check that the quantity of pizzas the customer
inputs is a whole number. You’ll learn how to do these kinds of
checks in""")
num = 2.5
print(num.is_integer())
num = 2.0
print(num.is_integer())


print("""1. Write a script that asks the user to input a number and then displays
that number rounded to two decimal places. When run, your
program should look like this:""")
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> review exercises')
num = float(input("enter a number as float with 4 deciamal points: "))
print(f"Your number is {num} and rounded to the 2 decimal places is {round(num,2)}")


print("""Write a script that asks the user to input a number and then displays
the absolute value of that number. When run, your program
should look like this:""")
user_input = int(input("ter your number"))
print("Your number is {} and its absolute is {}".format(user_input, abs(user_input)))


print("""Write a script that asks the user to input two numbers by using the
input() function twice, then display whether or not the difference
between those two number is an integer. When run, your program
should look like this:""")
print("Last question >>>>>>>>>>> >>>>>> >>>> :")
num1 = float(input("Enter the first number "))
num2 = float(input("Enter the second number "))
diff = num1 - num2
print(f" The difference betweeen the {num1} and {num2} is an integer? {diff.is_integer()} !")

n = 7.125
print(f"The value of n is: {n}")
print("""For example, to format the value of n in the above example to two
decimal places, replace the contents of the curly braces in the f-string
with {n:.2f}:""")
print(f" The value of n is : {n:.2f}")
print("""The colon (:) after the variable n indicates that everything after it is
part of the formatting specification. In this example, the formatting
specification is .2f.""")
n=1
print(f"The value of n is {n:.2f}")
n = 1234.56
print(f"The value of n is {n:,.2f}")
n = 1234567890
print(f"The value of n is {n:,}")

balance = 2000.0
spent = 256.35
remaining = balance - spent

print(f"After spending ${spent:.2f}, I was left with ${remaining:,.2f}")

print("""1. Print the result of the calculation 3 ** .125 as a fixed-point number
with three decimal places.""")
print(f"The caculation of 3 ** .125 as a fixed-point number with three decimal places is {3 **.125:.2f}")
print(f"{3 ** .125:.3f}")


print("""2. Print the number 150000 as currency, with the thousands grouped
with commas. Currency should be displayed with two decimal
places.""")
print(f"${150000:,.2f}")

print("""3. Print the result of 2 / 10 as a percentage with no decimal places.""")

print(f"{2 / 10:.0%}")
print(1 + 2j)

