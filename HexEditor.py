import struct

class HexEditor():
    def __init__(self, HexSavedFile):
        self.hexSave = HexSavedFile


    '''
    player_menu_options prints the given character selected by the edit_menu method.
        @param: int offset of strength stat in hex save file of selected character 
        @result: Prints stat options and gets user input. If selection isn't 0 the
            stat_edit method is called. After that method is finished or if the user
            chose 0 the program returns to the edit_menu method (primary menu)
    '''
    def player_menu_options(self, offset):
        print("1. Str\n"
              "2. Dex\n"
              "3. Int\n"
              "4. HP\n"
              "5. Max HP\n"
              "6. Exp\n"
              "0. Main Menu")
        selection = int(input("Choose 1-6 or 0 to quit:"))
        if(selection==1):
            print("You are changing this character's Str stat")
        if (selection == 2):
            print("You are changing this character's Dex stat")
        if (selection == 3):
            print("You are changing this character's Int stat")
        if (selection == 4):
            print("You are changing this character's HP stat")
        if (selection == 5):
            print("You are changing this character's Max HP stat")
        if (selection == 6):
            print("You are changing this character's Exp stat")
        if(selection != 0):
            self.stat_edit(offset, selection)

    '''
    player_menu prints the given character selected by the edit_menu method.
        @param: int index of character user chose.
        @result: If user doesn't exit to main menu this method will call the
            player_menu_options method with the offset of character they chose
            in the edit_menu method.
    '''
    def player_menu(self, index):
        print("-------------------------------------")
        if(index == 1):
            print("Player Cheat Menu:")
            offset = 14     #All offsets herein are the offset to the Strength stat of a given character
            self.player_menu_options(offset)
        elif(index == 2):
            print("Shamino Cheat Menu:")
            offset = 46
            self.player_menu_options(offset)
        elif (index == 3):
            print("Iolo Cheat Menu:")
            offset = 78
            self.player_menu_options(offset)
        elif (index == 4):
            print("Mariah Cheat Menu:")
            offset = 110
            self.player_menu_options(offset)
        elif (index == 5):
            print("Geoffrey Cheat Menu:")
            offset = 142
            self.player_menu_options(offset)
        elif (index == 6):
            print("Jaana Cheat Menu:")
            offset = 174
            self.player_menu_options(offset)
        elif (index == 7):
            print("Julia Cheat Menu:")
            offset = 206
            self.player_menu_options(offset)
        elif (index == 8):
            print("Dupre Cheat Menu:")
            offset = 238
            self.player_menu_options(offset)
        elif (index == 9):
            print("Katrina Cheat Menu:")
            offset = 270
            self.player_menu_options(offset)
        elif (index == 10):
            print("Senti Cheat Menu:")
            offset = 302
            self.player_menu_options(offset)
        elif (index == 11):
            print("Gwenno Cheat Menu:")
            offset = 334
            self.player_menu_options(offset)
        elif (index == 12):
            print("Johne Cheat Menu:")
            offset = 366
            self.player_menu_options(offset)
        elif (index == 13):
            print("Gorn Cheat Menu:")
            offset = 398
            self.player_menu_options(offset)
        elif (index == 14):
            print("Maxwell Cheat Menu:")
            offset = 430
            self.player_menu_options(offset)
        elif (index == 15):
            print("Toshi Cheat Menu:")
            offset = 462
            self.player_menu_options(offset)
        elif (index == 16):
            print("Saduj Cheat Menu:")
            offset = 494
            self.player_menu_options(offset)
        elif (index == 17):
            self.item_menu()
        else:
            return 0

    '''
    item_menu takes user input for which item they want to modify and then allows the user
    to change the number of said items in the inventory
        @result: If the user doesn't exit they can change the quantity of a given item
    '''
    def item_menu(self):
        '''
        gold() is essentially fourBit() but specifically for gold and it's 9999 limit.
            @result: change gold quantity to input of user
        '''
        def gold():
            print("***************************************")
            print("WARNING GOLD has a maximum of 9999")
            print("Only you can prevent save corruption!")
            print("***************************************")
            value = int(input("Enter a value 0-9999:"))
            if (value > 9999 or value < 0):
                print("ENTERED VALUE IS OUT OF RANGE TRY AGAIN!")
                self.item_menu()
                return 0
            else:
                hexValue = hex(value)
                hexValue = struct.pack('<Q', int(hexValue, base=16))
                self.hexSave[offset] = hexValue[0]
                self.hexSave[offset+1] = hexValue[1]
                print(self.hexSave[516])
                print(self.hexSave[517])

        '''
        byte() is tasked with modifying data that is stored in 1 byte (all of the items other than gold)
            @result: 1 byte is changed to the input of the user
        '''
        def byte():
            print("***************************************")
            print("WARNING this stat has a maximum of 99")
            print("Only you can prevent save corruption!")
            print("***************************************")
            value = int(input("Enter a value 0-99:"))
            if (value > 99 or value < 0):
                print("ENTERED VALUE IS OUT OF RANGE TRY AGAIN!")
                self.item_menu()
                return 0
            else:
                self.hexSave[offset] = value
        print("Gold/Items Cheat Menu:\n"
              "1. Gold\n"
              "2. Keys\n"
              "3. Skull Keys\n"
              "4. Gems\n"
              "5. Black Badge\n"
              "6. Magic Carpets\n"
              "7. Magic Axes\n")
        selection = int(input("Choose 1-7 or 0 to quit:"))
        if(selection == 1):     #word
            offset = 516
            gold()
        elif(selection == 2):   #byte
            offset = 518
            byte()
        elif(selection == 3):   #byte
            offset = 523
            byte()
        elif(selection == 4):   #byte
            offset = 519
            byte()
        elif(selection == 5):   #byte
            offset = 536
            byte()
        elif(selection == 6):   #byte
            offset = 522
            byte()
        elif(selection == 7):   #byte
            offset = 576
            byte()
        self.edit_menu()

    '''
    edit_menu prints all of the characters and asks the user to select one to modify.
    This serves as the main menu of the program.
        @result: If the user doesn't exit this will call the player_menu method
            with the int index of character they chose
    '''
    def edit_menu(self):
        print("-------------------------------------------------------")
        print("Cheat menu:\n"
              "-------------------------------------------------------\n"
              "1. Player\n"
              "2. Shamino\n"
              "3. Iolo\n"
              "4. Mariah\n"
              "5. Geoffrey\n"
              "6. Jaana\n"
              "7. Julia\n"
              "8. Dupre\n"
              "9. Katrina\n"
              "10. Sentri\n"
              "11. Gwenno\n"
              "12. Johne\n"
              "13. Gorn\n"
              "14. Maxwell\n"
              "15. Toshi\n"
              "16. Saduj\n"
              "17. Gold/Items")
        selection = int(input("Choose 1-17 or 0 to save and quit:"))
        if(selection>0 and selection<18):
            self.player_menu(selection)

    '''
    stat_edit will modify the hex of the save file. 
        @param: It will take the int offset of whatever character the user chooses and 
            the int selection index of whatever stat they chose to change. 
        @result: Using that index this method will ask the user what value they want
            to change the stat to and the method will alter that stat.
    '''
    def stat_edit(self, offset, selection):
        modifier = 0
        '''
        twoBit is tasked with modifying data that is stored in 1 byte
            @result: 1 byte is changed to the input of the user
        '''
        def twoBit():
            print("*************************************")
            print("WARNING this stat has a maximum of 99")
            print("Only you can prevent save corruption!")
            print("*************************************")
            value = int(input("Enter a value 0-99:"))
            if (value >99 or value <0):
                print("ENTERED VALUE IS OUT OF RANGE TRY AGAIN!")
                twoBit()
                return 0
            else:
                self.hexSave[offset+(selection-1)] = value  #Indexes to offset which positions to the strength byte
                                                            # of a given character. Then shifts selection-1 bytes to the
                                                            # right of the strength byte. Sets that byte to inputted value

        '''
        fourBit is tasked with modifying data that is stored in 2 bytes. This utilizes little endian.
            @param: modifier is an int given in lines 280 and 282. it's purpose is to skip every other byte because
                    we are modifying 2 bytes at a time
            @result: 2 bytes are changed to the input of the user.
        '''
        def fourBit(modifier):      #I wanted a variable for offset shifting because in 4 bit there is a 2 byte gap
                                    #I was also worried that my original idea of adding to offset would somehow create
                                    #a bug upon multiple uses of this method (I did not test my original idea)
            if(selection == 5 or selection == 4):
                print("**************************************")
                print("WARNING this stat has a maximum of 999")
                print("Only you can prevent save corruption!")
                print("**************************************")
                value = int(input("Enter a value 0-999:"))
                if (value > 999 or value < 0):
                    print("ENTERED VALUE IS OUT OF RANGE TRY AGAIN!")
                    fourBit()
                    return 0
            else:
                print("***************************************")
                print("WARNING this stat has a maximum of 9999")
                print("Only you can prevent save corruption!")
                print("***************************************")
                value = int(input("Enter a value 0-9999:"))
                if (value > 9999 or value < 0):
                    print("ENTERED VALUE IS OUT OF RANGE TRY AGAIN!")
                    fourBit()
                    return 0

            hexValue = hex(value)
            hexValue = struct.pack('<Q', int(hexValue, base=16))
            self.hexSave[offset+(selection) + modifier] = hexValue[0]   #sets second byte of save data to first byte of input
            self.hexSave[offset+(selection-1) + modifier] = hexValue[1] #sets first byte of save data to second byte of input
            #print(self.hexSave)
        if(selection == 1 or selection == 2 or selection == 3):
            twoBit()
        elif(selection == 4 or selection == 5 or selection == 6):
            if(selection == 5):
                modifier = 1        #This looks terrible but because of the offset selection 5 is 4 hex bits off instead of 2
            elif(selection == 6):   #which is where selection 6 would be.
                modifier = 2
            fourBit(modifier)
        self.edit_menu()

