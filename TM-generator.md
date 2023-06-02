# Source and target text aligner
Sometimes, you still have some translations left over from a time where you didn't use CAT-tools and you'd like to feed them into your translation memory. Some CAT-tools have built-in text aligners, but not all of them, so how do you go from two separate text documents to an aligned bilingual (csv-)file ready to be fed into your TM?

## Step one: Prepare the source and target text
The easiest file format to start from is a pure txt-file... and since for a TM only the pure text is of interest, converting a Word-, PowerPoint- or whatever file to a txt-file isn't an issue. So, we'll take the original source and target document and export them to a txt-format (with utf-8 encoding).
## Step two: Store the two (continuous) texts into variables


```python
with open('python_en.txt', encoding = 'utf-8') as f:
    st_1 = f.read()
st_1
```




    'Introduction to Machine Learning with Python.\n\nThis module provides an introduction to the basic concepts and use of the Python programming language in support of translation. Focus lies on the main concepts that include Natural Language Processing, automation, text analysis and machine learning.\n'




```python
with open('python_fr.txt', encoding = 'utf-8') as f:
    tt_1 = f.read()
tt_1
```




    'Introduction au machine learning à l’aide de Python.\n\nCe module offre une introduction aux concepts de base et à l’utilisation du langage de programmation Python comme aide à la traduction. L’accent est mis sur le traitement du langage naturel (NLP), l’automatisation, l’analyse de texte et le machine learning.\n'



## Step three: Split the single text string into list of sentences
Since most TMs (and CAT-tools) use sentence segmentation, the source and target text need to be split up into sentences. So, each text becomes a list of separate sentences.

For this, we use `nltk tokenizer`, which functions with English and French (and many other languages, but English and French are the ones that interest us right now).


```python
from nltk.tokenize import sent_tokenize
split_st_1 = sent_tokenize(st_1, language = 'english')
split_st_1
```




    ['Introduction to Machine Learning with Python.',
     'This module provides an introduction to the basic concepts and use of the Python programming language in support of translation.',
     'Focus lies on the main concepts that include Natural Language Processing, automation, text analysis and machine learning.']




```python
from nltk.tokenize import sent_tokenize
split_tt_1 = sent_tokenize(tt_1, language = 'french')
split_tt_1
```




    ['Introduction au machine learning à l’aide de Python.',
     'Ce module offre une introduction aux concepts de base et à l’utilisation du langage de programmation Python comme aide à la traduction.',
     'L’accent est mis sur le traitement du langage naturel (NLP), l’automatisation, l’analyse de texte et le machine learning.']



## Step four: Aligning those lists and exporting the tuples list to a csv-file
Writing a csv-file looks fairly similar to reading a txt-file, like we did at the start of the process, except this time we use `f.write` instead of `f.read`.
A csv-file consists of rows, often a first header row with the label of each column, followed by the actual content of the file. Both are defined separately.
- The content of the header row  (defined in the first indented line) simply consists of the language codes of the source and target language.
- The content of the next rows (defined in the next indented lines) contains our texts.
    - The `zip()`-function aligns the first sentence of the source text with the first sentence of the target text, the second with the second... and so on in x, y tuples.
    - Next, those tuples are put inside an f-string that separates x and y with a tab and places makes a new line start after each y.


```python
with open("translation_memory.csv", "w", encoding = "utf-8") as f: # open file to overwrite
    f.write("EN\tFR\n") # write heading
    for x, y in zip(split_st_1, split_tt_1): # go through each pair of lines
        f.write(f"{x}\t{y}\n") # write the line
```

## Step five: Admiring our work
Using pandas, we can read the newly created csv-file.


```python
import pandas as pd
```


```python
read_tm = pd.read_csv('translation_memory.csv', sep = '\t')
read_tm.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>EN</th>
      <th>FR</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Introduction to Machine Learning with Python.</td>
      <td>Introduction au machine learning à l’aide de P...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>This module provides an introduction to the ba...</td>
      <td>Ce module offre une introduction aux concepts ...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Focus lies on the main concepts that include N...</td>
      <td>L’accent est mis sur le traitement du langage ...</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
