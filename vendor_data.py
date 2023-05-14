#! /usr/bin/python

"""This script is meant to help Translation Project Managers with keeping a clear overview of the vendors participating in a project.

The script contains three classes:
    1. The main parent class ´VendorData´. This class is meant for a general potential vendor profile, without assigning a status (preferred/back-up).
       It has 2 class arguments ´ProjectName´, representing the project name and ´SourceLang´, the source language the translators will be translating from, and takes 5 arguments:
            - ´VendorName´: The first and last name of the vendor.
            - ´VendorMail´: The vendor's email address.
            - ´TargLang´: the language the translators will be translating into.
            - ´WordRate´: the translator's word rate in Euro.
            -  ´CatTool´: the vendor's preferred cat tool.
    2. The subclass ´PrefVendor´, for the preferred vendors. They are assigned the status "Preferred".
    3. The subclass ´BackupVendor´ for the back-up vendors. They are assigned the status "Back-up"
"""
import argparse

# write here your function and class definitions
class VendorData:
    ProjectName = "Toyota MM24" #Class attribute no.1, the project the vendors will be working on
    SourceLang = "English" #Class attribute no.2, the source language
    
    def __init__(self, VendorName, VendorMail, TargLang, WordRate, CatTool):
        """ Instantiate
        Args:
            "VendorName" (str): First and last name of the vendor
            "VendorMail" (str): the vendor's email address
            "TargLang" (str): Language the vendor will be translating to
            "WordRate" (float): Vendor's word rate for new words in Euro
            "CatTool" (str): Vendor's preferred CAT-tool
            """
        self.VendorName = VendorName
        self.VendorMail = VendorMail
        self.TargLang = TargLang
        self.WordRate = WordRate
        self.CatTool = CatTool
        
        """Exceptions:
                VendorName should be a string, if not a TypeError is raised.
                VendorMail should be a string, if not a TypeError is raised.
                TargLang should be a string, if not a TypeError is raised.
                WordRate should be a float, if not a TypeError is raised.
                WordRate should be > 0.15, if not a ValueError is raised.
                CatTool should be a string, if not a TypeError is raised.
        """
        
        if type(VendorName) !=str:
            raise TypeError("VendorName should be a string!")
        if type(VendorMail) != str:
            raise TypeError ("VendorMail should be a string!")
        if type(TargLang) != str:
            raise TypeError("TargLang should be a string!")
        if type(WordRate) != float:
            raise TypeError("WordRate should be a float!")
        if WordRate > 0.15:
            raise ValueError("This vendor is too expensive, consider another one.")
        if type(CatTool) != str:
            raise TypeError("CatTool should be a string!")
        
class PrefVendor(VendorData):
    Preferred = True #Subclass Attribute set to True by default: indicating these vendors are the preferred vendors
    
    def __init__(self, VendorName, VendorMail, TargLang, WordRate, CatTool):
        super().__init__(VendorName, VendorMail, TargLang, WordRate, CatTool)

class BackupVendor(VendorData):
    Preferred = False #Subclass Attribute set to False by default: indicating these vendors are the back-up vendors

    def __init__(self, VendorName, VendorMail, TargLang, WordRate, CatTool):
        super().__init__(VendorName, VendorMail, TargLang, WordRate, CatTool)

# don't forget to properly document them with docstrings!!

if __name__ == "__main":
    # write here what happens if the code is run instead of imported
    # include argparse code!