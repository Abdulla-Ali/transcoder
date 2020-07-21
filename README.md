---
title: Transcoder
author: James Shuttleworth and YOUR NAME HERE
---

Transcoder is a tool for converting data from one format to
another. It's incomplete at the moment, so you will need to help
finish it.

You will need to learn a few things along the way, unless you know
them already. In particular, you will need:

 - Basic python
 - Virtual environments (venv)
 - PyDoc
 - PyTest
 - Basic Linux CLI
 - Data representation
 
# Introduction

This is a very simple tool, but it does (or will do) a few useful things.  

In cybersecurity, we often have to work with data in different
representations. For example, when creating payloads for exploits, we
might have to switch between bytes represented as their ASCII values
and their binary, decimal or hexadecimal (hex) representation.  For
example, the capital letter A has the ASCII code 65.  65 in hex
is 41. In octal it is 101, and in binary it is 01000001.

In linux, you can view data in different formats using `hexdump` and `xxd`.

If you type `xxd` into the shell and press enter, then type some text followed by ^D (Control-D), it will display it in hex.

```
$xxd
This is some text. ABC
^D
00000000: 5468 6973 2069 7320 736f 6d65 2074 6578  This is some tex
00000010: 742e 2041 4243 0a                        t. ABC.

```

You can probaly spot the ABC in hex, since it comes out as 41 42 43.
The leftmost column is an address for the start of the line.  The
first line is at position 0. The next one at position 10 in hex, so 16
in decimal - count the characters and you can verify this. The
`hexdump` command could do this, too.

We can get the same using binary like this:

```
$xxd -b
This is some text. ABC
^D
00000000: 01010100 01101000 01101001 01110011 00100000 01101001  This i
00000006: 01110011 00100000 01110011 01101111 01101101 01100101  s some
0000000c: 00100000 01110100 01100101 01110011 01110100 00101110   test.
00000012: 00100000 01000001 01000010 01000011 00101110 00001010   ABC..
```

Here we can only get 6 characters per line, because of how long th ebinary representation is. As you can see, the addresses on the left are still in hex.

And for octal, we can use `hexdump`:

```
hexdump -b
This is some text. ABC.
^D
This is some text. ABC.
0000000 124 150 151 163 040 151 163 040 163 157 155 145 040 164 145 170
0000010 164 056 040 101 102 103 056 012
0000018
```

And you should spot the 101 102 103 that is "ABC".


But what a lot of hassle! Wouldn't it be nice to have a single command
that gave us *all* representations at once?  Enter TRANSCODER!

# Getting Started

This repository contains an incomplete version of the `transcoder`
application, and your job is to finish it.

## Comments and docstrings

You'll find a lot of guidance in the source code in the form of
comments (In Python, these are lines beginning with the `#`
character - pronounced 'hash', not 'pound') and "docstrings". You can
find out about these concepts by searching the Web, or referring to
the module material if you're here from the Coventry University module
4061CEM.

The commented lines are just for helping anyone reading the code. They
describe what the intention is and, if the code is written properly,
what the code does.  Unfortunately it is all too easy to make mistakes
in code and so you can't always be 100% sure that the code does what
the comment tells you it does. The code in this repo is hopefully 100%
correct, but as you develop your own or review that of others, bear
this in mind.

The docstrings are descriptions of what units of code do. Usually this
will be classes, functions, modules and the data passed to or stored
by these.

To view the documentation for the file `transcoder.py`, from the
directory in which this readme is located, you can execute `pdoc
./src/transcoder.py`. It's just like a Linux `man` page.  Press Q to
quit if it goes over one screen.

You should document your code as you write. Use comments for people
that need to know what your code does in order to modify or maintain
it (including yourself) and docstrings for people that have to make
use of it without viewing the internals.  That could be users, or
people calling on your classes and functions in their own code.

### Prettier documentation

To view the documentation in your browser, you can output the content
as HTML and view it.  To do this, use `pdoc --html
./src/transcoder.py`, which will generate a file called
`transcoder.m.html` that you can view in your browser.

To regenerate, you need to add the `--overwrite` option to the command
to tell pdoc to overwrite the existing file.

We've included a `Makefile` which is a special kind of file that the
'make' command reads. We won't get into the details of `make` in this
project, but what we have provided means that you can create the documentation. Just use `make
docs`. 

TODO: this bit

## Virtualenv

Python is a very popular programming language. This means there are
lots of libraries that you can get for it that help you do things.
This could be simple things like coloured terminal output, or much
more complex, like interact with web servers or perform machine
learning functions.

But what if you write code that relies on these, but they don't exist
on your target platform? Or you need libraries that are incompatible
with others that a target system might have installed? Or you just
need Python version 3 and the system has to keep Python version 2 as
its default?

For this we use a virtual environment. This isn't like a virtual
machine - it's much lighter and simpler.  A virtual-env (or venv) is a
directory with special versions of python, libraries, etc. along with
scripts to make your system use them instead of the system-wide
versions when required.

This project make use of this system.  To enable it, in a terminal you
need to first create a virtual environment.  You can create it like
this, from the root directory of this repository:

```
python3 -m venv venv
```

You don't have to redo this on the same system. Once it is done, it stays. Now, when you want to use the contents of the venv, you activate it from the same place, like this:

```
. ./venv/bin/activate
```

Note the extra dot at the start. It tells your shell to import the
environment variables from within the file `venv/bin/activate` into
the current environment.

It is usual to have special libraries and such that should be included.  This project uses some, such as `colored` for creating coloured terminal output. To install them, use this command:

```
pip install -r requirements.txt
```

Pip is the Python package installer. It will read the contents of
`requirements.txt` and download and install the packages listed in
there. Feel free to look in the file.

Again, you only need to do this once.  Or after adding to
`requirements.txt`.

We've included a `Makefile` which is a special kind of file that the
'make' command reads. We won't get into the details of `make` in this
project, but what we have provided means that you can create the venv
by typing `make venv` and install prerequisite packages using `make
prereqs`. 

## Testing

If you've cloned the repository, made the venv, activated it and
installed the prerequisite packages, you can test the software by
running it.

Just type "./src/transcode.py".

It's not complete, but it will do something.  

This is OK to test that you at least have your environment set up, but
it's not really enough to test the software is working perfectly.

TODO: write about testing.


# Completing Transcoder

TODO:

 - asASCII (basic)
 - User input (intermediate)
 - wrapping (advanced)

# TODO - things left to do before students get access

 - Clear up TODO items
 - Put proper pydoc generation in and fill in all docstrings
 - Write bit about cloning repo
 - Write tests for asASCII (but not give the function)

<!--  LocalWords:  pdoc
 -->
