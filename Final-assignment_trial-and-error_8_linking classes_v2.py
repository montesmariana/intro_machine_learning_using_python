#!/usr/bin/env python
# coding: utf-8

# # Import modules

# In[1]:


import datetime #datetime package to convert strings into dates, calculate time periods etc.
import re
import json


# # Freelancers

# In[12]:


class Freelancers:
    is_internal = False
    
    def __init__(self, name, email, phone, ref):
        self.name = name
        self.email = email
        self.phone = phone
        self.ref = ref
        
        self.task = set()
        self.language = set()
    
    def add_task(self, task):
        self.task.add(task)
    
    def add_language(self, language):
        self.language.add(language)
    
    def __str__(self):
        sent_1 = f"{self.name} can be contacted via e-mail ({self.email}) or via phone ({self.phone})."
        sent_2 = f"{self.name}'s ID in our database is {self.ref}."
        sent_3 = f"{self.name} works as a {', '.join(self.task)} for {', '.join(self.language)}."
        return "\n".join([sent_1, sent_2, sent_3])


# In[2]:


sdw = {
    'name' : 'Sibylle de Woot',
    'email' : 'sdewoot@email.be',
    'phone' : '+32 485 12 34 56',
    'ref' : 'sdw',
    'task' : [
        'translator',
        'reviewer'
    ],
    'language' : [
        'FR',
        'NL',
        'EN',
        'DE'
    ]
}
mm = {
    'name' : 'Mariana Montes',
    'email' : 'mariana.montes@company.com',
    'phone' : '+32 487 98 76 54',
    'ref' : 'mm',
    'task' : [
        'reviewer'
    ],
    'language' : [
        'ES',
        'EN'
    ]
}
evdl = {
    'name' : 'Emily van der Londen',
    'email' : 'evdl@translation.net',
    'phone' : '+32 486 19 28 37',
    'ref' : 'evdl',
    'task' : [
        'translator'
    ],
    'language' : [
        'NL',
        'EN',
        'FR'
    ]
}


# In[3]:


freelancers = [sdw, mm, evdl]


# In[6]:


with open('freelancers_db.json', 'w', encoding='utf-8') as f:
    json.dump(freelancers, f)


# ## Class instances from dictionary

# In[3]:


class Freelancer():
    def __init__(self, dictionary):

        for key, value in dictionary.items():
            setattr(self, key, value)
    
    def __str__(self):
        sent_1 = f"{self.name} can be contacted via e-mail ({self.email}) or via phone ({self.phone})."
        sent_2 = f"{self.name}'s ID in our database is {self.id}."
        sent_3 = f"{self.name} works as a {', '.join(self.task)} for {', '.join(self.language)}."
        return "\n".join([sent_1, sent_2, sent_3])

sdw = Freelancer(sdw_info)
mm = Freelancer(mm_info)
evdl = Freelancer(evdl_info)


# In[20]:


sdw.name


# In[21]:


sdw.task


# In[25]:


print(sdw)


# # Class instances with kwargs

# In[2]:


class Freelancer():

    def __init__(self, name, email, phone, ref):
        self.name = name
        self.email = email
        self.phone = phone
        self.ref = ref
        
        self.task = set()
        self.language = set()
    
    def add_task(self, task):
        self.task.add(task)
    
    def add_language(self, language):
        self.language.add(language)
    
    def function_with_kwargs(**kwargs):
        if "name" in kwargs:
            print(kwargs["name"])
        else:
            print("no name found")
    
    def __str__(self):
        sent_1 = f"{self.name} can be contacted via e-mail ({self.email}) or via phone ({self.phone})."
        sent_2 = f"{self.name}'s ID in our database is {self.id}."
        sent_3 = f"{self.name} works as a {', '.join(self.task)} for {', '.join(self.language)}."
        return "\n".join([sent_1, sent_2, sent_3])


# # Projects

# In[3]:


class Project:

    def __init__(self, title, client, source, target, words, start, deadline, price, tm, translator = 'internal', reviewer = 'internal', status = 'created', domain = ''):
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
        elif not re.match ("[0-9]{4}-[0-9]{2}-[0-9]{2}", start):
            raise ValueError("A valid start date must be provided in ISO format.")
        else:
            self.start = start
        if type(deadline) != str:
            raise TypeError("The deadline must be provided as a string.")
        elif not re.match ("[0-9]{4}-[0-9]{2}-[0-9]{2}", deadline):
            raise ValueError("A valid deadline must be provided in ISO format.")
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
        self.st = datetime.date.fromisoformat(start)
        self.dl = datetime.date.fromisoformat(deadline)
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
        # prints a text indicating how many days are left until the project deadline
        if self.dl < datetime.date.today():
            # if the deadline is in the past
            return f"The deadline has been exceeded already."
        else:
            # if the deadline is not in the past
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


# In[4]:


rhumatismes_inflammatoires = {
    'title' : 'La polyarthrite rhumatoïde et autres rhumatismes inflammatoires',
    'client' : 'Reuma vzw',
    'source' : 'FR',
    'target' : 'NL',
    'words' : 2131,
    'start' : '2020-09-24',
    'deadline' : '2020-10-15',
    'price' : 210.00,
    'tm' : False,
    'translator' : '',
    'reviewer' : '',
    'status' : '',
    'domain' : 'healthcare'
}
handboek = {
    'title' : 'Handboek voor studentenvertegenwoordigers',
    'client' : 'KU Leuven',
    'source' : 'NL',
    'target' : 'EN',
    'words' : 3654,
    'start' : '2023-02-21',
    'deadline' : '2023-03-02',
    'price' : 540.00,
    'tm' : True,
    'translator' : 'sdw',
    'reviewer' : '',
    'status' : 'delayed',    
    'domain' : 'education'
}
user_guide = {
    'title' : 'User Guide MFPs',
    'client' : 'UGent',
    'source' : 'EN',
    'target' : 'NL',
    'words' : 1852,
    'start' : '2023-04-12',
    'deadline' : '2023-04-14',
    'price' : 280.00,
    'tm' : True,
    'translator' : '',
    'reviewer' : 'mm',
    'status' : 'cancelled',
    'domain' : ''
}
guide_bruxelles = {
    'title' : 'Guide de Bruxelles',
    'client' : 'Foodies',
    'source' : 'NL',
    'target' : 'FR',
    'words' : 11500,
    'start' : '2023-04-06',
    'deadline' : '2023-05-27',
    'price' : 1610.00,
    'tm' : False,
    'translator' : 'evdl',
    'reviewer' : 'sdw',
    'status' : 'in revision',    
    'domain' : ''
}


# In[6]:


translation_projects = [rhumatismes_inflammatoires, handboek, user_guide, guide_bruxelles]


# In[16]:


for project in translation_projects:
    my_project = Project(project['title'], project['client'], project['source'], project['target'], project['words'], project['start'], project['deadline'], project['price'], project['tm'], project['translator'], project['reviewer'], project['status'], project['domain'])
    print(my_project)
    print('----')


# In[21]:


my_project.price


# In[22]:


my_project.reviewer


# In[23]:


my_project.reviewer.name


# In[25]:


my_project.reviewer.email


# # Separate jsons projects

# In[5]:


with open('proj_rhumatismes_inflammatoires.json', 'w', encoding='utf-8') as f:
    json.dump(rhumatismes_inflammatoires, f)


# In[6]:


with open('proj_handboek.json', 'w', encoding='utf-8') as f:
    json.dump(handboek, f)


# In[7]:


with open('proj_user_guide.json', 'w', encoding='utf-8') as f:
    json.dump(user_guide, f)


# In[8]:


with open('proj_guide_bruxelles.json', 'w', encoding='utf-8') as f:
    json.dump(guide_bruxelles, f)


# # Linking projects and freelancers

# In[9]:


with open('freelancers_db.json', 'r') as f:
    my_freelancers = {x.ref : x for x in json.load(f)} # if the json is a list of dictionaries
with open('proj_guide_bruxelles.json', 'r') as f2:
    project_dict = json.load(f2)
    if 'translator' in project_dict and project_dict['translator'] in my_freelancers:
        project_dict['translator'] = Freelancer(**my_freelancers[project_dict['translator']])
    if 'reviewer' in project_dict and project_dict['reviewer'] in my_freelancers:
        project_dict['reviewer'] = Freelancer(**my_freelancers[project_dict['reviewer']])
    project = Project(**project_dict) # of course you have to allow 


# In[ ]:




