#! /usr/bin/python

"""This script is meant to help Translation Project Managers with keeping a clear overview of the vendors participating in a project.

The script contains three classes:
    1. The main parent class ´VendorData´. This class is meant for a general potential vendor profile, without assigning a status (preferred/back-up).
       It has 4 class attributes ´ProjectName´, representing the project name and ´SourceLang´, the source language the translators will be translating from (by default set to English), 
       ´CatTools´, the possible Cat Tools the translator can use and ´Status´ which is by default set to "Potential". 
       It takes 5 arguments:
            - ´VendorName´: The first and last name of the vendor.
            - ´TargLang´: the language the translators will be translating into.
            - ´WordRate´: the translator's word rate in Euro.
            - ´VendorMail´: The vendor's email address.
            -  ´CatTool´: the vendor's preferred cat tool.
    2. The subclass ´PrefVendor´, for the preferred vendors, that has 2 class attributes: ´Preferred´ by default set to True, and ´Status´ by default set to "Preferred".
        It is possible to change those values using the change_status function.
"""

import argparse
import re
import pandas as pd
import os
import pyinputplus as pyip

class VendorData:
    ProjectName = "Toyota MM24" #Class attribute no.1, the project the vendors will be working on
    SourceLang = "English" #Class attribute no.2, the source language
    CatTools = ["XTM", "Trados Studio", "MemoQ", "Memsource"] #Class attribute no.3, the list of possible Cat Tools
    Preference = [True, False, None]
    
    def __init__(self, VendorName, TargLang, WordRate = None, Preferred = None, VendorMail = "", CatTool = "XTM"):
        """ Instantiate
        Args:
            "VendorName" (str): First and last name of the vendor
            "VendorMail" (str): the vendor's email address
            "TargLang" (str): Language the vendor will be translating to
            "WordRate" (float): Vendor's word rate for new words in Euro
            "CatTool" (str): Vendor's preferred CAT-tool
            """  
        """
        Exceptions:
            VendorName should be a string, if not a TypeError is raised.
            TargLang should be a string, if not a TypeError is raised.
            WordRate should be a float, if not a TypeError is raised.
            WordRate should NOT be > 0.15, if not a ValueError is raised.
            VendorMail should be a string, if not a TypeError is raised.
            VendorMail should be an email, if not a ValueError is raised.
            CatTool should be a string, if not a TypeError is raised.
            CatTool should be one of the options in the list "CatTools", if not a ValueError is raised.
        """
        regex_mail = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$" #regex used to validate email
        
        if type(VendorName) !=str:
            raise TypeError("VendorName should be a string!")
        else:
            self.VendorName = VendorName
            
        if type(TargLang) != str:
            raise TypeError("TargLang should be a string!")
        else:
            self.TargLang = TargLang
            
        if WordRate:
            if type(WordRate) != float:
                raise TypeError("WordRate should be a float!")
            if WordRate > 0.15:
                raise ValueError("This vendor is too expensive, consider another one.")
            if WordRate == 0.00:
                raise ValueError("Word rate cannot be 0.00.")
        else:
            self.WordRate = WordRate
            
        if Preferred in VendorData.Preference:
            self.Preferred = Preferred
        else:
            raise ValueError("Run 'VendorData.Preference' to check options!")
        if Preferred == True:
            self.Status = "Preferred"
        elif Preferred == False:
            self.Status = "Back-up"
        else:
            self.Status = "Potential"
            
        if VendorMail: 
            if type(VendorMail) != str:
                raise TypeError ("VendorMail should be a string!")
            if(re.search(regex_mail,VendorMail)):
                self.VendorMail = VendorMail
            else:
                raise ValueError("Please insert a valid email address.")
        else:
            self.VendorMail = VendorMail
            
        if type(CatTool) != str:
            raise TypeError("CatTool should be a string!")
        else:
            self.CatTool = CatTool
        if CatTool in VendorData.CatTools:
            self.CatTool = CatTool
        else:
            raise ValueError("This CAT tool is not valid. Run 'VendorData.CatTools' to check options.")
        
    def set_wordrate(self, NewRate):
        if type(NewRate) != float:
            raise TypeError("WordRate should be a float!")
        elif NewRate > 0.15:
            raise ValueError("This vendor is too expensive, consider another one.")
        elif NewRate == 0.00:
                raise ValueError("Word rate cannot be 0.00.")
        else:
            self.WordRate = NewRate

    def set_status(self, PrefVend):
        if PrefVend in VendorData.Preference:
            PrefVend = PrefVend
        else:
            raise ValueError("Run 'VendorData.Preference' to check options!")
        if PrefVend == True:
            self.Status = "Preferred"
        elif PrefVend == False:
            self.Status = "Back-up"
        else:
            self.Status = "Potential"
            
    def set_mail(self,mail):
        regex_mail = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$" #regex used to validate email
        if (re.search(regex_mail,mail)):
            self.VendorMail = mail
        else:
            raise ValueError("Please insert a valid email address.")
    
    def change_tool (self, tool):
        if type(tool) != str:
            raise TypeError("CatTool should be a string!")
        elif tool not in VendorData.CatTools:
            raise ValueError("This CAT tool is not valid. Run 'VendorData.CatTools' to check options.")
        else:
            self.CatTool = tool
    
   
    def to_excel(self):
        data = {
            "Target Language": [self.TargLang],
            "Vendor": [self.VendorName],
            "E-mail": [self.VendorMail],
            "CAT Tool": [self.CatTool],
            "Status": [self.Status],
        }
        filename = "_".join([str(self.ProjectName), str(self.SourceLang)])
        df = pd.DataFrame(data)
        if os.path.exists(f"{filename}.xlsx") != True:
            df.to_excel(f"{filename}.xlsx", index=False, sheet_name="VendorData")
        else:
            with pd.ExcelWriter(f"{filename}.xlsx", mode="a", engine="openpyxl", if_sheet_exists="overlay") as writer:
                df.to_excel(writer, sheet_name = "VendorData", startrow=writer.sheets["VendorData"].max_row, header = None, index=False)

# don't forget to properly dcument them with docstrings!!

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--add", action='store_true', help = "Add a vendor")
    parser.add_argument ("-m", "--modify", action='store_true', help = "Modify an existing vendor")
    args = parser.parse_args()
    
    if args.add == True:
        done = "no"
        while done.lower() != "yes":
            VendorName = pyip.inputStr(f"What's the vendor's name?")
            TargLang = pyip.inputStr(f"Into which language will the vendor translate?")
            WordRate = pyip.inputNum(f"What is the vendor's word rate in EUR?", blank = True, default=None)
            Preferred = pyip.inputBool(f"True or False: Is this vendor a preferred vendor? If neither, leave blank.", blank = True, default=None)
            VendorMail = pyip.inputStr(f"What is the vendor's email address?", blank = True, default="")
            CatTool= pyip.inputStr(f"In which tool will the vendor be working?", blank = True, default = "XTM")
            done = pyip.inputStr("Are you done? ")
            if done.lower() == "yes":
                Vndr=VendorData(VendorName, TargLang, WordRate, Preferred, VendorMail, CatTool)
                Excel = pyip.inputStr(f"Do you want add this vendor to the excel file?")
                if Excel.lower() == "yes":
                    Vndr.to_excel()