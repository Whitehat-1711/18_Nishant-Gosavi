import pandas as pd
import numpy as np
import seaborn as sns

dataset=pd.read_csv('AI_Human.csv.zip')

dataset.head()

dataset.info()

dataset.describe()

sns.countplot(data=dataset,x='generated')

print('total text: ',dataset['generated'].count())
print('Human Written Texts: ',(dataset['generated']==0.0).sum())
print('AI Generated Texts: ',(dataset['generated']==1.0).sum())

dataset['text'][0]

def remove_tags(text):
    tags=['\n','\'']
    for tag in tags:
        text=text.replace(tag,'')
        
    return text
dataset['text']=dataset['text'].apply(remove_tags)

dataset['text'][0]

import nltk
from nltk.corpus import words

nltk.download('words')
english_words = set(words.words())


def is_spelled_correctly(word):
    return word in english_words



