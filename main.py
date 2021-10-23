import binascii
import struct
from HexEditor import HexEditor

directory = ""

'''
    getFile takes in the user's inputted directory for the saved file and 
        reads it's hexadecimal contents into a string (I think)
'''
def getFile(directory):
    with open(directory, 'rb') as savedFile:
        if(savedFile.name.__contains__("SAVED.GAM")):
            #saveFileHex = bytearray(binascii.hexlify(savedFile.read()))
            saveFileHex = bytearray(savedFile.read())
            return saveFileHex
        else:
            print("That file is not the saved game file.")
            directory = input("Enter the file path of your save game (Example: D:\\Program Files (x86)\\Ultima_5\\SAVED.GAM):\n")
            return getFile(directory)

'''
MAIN STARTS HERE
'''

print("=================================================================================================")
print("=================================================================================================")
print("                                      Welcome to ULTIMA 5 HACK")
print("=================================================================================================")
print("=================================================================================================")

directory = input("Enter the file path of your save game (Example: D:\\Program Files (x86)\\Ultima_5\\SAVED.GAM):\n")
saveFileHex = getFile(directory)


hexEditor = HexEditor(saveFileHex)  #Initializes hex editor
hexEditor.edit_menu()               #Runs the cheat engine


'''
The underlying code writes the modified saveFileHex to the location of SAVED.GAM
'''
file = open(directory, "wb")
file.write(bytes(saveFileHex))
