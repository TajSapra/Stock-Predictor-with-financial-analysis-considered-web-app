def predict_review(review):
    import re
    from nltk.corpus import stopwords
    from nltk.stem.porter import PorterStemmer
    from nltk import word_tokenize, WordNetLemmatizer
    import pandas as pd
    from sklearn.decomposition import PCA
    from sklearn.svm import SVC
    from sklearn.feature_extraction.text import CountVectorizer
    df1=pd.read_csv('all-data.csv', encoding='latin-1', header=None)
    df1.columns=["Sentiment", "Text"]
    df3=pd.read_csv('0000000000002747_training_twitter_x_y_train (1).csv', encoding='latin-1', header=None)
    df3_updated=pd.DataFrame(columns=["Sentiment", "Text"])
    df3_updated["Sentiment"]=df3[1]
    df3_updated["Text"]=df3[7]
    df3_updated=df3_updated.drop(df3_updated.index[0])
    df_updated=pd.concat([df1,df3_updated])
    df=df_updated[df_updated['Sentiment']!='neutral']
    df=df.dropna()
    df=df.reset_index()
    df=df.drop(columns=['index'])
    for i in review:
        df=df.append({'Text': i,'Sentiment':'neutral'},ignore_index=True)
    df=df.reset_index()
    df=df.drop(columns=['index'])
    df['Sentiment']=df['Sentiment'].replace('positive', 1)
    df['Sentiment']=df['Sentiment'].replace('neutral', 0)
    df['Sentiment']=df['Sentiment'].replace('negative', -1)
    df['Sentiment']=df['Sentiment'].replace('negative ', -1)
    df['Sentiment']=df['Sentiment'].replace(4, 1)
    df['Sentiment']=df['Sentiment'].replace(2, 0)
    df['Sentiment']=df['Sentiment'].replace(0, -1)
    ps = PorterStemmer()
    lemma = WordNetLemmatizer()
    stopwordSet = set(stopwords.words('english'))
    textList = list()
    for i in range(len(df)):
        text = re.sub('[^a-zA-Z]'," ",df['Text'][i])
        text = text.lower()
        text = word_tokenize(text,language='english')
        text = [lemma.lemmatize(word) for word in text if(word) not in stopwordSet]
        text = " ".join(text)
        textList.append(text)
    cv = CountVectorizer(max_features=6250)
    x = cv.fit_transform(textList).toarray()
    y = df["Sentiment"]
    y=y.astype('int')
    pca = PCA(n_components=256)
    x = pca.fit_transform(x)    
    x_test=x[len(x)-len(review):]
    x_train=x[:len(x)-len(review)]
    y_train=y[:len(x)-len(review)]
    model=SVC()
    model.fit(x_train, y_train)
    return model.predict(x_test)    