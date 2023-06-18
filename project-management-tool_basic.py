#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import datetime

"""This script gives a translation agency an overview of all its projects.
"""

import argparse

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
            raise TypeError("The start date must be provided in ISOFormat")
        else:
            self.start = start
        if type(deadline) != str:
            raise TypeError("The deadline must be provided as a string.")
        try:
            self.dl = datetime.date.fromisoformat(deadline)
        except:
            raise TypeError("The start deadline must be provided in ISOFormat")
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
        if type(translator) != str:
            raise TypeError("The translator's name must be a string.")
        elif translator == '':
            self.translator = "internal"
        else:
            self.translator = translator
        if type(reviewer) != str:
            raise TypeError("The reviewer's name must be a string.")
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

if __name__ == "__main__":
    parser = argparse.ArgumentParser("project")
    parser.add_argument("title", type=str, help="Title of the project")
    parser.add_argument("client", type=str, help="Client who ordered the translation")
    parser.add_argument("source", type=str, help="Source language")
    parser.add_argument("target", type=str, help="Target language")
    parser.add_argument("words", type=int, help="Project word count")
    parser.add_argument("start", type=str, help="Project start date")
    parser.add_argument("deadline", type=str, help="Project deadline")
    parser.add_argument("price", type=float, help="Total price project")
    parser.add_argument("tm", type=bool, help="Whether a translation memory is available")
    parser.add_argument("--translator", type=str, default = "internal", help="Translator assigned to the project")
    parser.add_argument("--revisor", type=str, default = "internal",help="Revisor assigned to the project")
    parser.add_argument("--status", type=str, default = "created",
                            choices = ["created", "in translation", "in revision", "delivered", "delayed", "cancelled", "canceled"], help="Project status in the agency workflow")
    parser.add_argument("--domain", type=str, default = "", help="Overall domain of the text")
    args = parser.parse_args()
    proj = Project(args.title, args.client, args.source, args.target, args.words, args.start, args.deadline, args.price, args.tm, args.translator, args.revisor, args.status, args.domain)
    proj.days_left()
    proj.project_length()
    print(proj)

