print("""These input and output methods are not useful in several common
scenarios:
• The input values are unknown while writing the program
• The program requires more data than a user can be expected to
type in by themselves
• Output must be shared with other people after the program runs
This is where files come in.
In this chapter, you will learn how to:
• Work with file paths and file metadata
• How to read and write text files
• How to read and write Comma-Separated Value (CSV) files
• How to create, delete, copy, and move files and folders

The Anatomy of a File
There are a multitude of types of files out there: text files, image files,
audio files, and PDF files, just to name a few. Ultimately, though, a
file is just a sequence of bytes called the contents of the file.
Each byte in a file can be thought of as an integer with a value between
0 and 255, including both endpoints. The bytes are the values that are
stored on a physical storage device when a file is saved.
When you access a file on a computer, the contents of the file are read
from the disk in the correct sequence of bytes. The important thing to
know here is that there is nothing intrinsic to the file itself that dictates
how to interpret the contents.
As a programmer, it’s your job to properly interpret the contents when
you open a file. This might sound difficult, but Python does a lot of the
hard work for you.


For example, when you open a text file, Python can convert the numerical
bytes of the file into text characters for you. You do not need to
know the specifics of how this conversion happens. There are tools in
the standard library for working with all sorts of file types, including
images and audio files.
In order to access a file from a storage device, a whole host of things
need to happen. You need to know on which device the file is stored,
how to interact with that device, and where exactly on the device the
file is located.
This monumental task is managed by a file system. Python interacts
with the file system on your computer in order to read, write, and manipulate
files.""")


print("""\n \n \n The file system on a computer does two things:
1. It provides an abstract representation of the files stored on your
computer and devices connected to it.
2. It interfaces with devices to control storage and retrieval file data.

Different operating systems use different file systems. This is
very important to keep in mind when writing code that will be
run on different operating systems.


The file system itself manages communication between the computer
and the physical storage device, so the only part of the file system you
need to understand as a programmer is how it represents files.

""")


print("""The File System Hierarchy
File systems organize files in a hierarchy of directories, which are
also known as folders. At the top of the hierarchy is a directory called
the root directory. All other files and directories in the file system
are contained in the root directory.
Each file in directory has a 􀑀le name that must be unique from any
other file in the same directory. Directories can also contain other
directories, called subdirectories or subfolders.
The following directory tree visualizes the hierarchy of files and directories
in an example file system:

In this file system, the root folder is called root/. It has two subdirectories:
app/ and photos/. The app/ subdirectory contains a program.py file
and a data.txt file. The photos/ directory also has two subdirectories,
cats/ and dogs/, that both contains two image files.""")


print("""

For example, the file path for the jack_russel.gif file in the above file
system is root/photos/dogs/jack_russel.gif.
How you write file paths depends on your operating system. Here are
three examples of file paths on Windows, macOS, and Linux:

All three of these file paths locate a text file named hello.txt that is
stored in the Documents subfolder of the user directory for a user named
David. As you can see, there are some pretty big differences between
file paths from one operating system to another.
On macOS and Ubuntu Linux, the operating system uses a virtual
􀑀le system that organizes all files and directories for all devices on
the system under a single root directory, usually represented by a forward
slash symbol (/). Files and folders from external storage devices
are usually located in a subdirectory called media/.
In Windows, there is no universal root directory. Each device has a
separate file system with a unique root directory that is named with
a drive letter followed by a colon (:) and a back slash symbol (\).
Typically, the hard drive where the operating system is installed is
assigned the letter C, so the root directory of the file system for that
drive is C:.
The other major difference between Windows, macOS, and Ubuntu
files paths is that directories in a Windows file path are separated by
back slashes (\), whereas directories in macOS and Ubuntu file paths
are separated by forward slashes (/

When you write programs that need to run on multiple operating systems,
it is critical that you handle the differences in file paths appro-
priately. In versions of Python greater than 3.4, the standard library
contains a module called pathlib helps take the pain out of handling
file paths across operating systems.
Read on to learn how to use pathlib to work with file paths in Python.

""")


print("""To work with file paths in Python, use the standard libraries pathlib
module. You’ll need to import the module before you can do anything
with it.""")

import pathlib


print("""Creating Path Objects
There are several ways to create a new Path object:
1. From a string
2. With Path.home() and Path.cwd() class methods
3. With the / operator
The most straightforward way to create a Path object is from a string

Creating Path Objects from Strings
For instance, the following creates a Path object representing the
macOS file path "/Users/David/Documents/hello.txt":
""")

file_path = pathlib.Path('/home/hamdan/Documents/RealPython/files/mytext.txt')
print(file_path) 
print("""There’s problem, though, with Windows paths. On Windows, directories
are separated by back slashes \. Python interprets back slashes as
the start of an escape sequence that represent a special character in
the string, such as the newline character (\n).
Attempting to create a Path object with the Windows file path
  raises an exception:""")

print("You can also turn the string into a raw string by prefixing it with an r:")
path = pathlib.Path(r"C:\Users\Hamdan\Desktop\hello.txt")
print(""" r 'C:\... This tells Python to ignore any escape sequences and just read the
string as-is.""")

print("""Path.home() and Path.cwd()
Besides creating a Path object from a string, the Path class has class
methods that return Path objects of special directories. Two of the
most useful class methods are Path.home() and Path.cwd().
Every operating system has a special directory for storing data for the
currently logged in user. This directory is called the user’s home directory.
The location of this directory depends on the operating system: Users for Windows
and macOS and home for Ubuntu Linux""")

print("""The Path.home() class method creates a Path object representing the
home directory regardless of which operating system the code runs
on:
When you inspect the home variable on Windows, you will see something
like this:
The Path object created is a subclass of Path called WindowsPath. On
other operating systems, the Path object returned is a subclass called
PosixPath.
For example, on macOS, inspecting home will display something like
the following:""")

home = pathlib.Path.home()
print(home)
file_path = pathlib.Path('/home/hamdan/Documents/RealPython/files/mytext.txt')
print(file_path)

print("""The Path.cwd() class method returns a Path object representing the
current working directory, or CWD. The current working directory
is a dynamic reference to a directory that depends on where a
process on the computer is currently working.
This is not always the case, though. Moreover, the current working
directory may change during the lifetime of a program.
Path.cwd() is useful, but be careful when you use it. When you do,
make sure you know that the current working directory refers the directory
that you expect it to""")

print("""Using the / Operator
If you have an existing Path object, you can use the / operator to extend
the path with subdirectories or file names.
For example, the following creates a Path object representing a file
named hello.txt in the Documents subdirectory of the current user’s
home directory:
The / operator must always have a Path object on the left hand side.
The right hand side can have either string representing a single file or
directory, or a string representing a path, or another Path object.""")

file = pathlib.Path.cwd()
print(file)

print("""Absolute vs. Relative Paths
A path that begins with the root directory in a file system is called an
absolute 􀑀le path. Not all file paths are absolute. A file path that is
not absolute is called a relative 􀑀le path.
Here’s an example of a Path object that references a relative path:
>>> # Relative Windows path
>>> path = pathlib.Path(r"Photos\image.jpg")
>>> # Relative macOS or Linux path
>>> path = pathlib.Path("Photos/image.jpg")
Notice that the path string does not start with C:\ on Windows, or /
on macOS and Linux.
You can check whether or not a file path is absolute using the .is_-
absolute() method:
>>> path.is_absolute()
False""")

print(file.is_absolute())

print("""Relative paths only make sense when considered within the context
of some other directory. They are perhaps most commonly used to
describe the path to a file relative to the current working directory, or
the user’s home directory.
You can extend a relative path to an absolute path using the forward
slash (/) operator:
>>> home = pathlib.Path.home()
WindowsPath('C:/Users/David')
>>> home / pathlib.Path(r"Photos\image.png")
WindowsPath('C:/Users/David/Photos/image.png')
On the left of the forward slash (/), put an absolute path to the directory
that contains the relative path. Then put the relative path on the
right side of the forward slash.

Once you create a Path object, you can inspect the various components
of the file path that it refers to.""")



print("""Accessing File Path Components
All file paths contain a list of directories. The .parents attribute of a
Path object returns an iterable containing the list of directories in the
file path:""")

path = pathlib.Path.home() / "mytext.txt"
print(path)
print(list(path.parents))

print("""Notice that the list of the directories are returned in reverse order
from how they appear in the file path. That is, the last directory in
the path is the first directory in the list of parent directories.
You can iterate over the parent directories in a for loop:
>>> for directory in path.parents:
... print(directory)""")

for directory in path.parents:
    print(directory)

print("""The .parent attribute returns the name of the first parent directory in
the file path as a string:""")
print(path.parent)


print("""If the file path is absolute, you can access the root directory of the file
path with the .anchor attribute:""")

print(path.anchor)

print("""Note that .anchor returns a string, and not another Path object.
For relative paths, .anchor return an empty string:""")
path = pathlib.Path('mytext.txt')
print(path.anchor)


print("""The .name attribute returns the name of the file or directory that the
path points to:""")

home = pathlib.Path.home()
print(home.name)
path = home / 'mytext.txt'
print(path.name)

print("""The name of a file is broken down into two parts. The part to the left
of the dot (.) is called the stem, and the part to the right of the dot (.)
is called the su􀑂x or 􀑀le extension.
The .stem and .suffix attributes return strings containing each of these
parts of the file name:""")

path = pathlib.Path.home() / "hello.txt"
print(path.stem)
print(path.suffix)

print(path.exists())

print(file_path.exists())
print(path.is_file())
print(file_path.is_file())

print(path.is_dir())
print(file_path.is_dir())
print(home.is_dir())


print("""Create a new Path object to a file called my_file.txt in a folder called
my_folder/ in your computer’s home directory. Assign this Path object
to the variable name file_path.""")

print("""Check whether or not the path assigned to file_path exists.""")
my_path = pathlib.Path.home() / 'my_folder/my_file.txt'
print(my_path.exists())
print(my_path.is_dir())
print(my_path.is_file())

print("""Print the name of the path assigned to file_path. The output
should be my_file.txt.""")
print(my_path.name)

print("""4. Print the name of the parent directory of the path assigned to
file_path. The output should be my_folder.""")

print(my_path.parent)

print(my_path.anchor)
print((my_path.parent.name))




