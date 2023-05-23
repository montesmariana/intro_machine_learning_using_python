import argparse
import pandas as pd

mydict = [
    { "vendor_name" : "Jane Doe",
     "target_language" : "French",
     "word_rate" : 0.14},
    { "vendor_name" : "Jan De Smet",
     "target_language" : "Dutch",
     "word_rate" : 0.13},
    { "vendor_name" : "Kenzo Tamaki",
     "target_language" : "Japanese",
     "word_rate" : 0.15}
]
mydf = pd.DataFrame(mydict, index = ["jane_doe", "jan_de_smet", "kenzo_tamaki"])


def convert_word_rate(word_rate):
    try:
        word_rate = float(word_rate)
    except:
        word_rate = 0
    return word_rate

def add_entry():
    new_name = ""
    new_target_language = ""
    new_word_rate = 0
    while not new_name or not new_target_language or new_word_rate <= 0:
        if not new_name:
            new_name = input("What is the name of the vendor? ")
            # you can also add validation here and reset new_name if it fails
        if not new_target_language:
            new_target_language = input("What is the vendor's target language? ")
            # add validation if necessary, e.g. language codes
        if new_word_rate <= 0:
            new_word_rate = convert_word_rate(input("What is the vendor's word rate? "))
            # I add here custom validation but the one from the pyinput package should help
            # this setup FORCES you to provide an acceptable word rate
            while new_word_rate <= 0:
                message = "The word rate has to be larger than 0! What is the vendor's word rate? "
                new_word_rate = convert_word_rate(input(message))
            while new_word_rate > 0.15:
                message = "The word rate has to be lower than 0.15! What is the vendor's word rate? "
                new_word_rate = convert_word_rate(input(message))
    id = new_name.replace(" ", "_").lower()
    mydf.loc[id] = {
        "vendor_name" : new_name,
        "target_language" : new_target_language,
        "word_rate" : new_word_rate
    }
    print("This is the current database: ")
    print(mydf)
    cont = input("Would you like to add a new entry? (Type 'y' if so) ")
    if cont == "y":
        add_entry()
    else:
        print("Ok, bye!")

def modify_entry(id):
    print(f"The entry {id} will be modified. Invalid values will be ignored.")
    current_entry = mydf.loc[id]
    new_name = input(f"What is the vendor's name? (Current value: {current_entry.vendor_name}) ") or current_entry.vendor_name
    new_target_language = input(f"What is the vendor's target language? (Current value: {current_entry.target_language}) ") or current_entry.target_language
    new_word_rate = convert_word_rate(input(f"What is the vendor's word rate? (Current value: {current_entry.word_rate}) "))
    if new_word_rate <= 0 or new_word_rate > 0.15:
        new_word_rate = current_entry.word_rate
    new_values = { "vendor_name" : new_name, "target_language" : new_target_language, "word_rate" : new_word_rate}
    print(f"This is the current value of {id}, is this ok?")
    print(new_values)
    ok = input("Type 'y' to confirm the changes: ")
    if not ok:
        modify_entry(id)
    else:
        mydf.loc[id] = new_values
        print("The entry has been updated, bye!")
    
if __name__ == "__main__":
    # this code does not include an argument for a filename
    # If the vendor_name of your excel file is hard-coded, you can already open it here
    # Otherwise, right after `parser.parse_args()` with whatever argument receives it
    parser = argparse.ArgumentParser()
    
    # option one: flag to add, another argument to modify ----
    parser.add_argument("-a", "--add", action="store_true", help="Add an entry")
    parser.add_argument("-m", "--modify", type=str, help="Modify an entry")
    args = parser.parse_args()

    if args.add:
        add_entry()
        # inputs to add
    else:
        if not args.modify in mydf.index:
            raise ValueError(f"There is no entry for {args.modify}.")
        modify_entry(args.modify)
        
    # # option two: same argument for both adding and modifying ----
    # with one argument, assuming that you only add or modify
    # parser.add_argument('--id', type=str, help="ID of the entry to add (if it doesn't exist) or modify (if it does).",
    #                     default="new")
    # args = parser.parse_args()
    # if args.id in mydf.index:
    #     modify_entry(args.id)
    # else:
    #     if args.id != "new":
    #         print(f"There is no id for {args.id}, so a new entry will be created!")
    #     else:
    #         print("Creating a new entry!")
    #     add_entry() # and modify it so the vendor_name is just that id
        
    # Then the code to save your file would go here