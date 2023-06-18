# The two classes
Below, you'll find the two classes described in `README.md`. Make their respective cells run to initialise the classes.


```python
import datetime

"""This script gives a translation agency an overview of all its projects.
"""

class Project:

    def __init__(
        self,
        title,
        client,
        source,
        target,
        words,
        start,
        deadline,
        price,
        tm,
        translator = 'internal',
        reviewer = 'internal',
        status = 'created',
        domain = ''):
        """Initialises an object of the Project class, a class that represents a translation project of a translation agency.
        
            Args:
                title (str): Title of the project (typically the title of the source document, or the overall title the agency gave the project if there's more than one document to be translated).
                client (str): Client who ordered the translation.
                source (str): Language of the source document(s) (document(s) to be translated).
                target (str): Language of the target document(s) (translation(s)).
                words (int): Word count of the source document(s).
                start (str): Project's start date in ISO format (YYYY-MM-DD).
                deadline (str): Project's deadline in ISO format (YYYY-MM-DD).
                price (float): Total price invoiced to the client (excl. VAT).
                tm (bool): Whether a translation memory is available for this project.
                translator (string, optional): Translator assigned to the project. Defaults to 'internal'.
                reviewer (string, optional): Reviewer assigned to the project. Defaults to 'internal'.
                status (string, optional): Current project status inside the agency's workflow. Defaults to 'created'.
                domain (str, optional): Overall domain to which the project belongs. Defaults to an empty string.
        
            Attributes:
                title (str): Title of the project (typically the title of the source document, or the overall title the agency gave the project if there's more than one document to be translated).
                client (str): Client who ordered the translation.
                source (str): Language of the source document(s) (document(s) to be translated).
                target (str): Language of the target document(s) (translation(s)).
                words (int): Word count of the source document(s).
                start (str): Project's start date in ISO format (YYYY-MM-DD).
                deadline (str): Project's deadline in ISO format (YYYY-MM-DD).
                price (float): Total price invoiced to the client (excl. VAT).
                tm (bool): Whether a translation memory is available for this project.
                translator (string, optional): Translator assigned to the project.
                reviewer (string, optional): Reviewer assigned to the project.
                status (string, optional): Current project status inside the agency's workflow.
                domain (str): Overall domain to which the project belongs.
                today (date): Date of the day where the script is run.
                st (date): Project's start date, turned from an ISO-formatted string into a date.
                dl (date): Project's deadline, turned from an ISO-formatted string into a date.
                daysleft (timedelta): Time left until the project's deadline.
                length (timedelta): Total time allocated to the project.
                rate (float): Project's word rate.
                efficiency (float): Number of words to be translated or revised per day to meet the deadline (assuming a five-day workweek).
            
            Raises:
                TypeError: If 'title' is not a string.
                TypeError: If 'client' is not a string.
                TypeError: If 'source' is not a string.
                TypeError: If 'target' is not a string.
                TypeError: If 'words' is not an integer.
                TypeError: If 'start' is not a string.
                ValueError: If 'start' does not follow the pattern 4 digits-2 digits-2 digits.
                TypeError: If 'deadline' is not a string.
                ValueError: If 'deadline' does not follow the pattern 4 digits-2 digits-2 digits.
                TypeError: If 'price' is not a float.
                TypeError: If 'tm' is not a boolean.
                TypeError: If 'translator' is not a string.
                TypeError: If 'reviewer' is not a string.
                TypeError: If 'status' is not a string.
                ValueError: If 'status' is not a label in the agency workflow: created, in translation, in revision, delivered, delayed, cancel(l)ed.
                TypeError: If 'domain' is not a string.
        """
        if type(title) != str:
            raise TypeError("The title must be a string.")
        else:
            self.title = title
        if type(client) != str:
            raise TypeError("The client name must be a string.")
        else:
            self.client = client
        if type(source) != str:
            raise TypeError("The source language must be a string.")
        else:
            self.source = source
        if type(target) != str:
            raise TypeError("The target langague must be a string.")
        else:
            self.target = target
        if type(words) != int:
            raise TypeError("The word count must be an integer.")
        else:
            self.words = words
        if type(start) != str:
            raise TypeError("The start date must be provided as a string.")
        try:
            self.st = datetime.date.fromisoformat(start)
        except:
            raise TypeError("The start date must be provided in ISO format")
        else:
            self.start = start
        if type(deadline) != str:
            raise TypeError("The deadline must be provided as a string.")
        try:
            self.dl = datetime.date.fromisoformat(deadline)
        except:
            raise TypeError("The deadline must be provided in ISO format")
        else:
            self.deadline = deadline
        if type(price) != float:
            raise TypeError("The price must be a float.")
        else:
            self.price = price
        if type(tm) != bool:
            raise TypeError("The TM availability must be a boolean.")
        else:
            self.tm = tm
        if type(translator) != str and type(translator) != Freelancer:
            raise TypeError("The translator's name must be a string or an entry in our freelancer database.")
        elif translator == '':
            self.translator = "internal"
        else:
            self.translator = translator
        if type(reviewer) != str and type(reviewer) != Freelancer:
            raise TypeError("The reviewer's name must be a string or an entry in our freelancer database.")
        elif reviewer == '':
            self.reviewer = "internal"
        else:
            self.reviewer = reviewer
        if type(status) != str:
            raise TypeError("The status must be a string.")
        elif status == '':
            self.status = "created"
        elif not status.lower() in ["created",
                                     "in translation",
                                     "in revision",
                                     "delivered",
                                     "delayed",
                                     "cancelled",
                                     "canceled"]:
            raise ValueError("Please pick a status from the workflow: created, in translation, in revision, delivered, delayed or cancelled.")
        else:
            self.status = status
        if type(domain) != str:
            raise TypeError("The domain must be a string.")
        else:
            self.domain = domain
                
        today = datetime.date.today()
        self.daysleft = self.dl - today
        self.length = self.dl - self.st
        self.rate = self.price/self.words
        self.efficiency = words/((5/7)*self.length.days)

    def days_left(self):
        """Displays how many days remain until the project deadline.
        
        Args:
            None
            
        Returns:
            str: A message informing the user that the deadline has been exceeded already if the deadline is in the past.
            str: A message informing the user of the number of days left until the deadline if the deadline is not in the past.
        """
        if self.dl < datetime.date.today():
            return f"The deadline has been exceeded already."
        else:
            return f"There are {self.daysleft.days} days left until the deadline."
    
    def project_length(self):
        """Displays the total number of days allocated to the project.
        
        Args:
            None
        
        Returns:
            str: The total number of days allocated to the project.
        """
        return f"{self.length.days} days"
    
    def __str__(self):
        # defines the print behaviour: returns a text providing the main information about the project
        sent_1 = f"{self.title} is a translation for {self.client} from {self.source} into {self.target}."
        if self.translator.lower() == "internal" and self.reviewer.lower() == "internal":
            sent_2 = f"Both the translator and the reviewer are agency collaborators."
        elif self.translator.lower() == "internal" and self.reviewer.lower() != "internal":
            sent_2 = f"The translator is an agency collaborator and the reviewer is {self.reviewer}."
        elif self.translator.lower() != "internal" and self.reviewer.lower() == "internal":
            sent_2 = f"The translator is {self.translator} and the reviewer is an agency collaborator."
        else:
            sent_2 = f"The translator is {self.translator} and the reviewer is {self.reviewer}."
        # this if-statement considers whether a domain was added
        if len(self.domain) > 0:
            sent_3 = f"The domain is: {self.domain}."
        else:
            sent_3 = "The domain is unspecified." # if no domain was added, the text mentions it
        sent_4 = f"It's {self.words} words long, with a rate of {round(self.rate, 2)} € per word." #the word rate is rounded to two decimal places to avoid cumbersomely long numbers
        # this if-statement considers whether the deadline is in the past
        if self.dl < datetime.date.today():
            sent_5 = f"It started on {self.st} and was due on {self.dl}, so {self.length.days} days were foreseen for it. To meet the deadline, {round(self.efficiency)} words needed to be translated or revised per day." # the efficiency is rounded to units because you can't translate a fraction of a word anyway
        else:
            sent_5 = f"It started on {self.st} and is due on {self.dl}, so {self.length.days} days are foreseen for it, of which {self.daysleft.days} left. To meet the deadline, {round(self.efficiency)} words need to be translated or revised per day."
        # this if-statement considers whether there is a translation memory for the project
        sent_6 = f"There is {'a' if self.tm else 'no'} translation memory."
        sent_7 = f"The project is currently {self.status}."
        # print each sentence in a different line
        return "\n".join([sent_1, sent_2, sent_3, sent_4, sent_5, sent_6, sent_7])
```


```python
class Freelancer():

    def __init__(self, name, email, phone, ref, task, language):
        self.name = name
        self.email = email
        self.phone = phone
        self.ref = ref
        self.task = task
        self.language = language
    
    def function_with_kwargs(**kwargs):
        if "name" in kwargs:
            print(kwargs["name"])
        else:
            print("no name found")
    
    def __str__(self):
        sent_1 = f"{self.name} can be contacted via e-mail ({self.email}) or via phone ({self.phone})."
        sent_2 = f"{self.name}'s reference in our database is {self.ref}."
        sent_3 = f"{self.name} works as a {', '.join(self.task)} for {', '.join(self.language)}."
        return "\n".join([sent_1, sent_2, sent_3])
```

# Creating and using objects of the Project class

## Manually
It is possible to manually define objects of each class, meaning that you write out each mandatory attribute (and any optional attribute you want to make deviate from the default value), for example:


```python
project1 = Project("The project title", "some client", "FR", "EN", 10000, "2023-06-17", "2023-06-30", 3600.00, True)
```

In this case, the name of the object is "project1" and no optional attribute differs from the default value. But you can also change all the optional attributes:


```python
project2 = Project("A second project title", "another client", "NL", "DE", 7500, "2023-06-16", "2023-06-28", 3200.00, True, "Sibylle de Woot", "Mariana Montes", "in translation", "education")
```

Or only some of them:


```python
project3 = Project("Some other project title", "new client", "EN", "NL", 12000, "2023-06-15", "2023-06-30", 3800.00, True, reviewer = "Sibylle de Woot", domain = "healthcare")
```

Once an object has been created, you can use the various methods to
- Print an overview of all the project information:


```python
print(project1)
# The printing method is the only one that doesn't require you to specify that it's specific to the Project class, you simply need the name of the object
```

    The project title is a translation for some client from FR into EN.
    Both the translator and the reviewer are agency collaborators.
    The domain is unspecified.
    It's 10000 words long, with a rate of 0.36 € per word.
    It started on 2023-06-17 and is due on 2023-06-30, so 13 days are foreseen for it, of which 12 left. To meet the deadline, 1077 words need to be translated or revised per day.
    There is a translation memory.
    The project is currently created.



```python
print(project2)
```

    A second project title is a translation for another client from NL into DE.
    The translator is Sibylle de Woot and the reviewer is Mariana Montes.
    The domain is: education.
    It's 7500 words long, with a rate of 0.43 € per word.
    It started on 2023-06-16 and is due on 2023-06-28, so 12 days are foreseen for it, of which 10 left. To meet the deadline, 875 words need to be translated or revised per day.
    There is a translation memory.
    The project is currently in translation.



```python
print(project3)
```

    Some other project title is a translation for new client from EN into NL.
    The translator is an agency collaborator and the reviewer is Sibylle de Woot.
    The domain is: healthcare.
    It's 12000 words long, with a rate of 0.32 € per word.
    It started on 2023-06-15 and is due on 2023-06-30, so 15 days are foreseen for it, of which 12 left. To meet the deadline, 1120 words need to be translated or revised per day.
    There is a translation memory.
    The project is currently created.


- Find out how much time is left until the deadline:


```python
Project.days_left(project1)
# To use any other class method, you need to use the format "Class.method(object)"
```




    'There are 12 days left until the deadline.'



- Find out how many days are foreseen in total for the project:


```python
Project.project_length(project1)
```




    '13 days'



Attributes can also be retrieved separately, with `object.attribute`, for example


```python
project1.title
```




    'The project title'




```python
project1.start
```




    '2023-06-17'




```python
project1.length
```




    datetime.timedelta(days=13)



As you can see, the value of the attribute "length" isn't very user-friendly, as it is a timedelta computed with the datetime module. That is the reason why the method `project_length` was created, to display the attribute in a more readable way. Another user-friendely ways to display the project length is by printing the attribute, rather than simply retrieving it:


```python
print(project1.length)
```

    13 days, 0:00:00


As you can see, the project length is calculated to the second here. For now, that's not useful, but when a future update allows PMs to specify the start and end time, it will be.

So, feeding the project information into an object of the `Project` class makes for easy information retrieval and allows the PM to generate a clear global overview of the project in full sentences. However, especially with manual information input, issues can occur when the user makes a typo, or inputs the wrong type of variable. To counter those issues, validation was integrated into the `Project` class. Any wrong variable type raises an error, and the user is asked to use the right variable type.

Say, for example, that I forget that the price needs to be a float (i.e. a decimal number):


```python
project4 = Project("Yet another title", "another client", "FR", "NL", 8000, "2023-06-16", "2023-06-28", 3300, True, "Sibylle de Woot", "Mariana Montes", "in translation", "technical")
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Cell In[15], line 1
    ----> 1 project4 = Project("Yet another title", "another client", "FR", "NL", 8000, "2023-06-16", "2023-06-28", 3300, True, "Sibylle de Woot", "Mariana Montes", "in translation", "technical")


    Cell In[1], line 117, in Project.__init__(self, title, client, source, target, words, start, deadline, price, tm, translator, reviewer, status, domain)
        115     self.deadline = deadline
        116 if type(price) != float:
    --> 117     raise TypeError("The price must be a float.")
        118 else:
        119     self.price = price


    TypeError: The price must be a float.


As you can see, the script informs me that the price must be a float. Now, let's say that my numbers are correct, but that I didn't write my dates in ISO format:


```python
project4 = Project("Yet another title", "another client", "FR", "NL", 8000, "23-06-16", "23-06-28", 3300.00, True, "Sibylle de Woot", "Mariana Montes", "in translation", "technical")
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    Cell In[1], line 103, in Project.__init__(self, title, client, source, target, words, start, deadline, price, tm, translator, reviewer, status, domain)
        102 try:
    --> 103     self.st = datetime.date.fromisoformat(start)
        104 except:


    ValueError: Invalid isoformat string: '23-06-16'

    
    During handling of the above exception, another exception occurred:


    TypeError                                 Traceback (most recent call last)

    Cell In[16], line 1
    ----> 1 project4 = Project("Yet another title", "another client", "FR", "NL", 8000, "23-06-16", "23-06-28", 3300.00, True, "Sibylle de Woot", "Mariana Montes", "in translation", "technical")


    Cell In[1], line 105, in Project.__init__(self, title, client, source, target, words, start, deadline, price, tm, translator, reviewer, status, domain)
        103     self.st = datetime.date.fromisoformat(start)
        104 except:
    --> 105     raise TypeError("The start date must be provided in ISO format")
        106 else:
        107     self.start = start


    TypeError: The start date must be provided in ISO format


While both dates are wrong, only the error with the start date is raised. That's because the script stops at the first detected error. However, if I only correct one and not the other, it will raise the error in the deadline:


```python
project4 = Project("Yet another title", "another client", "FR", "NL", 8000, "2023-06-16", "23-06-28", 3300.00, True, "Sibylle de Woot", "Mariana Montes", "in translation", "technical")
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    Cell In[1], line 111, in Project.__init__(self, title, client, source, target, words, start, deadline, price, tm, translator, reviewer, status, domain)
        110 try:
    --> 111     self.dl = datetime.date.fromisoformat(deadline)
        112 except:


    ValueError: Invalid isoformat string: '23-06-28'

    
    During handling of the above exception, another exception occurred:


    TypeError                                 Traceback (most recent call last)

    Cell In[17], line 1
    ----> 1 project4 = Project("Yet another title", "another client", "FR", "NL", 8000, "2023-06-16", "23-06-28", 3300.00, True, "Sibylle de Woot", "Mariana Montes", "in translation", "technical")


    Cell In[1], line 113, in Project.__init__(self, title, client, source, target, words, start, deadline, price, tm, translator, reviewer, status, domain)
        111     self.dl = datetime.date.fromisoformat(deadline)
        112 except:
    --> 113     raise TypeError("The deadline must be provided in ISO format")
        114 else:
        115     self.deadline = deadline


    TypeError: The deadline must be provided in ISO format


The way the script detects whether or not the date format is correct, is by trying to turn the string I inputted into an actual date with the datetime module. Because if that, it can also catch some errors if I provide the date in YYYY-DD-MM format, rather than YYYY-MM-DD:


```python
project4 = Project("Yet another title", "another client", "FR", "NL", 8000, "2023-16-06", "2023-06-28", 3300.00, True, "Sibylle de Woot", "Mariana Montes", "in translation", "technical")
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    Cell In[1], line 103, in Project.__init__(self, title, client, source, target, words, start, deadline, price, tm, translator, reviewer, status, domain)
        102 try:
    --> 103     self.st = datetime.date.fromisoformat(start)
        104 except:


    ValueError: month must be in 1..12

    
    During handling of the above exception, another exception occurred:


    TypeError                                 Traceback (most recent call last)

    Cell In[18], line 1
    ----> 1 project4 = Project("Yet another title", "another client", "FR", "NL", 8000, "2023-16-06", "2023-06-28", 3300.00, True, "Sibylle de Woot", "Mariana Montes", "in translation", "technical")


    Cell In[1], line 105, in Project.__init__(self, title, client, source, target, words, start, deadline, price, tm, translator, reviewer, status, domain)
        103     self.st = datetime.date.fromisoformat(start)
        104 except:
    --> 105     raise TypeError("The start date must be provided in ISO format")
        106 else:
        107     self.start = start


    TypeError: The start date must be provided in ISO format


When trying to convert the string into a date, the script runs into a problem, as there is no sixteenth month in the year, which leads it to ask for an ISO-formatted date. This is handy, but has its limitations for dates until the twelvth of the month, in which day and month can me inverted and still yield a valid ISO-formatted date. Validation is a useful feature to weed out many mistakes, but it's no miracle solution and in the end it's up to the user to ensure that they use correct information.

A last "special" type of validation used in the `Project` class concerns the attribute `status`. To make sure everyone is on the same page concerning project progress, only labels from the agency workflow are allowed for this attribute, namely:
- created,
- in translation,
- in revision,
- delivered,
- delayed,
- cancel(l)ed.

If a user tries to invent their own labels, they will receive a request to use a status in the agency workflow:


```python
project4 = Project("Yet another title", "another client", "FR", "NL", 8000, "2023-06-16", "2023-06-28", 3300.00, True, "Sibylle de Woot", "Mariana Montes", "ongoing", "technical")
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    Cell In[19], line 1
    ----> 1 project4 = Project("Yet another title", "another client", "FR", "NL", 8000, "2023-06-16", "2023-06-28", 3300.00, True, "Sibylle de Woot", "Mariana Montes", "ongoing", "technical")


    Cell In[1], line 147, in Project.__init__(self, title, client, source, target, words, start, deadline, price, tm, translator, reviewer, status, domain)
        139     self.status = "created"
        140 elif not status.lower() in ["created",
        141                              "in translation",
        142                              "in revision",
       (...)
        145                              "cancelled",
        146                              "canceled"]:
    --> 147     raise ValueError("Please pick a status from the workflow: created, in translation, in revision, delivered, delayed or cancelled.")
        148 else:
        149     self.status = status


    ValueError: Please pick a status from the workflow: created, in translation, in revision, delivered, delayed or cancelled.


A last point you may have noticed is that, while the default value when no domain is provided is an empty string, the default value for `translator` and `reviewer` is "internal" and even an empty string is turned into "internal", even though it does not appear as such in the printed text with project information (and an empty string can be turned into "an agency collaborator" just as easily as a string containing "internal"). The reason is that, if the user wants to retrieve the value of the attribute `translator`, "internal" is much clearer than an empty string, which looks like missing information and which requires more reflexion on the part of the user to understand that it's empty because the project was assigned to an agency collaborator.


```python
project1.translator
```




    'internal'



## Using files

Since creating each instance of the `Project` class manually would be both cumbersome and *very* time-consuming, a way to speed up the process is to export the project information to a file and use that file to feed the information into the `Project` class. In this example, all the project information was exported as a list of dictionaries (one dictionary per project) in the json-file called `projects_db.json`. Bear in mind that, for the system to find the file, it needs to be in the folder you're running the script from (otherwise you need to use the full path to the file, but we'll not go into that here).

If all you want is an overview of all the projects printed as text, you can go through the dictionaries one by one and print their information, without actually creating `Project` objects:


```python
import json # we'll need the json module to use the file
# store the file's content in a variable:
projects = 'projects_db.json' # assign filename to a string variable
with open(projects, encoding = 'utf-8') as f:
    # open file and use json to parse it
    projects = json.load(f) # projects is now a list of dictionaries.   

# go through each of the items in the list
for project in projects:
    # create a Project instance with title, client, source, target, words, start, deadline, price, tm, translator, reviewer, status and domain
    my_project = Project(project['title'], project['client'], project['source'], project['target'], project['words'], project['start'], project['deadline'], project['price'], project['tm'], project['translator'], project['reviewer'], project['status'], project['domain'])
    # print the project information
    print(my_project)
    
    # print a separating line between translations
    print('----')
```

    La polyarthrite rhumatoïde et autres rhumatismes inflammatoires is a translation for Reuma vzw from FR into NL.
    Both the translator and the reviewer are agency collaborators.
    The domain is: healthcare.
    It's 2142 words long, with a rate of 0.33 € per word.
    It started on 2020-10-02 and was due on 2020-10-15, so 13 days were foreseen for it. To meet the deadline, 231 words needed to be translated or revised per day.
    There is no translation memory.
    The project is currently delivered.
    ----
    Handboek voor studentenvertegenwoordigers is a translation for KU Leuven from NL into EN.
    The translator is sdw and the reviewer is an agency collaborator.
    The domain is: education.
    It's 7237 words long, with a rate of 0.37 € per word.
    It started on 2023-02-21 and was due on 2023-03-07, so 14 days were foreseen for it. To meet the deadline, 724 words needed to be translated or revised per day.
    There is a translation memory.
    The project is currently delayed.
    ----
    User Guide MFPs is a translation for UGent from EN into NL.
    The translator is an agency collaborator and the reviewer is mm.
    The domain is unspecified.
    It's 1852 words long, with a rate of 0.4 € per word.
    It started on 2023-04-12 and was due on 2023-04-15, so 3 days were foreseen for it. To meet the deadline, 864 words needed to be translated or revised per day.
    There is a translation memory.
    The project is currently cancelled.
    ----
    Guide de Bruxelles is a translation for Foodies from NL into FR.
    The translator is evdl and the reviewer is sdw.
    The domain is unspecified.
    It's 11500 words long, with a rate of 0.35 € per word.
    It started on 2023-05-06 and is due on 2023-06-30, so 55 days are foreseen for it, of which 12 left. To meet the deadline, 293 words need to be translated or revised per day.
    There is no translation memory.
    The project is currently in revision.
    ----


If we don't only want a printed overview of all the projects, but want to be able to retrieve information from specific attributes or use the other methods, we'll need to create objects of the `Project` class. Before we come to that, however, you might have noticed that instead of a name in Firstname Lastname format, freelancers are now referred to with abbreviations. Those are their references in the agency freelancer database and they are used to make the link between the `Project` and the `Freelancer` classes. So, let's first have a look at `Freelancer`.

# Creating and using objects of the Freelancer class

## Manually
While the class contents (described in `README.md`) differ from `Projects`, the `Freelancer` class works the same way. Objects can be instantiated manually, for example:


```python
freelancer1 = Freelancer("Sibylle de Woot", "sdewoot@mail.be", "+32 486 12 34 56", "sdw", ["translator", "reviewer"], ["FR", "NL", "EN", "DE"])
```

Again, you can then print a text displaying all the information:


```python
print(freelancer1)
```

    Sibylle de Woot can be contacted via e-mail (sdewoot@mail.be) or via phone (+32 486 12 34 56).
    Sibylle de Woot's reference in our database is sdw.
    Sibylle de Woot works as a translator, reviewer for FR, NL, EN, DE.


Or retrieve specific information through the attributes:


```python
freelancer1.name
```




    'Sibylle de Woot'




```python
freelancer1.language
```




    ['FR', 'NL', 'EN', 'DE']



One limitation of the Freelancer class is its lack of validation. As a result, I can input virtually anything in any attribute: I could mix up information (for example exchange name and phone number), input the phone number as an integer rather than a string, not use the right format (for example not use the international version of the phone number), only give the freelancer's first name... Anything goes:


```python
freelancer2 = Freelancer("Sibylle", 486123456, "sdewoot@email.be", "sdw", "translator & reviewer", "French, Dutch, English and German")
```


```python
print(freelancer2)
```

    Sibylle can be contacted via e-mail (486123456) or via phone (sdewoot@email.be).
    Sibylle's reference in our database is sdw.
    Sibylle works as a t, r, a, n, s, l, a, t, o, r,  , &,  , r, e, v, i, e, w, e, r for F, r, e, n, c, h, ,,  , D, u, t, c, h, ,,  , E, n, g, l, i, s, h,  , a, n, d,  , G, e, r, m, a, n.



```python
freelancer2.email
```




    486123456




```python
freelancer2.language
```




    'French, Dutch, English and German'



As you can see, the result is useless, unstructured and completely nonsensical. Hence why validation is a priority in the coming updates.

## Using files
Like the `Project` class, the Freelancer class can go through a list (in this example, based on the file `freelancers_db.json`) and print each freelancer's information:


```python
freelancers = 'freelancers_db.json'
with open(freelancers, encoding = 'utf-8') as f:
    freelancers = json.load(f)

for freelancer in freelancers:
    my_freelancer = Freelancer(freelancer['name'], freelancer['email'], freelancer['phone'], freelancer['ref'], freelancer['task'], freelancer['language'])
    print(my_freelancer)
    
    print('----')
```

    Sibylle de Woot can be contacted via e-mail (sdewoot@email.be) or via phone (+32 485 12 34 56).
    Sibylle de Woot's reference in our database is sdw.
    Sibylle de Woot works as a translator, reviewer for FR, NL, EN, DE.
    ----
    Mariana Montes can be contacted via e-mail (mariana.montes@company.com) or via phone (+32 487 98 76 54).
    Mariana Montes's reference in our database is mm.
    Mariana Montes works as a reviewer for ES, EN.
    ----
    Emily van der Londen can be contacted via e-mail (evdl@translation.net) or via phone (+32 486 19 28 37).
    Emily van der Londen's reference in our database is evdl.
    Emily van der Londen works as a translator for NL, EN, FR.
    ----


But separate overviews of projects and freelancers aren't what interests us. What we're looking for, is to merge both in usable Python objects. So, let's see how that works.

# Linking the Project and Freelancer class
For this, we need to slightly edit the `Project` class to make sure that the freelancer's name is displayed in the printed out project information, rather than the full text containing the freelancer information. We replace `{self.translator}` and `{self.reviewer}` by `{self.translator.name}` and `{self.reviewer.name}`.


```python
"""This script gives a translation agency an overview of all its projects.
"""

class Project:

    def __init__(
        self,
        title,
        client,
        source,
        target,
        words,
        start,
        deadline,
        price,
        tm,
        translator = 'internal',
        reviewer = 'internal',
        status = 'created',
        domain = ''):
        """Initialises an object of the Project class, a class that represents a translation project of a translation agency.
        
            Args:
                title (str): Title of the project (typically the title of the source document, or the overall title the agency gave the project if there's more than one document to be translated).
                client (str): Client who ordered the translation.
                source (str): Language of the source document(s) (document(s) to be translated).
                target (str): Language of the target document(s) (translation(s)).
                words (int): Word count of the source document(s).
                start (str): Project's start date in ISO format (YYYY-MM-DD).
                deadline (str): Project's deadline in ISO format (YYYY-MM-DD).
                price (float): Total price invoiced to the client (excl. VAT).
                tm (bool): Whether a translation memory is available for this project.
                translator (string, optional): Translator assigned to the project. Defaults to 'internal'.
                reviewer (string, optional): Reviewer assigned to the project. Defaults to 'internal'.
                status (string, optional): Current project status inside the agency's workflow. Defaults to 'created'.
                domain (str, optional): Overall domain to which the project belongs. Defaults to an empty string.
        
            Attributes:
                title (str): Title of the project (typically the title of the source document, or the overall title the agency gave the project if there's more than one document to be translated).
                client (str): Client who ordered the translation.
                source (str): Language of the source document(s) (document(s) to be translated).
                target (str): Language of the target document(s) (translation(s)).
                words (int): Word count of the source document(s).
                start (str): Project's start date in ISO format (YYYY-MM-DD).
                deadline (str): Project's deadline in ISO format (YYYY-MM-DD).
                price (float): Total price invoiced to the client (excl. VAT).
                tm (bool): Whether a translation memory is available for this project.
                translator (string, optional): Translator assigned to the project.
                reviewer (string, optional): Reviewer assigned to the project.
                status (string, optional): Current project status inside the agency's workflow.
                domain (str): Overall domain to which the project belongs.
                today (date): Date of the day where the script is run.
                st (date): Project's start date, turned from an ISO-formatted string into a date.
                dl (date): Project's deadline, turned from an ISO-formatted string into a date.
                daysleft (timedelta): Time left until the project's deadline.
                length (timedelta): Total time allocated to the project.
                rate (float): Project's word rate.
                efficiency (float): Number of words to be translated or revised per day to meet the deadline (assuming a five-day workweek).
            
            Raises:
                TypeError: If 'title' is not a string.
                TypeError: If 'client' is not a string.
                TypeError: If 'source' is not a string.
                TypeError: If 'target' is not a string.
                TypeError: If 'words' is not an integer.
                TypeError: If 'start' is not a string.
                ValueError: If 'start' does not follow the pattern 4 digits-2 digits-2 digits.
                TypeError: If 'deadline' is not a string.
                ValueError: If 'deadline' does not follow the pattern 4 digits-2 digits-2 digits.
                TypeError: If 'price' is not a float.
                TypeError: If 'tm' is not a boolean.
                TypeError: If 'translator' is not a string.
                TypeError: If 'reviewer' is not a string.
                TypeError: If 'status' is not a string.
                ValueError: If 'status' is not a label in the agency workflow: created, in translation, in revision, delivered, delayed, cancel(l)ed.
                TypeError: If 'domain' is not a string.
        """
        if type(title) != str:
            raise TypeError("The title must be a string.")
        else:
            self.title = title
        if type(client) != str:
            raise TypeError("The client name must be a string.")
        else:
            self.client = client
        if type(source) != str:
            raise TypeError("The source language must be a string.")
        else:
            self.source = source
        if type(target) != str:
            raise TypeError("The target langague must be a string.")
        else:
            self.target = target
        if type(words) != int:
            raise TypeError("The word count must be an integer.")
        else:
            self.words = words
        if type(start) != str:
            raise TypeError("The start date must be provided as a string.")
        try:
            self.st = datetime.date.fromisoformat(start)
        except:
            raise TypeError("The start date must be provided in ISO format")
        else:
            self.start = start
        if type(deadline) != str:
            raise TypeError("The deadline must be provided as a string.")
        try:
            self.dl = datetime.date.fromisoformat(deadline)
        except:
            raise TypeError("The deadline must be provided in ISO format")
        else:
            self.deadline = deadline
        if type(price) != float:
            raise TypeError("The price must be a float.")
        else:
            self.price = price
        if type(tm) != bool:
            raise TypeError("The TM availability must be a boolean.")
        else:
            self.tm = tm
        if type(translator) != str and type(translator) != Freelancer:
            raise TypeError("The translator's name must be a string or an entry in our freelancer database.")
        elif translator == '':
            self.translator = "internal"
        else:
            self.translator = translator
        if type(reviewer) != str and type(reviewer) != Freelancer:
            raise TypeError("The reviewer's name must be a string or an entry in our freelancer database.")
        elif reviewer == '':
            self.reviewer = "internal"
        else:
            self.reviewer = reviewer
        if type(status) != str:
            raise TypeError("The status must be a string.")
        elif status == '':
            self.status = "created"
        elif not status.lower() in ["created",
                                     "in translation",
                                     "in revision",
                                     "delivered",
                                     "delayed",
                                     "cancelled",
                                     "canceled"]:
            raise ValueError("Please pick a status from the workflow: created, in translation, in revision, delivered, delayed or cancelled.")
        else:
            self.status = status
        if type(domain) != str:
            raise TypeError("The domain must be a string.")
        else:
            self.domain = domain
                
        today = datetime.date.today()
        self.daysleft = self.dl - today
        self.length = self.dl - self.st
        self.rate = self.price/self.words
        self.efficiency = words/((5/7)*self.length.days)

    def days_left(self):
        """Displays how many days remain until the project deadline.
        
        Args:
            None
            
        Returns:
            str: A message informing the user that the deadline has been exceeded already if the deadline is in the past.
            str: A message informing the user of the number of days left until the deadline if the deadline is not in the past.
        """
        if self.dl < datetime.date.today():
            return f"The deadline has been exceeded already."
        else:
            return f"There are {self.daysleft.days} days left until the deadline."
    
    def project_length(self):
        """Displays the total number of days allocated to the project.
        
        Args:
            None
        
        Returns:
            str: The total number of days allocated to the project.
        """
        return f"{self.length.days} days"
    
    def __str__(self):
        # defines the print behaviour: returns a text providing the main information about the project
        sent_1 = f"{self.title} is a translation for {self.client} from {self.source} into {self.target}."
        if self.translator == "internal" and self.reviewer == "internal":
            sent_2 = f"Both the translator and the reviewer are agency collaborators."
        elif self.translator == "internal" and self.reviewer != "internal":
            sent_2 = f"The translator is an agency collaborator and the reviewer is {self.reviewer.name}."
        elif self.translator != "internal" and self.reviewer == "internal":
            sent_2 = f"The translator is {self.translator.name} and the reviewer is an agency collaborator."
        else:
            sent_2 = f"The translator is {self.translator.name} and the reviewer is {self.reviewer.name}."
        # this if-statement considers whether a domain was added
        if len(self.domain) > 0:
            sent_3 = f"The domain is: {self.domain}."
        else:
            sent_3 = "The domain is unspecified." # if no domain was added, the text mentions it
        sent_4 = f"It's {self.words} words long, with a rate of {round(self.rate, 2)} € per word." #the word rate is rounded to two decimal places to avoid cumbersomely long numbers
        # this if-statement considers whether the deadline is in the past
        if self.dl < datetime.date.today():
            sent_5 = f"It started on {self.st} and was due on {self.dl}, so {self.length.days} days were foreseen for it. To meet the deadline, {round(self.efficiency)} words needed to be translated or revised per day." # the efficiency is rounded to units because you can't translate a fraction of a word anyway
        else:
            sent_5 = f"It started on {self.st} and is due on {self.dl}, so {self.length.days} days are foreseen for it, of which {self.daysleft.days} left. To meet the deadline, {round(self.efficiency)} words need to be translated or revised per day."
        # this if-statement considers whether there is a translation memory for the project
        sent_6 = f"There is {'a' if self.tm else 'no'} translation memory."
        sent_7 = f"The project is currently {self.status}."
        # print each sentence in a different line
        return "\n".join([sent_1, sent_2, sent_3, sent_4, sent_5, sent_6, sent_7])
```

First, we'll retrieve the freelancers' information from the json-file and save it as a list of dictionaries. Granted, we've already done so above, but as some people may have skipped directly to this part of the tutorial, we'll do it again here.


```python
with open('freelancers_db.json', 'r') as f:
    all_freelancers = {x['ref'] : x for x in json.load(f)} # the name of each dictionary is the value of the key "ref", so the freelancer's unique internal reference in the agency database
```

Then, we also read and save the project information as a dictionary. As mentioned above, the value of the "translator" and "reviewer" key are now internal references rather than names, which we can use to check whether the value of those keys (or attributes, once we instantiates objects of the `Project` class) correspond to a dictionary in our list `all_freelancers` (i.e. an entry in our freelancer database). If it is, the value of the attribute `translator` of our `Project` instance will not be a string, but an instance of the `Freelancer` class.


```python
with open('guide_bruxelles.json', 'r') as f2:
    guide_bruxelles_dict = json.load(f2)
    if 'translator' in guide_bruxelles_dict and guide_bruxelles_dict['translator'] in all_freelancers:
        guide_bruxelles_dict['translator'] = Freelancer(**all_freelancers[guide_bruxelles_dict['translator']])
    if 'reviewer' in guide_bruxelles_dict and guide_bruxelles_dict['reviewer'] in all_freelancers:
        guide_bruxelles_dict['reviewer'] = Freelancer(**all_freelancers[guide_bruxelles_dict['reviewer']])
    guide_bruxelles = Project(**guide_bruxelles_dict)

with open('handboek.json', 'r') as f3:
    handboek_dict = json.load(f3)
    if 'translator' in handboek_dict and handboek_dict['translator'] in all_freelancers:
        handboek_dict['translator'] = Freelancer(**all_freelancers[handboek_dict['translator']])
    if 'reviewer' in handboek_dict and handboek_dict['reviewer'] in all_freelancers:
        handboek_dict['reviewer'] = Freelancer(**all_freelancers[handboek_dict['reviewer']])
    handboek = Project(**handboek_dict)

with open('rhumatismes_inflammatoires.json', 'r') as f4:
    rhumatismes_inflammatoires_dict = json.load(f4)
    if 'translator' in rhumatismes_inflammatoires_dict and rhumatismes_inflammatoires_dict['translator'] in all_freelancers:
        rhumatismes_inflammatoires_dict['translator'] = Freelancer(**all_freelancers[rhumatismes_inflammatoires_dict['translator']])
    if 'reviewer' in rhumatismes_inflammatoires_dict and rhumatismes_inflammatoires_dict['reviewer'] in all_freelancers:
        rhumatismes_inflammatoires_dict['reviewer'] = Freelancer(**all_freelancers[rhumatismes_inflammatoires_dict['reviewer']])
    rhumatismes_inflammatoires = Project(**rhumatismes_inflammatoires_dict)

with open('user_guide.json', 'r') as f5:
    user_guide_dict = json.load(f5)
    if 'translator' in user_guide_dict and user_guide_dict['translator'] in all_freelancers:
        user_guide_dict['translator'] = Freelancer(**all_freelancers[user_guide_dict['translator']])
    if 'reviewer' in user_guide_dict and user_guide_dict['reviewer'] in all_freelancers:
        user_guide_dict['reviewer'] = Freelancer(**all_freelancers[user_guide_dict['reviewer']])
    user_guide = Project(**user_guide_dict)
```

Once that is done, we can print both the project information:


```python
print(guide_bruxelles)
print('----')
print(handboek)
print('----')
print(rhumatismes_inflammatoires)
print('----')
print (user_guide)
```

    Guide de Bruxelles is a translation for Foodies from NL into FR.
    The translator is Emily van der Londen and the reviewer is Sibylle de Woot.
    The domain is unspecified.
    It's 11500 words long, with a rate of 0.35 € per word.
    It started on 2023-05-06 and is due on 2023-06-30, so 55 days are foreseen for it, of which 12 left. To meet the deadline, 293 words need to be translated or revised per day.
    There is no translation memory.
    The project is currently in revision.
    ----
    Handboek voor studentenvertegenwoordigers is a translation for KU Leuven from NL into EN.
    The translator is Sibylle de Woot and the reviewer is an agency collaborator.
    The domain is: education.
    It's 7237 words long, with a rate of 0.37 € per word.
    It started on 2023-02-21 and was due on 2023-03-07, so 14 days were foreseen for it. To meet the deadline, 724 words needed to be translated or revised per day.
    There is a translation memory.
    The project is currently delayed.
    ----
    La polyarthrite rhumatoïde et autres rhumatismes inflammatoires is a translation for Reuma vzw from FR into NL.
    Both the translator and the reviewer are agency collaborators.
    The domain is: healthcare.
    It's 2142 words long, with a rate of 0.33 € per word.
    It started on 2020-10-02 and was due on 2020-10-15, so 13 days were foreseen for it. To meet the deadline, 231 words needed to be translated or revised per day.
    There is no translation memory.
    The project is currently delivered.
    ----
    User Guide MFPs is a translation for UGent from EN into NL.
    The translator is an agency collaborator and the reviewer is Mariana Montes.
    The domain is unspecified.
    It's 1852 words long, with a rate of 0.4 € per word.
    It started on 2023-04-12 and was due on 2023-04-15, so 3 days were foreseen for it. To meet the deadline, 864 words needed to be translated or revised per day.
    There is a translation memory.
    The project is currently cancelled.


The freelancer information can then be printed separately by asking to print the value of the `translator`/`reviewer` attribute.


```python
print(guide_bruxelles.translator)
```

    Emily van der Londen can be contacted via e-mail (evdl@translation.net) or via phone (+32 486 19 28 37).
    Emily van der Londen's reference in our database is evdl.
    Emily van der Londen works as a translator for NL, EN, FR.


The value of other `Project` attributes can be retrieved the usual way:


```python
guide_bruxelles.title
```




    'Guide de Bruxelles'




```python
guide_bruxelles.efficiency
```




    292.72727272727275




```python
Project.project_length(guide_bruxelles)
```




    '55 days'



And the freelancers' information can also be retrieved through the `Project` instance:


```python
guide_bruxelles.translator.name
```




    'Emily van der Londen'




```python
guide_bruxelles.reviewer.email
```




    'sdewoot@email.be'




```python
guide_bruxelles.translator.task
```




    ['translator']



# Conclusion
Hopefully, this script will make project management easier for many translation agencies. Of course, this is only version 1.0 and many updates, improvements and extra features are foreseen in the near to medium future, as you can see in the last section of `README.md`.
