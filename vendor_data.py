#! /usr/bin/python

"""This script is meant to help Translation Project Managers with keeping a clear overview of the vendors participating in a project.

The script contains three classes:
    1. The main parent class ´VendorData´. This class is meant for a general potential vendor profile, without assigning a status (preferred/back-up).
       It has 3 class arguments ´ProjectName´, representing the project name and ´SourceLang´, the source language the translators will be translating from and ´CatTools´, the possible Cat Tools the translator can use. 
       It takes 5 arguments:
            - ´VendorName´: The first and last name of the vendor.
            - ´TargLang´: the language the translators will be translating into.
            - ´WordRate´: the translator's word rate in Euro.
            - ´VendorMail´: The vendor's email address.
            -  ´CatTool´: the vendor's preferred cat tool.
    2. The subclass ´PrefVendor´, for the preferred vendors. They are assigned the status "Preferred".
    3. The subclass ´BackupVendor´ for the back-up vendors. They are assigned the status "Back-up"
"""
import argparse
import re

class VendorData:
    ProjectName = "Toyota MM24" #Class attribute no.1, the project the vendors will be working on
    SourceLang = "English" #Class attribute no.2, the source language
    CatTools = ["XTM", "Trados Studio", "MemoQ", "Memsource"] #Class attribute no.3, the list of possible Cat Tools
    
    def __init__(self, VendorName, TargLang, WordRate = None, VendorMail = "", CatTool = "XTM"):
        """ Instantiate
        Args:
            "VendorName" (str): First and last name of the vendor
            "VendorMail" (str): the vendor's email address
            "TargLang" (str): Language the vendor will be translating to
            "WordRate" (float): Vendor's word rate for new words in Euro
            "CatTool" (str): Vendor's preferred CAT-tool
            """
        self.VendorName = VendorName
        self.TargLang = TargLang
        self.WordRate = WordRate
        self.VendorMail = VendorMail
        self.CatTool = CatTool
        
        regex_mail = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$" #regex used to validate email
            

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
        
        if type(VendorName) !=str:
            raise TypeError("VendorName should be a string!")
        if type(TargLang) != str:
            raise TypeError("TargLang should be a string!")
        if type(WordRate) != float:
            raise TypeError("WordRate should be a float!")
        if WordRate:
            if WordRate > 0.15:
                raise ValueError("This vendor is too expensive, consider another one.")
        elif WordRate == 0.00:
            raise ValueError("Word rate cannot be 0.00.")
        else:
            self.WordRate = WordRate
        if type(CatTool) != str:
            raise TypeError("CatTool should be a string!")
        if type(VendorMail) != str:
            raise TypeError ("VendorMail should be a string!")
        if VendorMail:   
            if(re.search(regex_mail,VendorMail)):
                self.VendorMail = VendorMail
            else:
                raise ValueError("Please insert a valid email address.")
        else:
            self.VendorMail = VendorMail
        if CatTool in VendorData.CatTools:
            self.CatTool = CatTool
        else:
            raise ValueError("This CAT tool is not valid. Run 'VendorData.CatTools' to check options.")
            
    def set_mail(self,mail):
        regex_mail = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$" #regex used to validate email
        if (re.search(regex_mail,mail)):
            self.VendorMail = mail
        else:
            raise ValueError("Please insert a valid email address.")

        
class PrefVendor(VendorData):
    Preferred = True
    """ Class Attribute:
            Preffered (bool.) by default set to "True" indicating this is a Preferred Vendor, if "False" it is a back-up vendor."""
    
    def __init__(self, VendorName, TargLang, WordRate, VendorMail, CatTool):
        super().__init__(VendorName, TargLang, WordRate, VendorMail, CatTool)


# don't forget to properly dcument them with docstrings!!

if __name__ == "__main__":
    parser = argparse.ArgumentParser("docstring")
    parser.add_argument("VendorName", type=str, help="Vendor's name")
    parser.add_argument("TargLang", type=str, help="Language the vendor will be translating into")
    parser.add_argument("--WordRate", type=float, help="The vendor's word rate in Euro")
    parser.add_argument("--VendorMail", type=str, help="The vendor's email address")
    parser.add_argument("--CatTool", type=str, help="The CAT-tool the vendor wants to use")
    args = parser.parse_args()
    Vndr = VendorData(args.VendorName, args.TargLang, args.WordRate, args.VendorMail, args.CatTool)
