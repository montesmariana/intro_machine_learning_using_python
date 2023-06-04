# Tutorial: how to use `vendor_data.py`

## Using `vendor_data.py` as a module

This interactive notebook shows how to use the class and the different functions in the script `vendor_data.py`.

To use the script in this code, we can import the script as a module or run it directly.
We'll begin with importing the code as module:


```python
import sys
sys.path.append ('vendor_data.py') #this is the relative path to the script. If the script is not directly next to the notebook, it could be better to copy the full path of the notebook.
import vendor_data as vd # 'as vd' is not necessary but makes it shorter.
```

### Docstrings
The script is completely documented with docstrings in order to ensure that the script is correclty used.
You can read these docstrings by calling one of the following functions:


```python
help(vd)
```

    Help on module vendor_data:
    
    NAME
        vendor_data - This is a python script to help Translation Project Managers keep a clean overview of the vendors for a particular project by narrowing down the data in the excel.
    
    DESCRIPTION
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
    
    CLASSES
        builtins.object
            VendorData
        
        class VendorData(builtins.object)
         |  VendorData(ProjectName, SourceLang, TargLang, VendorName, VendorMail='', WordRate=None, CatTool='XTM', Preferred=None)
         |  
         |  Methods defined here:
         |  
         |  ChangeTool(self, NewTool)
         |      Method
         |      
         |      Args:
         |          NewTool (str): a new tool for a certain vendor
         |  
         |  ModExcel(self, Key, Index, NewValue)
         |      Method to modify existing vendor in excel file
         |      
         |      Args:
         |          Key (str): one of the modifiable keys in VendorData.Keys
         |          Index (int): the index of the value that needs to be modified
         |          NewValue : the new value of the index, type depends on the key, either str or float
         |      
         |      Raises:
         |          ValueError: raised if the key is not one of the keys in VendorData.Keys
         |          ValueError: raised if the Index is not valid for a certain key
         |  
         |  ReadExcel(self)
         |  
         |  SetStatus(self, PrefVend)
         |      Method
         |      
         |      Args:
         |          PrefVend (bool): new value for Preferred, has an influence on status
         |  
         |  SetVendorMail(self, NewMail)
         |      Method
         |      
         |      Args:
         |          NewMail (str): a new e-mail address for a certain vendor
         |  
         |  SetWordRate(self, NewRate)
         |      Method
         |      
         |      Args:
         |          NewRate (float): a new word rate for a certain vendor
         |  
         |  ToExcel(self)
         |  
         |  __init__(self, ProjectName, SourceLang, TargLang, VendorName, VendorMail='', WordRate=None, CatTool='XTM', Preferred=None)
         |      Instantiate
         |      
         |      Class Attributes:
         |          CatTools (list) :
         |          Keys (list) :
         |          Statuses (list) :
         |      
         |      Args:
         |          ProjectName (str): the name of the translation project
         |          SourceLang (str): the source language, i.e. the language the translator will translate from
         |          TargLang (str): the target language, i.e. the language the translator will translate into
         |          VendorName (str): the translator's/vendor's name
         |          VendorMail (str, optional): the vendor's e-mail address, by default empty
         |          WordRate (float, optional): the vendor's word rate in EUR/word, by default set to "None"
         |          CatTool (str, optional): the CAT Tool the translator will use, by default set to "XTM"
         |          Preferred (bool, optional): indicates if a vendor is a preferred vendor or not, by default set to "None".
         |      
         |      Raises:
         |          TypeError: ProjectName should be a string
         |          TypeError: SourceLang should be a string
         |          TypeError: TargLang should be a string
         |          TypeError: VendorName should be a string
         |  
         |  ----------------------------------------------------------------------
         |  Data descriptors defined here:
         |  
         |  __dict__
         |      dictionary for instance variables (if defined)
         |  
         |  __weakref__
         |      list of weak references to the object (if defined)
         |  
         |  ----------------------------------------------------------------------
         |  Data and other attributes defined here:
         |  
         |  CatTools = ['XTM', 'Trados Studio', 'MemoQ', 'Memsource']
         |  
         |  Keys = ['E-mail', 'CAT Tool', 'Word Rate', 'Status']
         |  
         |  Statuses = ['Preferred', 'Back-up', 'Potential']
    
    FUNCTIONS
        ChangeDictionaryValue(Dictionary, Key, Index, NewValue)
            ChangeDictionaryValue, change values of a dictionary
            
            Args:
                Dictionary (dict): name of the dictionary that will be read
                Key (str): the key for which the value will be changed
                Index (int): the index of the value that will be changed
                NewValue: new value for the chosen index, type depends on the key
        
        CheckCatTool(CatTool)
            CheckCatTool, validate CatTOol
            
            Args:
                CatTool (str): a CAT Tool
            
            Raises:
                TypeError: if the argument provided is not string, a TypeError is raised
                ValueError: the argument provided should be one of the four CAT Tools in the list ["XTM", "Trados Studio", "MemoQ", "Memsource"]
        
        CheckVendorMail(VendorMail)
            CheckVendorMail, validate e-mail address
            
            Args:
                VendorMail (str): an e-mail address
            
            Raises:
                TypeError: if the argument provided is not a string, a TypeError is raised
                ValueError: if the address provided does not conform with the regex string `regex_mail`, a ValueError is raised
        
        CheckWordRate(WordRate)
            CheckWordRate, validate word rate
            
            Args:
                WordRate (float): a word rate in EUR/word
            
            Raises:
                TypeError:  if the argument provided is not a float, a TypeError is raised
                ValueError: the argument provided should not be higher than 0.15
                ValueError: the argument provided should not be 0.00
    
    FILE
        c:\users\geera\onedrive\documenten\school\postgraduaattranslationtechnology\introductiontopython\final_assignment1\vendor_data.py
    
    
    


```python
?vd
```


```python
vd.__doc__
```




    'This is a python script to help Translation Project Managers keep a clean overview of the vendors for a particular project by narrowing down the data in the excel.\n\n    It contains:\n        - 4 functions: \n            `ChangeDictionaryValue` to easily change values in a certain dictionary.\n            `CheckVendorMail` to easily check if an e-mail address is valid.\n            `CheckWordRate` to check if a word rate falls between EUR 0.01 and EUR 0.15 per word.\n            `CheckCatTool` to validate the CAT tool provided.\n        - 1 class, `VendorData` that has 3 class attributes: `CatTools`, the CAT Tools that can be used for the project,\n            `Keys`, the keys of the dictionary that can be modified, and `Statuses`, the possible statuses a vendor can have.\n            The class takes 4 positional arguments and 4 optional arguments:\n                1. `ProjectName` (str): the name of the translation project\n                2. `SourceLang` (str): the source language, i.e. the language the translator will translate from\n                3. `TargLang` (str): the target language, i.e. the language the translator will translate into\n                4. `VendorName` (str): the translator\'s/vendor\'s name\n                5. `VendorMail` (str): the vendor\'s e-mail address, by default empty\n                6. `WordRate` (float): the vendor\'s word rate in EUR/word, by default set to "None"\n                7. `CatTool` (str): the CAT Tool the translator will use, by default set to "XTM"\n                8. `Preferred` (bool): indicates if a vendor is a preferred vendor or not, by default set to "None"\n        - `Argparse` inside `if __name__ == "__main__":` statement to receive arguments when the script is run\n    '



### Instantiating an instance of VendorData
Now that we know the different fucntionalities we can instantiate an instance of the class VendorData.
To illustrate the code to it's full extent, we'll instantiate a couple of them:


```python
VendorNL = vd.VendorData("Tutorial", "English", "Dutch", "Elmo Geeraerts") #An instance with only the positional arguments provided
VendorFR = vd.VendorData("Tutorial", "English", "French", "Jean Lefèvre", "j.lefevre@hotmail.com", 0.10, "Trados Studio", True) #An instance with all the arguments provided
VendorES = vd.VendorData("Tutorial", "English", "Spanish", "Emilio De La Banda", WordRate = 0.09, Preferred = False) #An instance with some of the optional arguments
```

We can check the values of the arguments for the three vendors as follows:


```python
VendorNL.VendorName
```




    'Elmo Geeraerts'




```python
VendorFR.VendorMail
```




    'j.lefevre@hotmail.com'




```python
VendorES.WordRate
```




    0.09



Some arguments had default arguments. When we check the e-mail for VendorNL, for which we didn't provide one, we'll see that it does not return anything:


```python
VendorNL.VendorMail
```




    ''



When we check the CAT tool for the Spanish vendor, we'll get "XTM". We did not provide any argument, but in the class it is set to default since that is the main CAT tool used in the particular agency. This can be changed in the actual code.


```python
VendorES.CatTool
```




    'XTM'



The value for the argument Preferred can be True, False or None. This has an influence of the vendor's status.
If Preferred is True, the vendor gets the status Preferred. If it is False, the vendor gets the status Back-up. If it is None, the vendor gets the status Potential.


```python
VendorFR.Preferred
```




    True




```python
VendorFR.Status
```




    'Preferred'




```python
VendorES.Preferred
```




    False




```python
VendorES.Status
```




    'Back-up'




```python
VendorNL.Preferred #Will not return anything since value is None
```


```python
VendorNL.Status
```




    'Potential'



### Functions
The class also contains a couple of functions:
- `SetVendorMail` to set an e-mail address for a specific vendor
- `SetWordRate` to add a word rate in EUR/word for a specific vendor
- `ChangeTool` to change the preferred CAT tool
- `SetStatus` to change the vendor's status
- `ToExcel` to write the data to an excel file
- `ReadExcel` to print the data in the excel file to a dictionary, if the excel file exists
- `ModExcel` to modify certain values for a vendor in the excel file, if the excel file exists

We did not provide an e-mail for the Spanish vendor so we'll start with that:


```python
VendorES.SetVendorMail("e.dlbanda@outlook.com")
VendorES.VendorMail
```




    'e.dlbanda@outlook.com'



We did not set a word rate for the Dutch vendor, so now we can add one:


```python
VendorNL.SetWordRate(0.08)
VendorNL.WordRate
```




    0.08



Say, we did not yet know which CAT Tool the Spanish Vendor was going to use, but now we know that they will use Trados Studio. First it was set to 'XTM', we can change this as follows:


```python
VendorES.ChangeTool("Trados Studio")
VendorES.CatTool
```




    'Trados Studio'



Because we sat the value for preferred to True for the French vendor, they got the status "Preferred". If for some reason this changes, we can change the status easily, by changing the value for Preferred to False or None:


```python
VendorFR.SetStatus(False)
VendorFR.Preferred
```




    False




```python
VendorFR.Status
```




    'Back-up'



We can now write the data for the vendors to an excel file. Since every vendor has the value for the argument `ProjectName` and `SourceLang`, they will be written to the same excel file. We should execute this function for every vendor. Be careful because if you run this function multiple times for the same vendor, it will not overwrite but append and you will have duplicates in the excel file.


```python
VendorNL.ToExcel()
VendorFR.ToExcel()
VendorES.ToExcel()
```

An excel file named `Tutorial_English.xlsx` should appear in the same folder where you stored this tutorial notebook.
We can now read the entire excel file by calling the function ReadExcel for any vendor in the excel file. We'll get the information for every vendor in the excel file, no matter what vendor we pick:


```python
VendorNL.ReadExcel()
```




    {'Target Language': {0: 'Dutch', 1: 'French', 2: 'Spanish'},
     'Vendor': {0: 'Elmo Geeraerts', 1: 'Jean Lefèvre', 2: 'Emilio De La Banda'},
     'E-mail': {0: nan, 1: 'j.lefevre@hotmail.com', 2: 'e.dlbanda@outlook.com'},
     'CAT Tool': {0: 'XTM', 1: 'Trados Studio', 2: 'Trados Studio'},
     'Word Rate': {0: 0.08, 1: 0.1, 2: 0.09},
     'Status': {0: 'Potential', 1: 'Back-up', 2: 'Back-up'}}



If we create another vendor that works on a different project or translates from another source language and call the same function without writing it to an excel file, we'll get an error message saying that a file for the project in the given source language does not exist.


```python
VendorBG = vd.VendorData("Tutorial", "German", "Bulgarian", "Bulgarian Jacob")
VendorBG.ReadExcel()
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    ~\AppData\Local\Temp\ipykernel_12116\1804978508.py in <module>
          1 VendorBG = vd.VendorData("Tutorial", "German", "Bulgarian", "Bulgarian Jacob")
    ----> 2 VendorBG.ReadExcel()
    

    ~\OneDrive\Documenten\School\PostgraduaatTranslationTechnology\IntroductionToPython\Final_Assignment1\vendor_data.py in ReadExcel(self)
        222             return VendorDict #print the Dictionary
        223         else:
    --> 224             raise ValueError(f"There is no file for {self.ProjectName} in {self.SourceLang}")
        225 
        226     def ModExcel(self, Key, Index, NewValue):
    

    ValueError: There is no file for Tutorial in German


We can also modify the excel file by running the `ModExcel` function. Again, it does not matter for which vendor you call this function.
This function takes 3 arguments:
1. The `Key` which represents the arguments you can change the values for. You can check the modifiable keys by running vd.VendorData.Keys
2. The `Index`: if you have run the ReadExcel() function, you have noticed that before every value for a key in the dictionrary there's a number. By picking a number, you can change the value for that index.
3. The `NewValue`, the new value for the index in a key.

First we'll run `vd.VendorData.Keys` to see the modifiable keys:


```python
vd.VendorData.Keys
```




    ['E-mail', 'CAT Tool', 'Word Rate', 'Status']



Now we'll again read the excel file for the project "Tutorial" with source language "English". Again, it does not matter which vendor you do this for:


```python
VendorNL.ReadExcel()
```




    {'Target Language': {0: 'Dutch', 1: 'French', 2: 'Spanish'},
     'Vendor': {0: 'Elmo Geeraerts', 1: 'Jean Lefèvre', 2: 'Emilio De La Banda'},
     'E-mail': {0: nan, 1: 'j.lefevre@hotmail.com', 2: 'e.dlbanda@outlook.com'},
     'CAT Tool': {0: 'XTM', 1: 'Trados Studio', 2: 'Trados Studio'},
     'Word Rate': {0: 0.08, 1: 0.1, 2: 0.09},
     'Status': {0: 'Potential', 1: 'Back-up', 2: 'Back-up'}}



Now we can choose for which index in which key we want to change the value for. We can for example change the CAT Tool the Spanish vendor will use like this:


```python
VendorES.ModExcel("CAT Tool", 2, "MemoQ")
```

If you check this by running `.CatTool`, the old value will still be there.


```python
VendorES.CatTool
```




    'Trados Studio'



However, if we read the excel file again, we'll notice it has changed:


```python
VendorES.ReadExcel()
```




    {'Target Language': {0: 'Dutch', 1: 'French', 2: 'Spanish'},
     'Vendor': {0: 'Elmo Geeraerts', 1: 'Jean Lefèvre', 2: 'Emilio De La Banda'},
     'E-mail': {0: nan, 1: 'j.lefevre@hotmail.com', 2: 'e.dlbanda@outlook.com'},
     'CAT Tool': {0: 'XTM', 1: 'Trados Studio', 2: 'MemoQ'},
     'Word Rate': {0: 0.08, 1: 0.1, 2: 0.09},
     'Status': {0: 'Potential', 1: 'Back-up', 2: 'Back-up'}}



### Validation

This script also uses some functions to validate the user input anytime when user interaction is necessary.
That is:
- upon instantiating an instance of VendorData
- upon changing a value using one of the functions illustrated above
- upon modifying the excel file

The examples below illustrate what happens when wrong user input is provided. We'll start with the simple TypeErrors.
TypeErrors are raised when:
- `ProjectName` is not a string
- `SourceLang` is not a string
- `TargLang` is not a string
- `VendorName` is not a string
- `VendorMail` is not a string
- `WordRate` is not a float
- `CatTool` is not a string
- `Preferred` is not None or one of the Boolean operators, True or False


```python
VendorDE = vd.VendorData(0.1, "English", "German", "Thomas Zwiebel")
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    ~\AppData\Local\Temp\ipykernel_12116\3042631035.py in <module>
    ----> 1 VendorDE = vd.VendorData(0.1, "English", "German", "Thomas Zwiebel")
    

    ~\OneDrive\Documenten\School\PostgraduaatTranslationTechnology\IntroductionToPython\Final_Assignment1\vendor_data.py in __init__(self, ProjectName, SourceLang, TargLang, VendorName, VendorMail, WordRate, CatTool, Preferred)
        118         """
        119         if type(ProjectName) != str:
    --> 120             raise TypeError("ProjectName should be a string!")
        121         if type(SourceLang) != str:
        122             raise TypeError("SourceLang should be a string!")
    

    TypeError: ProjectName should be a string!



```python
VendorDE = vd.VendorData("Tutorial", 1, "German", "Thomas Zwiebel")
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    ~\AppData\Local\Temp\ipykernel_12116\2835384243.py in <module>
    ----> 1 VendorDE = vd.VendorData("Tutorial", 1, "German", "Thomas Zwiebel")
    

    ~\OneDrive\Documenten\School\PostgraduaatTranslationTechnology\IntroductionToPython\Final_Assignment1\vendor_data.py in __init__(self, ProjectName, SourceLang, TargLang, VendorName, VendorMail, WordRate, CatTool, Preferred)
        120             raise TypeError("ProjectName should be a string!")
        121         if type(SourceLang) != str:
    --> 122             raise TypeError("SourceLang should be a string!")
        123         if type(TargLang) != str:
        124             raise TypeError("TargLang should be a string!")
    

    TypeError: SourceLang should be a string!



```python
VendorDE = vd.VendorData("Tutorial", "English", True, "Thomas Zwiebel")
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    ~\AppData\Local\Temp\ipykernel_12116\2057797999.py in <module>
    ----> 1 VendorDE = vd.VendorData("Tutorial", "English", True, "Thomas Zwiebel")
    

    ~\OneDrive\Documenten\School\PostgraduaatTranslationTechnology\IntroductionToPython\Final_Assignment1\vendor_data.py in __init__(self, ProjectName, SourceLang, TargLang, VendorName, VendorMail, WordRate, CatTool, Preferred)
        122             raise TypeError("SourceLang should be a string!")
        123         if type(TargLang) != str:
    --> 124             raise TypeError("TargLang should be a string!")
        125         if type(VendorName) !=str:
        126             raise TypeError("VendorName should be a string!")
    

    TypeError: TargLang should be a string!



```python
VendorDE = vd.VendorData("Tutorial", "English", "German", None)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    ~\AppData\Local\Temp\ipykernel_12116\1683973233.py in <module>
    ----> 1 VendorDE = vd.VendorData("Tutorial", "English", "German", None)
    

    ~\OneDrive\Documenten\School\PostgraduaatTranslationTechnology\IntroductionToPython\Final_Assignment1\vendor_data.py in __init__(self, ProjectName, SourceLang, TargLang, VendorName, VendorMail, WordRate, CatTool, Preferred)
        124             raise TypeError("TargLang should be a string!")
        125         if type(VendorName) !=str:
    --> 126             raise TypeError("VendorName should be a string!")
        127         if VendorMail: #validate e-mail address if one is provided
        128             CheckVendorMail(VendorMail)
    

    TypeError: VendorName should be a string!



```python
VendorDE = vd.VendorData("Tutorial", "English", "German", "Thomas Zwiebel", 3)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    ~\AppData\Local\Temp\ipykernel_12116\2269134755.py in <module>
    ----> 1 VendorDE = vd.VendorData("Tutorial", "English", "German", "Thomas Zwiebel", 3)
    

    ~\OneDrive\Documenten\School\PostgraduaatTranslationTechnology\IntroductionToPython\Final_Assignment1\vendor_data.py in __init__(self, ProjectName, SourceLang, TargLang, VendorName, VendorMail, WordRate, CatTool, Preferred)
        126             raise TypeError("VendorName should be a string!")
        127         if VendorMail: #validate e-mail address if one is provided
    --> 128             CheckVendorMail(VendorMail)
        129         if WordRate != None: #validate word rate if one is provided
        130             CheckWordRate(WordRate)
    

    ~\OneDrive\Documenten\School\PostgraduaatTranslationTechnology\IntroductionToPython\Final_Assignment1\vendor_data.py in CheckVendorMail(VendorMail)
         52     regex_mail = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$" #regex used to validate email
         53     if type(VendorMail) != str:
    ---> 54         raise TypeError ("VendorMail should be a string!")
         55     if not(re.search(regex_mail,VendorMail)):
         56         raise ValueError("Please insert a valid email address.")
    

    TypeError: VendorMail should be a string!



```python
VendorDE = vd.VendorData("Tutorial", "English", "German", "Thomas Zwiebel", WordRate = "0.15")
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    ~\AppData\Local\Temp\ipykernel_12116\2028391605.py in <module>
    ----> 1 VendorDE = vd.VendorData("Tutorial", "English", "German", "Thomas Zwiebel", WordRate = "0.15")
    

    ~\OneDrive\Documenten\School\PostgraduaatTranslationTechnology\IntroductionToPython\Final_Assignment1\vendor_data.py in __init__(self, ProjectName, SourceLang, TargLang, VendorName, VendorMail, WordRate, CatTool, Preferred)
        128             CheckVendorMail(VendorMail)
        129         if WordRate != None: #validate word rate if one is provided
    --> 130             CheckWordRate(WordRate)
        131         if CatTool: #validate CAT Tool if one is provided
        132             CheckCatTool(CatTool)
    

    ~\OneDrive\Documenten\School\PostgraduaatTranslationTechnology\IntroductionToPython\Final_Assignment1\vendor_data.py in CheckWordRate(WordRate)
         67     """
         68     if type(WordRate) != float:
    ---> 69         raise TypeError("WordRate should be a float!")
         70     if WordRate > 0.15:
         71         raise ValueError("This vendor is too expensive, pick another one.")
    

    TypeError: WordRate should be a float!



```python
VendorDE = vd.VendorData("Tutorial", "English", "German", "Thomas Zwiebel", Preferred = "Test")
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    ~\AppData\Local\Temp\ipykernel_12116\1300272076.py in <module>
    ----> 1 VendorDE = vd.VendorData("Tutorial", "English", "German", "Thomas Zwiebel", Preferred = "Test")
    

    ~\OneDrive\Documenten\School\PostgraduaatTranslationTechnology\IntroductionToPython\Final_Assignment1\vendor_data.py in __init__(self, ProjectName, SourceLang, TargLang, VendorName, VendorMail, WordRate, CatTool, Preferred)
        133         if Preferred != None:
        134             if type(Preferred) != bool:
    --> 135                 raise TypeError("Preferred should either be True, False or None.")
        136         if Preferred != None: #if Preferred is set to True, status will be preferred, if set to False, back-up and if neither "Potential"
        137             if Preferred:
    

    TypeError: Preferred should either be True, False or None.



```python
VendorDE = vd.VendorData("Tutorial", "English", "German", "Thomas Zwiebel", CatTool = True)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    ~\AppData\Local\Temp\ipykernel_12116\2908856665.py in <module>
    ----> 1 VendorDE = vd.VendorData("Tutorial", "English", "German", "Thomas Zwiebel", CatTool = True)
    

    ~\OneDrive\Documenten\School\PostgraduaatTranslationTechnology\IntroductionToPython\Final_Assignment1\vendor_data.py in __init__(self, ProjectName, SourceLang, TargLang, VendorName, VendorMail, WordRate, CatTool, Preferred)
        130             CheckWordRate(WordRate)
        131         if CatTool: #validate CAT Tool if one is provided
    --> 132             CheckCatTool(CatTool)
        133         if Preferred != None:
        134             if type(Preferred) != bool:
    

    ~\OneDrive\Documenten\School\PostgraduaatTranslationTechnology\IntroductionToPython\Final_Assignment1\vendor_data.py in CheckCatTool(CatTool)
         83     """
         84     if type(CatTool) != str:
    ---> 85         raise TypeError("CatTool should be a string!")
         86     if not CatTool in ["XTM", "Trados Studio", "MemoQ", "Memsource"]:
         87             raise ValueError("This CAT tool is not valid. Run 'VendorData.CatTools' to check options.")
    

    TypeError: CatTool should be a string!


There are also some functions that ensure that:
- `VendorMail` is a valid e-mail address by checking it against a regex string;
- `WordRate` is not 0.00 or more than 0.15
- `CatTool` is one of the following: XTM, Trados Studio, MemoQ or Memsource


```python
VendorDE = vd.VendorData("Tutorial", "English", "German", "Thomas Zwiebel", VendorMail = "thomas.zw")
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    ~\AppData\Local\Temp\ipykernel_12116\2329585938.py in <module>
    ----> 1 VendorDE = vd.VendorData("Tutorial", "English", "German", "Thomas Zwiebel", VendorMail = "thomas.zw")
    

    ~\OneDrive\Documenten\School\PostgraduaatTranslationTechnology\IntroductionToPython\Final_Assignment1\vendor_data.py in __init__(self, ProjectName, SourceLang, TargLang, VendorName, VendorMail, WordRate, CatTool, Preferred)
        126             raise TypeError("VendorName should be a string!")
        127         if VendorMail: #validate e-mail address if one is provided
    --> 128             CheckVendorMail(VendorMail)
        129         if WordRate != None: #validate word rate if one is provided
        130             CheckWordRate(WordRate)
    

    ~\OneDrive\Documenten\School\PostgraduaatTranslationTechnology\IntroductionToPython\Final_Assignment1\vendor_data.py in CheckVendorMail(VendorMail)
         54         raise TypeError ("VendorMail should be a string!")
         55     if not(re.search(regex_mail,VendorMail)):
    ---> 56         raise ValueError("Please insert a valid email address.")
         57 def CheckWordRate(WordRate):
         58     """CheckWordRate, validate word rate
    

    ValueError: Please insert a valid email address.



```python
VendorDE = vd.VendorData("Tutorial", "English", "German", "Thomas Zwiebel", WordRate = 0.19)
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    ~\AppData\Local\Temp\ipykernel_12116\389829205.py in <module>
    ----> 1 VendorDE = vd.VendorData("Tutorial", "English", "German", "Thomas Zwiebel", WordRate = 0.19)
    

    ~\OneDrive\Documenten\School\PostgraduaatTranslationTechnology\IntroductionToPython\Final_Assignment1\vendor_data.py in __init__(self, ProjectName, SourceLang, TargLang, VendorName, VendorMail, WordRate, CatTool, Preferred)
        128             CheckVendorMail(VendorMail)
        129         if WordRate != None: #validate word rate if one is provided
    --> 130             CheckWordRate(WordRate)
        131         if CatTool: #validate CAT Tool if one is provided
        132             CheckCatTool(CatTool)
    

    ~\OneDrive\Documenten\School\PostgraduaatTranslationTechnology\IntroductionToPython\Final_Assignment1\vendor_data.py in CheckWordRate(WordRate)
         69         raise TypeError("WordRate should be a float!")
         70     if WordRate > 0.15:
    ---> 71         raise ValueError("This vendor is too expensive, pick another one.")
         72     if WordRate == 0.00:
         73         raise ValueError("Word rate cannot be 0.00.")
    

    ValueError: This vendor is too expensive, pick another one.



```python
VendorDE = vd.VendorData("Tutorial", "English", "German", "Thomas Zwiebel", WordRate = 0.00)
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    ~\AppData\Local\Temp\ipykernel_12116\2186391260.py in <module>
    ----> 1 VendorDE = vd.VendorData("Tutorial", "English", "German", "Thomas Zwiebel", WordRate = 0.00)
    

    ~\OneDrive\Documenten\School\PostgraduaatTranslationTechnology\IntroductionToPython\Final_Assignment1\vendor_data.py in __init__(self, ProjectName, SourceLang, TargLang, VendorName, VendorMail, WordRate, CatTool, Preferred)
        128             CheckVendorMail(VendorMail)
        129         if WordRate != None: #validate word rate if one is provided
    --> 130             CheckWordRate(WordRate)
        131         if CatTool: #validate CAT Tool if one is provided
        132             CheckCatTool(CatTool)
    

    ~\OneDrive\Documenten\School\PostgraduaatTranslationTechnology\IntroductionToPython\Final_Assignment1\vendor_data.py in CheckWordRate(WordRate)
         71         raise ValueError("This vendor is too expensive, pick another one.")
         72     if WordRate == 0.00:
    ---> 73         raise ValueError("Word rate cannot be 0.00.")
         74 def CheckCatTool(CatTool):
         75     """CheckCatTool, validate CatTOol
    

    ValueError: Word rate cannot be 0.00.



```python
VendorDE = vd.VendorData("Tutorial", "English", "German", "Thomas Zwiebel", CatTool = "SDL Trados Studio")
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    ~\AppData\Local\Temp\ipykernel_12116\153109120.py in <module>
    ----> 1 VendorDE = vd.VendorData("Tutorial", "English", "German", "Thomas Zwiebel", CatTool = "SDL Trados Studio")
    

    ~\OneDrive\Documenten\School\PostgraduaatTranslationTechnology\IntroductionToPython\Final_Assignment1\vendor_data.py in __init__(self, ProjectName, SourceLang, TargLang, VendorName, VendorMail, WordRate, CatTool, Preferred)
        130             CheckWordRate(WordRate)
        131         if CatTool: #validate CAT Tool if one is provided
    --> 132             CheckCatTool(CatTool)
        133         if Preferred != None:
        134             if type(Preferred) != bool:
    

    ~\OneDrive\Documenten\School\PostgraduaatTranslationTechnology\IntroductionToPython\Final_Assignment1\vendor_data.py in CheckCatTool(CatTool)
         85         raise TypeError("CatTool should be a string!")
         86     if not CatTool in ["XTM", "Trados Studio", "MemoQ", "Memsource"]:
    ---> 87             raise ValueError("This CAT tool is not valid. Run 'VendorData.CatTools' to check options.")
         88 
         89 class VendorData:
    

    ValueError: This CAT tool is not valid. Run 'VendorData.CatTools' to check options.


As already mentioned, this kind of validation is done anytime user input is required, not only upon instantiating.
More precisely, validation is done when:
- One of the methods to set a value is run
- The excel is modified using the `ModExcel` method


```python
VendorDE = vd.VendorData("Tutorial", "English", "German", "Thomas Zwiebel") #for illustration we instantiate a new instance of VendorData
```


```python
VendorDE.SetVendorMail("thomas.zw@")
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    ~\AppData\Local\Temp\ipykernel_12116\4282007076.py in <module>
    ----> 1 VendorDE.SetVendorMail("thomas.zw@")
    

    ~\OneDrive\Documenten\School\PostgraduaatTranslationTechnology\IntroductionToPython\Final_Assignment1\vendor_data.py in SetVendorMail(self, NewMail)
        157             NewMail (str): a new e-mail address for a certain vendor
        158         """
    --> 159         CheckVendorMail(NewMail) #validate e-mail address
        160         self.VendorMail = NewMail #value of VendorMail is changed
        161 
    

    ~\OneDrive\Documenten\School\PostgraduaatTranslationTechnology\IntroductionToPython\Final_Assignment1\vendor_data.py in CheckVendorMail(VendorMail)
         54         raise TypeError ("VendorMail should be a string!")
         55     if not(re.search(regex_mail,VendorMail)):
    ---> 56         raise ValueError("Please insert a valid email address.")
         57 def CheckWordRate(WordRate):
         58     """CheckWordRate, validate word rate
    

    ValueError: Please insert a valid email address.



```python
VendorDE.SetWordRate(0.18)
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    ~\AppData\Local\Temp\ipykernel_12116\1677043638.py in <module>
    ----> 1 VendorDE.SetWordRate(0.18)
    

    ~\OneDrive\Documenten\School\PostgraduaatTranslationTechnology\IntroductionToPython\Final_Assignment1\vendor_data.py in SetWordRate(self, NewRate)
        166             NewRate (float): a new word rate for a certain vendor
        167         """
    --> 168         CheckWordRate(NewRate) #validate new word rate
        169         self.WordRate = NewRate #value of WordRate is changed
        170 
    

    ~\OneDrive\Documenten\School\PostgraduaatTranslationTechnology\IntroductionToPython\Final_Assignment1\vendor_data.py in CheckWordRate(WordRate)
         69         raise TypeError("WordRate should be a float!")
         70     if WordRate > 0.15:
    ---> 71         raise ValueError("This vendor is too expensive, pick another one.")
         72     if WordRate == 0.00:
         73         raise ValueError("Word rate cannot be 0.00.")
    

    ValueError: This vendor is too expensive, pick another one.



```python
VendorDE.SetWordRate (0.00)
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    ~\AppData\Local\Temp\ipykernel_12116\2070555766.py in <module>
    ----> 1 VendorDE.SetWordRate (0.00)
    

    ~\OneDrive\Documenten\School\PostgraduaatTranslationTechnology\IntroductionToPython\Final_Assignment1\vendor_data.py in SetWordRate(self, NewRate)
        166             NewRate (float): a new word rate for a certain vendor
        167         """
    --> 168         CheckWordRate(NewRate) #validate new word rate
        169         self.WordRate = NewRate #value of WordRate is changed
        170 
    

    ~\OneDrive\Documenten\School\PostgraduaatTranslationTechnology\IntroductionToPython\Final_Assignment1\vendor_data.py in CheckWordRate(WordRate)
         71         raise ValueError("This vendor is too expensive, pick another one.")
         72     if WordRate == 0.00:
    ---> 73         raise ValueError("Word rate cannot be 0.00.")
         74 def CheckCatTool(CatTool):
         75     """CheckCatTool, validate CatTOol
    

    ValueError: Word rate cannot be 0.00.



```python
VendorDE.ChangeTool("SDL Trados Studio")
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    ~\AppData\Local\Temp\ipykernel_12116\3483989379.py in <module>
    ----> 1 VendorDE.ChangeTool("SDL Trados Studio")
    

    ~\OneDrive\Documenten\School\PostgraduaatTranslationTechnology\IntroductionToPython\Final_Assignment1\vendor_data.py in ChangeTool(self, NewTool)
        175             NewTool (str): a new tool for a certain vendor
        176         """
    --> 177         CheckCatTool(NewTool) #validate new CAT Tool
        178         self.CatTool = NewTool #value of CatTool is changed
        179 
    

    ~\OneDrive\Documenten\School\PostgraduaatTranslationTechnology\IntroductionToPython\Final_Assignment1\vendor_data.py in CheckCatTool(CatTool)
         85         raise TypeError("CatTool should be a string!")
         86     if not CatTool in ["XTM", "Trados Studio", "MemoQ", "Memsource"]:
    ---> 87             raise ValueError("This CAT tool is not valid. Run 'VendorData.CatTools' to check options.")
         88 
         89 class VendorData:
    

    ValueError: This CAT tool is not valid. Run 'VendorData.CatTools' to check options.



```python
VendorDE.SetStatus("None")
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    ~\AppData\Local\Temp\ipykernel_12116\3389852500.py in <module>
    ----> 1 VendorDE.SetStatus("None")
    

    ~\OneDrive\Documenten\School\PostgraduaatTranslationTechnology\IntroductionToPython\Final_Assignment1\vendor_data.py in SetStatus(self, PrefVend)
        186         if PrefVend != None:
        187             if type(PrefVend) != bool:
    --> 188                 raise TypeError("Preferred should either be True, False or None.")
        189         if PrefVend != None:
        190             if PrefVend == True:
    

    TypeError: Preferred should either be True, False or None.


To illustrate that validation is done when running the `ModExcel` method, we first have to write the data to the excel file:


```python
VendorDE.ToExcel()
```

Now we can modify the German vendor and the input will be validated:


```python
VendorDE.ModExcel("E-mail", 3, "thomaszw@")
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    ~\AppData\Local\Temp\ipykernel_12116\1589300048.py in <module>
    ----> 1 VendorDE.ModExcel("E-mail", 3, "thomaszw@")
    

    ~\OneDrive\Documenten\School\PostgraduaatTranslationTechnology\IntroductionToPython\Final_Assignment1\vendor_data.py in ModExcel(self, Key, Index, NewValue)
        246                 raise ValueError("Invalid index, run 'self.ReadExcel()' to see options")
        247             if Key == "E-mail": #validate e-mail address if a value for the key E-mail is modified
    --> 248                 CheckVendorMail(NewValue)
        249             if Key == "Word Rate": #validate word rate if a value for the key Word Rate is modified
        250                 CheckWordRate(NewValue)
    

    ~\OneDrive\Documenten\School\PostgraduaatTranslationTechnology\IntroductionToPython\Final_Assignment1\vendor_data.py in CheckVendorMail(VendorMail)
         54         raise TypeError ("VendorMail should be a string!")
         55     if not(re.search(regex_mail,VendorMail)):
    ---> 56         raise ValueError("Please insert a valid email address.")
         57 def CheckWordRate(WordRate):
         58     """CheckWordRate, validate word rate
    

    ValueError: Please insert a valid email address.



```python
VendorDE.ModExcel("CAT Tool", 3, "Trados Studio 2019")
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    ~\AppData\Local\Temp\ipykernel_12116\3469975144.py in <module>
    ----> 1 VendorDE.ModExcel("CAT Tool", 3, "Trados Studio 2019")
    

    ~\OneDrive\Documenten\School\PostgraduaatTranslationTechnology\IntroductionToPython\Final_Assignment1\vendor_data.py in ModExcel(self, Key, Index, NewValue)
        250                 CheckWordRate(NewValue)
        251             if Key == "CAT Tool": #validate CAT Tool if a value for the key CAT Tool is modified
    --> 252                 CheckCatTool(NewValue)
        253             if Key == "Status": #validate Status if a value for the key Status is modified
        254                 if not NewValue in VendorData.Statuses:
    

    ~\OneDrive\Documenten\School\PostgraduaatTranslationTechnology\IntroductionToPython\Final_Assignment1\vendor_data.py in CheckCatTool(CatTool)
         85         raise TypeError("CatTool should be a string!")
         86     if not CatTool in ["XTM", "Trados Studio", "MemoQ", "Memsource"]:
    ---> 87             raise ValueError("This CAT tool is not valid. Run 'VendorData.CatTools' to check options.")
         88 
         89 class VendorData:
    

    ValueError: This CAT tool is not valid. Run 'VendorData.CatTools' to check options.



```python
VendorDE.ModExcel("Word Rate", 3, 0.18)
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    ~\AppData\Local\Temp\ipykernel_12116\2651721014.py in <module>
    ----> 1 VendorDE.ModExcel("Word Rate", 3, 0.18)
    

    ~\OneDrive\Documenten\School\PostgraduaatTranslationTechnology\IntroductionToPython\Final_Assignment1\vendor_data.py in ModExcel(self, Key, Index, NewValue)
        248                 CheckVendorMail(NewValue)
        249             if Key == "Word Rate": #validate word rate if a value for the key Word Rate is modified
    --> 250                 CheckWordRate(NewValue)
        251             if Key == "CAT Tool": #validate CAT Tool if a value for the key CAT Tool is modified
        252                 CheckCatTool(NewValue)
    

    ~\OneDrive\Documenten\School\PostgraduaatTranslationTechnology\IntroductionToPython\Final_Assignment1\vendor_data.py in CheckWordRate(WordRate)
         69         raise TypeError("WordRate should be a float!")
         70     if WordRate > 0.15:
    ---> 71         raise ValueError("This vendor is too expensive, pick another one.")
         72     if WordRate == 0.00:
         73         raise ValueError("Word rate cannot be 0.00.")
    

    ValueError: This vendor is too expensive, pick another one.



```python
VendorDE.ModExcel("Status", 3, "Busy")
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    ~\AppData\Local\Temp\ipykernel_12116\3428613633.py in <module>
    ----> 1 VendorDE.ModExcel("Status", 3, "Busy")
    

    ~\OneDrive\Documenten\School\PostgraduaatTranslationTechnology\IntroductionToPython\Final_Assignment1\vendor_data.py in ModExcel(self, Key, Index, NewValue)
        253             if Key == "Status": #validate Status if a value for the key Status is modified
        254                 if not NewValue in VendorData.Statuses:
    --> 255                     raise ValueError("Invalid status, run 'VendorData.Statuses' to see options")
        256             ChangeDictionaryValue(VendorDict, Key, Index, NewValue) #change the dictionary value in the dictionary `VendorDict` using the arguments provided for the method ModExcel
        257             df = pd.DataFrame(VendorDict) #turn VendorDict dictionary back into a panda DataFrame
    

    ValueError: Invalid status, run 'VendorData.Statuses' to see options


For the `ModExcel` method there's an additional validation, namely the validation of keys in order to limit the keys for which you can modify the values. Modifiable keys can be checked by running `vd.VendorData.Keys`
Additionally it also is checked if the index is in the dictionary, otherwise the vendor is non-existent and cannot be modified.


```python
vd.VendorData.Keys
```




    ['E-mail', 'CAT Tool', 'Word Rate', 'Status']



If you try to modify any other key you will get an error message:


```python
VendorDE.ModExcel("Vendor", 2, "John Doe")
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    ~\AppData\Local\Temp\ipykernel_12116\2634951232.py in <module>
    ----> 1 VendorDE.ModExcel("Vendor", 2, "John Doe")
    

    ~\OneDrive\Documenten\School\PostgraduaatTranslationTechnology\IntroductionToPython\Final_Assignment1\vendor_data.py in ModExcel(self, Key, Index, NewValue)
        242             VendorDict = ExcelRecordsDf.to_dict()
        243             if not Key in self.Keys:
    --> 244                 raise ValueError("Invalid key, run 'VendorData.Keys' to see options.")
        245             if not Index in VendorDict[Key]:
        246                 raise ValueError("Invalid index, run 'self.ReadExcel()' to see options")
    

    ValueError: Invalid key, run 'VendorData.Keys' to see options.



```python
VendorDE.ModExcel("Target Language", 3, "Croatian")
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    ~\AppData\Local\Temp\ipykernel_12116\614258264.py in <module>
    ----> 1 VendorDE.ModExcel("Target Language", 3, "Croatian")
    

    ~\OneDrive\Documenten\School\PostgraduaatTranslationTechnology\IntroductionToPython\Final_Assignment1\vendor_data.py in ModExcel(self, Key, Index, NewValue)
        242             VendorDict = ExcelRecordsDf.to_dict()
        243             if not Key in self.Keys:
    --> 244                 raise ValueError("Invalid key, run 'VendorData.Keys' to see options.")
        245             if not Index in VendorDict[Key]:
        246                 raise ValueError("Invalid index, run 'self.ReadExcel()' to see options")
    

    ValueError: Invalid key, run 'VendorData.Keys' to see options.


Since there are only 4 vendors in the excel file and the index start at 0 and go up, an error message should appear when you try to modify a higher index:


```python
VendorDE.ModExcel("CAT Tool", 6, "XTM")
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    ~\AppData\Local\Temp\ipykernel_12116\235551850.py in <module>
    ----> 1 VendorDE.ModExcel("CAT Tool", 6, "XTM")
    

    ~\OneDrive\Documenten\School\PostgraduaatTranslationTechnology\IntroductionToPython\Final_Assignment1\vendor_data.py in ModExcel(self, Key, Index, NewValue)
        244                 raise ValueError("Invalid key, run 'VendorData.Keys' to see options.")
        245             if not Index in VendorDict[Key]:
    --> 246                 raise ValueError("Invalid index, run 'self.ReadExcel()' to see options")
        247             if Key == "E-mail": #validate e-mail address if a value for the key E-mail is modified
        248                 CheckVendorMail(NewValue)
    

    ValueError: Invalid index, run 'self.ReadExcel()' to see options


You can check for the right index by running the `ReadExcel` method for any vendor you already defined:


```python
VendorNL.ReadExcel()
```




    {'Target Language': {0: 'Dutch', 1: 'French', 2: 'Spanish', 3: 'German'},
     'Vendor': {0: 'Elmo Geeraerts',
      1: 'Jean Lefèvre',
      2: 'Emilio De La Banda',
      3: 'Thomas Zwiebel'},
     'E-mail': {0: nan,
      1: 'j.lefevre@hotmail.com',
      2: 'e.dlbanda@outlook.com',
      3: nan},
     'CAT Tool': {0: 'XTM', 1: 'Trados Studio', 2: 'MemoQ', 3: 'XTM'},
     'Word Rate': {0: 0.08, 1: 0.1, 2: 0.09, 3: nan},
     'Status': {0: 'Potential', 1: 'Back-up', 2: 'Back-up', 3: 'Potential'}}



Now you know the different functionalities of the script vendor__data.py and what triggers which error. Hopefully you can use this script in your daily life as a translation project manager. Have fun!

## Running `vendor_data.py`
The script can also be run on its own. We'll first look at the help for this script.


```python
%run vendor_data.py --help
```

    usage: vendor_data.py [-h] [-a] [-m]
    
    optional arguments:
      -h, --help    show this help message and exit
      -a, --add     Add a vendor
      -m, --modify  Modify an existing vendor
    

As you can see, apart from the help argument, there are two other optional arguments:
- `-a` or `--add` allows the user to add a new vendor to an excel file (existing or new);
- `-m` or `--modify` allows the user to modify a vendor in an existing excel file;

We'll start by writing a totally new excel file and adding a vendor to it:


```python
%run vendor_data.py --a
```

    What is the project name? TestProject
    What is the source language? English
    What's the vendor's name? Elmo Geeraerts
    Into which language will the vendor translate? Dutch
    What is the vendor's email address? geeraerts@me.com
    What is the vendor's word rate in EUR? Should be between 0.01 and 0.15. If higher, choose another vendor. 0.12
    In which tool will the vendor be working?* XTM
    * Trados Studio
    * MemoQ
    * Memsource
    
    True or False: Is this vendor a preferred vendor? If neither, leave blank. True
    Are you done? yes
    Do you want to add this vendor to the excel file? yes
    

A new excel file will appear next to where you stored this notebook with the name `TestProject_English`, i.e. the project name and source language we provided.
Just like when importing the script, it is possible to leave the following data blank:
- The vendor's email address
- The vendors word rate
- The tool in which the vendor will be working
- Whether or not the vendor is a preferred vendor


```python
%run vendor_data.py --a
```

    What is the project name? TestProject
    What is the source language? English
    What's the vendor's name? Jean Baptiste
    Into which language will the vendor translate? French
    What is the vendor's email address? 
    What is the vendor's word rate in EUR? Should be between 0.01 and 0.15. If higher, choose another vendor. 
    In which tool will the vendor be working?* XTM
    * Trados Studio
    * MemoQ
    * Memsource
    
    True or False: Is this vendor a preferred vendor? If neither, leave blank. 
    Are you done? 
    Blank values are not allowed.
    Are you done? yes
    Do you want to add this vendor to the excel file? yes
    

If the project name and the source language are the same as for the previous vendor you've entered, this vendor will be added to the same excel file, if not a new excel file is created using the project name and the source language as the file name. You'll notice that for the prompts you leave blank the default value is enterred OR it is left blank.

Just like when you use this script as a module, the data you provide is validate at every step of the user interaction. TypeErrors do not cause the prompts to stop but instead you get asked the same question again, ValueErrors do break off the code:


```python
%run vendor_data.py -a
```

    What is the project name? TestProject
    What is the source language? English
    What's the vendor's name? Emanuel Dos Santos
    Into which language will the vendor translate? Portuguese
    What is the vendor's email address? e_dossantos@gmail.com
    What is the vendor's word rate in EUR? Should be between 0.01 and 0.15. If higher, choose another vendor. 0.19
    


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    ~\OneDrive\Documenten\School\PostgraduaatTranslationTechnology\IntroductionToPython\Final_Assignment1\vendor_data.py in <module>
        304             NewWordRate = pyip.inputFloat("What is the vendor's word rate in EUR? Should be between 0.01 and 0.15. If higher, choose another vendor. ", blank = True)
        305             if NewWordRate:
    --> 306                 CheckWordRate(NewWordRate)
        307                 VendorWordRate = NewWordRate
        308             else:
    

    ~\OneDrive\Documenten\School\PostgraduaatTranslationTechnology\IntroductionToPython\Final_Assignment1\vendor_data.py in CheckWordRate(WordRate)
         69         raise TypeError("WordRate should be a float!")
         70     if WordRate > 0.15:
    ---> 71         raise ValueError("This vendor is too expensive, pick another one.")
         72     if WordRate == 0.00:
         73         raise ValueError("Word rate cannot be 0.00.")
    

    ValueError: This vendor is too expensive, pick another one.



```python
%run vendor_data.py -a
```

    What is the project name? TestProject
    What is the source language? English
    What's the vendor's name? Emanuel Dos Santos
    Into which language will the vendor translate? Portuguese
    What is the vendor's email address? e_dossantos@
    


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    ~\OneDrive\Documenten\School\PostgraduaatTranslationTechnology\IntroductionToPython\Final_Assignment1\vendor_data.py in <module>
        298             NewVendorMail = pyip.inputStr("What is the vendor's email address? ", blank = True, default="")
        299             if NewVendorMail:
    --> 300                 CheckVendorMail(NewVendorMail)
        301                 VendorMail = NewVendorMail
        302             else:
    

    ~\OneDrive\Documenten\School\PostgraduaatTranslationTechnology\IntroductionToPython\Final_Assignment1\vendor_data.py in CheckVendorMail(VendorMail)
         54         raise TypeError ("VendorMail should be a string!")
         55     if not(re.search(regex_mail,VendorMail)):
    ---> 56         raise ValueError("Please insert a valid email address.")
         57 def CheckWordRate(WordRate):
         58     """CheckWordRate, validate word rate
    

    ValueError: Please insert a valid email address.


Since we're using pyipinputplus we can already avoid some errors by:
- using the built in type validation of the package by using `pyip.inputStr` or `pyip.inputFloat`, so that the user is forced to put in a valid data type
- using the Menu option to limit the choices, for example for the CAT Tools

It is also possible to modify existing vendors. The user has to provide the project name and the source language, and is then further asked some questions regarding the vendor they want to modify:


```python
%run vendor_data.py -m
```

    What is the name of the project that the vendor you want to modify works on? TestProject
    What is the source language? English
    These are the vendor's already in the database: 
    0: Elmo Geeraerts
    1: Jean Baptiste
    Enter the index of the vendor you want to modify: 0
    What is the vendor's e-mail? 
    What is the vendor's word rate? Should be between 0.01 and 0.15. If higher, choose another vendor. 
    In which tool will the vendor be working?* XTM
    * Trados Studio
    * MemoQ
    * Memsource
    Trados Studio
    What is the vendor's new status? * Preferred
    * Back-up
    * Potential
    
    Are you done? yes
    This vendor is modified correctly.
    

The vendor in the excel file should now be modified.

Now you are totally ready to use this script and resolve any issues that might pop up! Hopefully this script makes your life as a translation project manager easier! Have fun!
