import pytest
import sys
sys.path.append("./src/")
import transcoder


    



def test_asHex():
    """ Test the 'asHex' function """

    #First a simple string
    assert transcoder.asHex("ABC")=="0x41 0x42 0x43"
    #An empty string
    assert transcoder.asHex("")==""
    #The highest byte value
    assert transcoder.asHex(chr(255))=="0xff"
    #Lowest byte value
    assert transcoder.asHex(chr(0))=="0x0"
    



def test_asOctal():
    """ Test the 'asOctal' function """

    #First a simple string
    assert transcoder.asOctal("ABC")=="0o101 0o102 0o103"
    #An empty string
    assert transcoder.asOctal("")==""
    #The highest byte value
    assert transcoder.asOctal(chr(255))=="0o377"
    #Lowest byte value
    assert transcoder.asOctal(chr(0))=="0o0"
    
    
def test_asBinary():
    """ Test the 'asBinary' function """

    #First a simple string
    assert transcoder.asBinary("ABC")=="0b1000001 0b1000010 0b1000011"
    #An empty string
    assert transcoder.asBinary("")==""
    #The highest byte value
    assert transcoder.asBinary(chr(255))=="0b11111111"
    #Lowest byte value
    assert transcoder.asBinary(chr(0))=="0b0"
