#!python
""" Software and functions to convert from arbitrary strings to various representations of the individual characters """
import colored

TODO: Docstrings

def asHex(data):
    #Start with an empty string
    output=""

    #Now for each character...
    for c in data:
        #Add the hex representation of the character to the string
        #The ord function returns the ASCII value of a character
        #The hex function returns the hexadecimal representation of a number
        output+=hex(ord(c))+" "

    return output.strip() #Take off any spare spaces at the start/end

def asOctal(data):
    output=""

    for c in data:
        output+=" "+oct(ord(c))

    return output.strip()

def asBinary(data):
    output=""
    
    for c in data:
        output+=" "+bin(ord(c))

    return output.strip()


def colourise(text, colour):
    return colored.fg(colour)+text+colored.attr('reset')


def main():
    """This function is called when this file is executed as a
program. Usually we don't bother putting a docstring in this function,
but I decided to add this one as a simple example. 

Notice that the String is 'triple quoted'. Usually, a String in Python
is bounded by one single or double quote mark. 'Like this' "or like
this". You can also use triples like this one does. It has a few
benefits that sometimes come in handy. In particular, you can easily
include single and double quote characters within it, because it takes
three in a row to signal the end. You can also go across multiple
lines, like I have here.

    """
    print(colourise("Transcoder V0.1 pre-alpha","#FF0000"))
    inputData="Any text could go here..."
    print(f"Input: {inputData}")
    hexData=asHex(inputData)
    octData=asOctal(inputData)
    binData=asBinary(inputData)
    print(f"Hex   : {hexData}")
    print(f"Octal : {octData}")
    print(f"Binary: {binData}")          




if __name__=="__main__":
    main()



# JS: You can ignore the stuff below. It's just for my spell-checker.
#  LocalWords:  Transcoder pre asHex JS inputData hexData  asOctal
#  LocalWords:  octData binData asBinary
