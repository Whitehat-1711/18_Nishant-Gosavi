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


