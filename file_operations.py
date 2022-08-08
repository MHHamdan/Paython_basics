print("""In this section, you’ll learn how to:
• Create directories and files
• Iterate over the contents of a directory""")


from pathlib import Path
new_dir = Path.home() / "my_new_directory1"


print("""After importing the Path class, you create a new path to a directory
called new_directory/ in your home folder and assign this path to the
new_dir variable. Then you use the .mkdir() method to create the new
directory.
You can now check that the new directory exists and is, in fact, a directory:""")





print("""When you call the .mkdir() method, Python attempts to create the
new_directory/ folder again. Since it already exists, this operation fails
and a FileExistsError exception is raised.
If you want to create a new directory if it doesn’t exists, but avoid raising
the FileExistsError if it does, then you can set the options exist_ok
parameter of the .mkdir() method to True:

When you execute .mkdir() with the exist_ok parameter set to True, the
directory is created if it does not exist, or nothing happens if it does.
Setting exist_ok to True when calling .mkdir() is equivalent to the following
code:""")

if not new_dir.exists():
    new_dir.mkdir()

new_dir.mkdir(exist_ok=True)

print(new_dir.exists())

print(new_dir.is_dir())

print("""Although the above code works just fine, setting the exist_ok parameter
to True is shorter and doesn’t sacrifice readability.
Now let’s see what happens if you try to create a subdirectory within
a directory that does not exist:

The problem is that the directory folder_a/ does not exist. Typically,
to create a directory, all of the parent directories of the target directory
folder_b/ in the path must already exist.
To create any parent directories needed in order to create the target
directory, set the optional parents parameter of .mkdir() to True:
""")

print("""Now .mkdir() creates the parent directory folder_a/ so that the target
directory folder_b/ can be created.
By putting all of this together you get the following common pattern
for creating directories:
path.mkdir(parents=True, exist_ok=True)
By setting both the parents and exist_ok parameters to True, the entire
path is created, if needed, and no exception is raised if the path already
exists.
This pattern is useful, but it may not always be what you want. For
example, if the path is input by a user, you may wish to instead catch
an exception so that you can ask the user to verify that the path they
entered is correct. They might have just mistyped a directory name!""")

nested_dir = new_dir / "folder_a" / "folder_b"
nested_dir.mkdir(parents=True, exist_ok=True)
print(nested_dir)


print("""Now let’s look at how to create files. Create a new Path object called
file_path for the path new_directory/file1.txt:""")
file_path = new_dir / 'file1.txt'
print(file_path.exists())

print("""You can create the file using the Path.touch() method:

Unlike .mkdir(), the .touch() method does not raise an exception if the
path being created already exists:""")
file_path.touch()
print(file_path.exists())


print("""Unlike .mkdir(), the .touch() method has no parents parameter that
you can set to automatically create an parent directories. This means
that you need to first create any directories needed before calling
.touch() to create the file.
For instance, you can use .parent to get the path to the parent folder
for file2.txt and then call .mkdir() to create the directory:
Since .parent returns Path object, you can chain the .mkdir() method
to write the entire operation on a single line of code.
With the folder_c/ directory created, you can successfully create the
file:""")
file_path = new_dir / "foder_c" / "file2.txt"
file_path.parent.mkdir(exist_ok=True)
file_path.touch()
print("""You can’t create a file in a directory that doesn’t exist:""")

#file_path.touch()
print(file_path.is_file())


print("""Iterating Over Directory Contents
Using pathlib, you can iterate over the contents of a directory. You
might need to do this in order to process all of the files in a directory.
The word process is vague. It could be reading the file and extracting
some data, or compressing files in the directory, or some other operation.
For now, let’s focus on how you go about retrieving all of the contents
of a directory. You’ll learn how to read data from files in the next
section.
Everything in a directory is either a file or a subdirectory. The
Path.iterdir() method returns an iterator over Path objects representing
each item in the directory.
To use .iterdir(), you first need a Path representing a directory. Let’s
use the new_directory/ folder you created previously in your home directory and assigned to the new_dir variable:""")

print("""You won’t often need to convert this to a list, but we’ll do it in subsequent
examples to keep the code short. Generally, you’ll use .iterdir()
in a for loop like you did in the first example.
Notice that .iterdir() only returns items that are directly contained
in the new_directoy/ folder. That is, you can’t see the path to the file
that exists in the folder_c/ directory.
There is a way to iterate over the contents a directory and all of its
subdirectories, but you can’t do it easily with .iterdir(). We’ll get to
this task in a moment, but first let’s talk about how to search for files
within a directory.""")

for path in new_dir.iterdir():
    print(path)
print(list(new_dir.iterdir()))


print("""Searching For Files In a Directory
Sometimes you only need to iterate over files of a certain type, or files
with certain naming schemes. You can use the Path.glob() method
on a path representing a directory to get an iterable over directory
contents that meet some criteria.
It might seem strange that a method that searches for files is called
.glob(). The reason the method is given this name is historical. In
early version of the Unix operating system, a program called glob was
used expand to file path patterns to full file paths.
The .glob() method does something similar. You pass to the method a
string containing a partial containing a wildcard character and .glob()
returns a list of file paths that match the pattern.""")


print("""A wildcard character is a special character that acts as a placeholder
in a pattern. The are replaced with other characters to create
a concrete file path. For example, in the pattern "*.txt", the asterisk *
is a wildcard character that can be replaced with any number of other
characters.
The pattern "*.txt" matches any file path that ends with.txt. That is,
if replacing the * in the pattern with everything in some file path up to
the last four characters results in the original file path, then that file
path is a match for the pattern "*.txt".
Let’s look at an example using the new_directory/ folder previously assigned
to the new_dir variable:""")
for path in new_dir.glob("*.txt"):
    print(path)

print("""Like .iterdir(), the .glob() method returns an iterable of paths, but
this time only paths that match the pattern "*.txt" are returned.
.glob() returns only paths that are directly contained in the folder on
which it is called.""")



print(list(new_dir.glob('*.txt')))

print("""Wildcard
Character Description Example Matches
Does Not
Match
* Any number
of characters
"*b*" b, ab, bc, abc a, c, ac
? A single
character
"?bc" abc, bbc, cbc bc, aabc,
abcd
[abc] Matches one
character in
the brackets
[CB]at Cat, Bat at, cat, bat
W""")

paths = [
    new_dir / "program1.py",
    new_dir / "program2.py",
    new_dir / "folder_a" / "program3.py",
    new_dir / "folder_a" / "folder_b" / "image1.jpg",
    new_dir / "folder_a" / "folder_b" / "image2.png",
    ]

for path in paths:
    path.touch()


print("""The * Wildcard
The * wildcard matches any number of characters in a file path pattern.
For example, the patter "*.py" matches all file paths that end in .py:""")

print(list(new_dir.glob('*.py')))
print(list(new_dir.glob('*1*')))

print("""The pattern "*1*" matches any file path containing the number 1 with
any number of characters before and after it. The only files in new_-
directory/ that contain the number 1 are file1.txt and program1.py.


The pattern "1*" matches files paths that start with the number 1 and
are followed by any number of characters after it. There are no files
in the new_directory/ folder that match this, so .glob() doesn’t return
anything.""")

print(list(new_dir.glob('1*')))
print("""The ? Wildcard
The ? wildcard character matches a single character in a pattern. For
example, the pattern "program?.py" will match any file path that starts
with the word program followed by a single character and then .py:""")

print(list(new_dir.glob('program?.py')))

print("""You can use multiple instances if ? in a single pattern:""")
print(list(new_dir.glob('?older_?')))

print("""The pattern "*1.??" matches any file path that contains a 1 followed
by a dot (.) and two more characters. The only path in new_directory/
matching this pattern is program1.py. Notice that file1.txt doesn’t""")
print(list(new_dir.glob('*1.??')))


print("""The [] Wildcard
The [] wildcard works kind of like the ? wildcard because it matches
only a single character. The difference is that instead of matching any
single character like ? does, [] only matches characters that are included
between the square brackets.
For example, the pattern "program[13].py" matches any path containing
the word program, followed by either a 1 or 3 and the extension .py.
In the new_directory/ folder, program1.py is the only path matching this
pattern:""")

print(list(new_dir.glob('program[14].py')))


print("""Recursive Matching With The ** Wildcard
The major limitation you’ve seen with both .iterdir() and .glob() is
that they only return paths that are directly contained in the folder on
which they are called.
For example, new_dir.glob("*.txt") only returns the file1.txt path in
new_directory/. It does not return the file2.txt path in the folder_c/
subdirectory, even though that path matches the "*.txt" pattern.
There is a special wildcard character ** that makes the pattern recursive.
The common was to use it is to prefix your pattern with "**/".
This tells .glob() to match your pattern in the current directory and
any of its subdirectories.
For example, the pattern "**/*.txt" matches both file1.txt and
folder_c/file2.txt":""")

print(list(new_dir.glob("**/*.txt")))
print(list(new_dir.glob("**/*.py")))

print("""There is also a shorthand method to doing recursive matching called
.rglob(). To use it, pass the pattern without the **/ prefix:
The r in .rglob() stands for “recursive.” Some people prefer to use
this method instead of prefixing their patterns with **/ because it is
slightly shorter. Both versions are perfectly valid. In this book, we’ll
use .rglob() instead of the **/ prefix.""")
print(list(new_dir.rglob("*.py")))

print("""To move a file or directory, use the .replace() method. For example,
the following moves the file1.txt file in the new_directory/ folder to
the folder_a/ subfolder:""")
source = new_dir / 'file1.txt'
destination = new_dir / 'folder_a' / 'file1.txt'
source.replace(destination)

print("""The .replace() method is called on the source path. The destination
path is passed to .replace() as a single argument. Notice that
.replace() returns the path to the new location of the file.


If the destination path already exists, .replace() overwrites the
destination with the source file without raising any kind of exception.
This can cause undesired loss of data if you aren’t careful.
You may want to first check if the destination file exists, and
move the file only in the case that it does not:""")


if not destination.exists():
    source.replace(destination)
    


print("""You can also use .replace() to move or rename an entire directory.
For instance, the following renames the folder_c subdirectory of new_-
directory/ to folder_d/:""")
##source = new_dir / "folder_a"
##destination = new_dir / "folder_d"
##print(destination)
##dd = source.replace(destination)
##print(dd)

print("""Again, if the destination folder already exists, it is completely replaces
with the source folder, which could result in the loss of quite a bit of
data.
To delete a file, use the .unlink() method:""")

#file_path = new_dir / "program2.py"

#print(list(new_dir.iterdir()))

print("""If you want to ignore the exception, set the optional missing_ok parameter
to True:""")
print(file_path.unlink(missing_ok = True))

print(""".unlink() only works for paths representing files. To remove a directory,
use the .rmdir() method. Keep in mind that the folder must be
empty, otherwise an OSError exception is raised:""")

#folder_d = new_dir / "folder_d"
#print(folder_d.rmdir())

print("""In the case of folder_d/, it only contains a single file called file2.txt.
To delete folder_d/, first delete all of the files it contains:""")
##print(folder_d.exists())
##for path in folder_d.iterdir():
##    path.unlink()
##
##folder_d.rmdir()


print("""If you need to delete an entire directory, even if it is non-empty, then
pathlib won’t help you much. However, you can use the rmtree() function
from the built-in shutil module:""")
import shutil

folder_a = new_dir / "folder_a"
shutil.rmtree(folder_a)

print(folder_a.exists())

print(list(new_dir.rglob("image*.*")))

print("""Create a new directory in your home folder called my_folder/.""")
from pathlib import Path

new_dir = Path.home() / "my_folder1"
new_dir.mkdir(exist_ok= True)
print(new_dir)

print("""Inside my_folder/ create three files """)
file1 = new_dir / 'file1.txt'
file2 = new_dir / "file2.txt"
image1 = new_dir / "image1.png"

file1.touch()
file2.touch()
image1.touch()

print("""Move the file image1.png to a new directory called images/ inside of
the my_folder/ directory.""")
images_dir = new_dir / "images"
images_dir.mkdir(exist_ok=True)
image1.replace(images_dir / "image1.png")

print("""Delete the file file1.txt""")
file1.unlink()

print("""Delete the my_folder/ directory.""")
shutil.rmtree(new_dir)



print("""Challenge: Move All Image Files To
a New Directory
In the Chapter 12 Practice Files folder, there is a subfolder called
documents/. The directory contains several files and subfolder. Some
of the files are images ending with either the .png, .gif, or the .jpg file
extension.
Create a new folder in the Practice Files folder called images/ and move
all image files to that folder. When you are done, the new folder should
have four files in it""")

from pathlib import Path
documents_dir = (
    Path.home() /
    "my_new_directory1" /
    "folder_d" /
    "folder_b"
    )

images_dir = Path.home() / "my_new_directory1" / "images"
images_dir.mkdir(exist_ok=True)

for path in documents_dir.rglob("*.*"):
    if path.suffix.lower() in [".png", ".jpg", ".gif"]:
        path.replace(images_dir / path.name)


print("""There are two issues, though, that can be frustrating
when working with text files:
1. Character encoding
2. Line endings""")

print("""Character Encoding
Text files are stored on disk as a sequence of bytes. Each byte, or group
of bytes in some cases, represents a different character in the file.
When text files are written, characters typed on the keyboard are converted
to bytes in a process called encoding. When a text file is read,
the bytes are decoded back into text.
The integer a character is associated to is determined by the file’s
character encoding. There are many character encodings. Four of
the most widely used character encodings are:
1. ASCII
2. UTF-8
3. UTF-16
4. UTF-32
Some character encodings, such as ASCII and UTF-8, encode characters
the same way. For example, numbers and English letters are
encoded the same way in both ASCII and UTF-8.
The difference between ASCII and UTF-8 is that UTF-8 can encode
more characters than ASCII. ASCII can’t encode characters like ñ or
ü, but UTF-8 can. This means you can decode ASCII encoded text with
UTF-8, but you can’t always decode UTF-8 encoded text with ASCII.""")

print("""Serious problems may occur when different encodings are used
to encode and decode text.
For instance, text encoded as UTF-8 that is decoded with UTF-
16 may be interpreted as an entirely different language than
originally intended!""")
print("""Knowing what encoding a file uses is important, but it isn’t always obvious.
On modern Windows computers, text files are usually encoded
with UTF-16 or UTF-8. On macOS and Ubuntu Linux, the default
character encoding is usually UTF-8.
For the remainder of this section, we’ll assume that the character encoding
of all text files that we work with is UTF-8. If you encounter
problems, you may need to alter the examples to use a different encoding.""")


print("""Line Endings
Each line in a text file ends with one or two characters that indicate
the line has ended. These characters aren’t usually displayed in a text
editor, but they exist as bytes in the file data.
The two characters used to represent line endings are the carriage
return and line feed characters. In Python strings, these characters
are represented by the escape sequence \r and \n, respectively.
On Windows, line endings are represented by default with both a carriage
return and a line feed. On macOS and most Linux distributions,
line endings are represented with just a single line feed character.
When you read a Windows file on macOS or Linux you will sometimes
see extra blank lines between lines of text. This is because the carriage
return also represents a line ending on macOS and Linux.
For example, suppose the following text file was created in Windows:""")

print("""There are two ways to create a file object in Python:
1. The Path.open() method
2. The open() built-in function
Let’s look at each of these.
The Path.open() Method
To use the Path.open() method, you first need a Path object""")

from pathlib import Path
path = Path.home() / "hello.txt"
print(path)
path.touch()
file = path.open(mode="r", encoding="utf-8")

print("""Two keyword parameters used to open the file:
1. The mode parameter determines in which mode the file should be
opened. The "r" argument opens the file in read mode.
2. The encoding parameter determines the character encoding used to
decode the file. The argument "utf-8" represents the UTF-8 character
encoding.
You can inspect the file variable to see that it is assigned to a text file
object:""")

print(file)


print("""Text file objects are instances of the TextIOWrapper class. You will never
need to instantiate this class directly, since you can create them with
the Path.open() method.
There are a number of different modes you can use to open a file.
These are described in the following table:
Mode Description
"r" Creates a text file object for reading and raises an error if
the file can’t be opened.
"w" Creates a text file object for writing and overwrites all
existing data in the file.
"a" Creates a text file object for appending data to the end of
a file.
"rb" Creates a binary file object for reading and raises an
error if the file can’t be opened.
"wb" Creates a binary file object for writing and overwrites all
existing data in the file.
"ab" Creates a binary file object for appending data to the end
of the file
The strings for some of the most commonly used character encodings
can be found in the table below:
String Character Encoding
"ascii" ASCII
"utf-8" UTF-8
“"utf-16” UTF-16
"utf-32" UTF-32""")
 
print("""When you create a file object with .open(), Python maintains a link to
the file resource until you either explicitly tell Python to close the file,
or the program ends.
Important
You should always explicitly tell Python to close a file.
Forgetting to close opened files like littering. When your program
stops running, it shouldn’t leave unnecessary waste laying
around the system.
To close a file, use the file object’s .close() method:""")
file.close()


print("""Using Path.open() is the preferred way to open a file when you have an
existing Path object, but there is also a built-in function called open()
that you can use to open a file.
The open() Built-in
The built-in open() function works almost exactly like the Path.open()
method, except that it’s first parameter is a string containing the path
the file you want to open.
First, create a new variable called file_path and assign to it a string
containing the path to the hello.txt file you created above""")

file_path = "/home/hamdan/hello.txt"
file = open(file_path, mode="r", encoding="utf-8")
print(file)
file.close()
print(file)



print("""The with Statement
When you open a file, your program is accessing data external to the
program itself. The operating system must manage the connection
between your program and physical file itself. When you call a file object’s
.close() method, the operating system knows to close the connection.
If your program crashes between the time that a file is opened and
when it is closed, the system resources maintained by the connection
may continue to live on until the operating system realizes that it’s no
longer needed.
To ensure that file system resources are cleaned up even if a program
crashes, you can open a file in a with statement. The pattern for using
the with statement looks like this:""")



with path.open(mode="r", encoding ="utf-8") as file:
    pass

print("""The with statement has two parts: a header and a body. The header
always starts with the with keyword and ends with a colon (:). The
return value of path.open() is assigned to the variable name after the
as keyword.
After the with statement header is an indented block of code. When
code execution leaves the indented block, the file object assigned to
file is closed automatically, even if any exception is raised during execution
of code inside of the block.
with statements also work with the open() built-in:""")

with open(file_path, mode="r", encoding="utf-8") as file:
    pass


print("""There really is no reason not to open files in a with statement. It is
considered the Pythonic way for working with files. For the rest of
this book, we will use this pattern whenever opening a file.""")

path = Path.home() / "hello.txt"
with path.open(mode="r", encoding="utf-8") as file:
    text = file.read()
    print(text)
print("*" * 6 )
with open(file_path, mode="r", encoding="utf-8") as file:
    text1 = file.read()
    print(text1)

print(type(text))

with path.open(mode="r", encoding="utf-8") as file:
    for line in file.readlines():
        print(line)

print("""The .readlines() method returns an iterable of lines from the file. At
each step of the for loop the next line of text in the file is returned and

Notice that an extra blank line is printed between the two lines of
text. This doesn’t have anything to do with line endings in the file. It
happens because the print() function automatically inserts a newline
character at the end of every string it prints.
To print the two lines without the extra blank line, set the print() function’s
optional end parameter to an empty string:""")

with path.open(mode="r", encoding="utf-8") as file:
    for line in file.readlines():
        print(line, end="")
print("""There are many times you might want to use .readlines() instead of
.read(). For example, each line in a file might represent a single record.
You can loop over the lines of text in the file with .readlines() and
process them as needed.
If you try to read from a file that does not exists, both .open() and
open() raise a FileNotFoundError""")

path = Path.home() / "new_file.txt"
path.touch()
with path.open(mode="r", encoding="utf-8") as file:
    text = file.read()
    print(text)

print(""".""")

with path.open(mode="w", encoding="utf-8") as file:
    print(file.write("""\n Hi there!
                     Writing Data To a File
To write data to a plain text file, you pass a string to a file object’s
.write() method. The file object must be opened in write mode by
passing the value "w" to the mode parameter"""))
print(path)
with path.open(mode='r', encoding='utf-8') as file:
    text = file.readlines()
    print(text, end='')


print("""When a file is opened in append mode new data is written to the end
of the file and old data is left intact. The newline character is put at
the beginning of the string so that the word "Hello" is printed on a new
line at the end of the file.
Without a newline character at the beginning of the string, the word
"Hello" would be printed on the same line as any existing text at the
end of the file.
You can check that the world "Hello" is written to the second line by
opening and reading from the file:""")


with path.open(mode='r', encoding='utf-8') as file:
    text = file.read()
    print(text)


lines_of_text = [
    "Hello from line 1\n",
    "Hello from line 2\n",
    "Hello from line 3\n",
    "Hello from line 4\n",
    "Hello from line 5\n",
    ]

with path.open(mode='w', encoding='utf-8') as file:
    print(file.writelines(lines_of_text))

with path.open(mode='r', encoding='utf-8') as file:
    text = file.read()
    print(text)


print("""If you open a non-existent path in write mode, Python attempts to
automatically create the file. If all of the parent folders in the path
exist, then the file can be created without problem:""")

path = Path.home() /"nn_new_file.txt"
path.touch()
with path.open(mode="w", encoding="utf-8") as file:
    print(file.write("Hello!"))
    
path = Path.home() /"test" / "test1" /"test2" /"test.txt"
path.parent.mkdir(exist_ok=True, parents=True)
with path.open(mode='w', encoding='utf-8') as file:
    print(file.write('Hello world'))



print("""Write the following text to file called starships.txt in your home direcotr""")

lines = [
    'Discovery\n',
    'Enterprise\n',
    'Defiant\n',
    'Voyager\n',
    ]

path = Path.home() / "review" /"startships.txt"
path.parent.mkdir(exist_ok=True, parents=True)
with path.open(mode='w', encoding='utf-8') as file:
    print(file.writelines(lines))


print("""Read the file starhips.txt you created in Exercise 1 and print each
line of text in the file. The output should not have extra blank lines
between each word.""")
with path.open(mode='r', encoding='utf-8') as file:
    text = file.read()
    print(text, end='')

with path.open(mode='r', encoding='utf-8') as file:
    for starship in file.readlines():
        print(starship, end='')
print("""3. Read the file startships.txt and print the names of the starships
that start with the letter D.""")

with path.open(mode='r', encoding='utf-8') as file:
    for starship in file.readlines():
        if starship.startswith("D"):
            print(starship, end='')



temperature_readings = [68, 65, 68, 70, 74, 72]
print("""Each day a new list of numbers is generated. To store these values to
a file, you can write the values from each day on a new line in a text
file and separate each value with a comma""")
from pathlib import Path
file_path = Path.home() /"temperatures.txt"
#file_path.touch()

with file_path.open(mode='a', encoding='utf-8') as file:
    print(file.write(str(temperature_readings[0])))
    for temp in temperature_readings[1:]:
        print(file.write(f", {temp}"))


print("""This creates a file called temperatures.csv in your home directory and
opens it in append mode. On a new line at the end of the file, the first
value in the temperature_readings list is written to the file. Then each
remaining value in the list is written, preceded by a comma, to the
same line.
The final string of text written to the file "68,65,68,70,74,72". You can
verify this by reading the to text:""")

with file_path.open(mode='r', encoding='utf-8') as file:
    text = file.read()

print(text)


print("""The format that in which you have saved the values is called commaseparated
value, or CSV for short. The temperatures.csv file is called
a CSV file.
CSV files are a great way to store records of sequential data because you
can recover each row of the CSV value as a list:""")

temperatures = text.split(",")
print(temperatures)

print("""You can change convert the strings to integers using a list comprehension:""")
int_temperatures = [int(temp) for temp in temperatures]
print(int_temperatures)


print("""The csv Module
The csv module can be used to read and write CSV files. We’ll re-work
the previous example using the csv module so that you see how it
works and what operations it takes care of for you.""")


import csv

daily_temperatures = [
  [68, 65, 68, 70, 74, 72],
  [67, 67, 70, 72, 72, 70],
  [68, 70, 74, 76, 74, 73],
  ]
print(daily_temperatures)

file_path = Path.home() / "temperature.csv"
file = file_path.open(mode="w", encoding="utf-8")

with file_path.open(mode="w", encoding="utf-8") as file:
    writer = csv.writer(file)
    for temp_list in daily_temperatures:
        print(writer.writerow(temp_list))

        
