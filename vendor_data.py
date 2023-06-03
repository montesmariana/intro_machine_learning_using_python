#! /usr/bin/python

import argparse
import re
import pandas as pd
import os
import pyinputplus as pyip

def ChangeDictionaryValue(Dictionary, Key, Index, NewValue):
    if Key in Dictionary and Index in Dictionary[Key]:
        Dictionary[Key][Index] = NewValue
def CheckVendorMail(VendorMail):
    regex_mail = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$" #regex used to validate email
    if type(VendorMail) != str:
        raise TypeError ("VendorMail should be a string!")
    if not(re.search(regex_mail,VendorMail)):
        raise ValueError("Please insert a valid email address.")
def CheckWordRate(WordRate):
    if type(WordRate) != float:
        raise TypeError("WordRate should be a float!")
    if WordRate > 0.15:
        raise ValueError("This vendor is too expensive, pick another one.")
    if WordRate == 0.00:
        raise ValueError("Word rate cannot be 0.00.")
def CheckCatTool(CatTool):
    if type(CatTool) != str:
        raise TypeError("CatTool should be a string!")
    if not CatTool in VendorData.CatTools:
            raise ValueError("This CAT tool is not valid. Run 'VendorData.CatTools' to check options.") 

class VendorData:
    CatTools = ["XTM", "Trados Studio", "MemoQ", "Memsource"] 
    
    def __init__(self, ProjectName, SourceLang, TargLang, VendorName, VendorMail = "", WordRate = None, CatTool = "XTM", Preferred = None):
        if type(ProjectName) != str:
            raise TypeError("ProjectName should be a string!")
        if type(SourceLang) != str:
            raise TypeError("SourceLang should be a string!")
        if type(TargLang) != str:
            raise TypeError("TargLang should be a string!")
        if type(VendorName) !=str:
            raise TypeError("VendorName should be a string!")
        if VendorMail:
            CheckVendorMail(VendorMail)   
        if WordRate != None:
            CheckWordRate(WordRate)
        if CatTool:
            CheckCatTool(CatTool)
        if Preferred != None:
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
        
    def SetVendorMail(self, NewMail):
        CheckVendorMail(NewMail)
        self.VendorMail = NewMail
        
    def SetWordRate(self, NewRate):
        CheckWordRate(NewRate)
        self.WordRate = NewRate
    
    def ChangeTool (self, NewTool):
        CheckCatTool(NewTool)
        self.CatTool = NewTool

    def SetStatus(self, PrefVend):
        if PrefVend != None:
            if PrefVend:
                self.Status = "Preferred"
            elif PrefVend == False:
                self.Status = "Back-Up"
        else:
            self.Status = "Potential"                  
   
    def ToExcel(self):
        data = {
            "Target Language": [self.TargLang],
            "Vendor": [self.VendorName],
            "E-mail": [self.VendorMail],
            "CAT Tool": [self.CatTool],
            "Word Rate": [self.WordRate],
            "Status": [self.Status]
        }
        filename = "_".join([str(self.ProjectName), str(self.SourceLang)]) + ".xlsx"
        df = pd.DataFrame(data)
        if not os.path.exists(filename):
            df.to_excel(filename, index=False, sheet_name="VendorData")
        else:
            with pd.ExcelWriter(filename, mode="a", engine="openpyxl", if_sheet_exists="overlay") as writer:
                df.to_excel(writer, sheet_name = "VendorData", startrow=writer.sheets["VendorData"].max_row, header = None, index=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--add", action='store_true', help = "Add a vendor")
    parser.add_argument ("-m", "--modify", action='store_true', help = "Modify an existing vendor")
    args = parser.parse_args()
    
    if args.add:
        done = "no"
        WordRate = None
        Preferred = None
        VendorMail = ""
        CatTool = "XTM"
        while done.lower() != "yes":
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
            NewWordRate = pyip.inputNum("What is the vendor's word rate in EUR? Should be between 0.01 and 0.15. If higher, choose another vendor. ", blank = True)
            if NewWordRate != None:
                CheckWordRate(NewWordRate)
                VendorWordRate = NewWordRate
            else:
                WordRate = WordRate
            NewPreferred = pyip.inputBool("True or False: Is this vendor a preferred vendor? If neither, leave blank. ", blank = True, default=None)
            NewCatTool= pyip.inputMenu(["XTM", "Trados Studio", "MemoQ", "Memsource"], prompt = "In which tool will the vendor be working?", blank = True, default = "XTM")
            CatTool = NewCatTool if NewCatTool else CatTool
            Preferred = NewPreferred if NewPreferred else Preferred
            done = pyip.inputStr("Are you done? ")

        Vndr=VendorData(ProjectName, SourceLang, TargLang, VendorName, VendorMail, WordRate, CatTool, Preferred)
        Excel = pyip.inputStr("Do you want to add this vendor to the excel file? ")
        if Excel.lower() == "yes":
            Vndr.ToExcel()
    if args.modify:
        done = "no"
        while done.lower() != "yes":
            ProjectName = pyip.inputStr("What is the name of the project that the vendor you want to modify works on? ")
            SourceLang = pyip.inputStr("What is the source language? ")
            FileName = "_".join([str(ProjectName), str(SourceLang)]) + ".xlsx"
            if os.path.exists(FileName):
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
                    NewWordRate = pyip.inputNum("What is the vendor's word rate? Should be between 0.01 and 0.15. If higher, choose another vendor. ", blank = True)
                    if NewWordRate != None:
                        CheckWordRate(NewWordRate)
                    NewCatTool = pyip.inputMenu(["XTM", "Trados Studio", "MemoQ", "Memsource"], prompt = "In which tool will the vendor be working?", blank = True, default = "XTM")
                    NewStatus = pyip.inputMenu(["Potential", "Preferred", "Back-up"], prompt = "What is the vendor's new status? ", blank = True)
                    done = pyip.inputStr("Are you done? ")
            else:
                print("A file for this project and this source language does not yet exist. Check the project name and source language.")

        if NewEmail:
            ChangeDictionaryValue(VendorDict, EmailKey, VendorIndex, NewEmail)
        if NewWordRate:
            ChangeDictionaryValue(VendorDict, WordRateKey, VendorIndex, NewWordRate)
        if NewCatTool:
            ChangeDictionaryValue(VendorDict, CatToolKey, VendorIndex, NewCatTool)
        if NewStatus:
            ChangeDictionaryValue(VendorDict, StatusKey, VendorIndex, NewStatus)
        df = pd.DataFrame(VendorDict)
        with pd.ExcelWriter(FileName, engine="openpyxl", mode="w") as writer:
            df.to_excel(writer, sheet_name = "VendorData", index=False)
            print("This vendor is modified correctly.")