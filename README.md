# Project management tool for a translation agency

## Introduction
Every translation agency needs to keep track of its past and ongoing projects, just like any company. However, when projects start to accumulate, it may become rather difficult to keep an overview. In addition, large tables or endless database entries do not make for comfortable reading. This tool enables project managers to quickly get an overview of their translation projects and all their information, as a user-friendly and informative text, as well as retrieving specific information.

## Files in this repository
- `README.md` (this file): Gives an overview of the repository, the files it contains and how to use them.
- `project-management-tool_basic.py`: A basic version of the project management tool, which can be run from the command line rather than importing it to use it.
- `project-management-tool_expanded.ipynb`: An interactive version of the script, with more features than the basic version, but which needs to be imported and opened and cannot be run from the command line.
- `project-management-tool_expanded.md`: The markdown version of the file above.
- `projects_db.json`: A sample project database, containing a list of dictionaries with all the information for each project, namely:
    - `title` (a string) indicates the project's title (typically the title of the source document, or the overall title the translator gave the project if there's more than one document to be translated);
    - `client` (a string) indicates the client who ordered the translation;
    - `source` (a string) indicates the language of the source document (document to be translated);
    - `target` (a string) indicates the language of the target document (translation);
    - `words` (an integer) indicates the word count of the source document;
    - `start` (a string) indicates the project's start date in ISO format (YYYY-MM-DD);
    - `deadline` (a string) indicates the project's deadline in ISO format (YYYY-MM-DD);
    - `price` (a float) indicates the total price invoiced to the client (excl. VAT);
    - `tm` (a boolean) indicates whether or not a translation memory is available for this project;
    - `translator` (a string) indicates the freelancer assigned to translate this project (using their unique reference inside the agency's database) or is left empty to indicate that an agency collaborator translated the project;
    - `reviewer` (a string) indicates the freelancer assigned to review this project (using their unique reference inside the agency's database) or is left empty to indicate that an agency collaborator reviewed the project;
    - `status` (a string) indicates the project's status in the agency workflow;
    - `domain` (a string) indicates the overall domain to which the project belongs.
- `guide_bruxelles.json`, `handboek.json`, `rhumatismes_inflammatoires.json` and `user_guide.json`: Separate files containing the same information as `projects_db.json`, but with one file per project.
- `freelancers_db.json`: A sample database (again, as a list of dictionaries), with an overview of three freelancers' information, namely:
    - `name` (a string): The freelancer's name in Firstname Lastname format;
    - `email`(a string): The freelancer's email address;
    - `phone`(a string): The freelancer's phone number (international version, so starting with "+");
    - `task` (a set of strings): The task(s) the freelancer usually performs for the agency, namely whether they're a translator or a reviewer;
    - `language`(a set of strings): The freelancer's working language(s). 
- `add-on_database-generator.ipynb` and `add-on_database-generator.md`: An add-on not integrated in the project management tool itself, but which you can use to generate the freelancer/project information in the dictionary format you may need for the script (i.e. same format as the json-files mentioned above).
- `add-on_TM-generator.ipynb` and `add-on_TM-generator.md`: An add-on not integrated in the project management tool itself, but which you can use to generate a translation memory based on a source and target text, so you can turn your project information from `TM = false` into `TM = true`.
- `python_en.txt` and `python_en.txt`: A sample source and target text to try out the TM generator.

## Composition of the project management tool

### Basic version
The tool consists of a Python class called `Project`. That class creates objects with the following **attributes**:
- 13 instance attributes, which are the same as dictionary keys in the project information dictionaries. The last four attributes are optional and have the following default values:
    - `translator`: "internal", meaning that an agency collaborator was assigned to the project in this role;
    - `reviewer`: "internal", meaning that an agency collaborator was assigned to the project in this role;
    - `status`: "created";
    - `domain`: An empty string, meaning that no domain was provided for this project (so it's probably a general text).
- 7 computed attributes, namely:
    - `st`: A conversion of the start date from a string into an ISO-formatted date using the `datetime` module.
    - `dl`: A conversion of the deadline from a string into an ISO-formatted date using the `datetime` module.
    - `today`: The date of the day on which the tool is used, computed using the `datetime` module.
    - `daysleft`: The number of days left until the project deadline, computed by substracting the current date (`today`) from the project deadline (`dl`).
    - `length`: The total number of days foreseen for the project (weekends and holidays included), computed by subtracting the start date (`st`) from the deadline (`dl`).
    - `rate`: The rate per word the client pays for the project, computed by dividing the project price by the  word count.
    - `efficiency`: The number of words to translate or revise per work day to meet the deadline, computed by dividing the word count by 5/7th of the total project length. Does not take into account holidays.

The class also has three **methods**:
- `days_left`: Prints a message indicating the number of days left until the project deadline if the deadline is in the past or present, and indicating that the deadline has been exceeded already if it is in the past.
- `project_length`: Prints the total number of days (weekends included) foreseen for the project (as calling that attribute would otherwise return a datetime timedelta, which isn't very clear for most users).
- a `printing method`, which displays the project information using the following text template:
    - "`title` is a translation for`client` from `source` into `target`.
    - Both the translator and the reviewer are agency collaborators. (Or "The translator is `translator` and the reviewer is `reviewer`." if they're freelancers.)
    - The domain is `domain`(or "unspecified" if no domain was provided).
    - It's `words` words long, with a rate of `rate` € per word.
    - It started on `st` and is due on `dl`, so `length` days are foreseen for it, of which `daysleft` left. To meet the deadline,`efficiency` words need to be translated or revised per day.
    - There is a translation memory. (Or "no" if there's none.)
    - The project is currently `status`."

The script is documented with **docstrings** and has an **argparse parser**, so it can be run directly from the command line.

### Expanded version
The expanded version of the script has all the features the basic version has, except for the argparse parser (due to time constraints). In addition, it has some extra features that the basic version does not have.

Next to the `Project` class, the expanded tool has a `Freelancer` class to turn the entries of the freelancer database found in `freelancers_db.json` into objects. The **attributes** of that class are the same as the keys in that list of dictionaries. The class also has two **methods**, namely:
- A method to import arguments using keyword arguments (`kwargs`), rather than manually inputting each attribute;
- A `printing method`, which displays the freelancer information using the following text template:
    - "`name` can be contacted via e-mail (`email`) or via phone (`phone`).
    - `name`'s reference in our database is `ref`.
    - `name` works as a `task` for `language`."

Due to time constraints, this class is **not documented with docstrings**.

This added `Freelancer` class allows project managers to not only get an overview of their project's information, but to link the project database and the freelancer database to easily look up information about the freelancers assigned to a project (say, if they're late to deliver or something changes in the project organisation and the PM wants to contact them via e-mail).

## How to use the project management tool

### Basic version
You can run the basic version of the script directly from the command line and manually feed it the project information, using:

`python project-management-tool_basic.py "title" "client" "source" "target" words "YYYY-MM-DD" "YYYY-MM-DD" price tm`

(The placeholders need to be replaced by the actual project information, check above that you input all the information as the right variable type, otherwise you will get an error message asking you to use the correct type.)

### Expanded version
Because no argparse parser was programmed yet for this version of the tool, it needs to be opened rather than being run from the command line. You can open `project-management-tool_expanded.ipynb` with Jupyter Notebooks, or `project-management-tool_expanded.md` with, for example, VS Code. For more information about how to use these files, open them and go through the tutorial in them. Unlike with the basic version run from the command line, this version of the tool allows files as input to instantiate objects. It is possible to print the information of all the projects in one go, using `projects_db.json`, or to link the `Freelancer` and `Project` class for a single project, using `freelancers_db.json` and one of the separate project files.

## Future features
Due to time constraints, several features could not be implemented, which will be added in future updates:
- An argparse parser for the expanded version, which will enable the user to run it from the command line rather than having to open the script. Said parser will also work with files, rather than forcing the user to manually input every attribute, which will result in a significant time gain and make use of the tool easier.
- Validation and docstrings in the `Freelancer` class.
- Validation of the project deadline: ensure that the deadline comes *after* the start date, not before.
- Fine-tuning the `start` date and `deadline`, so the PM can either specify at what time of the day the project starts/needs to be delivered, or not specify it (in which case, the default start/end time is midnight for the start and 11:59 pm for the deadline).
- Differentiate between a rush assignment (`efficiency` calculated on 7/7 of the project lenth instead of 5/7) and a regular assignment (`efficiency` calculated on 5/7 of the project length).
- Fine-tuning of the `efficiency` by taking into account weekends and holidays (ex. so a regular four-days project is counted as four full work days if it spans from Monday to Thursday, but only two full work days if it spans from Friday to Monday, rather than calculating 5/7 of the full project length in both cases).
- A `Client` class with all the necessary client information (contact, VAT-number, bank account number, domain, unique reference inside the agency database...) This class will be linked to the `Project` class just like `Freelancer`, facilitating retrieval of client information.
- The possibility to loop through all the separate project files even when linking `Project` and `Freelancer` objects, so you don't have to run the script for each project separately (which is feasible for four projects, but far too time-consuming in a real agency setting).
- An extension of the recognised file formats, from json or csv to xml, excel-documents...
- Fine-tuning the `efficiency` attribute by creating a specific attribute for translation and for review (for example 2/3 of the time for translation and 1/3 for review).
- Fine-tuning the `rate` and `price` attributes by linking the rate to a `rate` entry in the freelancer database (since each freelancer has their own rates, and rate is not applicable to agency collaborators, who receive a fixed salary per month rather than being paid per project) and calculating the agency's margin after substraction of the freelancer fees from the total project price.
- Ensuring standardisation of the dates in a certain time zone, to avoid calculation errors if the start date and deadline were fixed in a different time zone from that of the person using the script (since their time zone determines the computation of "today").
