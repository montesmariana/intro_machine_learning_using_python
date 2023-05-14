# Script: Translation Vendor Database

This repository contains a Python program that could help a translation agency to keep track of a vendor database. The idea is to make it easier for project managers to keep track of who the preferred and back-up vendors are for a project, in which languages they work, what their contact details and rates are and other information that might be useful for the PMs.

The code has been developed by Elmo Geeraerts.

## Installation and usage

Clone this repository with the following git command in the console (or download the ZIP file via GitHub):

```sh
git clone https://github.com/ElmoGeeraerts/intro_machine_learning_using_python.git
```

You can import the script as a module by adding the repository to your path in a Python script or interactive notebook and then calling `import`.

```python
import sys
sys.path.append('/path/to/intro_machine_learning_using_python')
import script as s
```

Check out `tutorial.md` to see an example of the different functionalities of the script!

You can also run the script directly with the following code in a console:

```sh
python script.py <example.json>
```

Or in Jupyter notebook with:

```python
%run script.py <example.json>
```

In both cases `example.json` stands for the `filename` argument that the script needs. You can use [the file in this repository](example.json) or a similar file of yours. Find more information on how this script works with:

```sh
python script.py --help
```

If you run this script, you become proud of yourself.
