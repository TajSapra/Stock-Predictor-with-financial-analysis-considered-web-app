/////////1st update/////////
Task:
To make a stock Predictor web app using Machine Learning and nodeJS

Well what is/will be(while under development) unique about this Stock Predictor:
Unlike other stock predictors that use previous stock values, we will also consider the current market sentiment for predictions. This will help in increasing the corectness of the prediction.

Tech Stacks Used:

1)Frontend:HTML, CSS, JS
2)Backend: NodeJS, Express, MongoDB and other NPM modules
3)Machine Learning: Initially the ml scripts in python but will be convert them to js if needed in the later stage of development.

Datasets used:
The datasets used can be found in the assets/datasets directory. They were downloaded from Kaggle. There are 2 seperate files and have different format, hence the data requires liitle bit of cleaning before it is ready to go.

Data Analysis:
This section will be uploaded later. Stay Tuned..... :)

Approach for ml predictions:
We will consider the past years stock data available on kaggle to train our model. We will try multiple methods to predict the value and will choose the one that give the best results. Also before finalising if the prediction made is correct or not, we will consider the financial sentiment analysis of the company from various news sites and other platforms. Now that will help us to reduce the chances of error.

As for sentiment analysis, we have tried a couple of approaches namely:
1)NLP+ Naive Bayes Classifier Method
2)NBSVM(Naive Bayes SVM)
In the second method, the features that we use in Naive Bayes are rather sent to SVM classifier. This helps us to get higher accuracy. In the second method, we also used concepts of nlp to increase accuracy like ngram while declaring the CountVectorizer. 

Accuracy for Method 1: 70%
Accuracy for Method 2: 77%
Added 3rd dataset, accuracy is now 79.35%



To do:Complete Python code for the ml scripts and data collection, preprocessing, Integrate with Javascript and complete UI.

Last Updated:08-09-2021