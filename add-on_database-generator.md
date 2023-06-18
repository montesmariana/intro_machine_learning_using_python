# Introduction
This script is an add-on to the project management tool. Most translation agencies already have their own databases (or apps) and would therefore not need an extra script to generate/export them. However, for agencies which do not yet have a handy way to record their freelancer and project information in a structured way and/or export it to a usable file format, here is a script to list the freelancer and project information as dictionaries exported to json-files.

# Freelancers
The entire freelancers database will be exported as a single file containing a list of dictionaries.

## Creating a list of dictionaries
The information of each freelancer is recorded in a single dictionary. Said information comprises:
- the freelancer's full `name` (in First name Last name format), a string,
- the freelancer's `email` address, a string,
- the freelancer's `phone`number, a string,
- the freelancer's `reference`, which is their unique identifier in the agency's database (this reference is also the name of the dictionary with that freelancer's information), a string,
- the freelancer's `task(s)`, so whether they are a translator and/or a reviewer, a set,
- the freelancer's `languages`, a set.


```python
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
```

The dictionaries are then assembled together into a list:


```python
freelancers = [sdw, mm, evdl]
```

## Creating the file
This list is then dumped into (= exported as) a json-file called `freelancers_db.json`:


```python
import json # to generate a json-file, the json-module is necessary
with open('freelancers_db.json', 'w', encoding='utf-8') as f:
    json.dump(freelancers, f)
```

# Projects
Unlike the freelancers' information, each project's information will also be exported into a separate file (as we need one file per project for the project management tool to work, see main script).

## Creating the dictionaries
The method is the same as for the freelancer database, only the information is obviously different:
- `title` (a string, ) indicates the project's title (typically the title of the source document, or the overall title the translator gave the project if there's more than one document to be translated);
- `client` (a string) indicates the client who ordered the translation;
- `source` (a string) indicates the language of the source document (document to be translated);
- `target` (a string) indicates the language of the target document (translation);
- `words` (an integer) indicates the word count of the source document;
- `start` (a string) indicates the project's start date in ISO format (YYYY-MM-DD);
- `deadline` (a string) indicates the project's deadline in ISO format (YYYY-MM-DD);
- `price` (a float) indicates the total price invoiced to the client (excl. VAT);
- `tm` (a boolean) indicates whether or not a translation memory is available for this project;
- `translator`(a string, optional, defaults to "internal") gives the internal reference of the freelance translator assigned to the project, or remains empty if the project was assigned to an internal translator;
- `reviewer`(a string, optional, defaults to "internal") gives the internal reference of the freelance reviewer assigned to the project, or remains empty if the project was assigned to an internal reviewer;
- `status`(a string, optional, defaults to "created") indicated the project status in the agency workflow, choosing from "created", "in translation", "in revision", "delivered", "delayed", or "cancel(l)ed";
- `domain` (a string, optional, defaults to empty string) indicates the overall domain to which the project belongs.


```python
rhumatismes_inflammatoires = {
    'title' : 'La polyarthrite rhumatoïde et autres rhumatismes inflammatoires',
    'client' : 'Reuma vzw',
    'source' : 'FR',
    'target' : 'NL',
    'words' : 2142,
    'start' : '2020-10-02',
    'deadline' : '2020-10-15',
    'price' : 715.00,
    'tm' : False,
    'translator' : '',
    'reviewer' : '',
    'status' : 'delivered',
    'domain' : 'healthcare'
}
handboek = {
    'title' : 'Handboek voor studentenvertegenwoordigers',
    'client' : 'KU Leuven',
    'source' : 'NL',
    'target' : 'EN',
    'words' : 7237,
    'start' : '2023-02-21',
    'deadline' : '2023-03-07',
    'price' : 2680.00,
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
    'deadline' : '2023-04-15',
    'price' : 740.00,
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
    'start' : '2023-05-06',
    'deadline' : '2023-06-30',
    'price' : 4025.00,
    'tm' : False,
    'translator' : 'evdl',
    'reviewer' : 'sdw',
    'status' : 'in revision',    
    'domain' : ''
}
```


```python
projects = [rhumatismes_inflammatoires, handboek, user_guide, guide_bruxelles]
```

## Creating the files
Unlike the freelancers database, each project is also exported separately into one json-file:


```python
with open('projects_db.json', 'w', encoding='utf-8') as f:
    json.dump(projects, f)

with open('rhumatismes_inflammatoires.json', 'w', encoding='utf-8') as f:
    json.dump(rhumatismes_inflammatoires, f)
with open('handboek.json', 'w', encoding='utf-8') as f:
    json.dump(handboek, f)
with open('user_guide.json', 'w', encoding='utf-8') as f:
    json.dump(user_guide, f)
with open('guide_bruxelles.json', 'w', encoding='utf-8') as f:
    json.dump(guide_bruxelles, f)
```
