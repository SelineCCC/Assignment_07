#------------------------------------------#
# Title: Assignment06.py
# Desc: Working with classes and functions.
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# JingyinChen, 2021-Aug-19, Modified File to Add TODOs for error handling and 
#using bBinary data.
# Also tested other methods with assigning global or local variables - doesn't work.
# JingyinChen, 2021-Aug-20, Modified File to add error-handlings in add_table, 
#write_file, strChoice == 'd', show_inventory, read_file_binary, and read_file_plain. 
# Also modied the permenent data store to use binary data.
# Also added selection on text file or text file with binary in strChoice == 'l' 
#------------------------------------------#

# -- DATA -- #
import pickle

strChoice = '' # User input
lstTbl = []  # list of lists to hold data
dicRow = {}  # list of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# -- PROCESSING -- #
class DataProcessor:
    # TODone add functions for processing here
    @staticmethod
    def add_table(lstInput, table):
        """Firstly store the new user inputs of ID, CD Title and Artist Name as 
        a tuple of threes string, to a dictionary in the memory. 
           Then add the dictionary to the table, which is a 2D data structure 
        as list of dicts

        Args:
            lstInput (new list from userinput): the list that holds the data from 
        userinput
            table (list of dict): 2D data structure (list of dicts) that holds the 
        dicts of data during runtime.

        Returns:
            None.
        """
        #TODone add error handling
        try:
            dicRow = {'ID': int(lstInput[0]), 'Title': lstInput[1], 'Artist': lstInput[2]}
            table.append(dicRow)
        except ValueError as e:
            print('\nMust enter an integer for ID')
            print('\nBuild in error info:')
            print(type(e), e, e.__doc__, sep='\n')
        except Exception as e:
            print('\nGeneral error.')
            print('\nBuild in error info:')
            print(type(e), e, e.__doc__, sep='\n')
        
    @staticmethod
    def delete_data(intInputDel, table):
        """Delete the CD entry user wanna remove by asking the user to enter the 
        ID of the entry as dict. Then match the ID inputed as integer to the ID as a key 
        in the dicts of the 2D data list.
        
        Args:
            intInputDel: the ID as integer of the entry user wanna delete
            table (list of dict): 2D data structure (list of dicts) that holds the 
        dicts of data during runtime.

        Returns:
            blnCDRemoved as the result of the for loop.
        """
        intRowNr = -1
        blnCDRemoved = False
        for row in lstTbl:
            intRowNr += 1
            if row['ID'] == intIDDel:
                del lstTbl[intRowNr]
                blnCDRemoved = True
                break
        return blnCDRemoved

class FileProcessor:
    """Processing the data to and from text file"""

    @staticmethod
    def read_file_plain(file_name, table):
        """Function to manage data ingestion from a plain text file to a list of dictionaries

        Reads the data from file identified by file_name into a 2D table
        (list of dicts) table one line in the file represents one dictionary row in table.

        Args:
            file_name (string): name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds 
        the data during runtime

        Returns:
            None.
        """
        #TODone add error handling
        try:
            table.clear()  # this clears existing data and allows to load data from file
            objFile = open(file_name, 'r')
            for line in objFile:
                data = line.strip().split(',')
                dicRow = {'ID': int(data[0]), 'Title': data[1], 'Artist': data[2]}
                table.append(dicRow)
            objFile.close()
        except FileNotFoundError as e:
            print('\nText file does not exist! Please check the folder.')
            print('\nBuild in error info:')
            print(type(e), e, e.__doc__, sep='\n')
        except ValueError as e:
            print('\nLooks like the file is a text file with binary data.')
            print('\nBuild in error info:')
            print(type(e), e, e.__doc__, sep='\n')
        except Exception as e:
            print('\nGeneral error.')
            print('\nBuild in error info:')
            print(type(e), e, e.__doc__, sep='\n')
        
    @staticmethod
    def read_file_binary(file_name, table):
        """Function to manage data ingestion from file to a list of dictionaries

        Reads the data from file identified by file_name into a 2D table
        (list of dicts) table one line in the file represents one dictionary row in table.

        Args:
            file_name (string): name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds 
        the data during runtime

        Returns:
            None.
        """
        #TODone add error handling
        try:
            table.clear()
            with open(file_name, 'rb') as fileObj:
                data = pickle.load(fileObj)
                for line in data:
                    table.append(line)
        except FileNotFoundError as e:
            print('\nText file does not exist! Please check the folder.')
            print('\nBuild in error info:')
            print(type(e), e, e.__doc__, sep='\n')
        except ValueError as e:
            print('\nLooks like the file is a plain text file.')
            print('\nBuild in error info:')
            print(type(e), e, e.__doc__, sep='\n')
        except Exception as e:
            print('\nGeneral error.')
            print('\nBuild in error info:')
            print(type(e), e, e.__doc__, sep='\n')

    @staticmethod
    def write_file(file_name, table):
        # TODone Add code here
        """Save the user input data to the file with binary data

        Args:
            file_name (string): name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds 
        the data during runtime

        Returns: None

        """
        #TODone use the with open and 'wb' to write a binary file
        #TODone add error handling
        try:
            with open(file_name, 'wb') as objFile:
                pickle.dump(table, objFile)
        except FileNotFoundError as e:
            print('\nText file does not exist! Please check the folder.')
            print('\nBuild in error info:')
            print(type(e), e, e.__doc__, sep='\n')
        except FileExistsError as e:
            print('\nText file with the same name exists! Please check the folder.')
            print('\nBuild in error info:')
            print(type(e), e, e.__doc__, sep='\n')
        except Exception as e:
            print('\nGeneral error.')
            print('\nBuild in error info:')
            print(type(e), e, e.__doc__, sep='\n')

# -- PRESENTATION (Input/Output) -- #

class IO:
    """Handling Input / Output"""

    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case string of the users input out of the choices l, a, i, d, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def show_inventory(table):
        """Displays current inventory table

        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        try:
            print('======= The Current Inventory: =======')
            print('ID\tCD Title (by: Artist)\n')
            for row in table:
                print('{}\t{} (by:{})'.format(*row.values()))
            print('======================================')
            print()
        except AttributeError as e:
            print('\nTable has datatype error. Try exit and reload.')
            print('\nBuild in error info:')
            print(type(e), e, e.__doc__, sep='\n')
        except Exception as e:
            print('\nGeneral error.')
            print('\nBuild in error info:')
            print(type(e), e, e.__doc__, sep='\n')

    # TODone add I/O functions as needed
    @staticmethod
    def input_data():
        """Ask user to enter new ID, CD Title and Artist Name
        
        Args:
            None

        Returns:
            A list of three strings: ID, CD Title, and Artist Name 
            
        """
        strID = input('Enter ID: ').strip()
        strTitle = input('What is the CD\'s title? ').strip()
        strArtist = input('What is the Artist\'s name? ').strip()
        return [strID, strTitle, strArtist]

# 1. start main loop
while True:
    # 1.1 Display Menu to user and get choice
    IO.print_menu()
    strChoice = IO.menu_choice()
    # 2. Process menu selection
    # 2.1 process exit first
    if strChoice == 'x':
        break
    # 2.2 process load inventory
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        print('\nIs the file a plain text file, or a text file with binary data?')
        fileType = input('type \'plain\' if it is a plain text file, type \'binary\' if it is a binary one: ')
        if fileType.lower() == 'plain':
            print('reloading...')
            FileProcessor.read_file_plain(strFileName, lstTbl)
            IO.show_inventory(lstTbl)
        elif fileType.lower() == 'binary': 
            print('reloading...')
            FileProcessor.read_file_binary(strFileName, lstTbl)
            IO.show_inventory(lstTbl)
        else:
            print('\nMust be either \'plain\' or \'binary\'!')
        continue  # start loop back at top.
    # 2.3 process add a CD
    elif strChoice == 'a':
        # 3.3.1 Ask user for new ID, CD Title and Artist
        # TODone move IO code into function
        lstInput = IO.input_data()
        # 3.3.2 Add item to the table
        # TODone move processing code into function
        DataProcessor.add_table(lstInput, lstTbl)
        print('Current inventory:')
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 2.4 process display current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 2.5 process delete a CD
    elif strChoice == 'd':
        #TODone add error handling
        # 3.5.1 get Userinput for which CD to delete
        # 3.5.1.1 display Inventory to user
        IO.show_inventory(lstTbl)
        # 3.5.1.2 ask user which ID to remove
        # 3.5.2 search thru table and delete CD
        # TODone move processing code into function
        try:
            intIDDel = int(input('Which ID would you like to delete? ').strip())
            result = DataProcessor.delete_data(intIDDel, lstTbl)
            if result:
                print('The CD was removed')
                print()
            else:
                print('Could not find this CD!')
                print()
        except ValueError as e:
            print('\nMust enter an integer for ID')
            print('\nBuild in error info:')
            print(type(e), e, e.__doc__, sep='\n')
        except Exception as e:
            print('\nGeneral error.')
            print('\nBuild in error info:')
            print(type(e), e, e.__doc__, sep='\n')
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 2.6 process save inventory to file
    elif strChoice == 's':
        # 3.6.1 Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstTbl)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        print()
        # 3.6.2 Process choice
        if strYesNo == 'y':
            # 3.6.2.1 save data
            # TODone move processing code into function
            FileProcessor.write_file(strFileName, lstTbl)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    # 2.7 catch-all should not be possible, as user choice gets vetted in IO, but to be save:
    else:
        print('General Error')




