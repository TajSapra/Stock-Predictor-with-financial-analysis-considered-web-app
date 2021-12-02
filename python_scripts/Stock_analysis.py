import csv
from sklearn.model_selection import train_test_split
import string
import pandas as pd
import random
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import CountVectorizer
from nltk.classify.scikitlearn import SklearnClassifier
import numpy as np
import pickle
from time import time
from datetime import datetime
import random
df1=pd.read_csv('all-data.csv', encoding='latin-1', header=None)
df1.columns=["Sentiment", "Text"]
df2=pd.read_csv('stock_data.csv')
df2=df2.reindex(columns=["Sentiment", "Text"])
df2['Sentiment']=df2['Sentiment'].replace([1], 'positive')
df2['Sentiment']=df2['Sentiment'].replace([-1], 'negative')
df3=pd.read_csv('training.1600000.processed.noemoticon.csv', encoding='latin-1', header=None)
df3.columns=["A", "B", "C", "D", "E", "f"]
df4=df3.loc[:,'A']
df4=pd.DataFrame(df4)
df4['text']=df3['f']
df4.columns=["Sentiment", "Text"]
df=pd.concat([df1,df2])
df['Sentiment']=df['Sentiment'].replace([4], 'positive')
df['Sentiment']=df['Sentiment'].replace([0], 'negative')
df['Sentiment']=df['Sentiment'].replace([2], 'neutral')
dfwithoutpositive=df[df['Sentiment']!='positive']
df=dfwithoutpositive
start=int(time())
ans=0
maxa=0
mini=100
print(datetime.now())
for i in range(1):
    print(i, end=" ")
    X_train, X_test, Y_train, Y_test=train_test_split(df.Text, df.Sentiment, test_size=0.1, random_state=random.randint(1,20))
    vectorizer=CountVectorizer(binary=True, ngram_range=(1,5))
    X=trn_term_doc_bin_ngram=vectorizer.fit_transform(X_train)
    tst_term_doc_bin_ngram=vectorizer.transform(X_test)
    y=np.array(Y_train)
    vocab=vectorizer.get_feature_names()
    R = np.log(
        (
            X[y=='positive'].sum(axis=0)+1)
            /(X[y=='positive'].sum(0).sum()+len(vocab)
         )
        /(X[y=='negative'].sum(axis=0)+1)
        /(X[y=='negative'].sum(0).sum()+len(vocab))
    )
    R = np.squeeze(np.asarray(R))
    X_nb=trn_term_doc_bin_ngram.multiply(R)
    print("processed", end=" ")
    m=LinearSVC().fit(X_nb, y)
    print("trained", end=" ")
    curr=m.score(tst_term_doc_bin_ngram.multiply(R), Y_test)
    ans+=curr
    maxa=max(maxa, curr)
    mini=min(mini, curr)
    print(int(time())-start)
print(ans/1, maxa, mini)
end=int(time())
print("Timing: ", end-start)
pickle.dump(m, open('../assets/ml_models/Review_model.sav', 'wb'))
#accuracy: 79.35%
#training time: 49 minutes on all 3 datasets
#dataset 3 is very huge to be uploaded, link: https://docs.google.com/file/d/0B04GJPshIjmPRnZManQwWEdTZjg/edit?resourcekey=0-betyQkEmWZgp8z0DFxWsHw