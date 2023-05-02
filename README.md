# A script to make you proud

This repository contains a small Python program that shows that I have learned Python in this semester.

The code has been developed by KU Leuven student, Kate Herrick.

## Installation and usage

Clone this repository with the following git command in the console (or download the ZIP file via GitHub):

```sh
git clone git@github.com:montesmariana/intro_machine_learning_using_python
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
