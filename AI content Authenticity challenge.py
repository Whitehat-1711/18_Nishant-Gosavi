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

word_to_check = dataset['text'][487232]
if is_spelled_correctly(word_to_check):
    print(f"The word '{word_to_check}' is spelled correctly.")
else:
    print(f"The word '{word_to_check}' is spelled incorrectly.")

dataset['text'][487232]

from nltk.corpus import stopwords
nltk.download('stopwords')

def remove_stopwords(text):
    stop_words = set(stopwords.words('english'))
    words = nltk.word_tokenize(text)
    filtered_words = [word for word in words if word.lower() not in stop_words]
    filtered_words= ' '.join(filtered_words)
    return filtered_words

dataset['text']=dataset['text'].apply(remove_stopwords)

dataset['text'][0]

y=dataset['generated']
X=dataset['text']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=42)

print(len(X_train))
print(len(y_train))

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report

pipeline = Pipeline([
    ('count_vectorizer', CountVectorizer()),  # Convert text to token counts
    ('tfidf_transformer', TfidfTransformer()),  # Transform token counts to TF-IDF
    ('naive_bayes', MultinomialNB())  # Naive Bayes classifier for text classification
])




