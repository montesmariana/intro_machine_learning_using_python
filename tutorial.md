# Tutorial: how to use `vendor_data.py`

## Using `vendor_data.py` as a module

This interactive notebook shows how to use the class and the different functions in the script `vendor_data.py`.

To use the script in this code, we can import the script as a module or run it directly.
We'll begin with importing the code as module:


```python
import sys
sys.path.append ('..\Final_Assignment1')
import vendor_data as vd # 'as vd' is not necessary but makes it shorter.
```

### Instantiating an instance of `VendorData`
We'll start with instantiating some instances of the class VendorData.
The class takes four positional arguments: `ProjectName`, `SourceLang`, `TargetLang` and `VendorName`.
It also takes four optional arguments: `VendorMail`, `WordRate`, `CatTool`, and `Preferred`.


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


Some arguments have default values or empty values. When we check the e-mail for VendorNL, for which we didn't provide one, we'll see that it returns an empty string:

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



### Methods
The class also contains a couple of methods:
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



Because we set the value for preferred to True for the French vendor, they got the status "Preferred". If for some reason this changes, we can change the status easily, by changing the value for Preferred to False or None:


```python
VendorFR.SetStatus(False)
VendorFR.Preferred
```




    False




```python
VendorFR.Status
```




    'Back-up'



We can now write the data for the vendors to an excel file. Since every vendor has the same value for the argument `ProjectName` and `SourceLang`, they will be written to the same excel file.
<div class="alert alert-danger">
If you run `.toExcel()` multiple times on the same vendor, it will generate multiple entries!
</div>


```python
VendorNL.ToExcel()
VendorFR.ToExcel()
VendorES.ToExcel()
```

    The file Tutorial_English.xlsx is correctly created and the vendor Elmo Geeraerts was added.
    The vendor Jean Lefèvre was added to Tutorial_English.xlsx.
    The vendor Emilio De La Banda was added to Tutorial_English.xlsx.
    

An excel file named `Tutorial_English.xlsx` should appear in the same folder where you stored this tutorial notebook.
We can now read the entire excel file by calling the method ReadExcel for any vendor in the excel file. We'll get the information for every vendor in the excel file, no matter what vendor we pick:


```python
VendorNL.ReadExcel()
```




    {'Target Language': {0: 'Dutch', 1: 'French', 2: 'Spanish'},
     'Vendor': {0: 'Elmo Geeraerts', 1: 'Jean Lefèvre', 2: 'Emilio De La Banda'},
     'E-mail': {0: nan, 1: 'j.lefevre@hotmail.com', 2: 'e.dlbanda@outlook.com'},
     'CAT Tool': {0: 'XTM', 1: 'Trados Studio', 2: 'Trados Studio'},
     'Word Rate': {0: 0.08, 1: 0.1, 2: 0.09},
     'Status': {0: 'Potential', 1: 'Back-up', 2: 'Back-up'}}



If we create another vendor that works on a different project or translates from another source language and call the same method without writing the data to an excel file first, we'll get an error message saying that a file for the project in the given source language does not exist.


```python
VendorBG = vd.VendorData("Tutorial", "German", "Bulgarian", "Bulgarian Jacob")
VendorBG.ReadExcel()
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    ~\AppData\Local\Temp\ipykernel_19840\1804978508.py in <module>
          1 VendorBG = vd.VendorData("Tutorial", "German", "Bulgarian", "Bulgarian Jacob")
    ----> 2 VendorBG.ReadExcel()
    

    ~\OneDrive\Documenten\School\PostgraduaatTranslationTechnology\IntroductionToPython\Final_Assignment1\vendor_data.py in ReadExcel(self)
        255             return VendorDict
        256         else:
    --> 257             raise ValueError(f"There is no file for {self.ProjectName} in {self.SourceLang}")
        258 
        259     def ModExcel(self, Key, NewValue):
    

    ValueError: There is no file for Tutorial in German


We can also modify the excel file by running the `ModExcel` method.
<div class="alert alert-danger">
You can only modify one value for one key at a time.
</div>

This method takes 2 arguments:
1. The `Key` which represents the arguments you can change the values for. You can check the modifiable keys by running vd.VendorData.Keys
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
VendorES.ModExcel("CAT Tool", "MemoQ")
```

    The vendor was correctly modified.
    

If you check this by running `.CatTool`, the value will be changed.


```python
VendorES.CatTool
```




    'MemoQ'



The script knows which vendor you want to change the value for because of the instance you call the method for. If you want to change information for the Dutch vendor, you should call the method for that vendor


```python
VendorNL.ModExcel("Status", "Preferred")
```

    The vendor was correctly modified.
    


```python
VendorNL.Status
```




    'Preferred'



If we read the excel (`ReadExcel()`), we'll see that the values for the correct vendors are changed. Here it does not matter for which vendor we call the method:


```python
VendorNL.ReadExcel()
```




    {'Target Language': {0: 'Dutch', 1: 'French', 2: 'Spanish'},
     'Vendor': {0: 'Elmo Geeraerts', 1: 'Jean Lefèvre', 2: 'Emilio De La Banda'},
     'E-mail': {0: nan, 1: 'j.lefevre@hotmail.com', 2: 'e.dlbanda@outlook.com'},
     'CAT Tool': {0: 'XTM', 1: 'Trados Studio', 2: 'MemoQ'},
     'Word Rate': {0: 0.08, 1: 0.1, 2: 0.09},
     'Status': {0: 'Preferred', 1: 'Back-up', 2: 'Back-up'}}



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

    ~\AppData\Local\Temp\ipykernel_19840\3042631035.py in <module>
    ----> 1 VendorDE = vd.VendorData(0.1, "English", "German", "Thomas Zwiebel")
    

    ~\OneDrive\Documenten\School\PostgraduaatTranslationTechnology\IntroductionToPython\Final_Assignment1\vendor_data.py in __init__(self, ProjectName, SourceLang, TargLang, VendorName, VendorMail, WordRate, CatTool, Preferred)
        113         """
        114         if type(ProjectName) != str:
    --> 115             raise TypeError("ProjectName should be a string!")
        116         if type(SourceLang) != str:
        117             raise TypeError("SourceLang should be a string!")
    

    TypeError: ProjectName should be a string!



```python
VendorDE = vd.VendorData("Tutorial", 1, "German", "Thomas Zwiebel")
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    ~\AppData\Local\Temp\ipykernel_19840\2835384243.py in <module>
    ----> 1 VendorDE = vd.VendorData("Tutorial", 1, "German", "Thomas Zwiebel")
    

    ~\OneDrive\Documenten\School\PostgraduaatTranslationTechnology\IntroductionToPython\Final_Assignment1\vendor_data.py in __init__(self, ProjectName, SourceLang, TargLang, VendorName, VendorMail, WordRate, CatTool, Preferred)
        115             raise TypeError("ProjectName should be a string!")
        116         if type(SourceLang) != str:
    --> 117             raise TypeError("SourceLang should be a string!")
        118         if type(TargLang) != str:
        119             raise TypeError("TargLang should be a string!")
    

    TypeError: SourceLang should be a string!



```python
VendorDE = vd.VendorData("Tutorial", "English", True, "Thomas Zwiebel")
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    ~\AppData\Local\Temp\ipykernel_19840\2057797999.py in <module>
    ----> 1 VendorDE = vd.VendorData("Tutorial", "English", True, "Thomas Zwiebel")
    

    ~\OneDrive\Documenten\School\PostgraduaatTranslationTechnology\IntroductionToPython\Final_Assignment1\vendor_data.py in __init__(self, ProjectName, SourceLang, TargLang, VendorName, VendorMail, WordRate, CatTool, Preferred)
        117             raise TypeError("SourceLang should be a string!")
        118         if type(TargLang) != str:
    --> 119             raise TypeError("TargLang should be a string!")
        120         if type(VendorName) !=str:
        121             raise TypeError("VendorName should be a string!")
    

    TypeError: TargLang should be a string!



```python
VendorDE = vd.VendorData("Tutorial", "English", "German", None)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    ~\AppData\Local\Temp\ipykernel_19840\1683973233.py in <module>
    ----> 1 VendorDE = vd.VendorData("Tutorial", "English", "German", None)
    

    ~\OneDrive\Documenten\School\PostgraduaatTranslationTechnology\IntroductionToPython\Final_Assignment1\vendor_data.py in __init__(self, ProjectName, SourceLang, TargLang, VendorName, VendorMail, WordRate, CatTool, Preferred)
        119             raise TypeError("TargLang should be a string!")
        120         if type(VendorName) !=str:
    --> 121             raise TypeError("VendorName should be a string!")
        122         if VendorMail: #validate e-mail address if one is provided
        123             CheckVendorMail(VendorMail)
    

    TypeError: VendorName should be a string!



```python
VendorDE = vd.VendorData("Tutorial", "English", "German", "Thomas Zwiebel", 3)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    ~\AppData\Local\Temp\ipykernel_19840\2269134755.py in <module>
    ----> 1 VendorDE = vd.VendorData("Tutorial", "English", "German", "Thomas Zwiebel", 3)
    

    ~\OneDrive\Documenten\School\PostgraduaatTranslationTechnology\IntroductionToPython\Final_Assignment1\vendor_data.py in __init__(self, ProjectName, SourceLang, TargLang, VendorName, VendorMail, WordRate, CatTool, Preferred)
        121             raise TypeError("VendorName should be a string!")
        122         if VendorMail: #validate e-mail address if one is provided
    --> 123             CheckVendorMail(VendorMail)
        124         if WordRate != None: #validate word rate if one is provided
        125             CheckWordRate(WordRate)
    

    ~\OneDrive\Documenten\School\PostgraduaatTranslationTechnology\IntroductionToPython\Final_Assignment1\vendor_data.py in CheckVendorMail(VendorMail)
         44     regex_mail = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$" #regex used to validate email
         45     if type(VendorMail) != str:
    ---> 46         raise TypeError ("VendorMail should be a string!")
         47     if not(re.search(regex_mail,VendorMail)):
         48         raise ValueError("Please insert a valid email address.")
    

    TypeError: VendorMail should be a string!



```python
VendorDE = vd.VendorData("Tutorial", "English", "German", "Thomas Zwiebel", WordRate = "0.15")
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    ~\AppData\Local\Temp\ipykernel_19840\2028391605.py in <module>
    ----> 1 VendorDE = vd.VendorData("Tutorial", "English", "German", "Thomas Zwiebel", WordRate = "0.15")
    

    ~\OneDrive\Documenten\School\PostgraduaatTranslationTechnology\IntroductionToPython\Final_Assignment1\vendor_data.py in __init__(self, ProjectName, SourceLang, TargLang, VendorName, VendorMail, WordRate, CatTool, Preferred)
        123             CheckVendorMail(VendorMail)
        124         if WordRate != None: #validate word rate if one is provided
    --> 125             CheckWordRate(WordRate)
        126         if CatTool: #validate CAT Tool if one is provided
        127             CheckCatTool(CatTool)
    

    ~\OneDrive\Documenten\School\PostgraduaatTranslationTechnology\IntroductionToPython\Final_Assignment1\vendor_data.py in CheckWordRate(WordRate)
         60     """
         61     if type(WordRate) != float:
    ---> 62         raise TypeError("WordRate should be a float!")
         63     if WordRate > 0.15:
         64         raise ValueError("This vendor is too expensive, pick another one.")
    

    TypeError: WordRate should be a float!



```python
VendorDE = vd.VendorData("Tutorial", "English", "German", "Thomas Zwiebel", Preferred = "Test")
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    ~\AppData\Local\Temp\ipykernel_19840\1300272076.py in <module>
    ----> 1 VendorDE = vd.VendorData("Tutorial", "English", "German", "Thomas Zwiebel", Preferred = "Test")
    

    ~\OneDrive\Documenten\School\PostgraduaatTranslationTechnology\IntroductionToPython\Final_Assignment1\vendor_data.py in __init__(self, ProjectName, SourceLang, TargLang, VendorName, VendorMail, WordRate, CatTool, Preferred)
        128         if Preferred != None:
        129             if type(Preferred) != bool:
    --> 130                 raise TypeError("Preferred should either be True, False or None.")
        131         if Preferred != None: #if Preferred is set to True, status will be preferred, if set to False, back-up and if neither "Potential"
        132             if Preferred:
    

    TypeError: Preferred should either be True, False or None.



```python
VendorDE = vd.VendorData("Tutorial", "English", "German", "Thomas Zwiebel", CatTool = True)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    ~\AppData\Local\Temp\ipykernel_19840\2908856665.py in <module>
    ----> 1 VendorDE = vd.VendorData("Tutorial", "English", "German", "Thomas Zwiebel", CatTool = True)
    

    ~\OneDrive\Documenten\School\PostgraduaatTranslationTechnology\IntroductionToPython\Final_Assignment1\vendor_data.py in __init__(self, ProjectName, SourceLang, TargLang, VendorName, VendorMail, WordRate, CatTool, Preferred)
        125             CheckWordRate(WordRate)
        126         if CatTool: #validate CAT Tool if one is provided
    --> 127             CheckCatTool(CatTool)
        128         if Preferred != None:
        129             if type(Preferred) != bool:
    

    ~\OneDrive\Documenten\School\PostgraduaatTranslationTechnology\IntroductionToPython\Final_Assignment1\vendor_data.py in CheckCatTool(CatTool)
         78     """
         79     if type(CatTool) != str:
    ---> 80         raise TypeError("CatTool should be a string!")
         81     if not CatTool in VendorData.CatTools:
         82         raise ValueError("This CAT tool is not valid. Run 'VendorData.CatTools' to check options.")
    

    TypeError: CatTool should be a string!


There are also some functions that ensure that:
- `VendorMail` is a valid e-mail address by checking it against a regex string;
- `WordRate` is not 0.00 or more than 0.15 and not negative;
- `CatTool` is one of the following: XTM, Trados Studio, MemoQ or Memsource.


```python
VendorDE = vd.VendorData("Tutorial", "English", "German", "Thomas Zwiebel", VendorMail = "thomas.zw")
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    ~\AppData\Local\Temp\ipykernel_19840\2329585938.py in <module>
    ----> 1 VendorDE = vd.VendorData("Tutorial", "English", "German", "Thomas Zwiebel", VendorMail = "thomas.zw")
    

    ~\OneDrive\Documenten\School\PostgraduaatTranslationTechnology\IntroductionToPython\Final_Assignment1\vendor_data.py in __init__(self, ProjectName, SourceLang, TargLang, VendorName, VendorMail, WordRate, CatTool, Preferred)
        121             raise TypeError("VendorName should be a string!")
        122         if VendorMail: #validate e-mail address if one is provided
    --> 123             CheckVendorMail(VendorMail)
        124         if WordRate != None: #validate word rate if one is provided
        125             CheckWordRate(WordRate)
    

    ~\OneDrive\Documenten\School\PostgraduaatTranslationTechnology\IntroductionToPython\Final_Assignment1\vendor_data.py in CheckVendorMail(VendorMail)
         46         raise TypeError ("VendorMail should be a string!")
         47     if not(re.search(regex_mail,VendorMail)):
    ---> 48         raise ValueError("Please insert a valid email address.")
         49 def CheckWordRate(WordRate):
         50     """Function to validate the word rate
    

    ValueError: Please insert a valid email address.



```python
VendorDE = vd.VendorData("Tutorial", "English", "German", "Thomas Zwiebel", WordRate = 0.19)
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    ~\AppData\Local\Temp\ipykernel_19840\389829205.py in <module>
    ----> 1 VendorDE = vd.VendorData("Tutorial", "English", "German", "Thomas Zwiebel", WordRate = 0.19)
    

    ~\OneDrive\Documenten\School\PostgraduaatTranslationTechnology\IntroductionToPython\Final_Assignment1\vendor_data.py in __init__(self, ProjectName, SourceLang, TargLang, VendorName, VendorMail, WordRate, CatTool, Preferred)
        123             CheckVendorMail(VendorMail)
        124         if WordRate != None: #validate word rate if one is provided
    --> 125             CheckWordRate(WordRate)
        126         if CatTool: #validate CAT Tool if one is provided
        127             CheckCatTool(CatTool)
    

    ~\OneDrive\Documenten\School\PostgraduaatTranslationTechnology\IntroductionToPython\Final_Assignment1\vendor_data.py in CheckWordRate(WordRate)
         62         raise TypeError("WordRate should be a float!")
         63     if WordRate > 0.15:
    ---> 64         raise ValueError("This vendor is too expensive, pick another one.")
         65     if WordRate == 0.00:
         66         raise ValueError("Word rate cannot be 0.00.")
    

    ValueError: This vendor is too expensive, pick another one.



```python
VendorDE = vd.VendorData("Tutorial", "English", "German", "Thomas Zwiebel", WordRate = 0.00)
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    ~\AppData\Local\Temp\ipykernel_19840\2186391260.py in <module>
    ----> 1 VendorDE = vd.VendorData("Tutorial", "English", "German", "Thomas Zwiebel", WordRate = 0.00)
    

    ~\OneDrive\Documenten\School\PostgraduaatTranslationTechnology\IntroductionToPython\Final_Assignment1\vendor_data.py in __init__(self, ProjectName, SourceLang, TargLang, VendorName, VendorMail, WordRate, CatTool, Preferred)
        123             CheckVendorMail(VendorMail)
        124         if WordRate != None: #validate word rate if one is provided
    --> 125             CheckWordRate(WordRate)
        126         if CatTool: #validate CAT Tool if one is provided
        127             CheckCatTool(CatTool)
    

    ~\OneDrive\Documenten\School\PostgraduaatTranslationTechnology\IntroductionToPython\Final_Assignment1\vendor_data.py in CheckWordRate(WordRate)
         64         raise ValueError("This vendor is too expensive, pick another one.")
         65     if WordRate == 0.00:
    ---> 66         raise ValueError("Word rate cannot be 0.00.")
         67     if WordRate < 0.00:
         68         raise ValueError("Word rate cannot be negative.")
    

    ValueError: Word rate cannot be 0.00.



```python
VendorDE = vd.VendorData("Tutorial", "English", "German", "Thomas Zwiebel", WordRate = -0.04)
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    ~\AppData\Local\Temp\ipykernel_19840\251048835.py in <module>
    ----> 1 VendorDE = vd.VendorData("Tutorial", "English", "German", "Thomas Zwiebel", WordRate = -0.04)
    

    ~\OneDrive\Documenten\School\PostgraduaatTranslationTechnology\IntroductionToPython\Final_Assignment1\vendor_data.py in __init__(self, ProjectName, SourceLang, TargLang, VendorName, VendorMail, WordRate, CatTool, Preferred)
        123             CheckVendorMail(VendorMail)
        124         if WordRate != None: #validate word rate if one is provided
    --> 125             CheckWordRate(WordRate)
        126         if CatTool: #validate CAT Tool if one is provided
        127             CheckCatTool(CatTool)
    

    ~\OneDrive\Documenten\School\PostgraduaatTranslationTechnology\IntroductionToPython\Final_Assignment1\vendor_data.py in CheckWordRate(WordRate)
         66         raise ValueError("Word rate cannot be 0.00.")
         67     if WordRate < 0.00:
    ---> 68         raise ValueError("Word rate cannot be negative.")
         69 def CheckCatTool(CatTool):
         70     """Function to validate the chosen CAT Tool
    

    ValueError: Word rate cannot be negative.



```python
VendorDE = vd.VendorData("Tutorial", "English", "German", "Thomas Zwiebel", CatTool = "SDL Trados Studio")
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    ~\AppData\Local\Temp\ipykernel_19840\153109120.py in <module>
    ----> 1 VendorDE = vd.VendorData("Tutorial", "English", "German", "Thomas Zwiebel", CatTool = "SDL Trados Studio")
    

    ~\OneDrive\Documenten\School\PostgraduaatTranslationTechnology\IntroductionToPython\Final_Assignment1\vendor_data.py in __init__(self, ProjectName, SourceLang, TargLang, VendorName, VendorMail, WordRate, CatTool, Preferred)
        125             CheckWordRate(WordRate)
        126         if CatTool: #validate CAT Tool if one is provided
    --> 127             CheckCatTool(CatTool)
        128         if Preferred != None:
        129             if type(Preferred) != bool:
    

    ~\OneDrive\Documenten\School\PostgraduaatTranslationTechnology\IntroductionToPython\Final_Assignment1\vendor_data.py in CheckCatTool(CatTool)
         80         raise TypeError("CatTool should be a string!")
         81     if not CatTool in VendorData.CatTools:
    ---> 82         raise ValueError("This CAT tool is not valid. Run 'VendorData.CatTools' to check options.")
         83 
         84 class VendorData:
    

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

    ~\AppData\Local\Temp\ipykernel_19840\4282007076.py in <module>
    ----> 1 VendorDE.SetVendorMail("thomas.zw@")
    

    ~\OneDrive\Documenten\School\PostgraduaatTranslationTechnology\IntroductionToPython\Final_Assignment1\vendor_data.py in SetVendorMail(self, NewMail)
        157             ValueError: if the address provided does not conform with the regex string `regex_mail`, a ValueError is raised
        158         """
    --> 159         CheckVendorMail(NewMail) #validate e-mail address
        160         self.VendorMail = NewMail #value of VendorMail is changed
        161 
    

    ~\OneDrive\Documenten\School\PostgraduaatTranslationTechnology\IntroductionToPython\Final_Assignment1\vendor_data.py in CheckVendorMail(VendorMail)
         46         raise TypeError ("VendorMail should be a string!")
         47     if not(re.search(regex_mail,VendorMail)):
    ---> 48         raise ValueError("Please insert a valid email address.")
         49 def CheckWordRate(WordRate):
         50     """Function to validate the word rate
    

    ValueError: Please insert a valid email address.



```python
VendorDE.SetWordRate(0.18)
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    ~\AppData\Local\Temp\ipykernel_19840\1677043638.py in <module>
    ----> 1 VendorDE.SetWordRate(0.18)
    

    ~\OneDrive\Documenten\School\PostgraduaatTranslationTechnology\IntroductionToPython\Final_Assignment1\vendor_data.py in SetWordRate(self, NewRate)
        173             ValueError: the argument provided should not be negative.
        174         """
    --> 175         CheckWordRate(NewRate) #validate new word rate
        176         self.WordRate = NewRate #value of WordRate is changed
        177 
    

    ~\OneDrive\Documenten\School\PostgraduaatTranslationTechnology\IntroductionToPython\Final_Assignment1\vendor_data.py in CheckWordRate(WordRate)
         62         raise TypeError("WordRate should be a float!")
         63     if WordRate > 0.15:
    ---> 64         raise ValueError("This vendor is too expensive, pick another one.")
         65     if WordRate == 0.00:
         66         raise ValueError("Word rate cannot be 0.00.")
    

    ValueError: This vendor is too expensive, pick another one.



```python
VendorDE.SetWordRate (0.00)
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    ~\AppData\Local\Temp\ipykernel_19840\2070555766.py in <module>
    ----> 1 VendorDE.SetWordRate (0.00)
    

    ~\OneDrive\Documenten\School\PostgraduaatTranslationTechnology\IntroductionToPython\Final_Assignment1\vendor_data.py in SetWordRate(self, NewRate)
        173             ValueError: the argument provided should not be negative.
        174         """
    --> 175         CheckWordRate(NewRate) #validate new word rate
        176         self.WordRate = NewRate #value of WordRate is changed
        177 
    

    ~\OneDrive\Documenten\School\PostgraduaatTranslationTechnology\IntroductionToPython\Final_Assignment1\vendor_data.py in CheckWordRate(WordRate)
         64         raise ValueError("This vendor is too expensive, pick another one.")
         65     if WordRate == 0.00:
    ---> 66         raise ValueError("Word rate cannot be 0.00.")
         67     if WordRate < 0.00:
         68         raise ValueError("Word rate cannot be negative.")
    

    ValueError: Word rate cannot be 0.00.



```python
VendorDE.SetWordRate(-0.04)
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    ~\AppData\Local\Temp\ipykernel_19840\1645063171.py in <module>
    ----> 1 VendorDE.SetWordRate(-0.04)
    

    ~\OneDrive\Documenten\School\PostgraduaatTranslationTechnology\IntroductionToPython\Final_Assignment1\vendor_data.py in SetWordRate(self, NewRate)
        173             ValueError: the argument provided should not be negative.
        174         """
    --> 175         CheckWordRate(NewRate) #validate new word rate
        176         self.WordRate = NewRate #value of WordRate is changed
        177 
    

    ~\OneDrive\Documenten\School\PostgraduaatTranslationTechnology\IntroductionToPython\Final_Assignment1\vendor_data.py in CheckWordRate(WordRate)
         66         raise ValueError("Word rate cannot be 0.00.")
         67     if WordRate < 0.00:
    ---> 68         raise ValueError("Word rate cannot be negative.")
         69 def CheckCatTool(CatTool):
         70     """Function to validate the chosen CAT Tool
    

    ValueError: Word rate cannot be negative.



```python
VendorDE.ChangeTool("SDL Trados Studio")
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    ~\AppData\Local\Temp\ipykernel_19840\3483989379.py in <module>
    ----> 1 VendorDE.ChangeTool("SDL Trados Studio")
    

    ~\OneDrive\Documenten\School\PostgraduaatTranslationTechnology\IntroductionToPython\Final_Assignment1\vendor_data.py in ChangeTool(self, NewTool)
        187             ValueError: the argument provided should be one of the four CAT Tools in the list VendorData.CatTools
        188         """
    --> 189         CheckCatTool(NewTool) #validate new CAT Tool
        190         self.CatTool = NewTool #value of CatTool is changed
        191 
    

    ~\OneDrive\Documenten\School\PostgraduaatTranslationTechnology\IntroductionToPython\Final_Assignment1\vendor_data.py in CheckCatTool(CatTool)
         80         raise TypeError("CatTool should be a string!")
         81     if not CatTool in VendorData.CatTools:
    ---> 82         raise ValueError("This CAT tool is not valid. Run 'VendorData.CatTools' to check options.")
         83 
         84 class VendorData:
    

    ValueError: This CAT tool is not valid. Run 'VendorData.CatTools' to check options.



```python
VendorDE.SetStatus("None")
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    ~\AppData\Local\Temp\ipykernel_19840\3389852500.py in <module>
    ----> 1 VendorDE.SetStatus("None")
    

    ~\OneDrive\Documenten\School\PostgraduaatTranslationTechnology\IntroductionToPython\Final_Assignment1\vendor_data.py in SetStatus(self, PrefVend)
        198         if PrefVend != None:
        199             if type(PrefVend) != bool:
    --> 200                 raise TypeError("Preferred should either be True, False or None.")
        201         if PrefVend != None:
        202             if PrefVend == True:
    

    TypeError: Preferred should either be True, False or None.


To illustrate that validation is done when running the `ModExcel` method, we first have to write the data to the excel file:
<div class="alert alert-danger">
If you run `.toExcel()` multiple times on the same vendor, it will generate multiple entries!
</div>


```python
VendorDE.ToExcel()
```

    The vendor Thomas Zwiebel was added to Tutorial_English.xlsx.
    

Now we can modify the German vendor and the input will be validated:


```python
VendorDE.ModExcel("E-mail", 3, "thomaszw@")
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    ~\AppData\Local\Temp\ipykernel_19840\1589300048.py in <module>
    ----> 1 VendorDE.ModExcel("E-mail", 3, "thomaszw@")
    

    TypeError: ModExcel() takes 3 positional arguments but 4 were given



```python
VendorDE.ModExcel("CAT Tool", 3, "Trados Studio 2019")
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    ~\AppData\Local\Temp\ipykernel_19840\3469975144.py in <module>
    ----> 1 VendorDE.ModExcel("CAT Tool", 3, "Trados Studio 2019")
    

    TypeError: ModExcel() takes 3 positional arguments but 4 were given



```python
VendorDE.ModExcel("Word Rate", 3, 0.18)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    ~\AppData\Local\Temp\ipykernel_19840\2651721014.py in <module>
    ----> 1 VendorDE.ModExcel("Word Rate", 3, 0.18)
    

    TypeError: ModExcel() takes 3 positional arguments but 4 were given



```python
VendorDE.ModExcel("Status", 3, "Busy")
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    ~\AppData\Local\Temp\ipykernel_19840\3428613633.py in <module>
    ----> 1 VendorDE.ModExcel("Status", 3, "Busy")
    

    TypeError: ModExcel() takes 3 positional arguments but 4 were given


For the `ModExcel` method there's an additional validation, namely the validation of keys in order to limit the keys for which you can modify the values. Modifiable keys can be checked by running `vd.VendorData.Keys`
<div class="alert alert-danger">
You can only modify one value for one key.
</div>


```python
vd.VendorData.Keys
```




    ['E-mail', 'CAT Tool', 'Word Rate', 'Status']



If you try to modify any other key you will get an error message:


```python
VendorDE.ModExcel("Vendor", "John Doe")
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    ~\AppData\Local\Temp\ipykernel_19840\1799726010.py in <module>
    ----> 1 VendorDE.ModExcel("Vendor", "John Doe")
    

    ~\OneDrive\Documenten\School\PostgraduaatTranslationTechnology\IntroductionToPython\Final_Assignment1\vendor_data.py in ModExcel(self, Key, NewValue)
        273             ExcelRecordsDf = pd.read_excel(FileName)
        274             if not Key in self.Keys:
    --> 275                 raise ValueError("Invalid key, run 'VendorData.Keys' to see options.")
        276 
        277             VendorRow = ExcelRecordsDf[ExcelRecordsDf.Vendor == self.VendorName]
    

    ValueError: Invalid key, run 'VendorData.Keys' to see options.



```python
VendorDE.ModExcel("Target Language", "Croatian")
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    ~\AppData\Local\Temp\ipykernel_19840\3386871677.py in <module>
    ----> 1 VendorDE.ModExcel("Target Language", "Croatian")
    

    ~\OneDrive\Documenten\School\PostgraduaatTranslationTechnology\IntroductionToPython\Final_Assignment1\vendor_data.py in ModExcel(self, Key, NewValue)
        273             ExcelRecordsDf = pd.read_excel(FileName)
        274             if not Key in self.Keys:
    --> 275                 raise ValueError("Invalid key, run 'VendorData.Keys' to see options.")
        276 
        277             VendorRow = ExcelRecordsDf[ExcelRecordsDf.Vendor == self.VendorName]
    

    ValueError: Invalid key, run 'VendorData.Keys' to see options.


We will now delete the file we generated during this tutorial so that when you go through it again, you can have a fresh start.


```python
import os
os.remove(".\Tutorial_English.xlsx")
```

Now you know the different functionalities of the script vendor__data.py and what triggers which error. Hopefully you can use this script in your daily life as a translation project manager. Have fun!

## Running `vendor_data.py`
The script can also be run on its own. The script takes two optional arguments:
- `-a` or `--add` allows the user to add a new vendor to an excel file (existing or new);
- `-m` or `--modify` allows the user to modify a vendor in an existing excel file;
The same validation is done as if you would import this script as a module. TypeErrors do not cause the prompts to stop but instead you get asked the same question again, ValueErrors do break off the code.

We'll begin with writing data to a brand new excel file by providing a new project name and source language, i.e. not Example and not English since an excel file already exists for this project.


```python
%run vendor_data.py -a
```

    What is the project name? Example
    What is the source language? Dutch
    What's the vendor's name? John Doe
    Into which language will the vendor translate? English
    What is the vendor's email address? 
    What is the vendor's word rate in EUR? Should be between 0.01 and 0.15. If higher, choose another vendor. 
    In which tool will the vendor be working?* XTM
    * Trados Studio
    * MemoQ
    * Memsource
    
    True or False: Is this vendor a preferred vendor? If neither, leave blank. 
    Are you done? yes
    Do you want to add this vendor to the excel file? yes
    The file Example_Dutch.xlsx is correctly created and the vendor John Doe was added.
    

You can also append a new vendor to the existing `Example_English.xlsx` file by providing `Example` as the project name and `English` as the source language. Again, the code does not check if a vendor already exists in the excel file, so you should add a vendor only once.

<div class="alert alert-danger">
You can only modify one value for one key.
</div>


```python
%run vendor_data.py -a
```

    What is the project name? Example
    What is the source language? English
    What's the vendor's name? Thomas Zwiebel
    Into which language will the vendor translate? German
    What is the vendor's email address? th.zwiebel@gmail.com
    What is the vendor's word rate in EUR? Should be between 0.01 and 0.15. If higher, choose another vendor. 0.08
    In which tool will the vendor be working?* XTM
    * Trados Studio
    * MemoQ
    * Memsource
    MemoQ
    True or False: Is this vendor a preferred vendor? If neither, leave blank. False
    Are you done? yes
    Do you want to add this vendor to the excel file? yes
    The vendor Thomas Zwiebel was added to Example_English.xlsx.
    

Just like when importing the script, it is possible to leave the following data blank:
- The vendor's email address
- The vendors word rate
- The tool in which the vendor will be working
- Whether or not the vendor is a preferred vendor

We'll append another vendor to the `Example_English` file:


```python
%run vendor_data.py -a
```

    What is the project name? Example
    What is the source language? English
    What's the vendor's name? Joao Felix
    Into which language will the vendor translate? Portuguese
    What is the vendor's email address? 
    What is the vendor's word rate in EUR? Should be between 0.01 and 0.15. If higher, choose another vendor. 
    In which tool will the vendor be working?* XTM
    * Trados Studio
    * MemoQ
    * Memsource
    
    True or False: Is this vendor a preferred vendor? If neither, leave blank. 
    Are you done? yes
    Do you want to add this vendor to the excel file? yes
    The vendor Joao Felix was added to Example_English.xlsx.
    

Since we're using pyipinputplus we can already avoid some errors by:
- using the built in type validation of the package by using `pyip.inputStr` or `pyip.inputFloat`, so that the user is forced to put in a valid data type
- using the Menu option to limit the choices, for example for the CAT Tools
In the background the same validation is run as when you import this script as a module. To see which kind of validation is done, please go to `Validation` above.

It is also possible to modify existing vendors. The user has to provide the project name and the source language, and is then further asked some questions regarding the vendor they want to modify:


```python
%run vendor_data.py -m
```

    What is the name of the project that the vendor you want to modify works on? Example
    What is the source language? English
    These are the vendor's already in the database: 
    0: Elmo Geeraerts
    1: Jean De Gaule
    2: Emanuel De la Banda
    3: Thomas Zwiebel
    4: Joao Felix
    Enter the index of the vendor you want to modify: 0
    What is the vendor's e-mail? geeraerts@me.com
    What is the vendor's word rate? Should be between 0.01 and 0.15. If higher, choose another vendor. 0.10
    In which tool will the vendor be working?* XTM
    * Trados Studio
    * MemoQ
    * Memsource
    Trados Studio
    What is the vendor's new status? * Preferred
    * Back-up
    * Potential
    Preferred
    Are you done? yes
    This vendor is modified correctly.
    

The vendor in the excel file should now be modified.

Now you are totally ready to use this script and resolve any issues that might pop up! Hopefully this script makes your life as a translation project manager easier! Have fun!

### Docstrings
The script is completely documented with docstrings in order to ensure that the script is correclty used.
You can read these docstrings by calling one of the following functions if you have imported the script as a module:
```python
help(vd)
```
OR
```python
?vd
```
OR
```python
vd.__doc__
```

You can also read the documentation for the script if you run this code:
```python
%run vendor_data.py --help
```
OR
```python
%run vendor_data.py --h
```
