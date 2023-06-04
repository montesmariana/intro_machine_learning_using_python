#! /usr/bin/python
"""This is a python script to help Translation Project Managers keep a clean overview of the vendors for a particular project by narrowing down the data in the excel.

    It contains:
        - 4 functions: 
            `ChangeDictionaryValue` to easily change values in a certain dictionary.
            `CheckVendorMail` to easily check if an e-mail address is valid.
            `CheckWordRate` to check if a word rate falls between EUR 0.01 and EUR 0.15 per word.
            `CheckCatTool` to validate the CAT tool provided.
        - 1 class, `VendorData` that has 3 class attributes: `CatTools`, the CAT Tools that can be used for the project,
            `Keys`, the keys of the dictionary that can be modified, and `Statuses`, the possible statuses a vendor can have.
            The class takes 4 positional arguments and 4 optional arguments:
                1. `ProjectName` (str): the name of the translation project
                2. `SourceLang` (str): the source language, i.e. the language the translator will translate from
                3. `TargLang` (str): the target language, i.e. the language the translator will translate into
                4. `VendorName` (str): the translator's/vendor's name
                5. `VendorMail` (str): the vendor's e-mail address, by default empty
                6. `WordRate` (float): the vendor's word rate in EUR/word, by default set to "None"
                7. `CatTool` (str): the CAT Tool the translator will use, by default set to "XTM"
                8. `Preferred` (bool): indicates if a vendor is a preferred vendor or not, by default set to "None"
        - `Argparse` inside `if __name__ == "__main__":` statement to receive arguments when the script is run
    """
#Import some python packages that will be needed:
import argparse
import re #regular expression package to validate e-mail
import pandas as pd #pandas package to write excel file
import os #os package to check if files exists
import pyinputplus as pyip #pyinputplus package to facilitate providing arguments

#4 methods to make validation easier
def ChangeDictionaryValue(Dictionary, Key, Index, NewValue):
    """ChangeDictionaryValue, change values of a dictionary

    Args:
        Dictionary (dict): name of the dictionary that will be read
        Key (str): the key for which the value will be changed
        Index (int): the index of the value that will be changed
        NewValue: new value for the chosen index, type depends on the key
    """
    if Key in Dictionary and Index in Dictionary[Key]:
        Dictionary[Key][Index] = NewValue
def CheckVendorMail(VendorMail):
    """CheckVendorMail, validate e-mail address

    Args:
        VendorMail (str): an e-mail address

    Raises:
        TypeError: if the argument provided is not a string, a TypeError is raised
        ValueError: if the address provided does not conform with the regex string `regex_mail`, a ValueError is raised
    """
    regex_mail = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$" #regex used to validate email
    if type(VendorMail) != str:
        raise TypeError ("VendorMail should be a string!")
    if not(re.search(regex_mail,VendorMail)):
        raise ValueError("Please insert a valid email address.")
def CheckWordRate(WordRate):
    """CheckWordRate, validate word rate

    Args:
        WordRate (float): a word rate in EUR/word

    Raises:
        TypeError:  if the argument provided is not a float, a TypeError is raised
        ValueError: the argument provided should not be higher than 0.15
        ValueError: the argument provided should not be 0.00
    """
    if type(WordRate) != float:
        raise TypeError("WordRate should be a float!")
    if WordRate > 0.15:
        raise ValueError("This vendor is too expensive, pick another one.")
    if WordRate == 0.00:
        raise ValueError("Word rate cannot be 0.00.")
def CheckCatTool(CatTool):
    """CheckCatTool, validate CatTOol

    Args:
        CatTool (str): a CAT Tool

    Raises:
        TypeError: if the argument provided is not string, a TypeError is raised
        ValueError: the argument provided should be one of the four CAT Tools in the list ["XTM", "Trados Studio", "MemoQ", "Memsource"]
    """
    if type(CatTool) != str:
        raise TypeError("CatTool should be a string!")
    if not CatTool in ["XTM", "Trados Studio", "MemoQ", "Memsource"]:
            raise ValueError("This CAT tool is not valid. Run 'VendorData.CatTools' to check options.") 
    
class VendorData:

    CatTools = ["XTM", "Trados Studio", "MemoQ", "Memsource"]
    Keys = ["E-mail", "CAT Tool", "Word Rate", "Status"]
    Statuses = ["Preferred", "Back-up", "Potential"]
    
    def __init__(self, ProjectName, SourceLang, TargLang, VendorName, VendorMail = "", WordRate = None, CatTool = "XTM", Preferred = None):
        """Instantiate

        Class Attributes:
            CatTools (list) :
            Keys (list) :
            Statuses (list) :

        Args:
            ProjectName (str): the name of the translation project
            SourceLang (str): the source language, i.e. the language the translator will translate from
            TargLang (str): the target language, i.e. the language the translator will translate into
            VendorName (str): the translator's/vendor's name
            VendorMail (str, optional): the vendor's e-mail address, by default empty
            WordRate (float, optional): the vendor's word rate in EUR/word, by default set to "None"
            CatTool (str, optional): the CAT Tool the translator will use, by default set to "XTM"
            Preferred (bool, optional): indicates if a vendor is a preferred vendor or not, by default set to "None".

        Raises:
            TypeError: ProjectName should be a string
            TypeError: SourceLang should be a string
            TypeError: TargLang should be a string
            TypeError: VendorName should be a string
        """
        if type(ProjectName) != str:
            raise TypeError("ProjectName should be a string!")
        if type(SourceLang) != str:
            raise TypeError("SourceLang should be a string!")
        if type(TargLang) != str:
            raise TypeError("TargLang should be a string!")
        if type(VendorName) !=str:
            raise TypeError("VendorName should be a string!")
        if VendorMail: #validate e-mail address if one is provided
            CheckVendorMail(VendorMail)   
        if WordRate != None: #validate word rate if one is provided
            CheckWordRate(WordRate)
        if CatTool: #validate CAT Tool if one is provided
            CheckCatTool(CatTool)
        if Preferred != None:
            if type(Preferred) != bool:
                raise TypeError("Preferred should either be True, False or None.")
        if Preferred != None: #if Preferred is set to True, status will be preferred, if set to False, back-up and if neither "Potential"
            if Preferred:
                self.Status = "Preferred"
            elif Preferred == False:
                self.Status = "Back-up"
        else:
            self.Status = "Potential"
            
        self.ProjectName = ProjectName
        self.SourceLang = SourceLang
        self.VendorName = VendorName
        self.TargLang = TargLang
        self.WordRate = WordRate
        self.VendorMail = VendorMail
        self.CatTool = CatTool
        self.Preferred = Preferred
        
    def SetVendorMail(self, NewMail):
        """Method

        Args:
            NewMail (str): a new e-mail address for a certain vendor
        """
        CheckVendorMail(NewMail) #validate e-mail address
        self.VendorMail = NewMail #value of VendorMail is changed
        
    def SetWordRate(self, NewRate):
        """Method

        Args:
            NewRate (float): a new word rate for a certain vendor
        """
        CheckWordRate(NewRate) #validate new word rate
        self.WordRate = NewRate #value of WordRate is changed
    
    def ChangeTool (self, NewTool):
        """Method

        Args:
            NewTool (str): a new tool for a certain vendor
        """
        CheckCatTool(NewTool) #validate new CAT Tool
        self.CatTool = NewTool #value of CatTool is changed

    def SetStatus(self, PrefVend):
        """Method

        Args:
            PrefVend (bool): new value for Preferred, has an influence on status
        """
        if PrefVend != None:
            if type(PrefVend) != bool:
                raise TypeError("Preferred should either be True, False or None.")
        if PrefVend != None:
            if PrefVend == True:
                self.Preferred = True
                self.Status = "Preferred"
            elif PrefVend == False:
                self.Preferred = False
                self.Status = "Back-up"
        else:
            self.Preferred = None
            self.Status = "Potential"             
   
    def ToExcel(self): #method to write data to an excel file
        Data = { #dump arguments provided in a dictionary
            "Target Language": [self.TargLang],
            "Vendor": [self.VendorName],
            "E-mail": [self.VendorMail],
            "CAT Tool": [self.CatTool],
            "Word Rate": [self.WordRate],
            "Status": [self.Status]
        }
        FileName = "_".join([str(self.ProjectName), str(self.SourceLang)]) + ".xlsx" #the name of the excel file, based on arguments `ProjectName` and `SourceLang`
        df = pd.DataFrame(Data) #make a panda dataframe out of the dictionary
        if not os.path.exists(FileName): #check if the file exists, if not a new file is written
            df.to_excel(FileName, index=False, sheet_name="VendorData")
        else: #if file exists, the data is appended to the existing file
            with pd.ExcelWriter(FileName, mode="a", engine="openpyxl", if_sheet_exists="overlay") as writer:
                df.to_excel(writer, sheet_name = "VendorData", startrow=writer.sheets["VendorData"].max_row, header = None, index=False)
    def ReadExcel(self): #method to read the file with filename {ProjectName_SourceLang} into a dictionary
        FileName = "_".join([str(self.ProjectName), str(self.SourceLang)]) + ".xlsx"
        if os.path.exists(FileName):
            ExcelRecords = pd.read_excel(FileName) #read filename
            ExcelRecordsDf = ExcelRecords.loc[:, ~ExcelRecords.columns.str.contains('^Unnamed')] #remove any unnamed columns
            VendorDict = ExcelRecordsDf.to_dict() #turn dataframe into a dictionary
            return VendorDict #print the Dictionary
        else:
            raise ValueError(f"There is no file for {self.ProjectName} in {self.SourceLang}")
    
    def ModExcel(self, Key, Index, NewValue):
        """Method to modify existing vendor in excel file

        Args:
            Key (str): one of the modifiable keys in VendorData.Keys
            Index (int): the index of the value that needs to be modified
            NewValue : the new value of the index, type depends on the key, either str or float

        Raises:
            ValueError: raised if the key is not one of the keys in VendorData.Keys
            ValueError: raised if the Index is not valid for a certain key
        """
        FileName = "_".join([str(self.ProjectName), str(self.SourceLang)]) + ".xlsx"
        if os.path.exists(FileName):
            ExcelRecords = pd.read_excel(FileName)
            ExcelRecordsDf = ExcelRecords.loc[:, ~ExcelRecords.columns.str.contains('^Unnamed')]
            VendorDict = ExcelRecordsDf.to_dict()
            if not Key in self.Keys:
                raise ValueError("Invalid key, run 'VendorData.Keys' to see options.")
            if not Index in VendorDict[Key]:
                raise ValueError("Invalid index, run 'self.ReadExcel()' to see options")
            if Key == "E-mail": #validate e-mail address if a value for the key E-mail is modified
                CheckVendorMail(NewValue)
            if Key == "Word Rate": #validate word rate if a value for the key Word Rate is modified
                CheckWordRate(NewValue)
            if Key == "CAT Tool": #validate CAT Tool if a value for the key CAT Tool is modified
                CheckCatTool(NewValue)
            if Key == "Status": #validate Status if a value for the key Status is modified
                if not NewValue in VendorData.Statuses:
                    raise ValueError("Invalid status, run 'VendorData.Statuses' to see options")
            ChangeDictionaryValue(VendorDict, Key, Index, NewValue) #change the dictionary value in the dictionary `VendorDict` using the arguments provided for the method ModExcel
            df = pd.DataFrame(VendorDict) #turn VendorDict dictionary back into a panda DataFrame
            with pd.ExcelWriter(FileName, engine="openpyxl", mode="w") as writer:
                df.to_excel(writer, sheet_name = "VendorData", index=False) #overwrite the existing excel file
        else:
            raise ValueError(f"There is no file for {self.ProjectName} in {self.SourceLang}")

if __name__ == "__main__":
    """Parse command line arguments to provide arguments when the code is run

    Args:
        --add, -a (flag) : indicating the user wants to add a new vendor
        --modify, -m (flag) : indicating the user wants to modify an existing vendor
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--add", action='store_true', help = "Add a vendor")
    parser.add_argument ("-m", "--modify", action='store_true', help = "Modify an existing vendor")
    args = parser.parse_args()
    
    if args.add:
        """Action: add a vendor

        Prompts the user to provide the following data, validates it and writes it to an excel file with {ProjectName_SourceLang} as name:
            ProjectName (str): the name of the translation project
            SourceLang (str): the source language, i.e. the language the translator will translate from
            TargLang (str): the target language, i.e. the language the translator will translate into
            VendorName (str): the translator's/vendor's name
            VendorMail (str, optional): the vendor's e-mail address, by default empty
            WordRate (float, optional): the vendor's word rate in EUR/word, by default set to "None"
            CatTool (str, optional): the CAT Tool the translator will use, by default set to "XTM"
            Preferred (bool, optional): indicates if a vendor is a preferred vendor or not, by default set to "None".  
        """
        done = "no"
        WordRate = None
        Preferred = None
        VendorMail = ""
        CatTool = "XTM"
        while done.lower() != "yes": #Code underneath is run unless value for done is changed to "no"
            ProjectName = pyip.inputStr("What is the project name? ")
            SourceLang = pyip.inputStr("What is the source language? ")
            VendorName = pyip.inputStr("What's the vendor's name? ")
            TargLang = pyip.inputStr("Into which language will the vendor translate? ")
            NewVendorMail = pyip.inputStr("What is the vendor's email address? ", blank = True, default="")
            if NewVendorMail:
                CheckVendorMail(NewVendorMail)
                VendorMail = NewVendorMail
            else:
                VendorMail = VendorMail
            NewWordRate = pyip.inputFloat("What is the vendor's word rate in EUR? Should be between 0.01 and 0.15. If higher, choose another vendor. ", blank = True)
            if NewWordRate:
                CheckWordRate(NewWordRate)
                VendorWordRate = NewWordRate
            else:
                WordRate = WordRate
            NewCatTool= pyip.inputMenu(VendorData.CatTools, prompt = "In which tool will the vendor be working?", blank = True, default = "XTM")
            CatTool = NewCatTool if NewCatTool else CatTool
            NewPreferred = pyip.inputBool("True or False: Is this vendor a preferred vendor? If neither, leave blank. ", blank = True, default=None)
            Preferred = NewPreferred if NewPreferred else Preferred
            done = pyip.inputStr("Are you done? ") #user gets the chance to change value for done to "no"
            
        Vndr=VendorData(ProjectName, SourceLang, TargLang, VendorName, VendorMail, WordRate, CatTool, Preferred)
        Excel = pyip.inputStr("Do you want to add this vendor to the excel file? ") #user gets the chance to write data to excel
        if Excel.lower() == "yes":
            Vndr.ToExcel() #data written to excel
    if args.modify:
        """Action: modify an existing vendor
        """
        done = "no"
        while done.lower() != "yes": #Code underneath is run as long as value for done = no
            """Provide ProjectName and SourceLang to look for the excel file
            """
            ProjectName = pyip.inputStr("What is the name of the project that the vendor you want to modify works on? ")
            SourceLang = pyip.inputStr("What is the source language? ")
            FileName = "_".join([str(ProjectName), str(SourceLang)]) + ".xlsx"
            if os.path.exists(FileName):
                """If the file exists, excel file is read and turned into a dictionary
                Prompts the user to choose the vendor for which certain values will be changed.
                """
                ExcelRecords = pd.read_excel(FileName)
                ExcelRecordsDf = ExcelRecords.loc[:, ~ExcelRecords.columns.str.contains('^Unnamed')]
                VendorDict=ExcelRecordsDf.to_dict()

                Vendors = VendorDict["Vendor"]
                print ("These are the vendor's already in the database: ")
                for index, VendorName in Vendors.items():
                    print(f"{index}: {VendorName}")
                
                VendorIndex = pyip.inputInt("Enter the index of the vendor you want to modify: ")
                if VendorIndex in Vendors:
                    VendorKey = "Vendor"
                    EmailKey = "E-mail"
                    WordRateKey = "Word Rate"
                    CatToolKey = "CAT Tool"
                    StatusKey = "Status"

                    NewEmail = pyip.inputStr("What is the vendor's e-mail? ", blank = True)
                    if NewEmail:
                        CheckVendorMail(NewEmail)
                    NewWordRate = pyip.inputFloat("What is the vendor's word rate? Should be between 0.01 and 0.15. If higher, choose another vendor. ", blank = True)
                    if NewWordRate:
                        CheckWordRate(NewWordRate)
                    NewCatTool = pyip.inputMenu(VendorData.CatTools, prompt = "In which tool will the vendor be working?", blank = True, default = "XTM")
                    NewStatus = pyip.inputMenu(VendorData.Statuses, prompt = "What is the vendor's new status? ", blank = True)
                    done = pyip.inputStr("Are you done? ")
            else:
                print("A file for this project and this source language does not yet exist. Check the project name and source language.")
        """Values for provided keys are changed
        """
        if NewEmail:
            ChangeDictionaryValue(VendorDict, EmailKey, VendorIndex, NewEmail)
        if NewWordRate:
            ChangeDictionaryValue(VendorDict, WordRateKey, VendorIndex, NewWordRate)
        if NewCatTool:
            ChangeDictionaryValue(VendorDict, CatToolKey, VendorIndex, NewCatTool)
        if NewStatus:
            ChangeDictionaryValue(VendorDict, StatusKey, VendorIndex, NewStatus)
        df = pd.DataFrame(VendorDict) #VendorDict dictionary is turned into pandas dataframe
        with pd.ExcelWriter(FileName, engine="openpyxl", mode="w") as writer: #Excel file is overwritten with new data
            df.to_excel(writer, sheet_name = "VendorData", index=False)
            print("This vendor is modified correctly.")