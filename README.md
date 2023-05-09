# What I'm planning

- Start from the translation job management script created for the first assignment, but expand on it to make it useful for a translation agency rather than an independent translator.
- Three class attributes (strings) :
    - Translator
    - Revisor
    - Status
   
   -> The default value for "Translator" and "Revisor" is "Internal", meaning that an employee of the translation agency took up the job. If the agency assigned the job to a freelancer, the default value can be changed to their name.
   
   -> The default value for "Status" is "Created". The status can then be updated as the project progresses to "In translation", "In revision", "Delivered", "Delayed" or "Cancelled". If possible, the script should only accept these six labels to prevent organisational chaos due to everyone using their own labels.
- Instance and computed attributes remain the same as in the first assignment (with some edits to add the advice from the first assignment's feedback).
- Add validation for unexpected input (+ for "Status" labels different from the six authorised labels?)
- Add methods (?) to call the computed attributes and get a result that's more legible than what this currently generates (for example "22 days" instead of "datetime.timedelta(days=22)")
- The input will still be read from a list of dictionaries in a separate json-file. Those dictionaries will be described in a separate markdown file.

# What I'd like to add but don't know how

- It would be neat if I could do something with the translation memory and termbase of each project. Maybe add a method that opens them for a preview?
- It would also be super useful to have a way to align a source and a target text and generate a file that can be added to a translation memory. So, to start from two docx-files (or txt-files), split them into sentences and pair each sentence in the source text with the corresponding sentence in the target text and generate a single csv-file with the paired sentences. Ideally, the context (i.e. the surrounding sentences) should also be considered, but if that's not possible an aligned csv would already be awesome.

# Things I'm not yet sure how to integrate into the assignment

- Use of argparse.
- Use of regular expressions.
