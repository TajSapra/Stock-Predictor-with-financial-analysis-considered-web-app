print("Python started")
import sys
import subprocess
import importlib
import time
import pandas as pd
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pymongo'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'schedule'])
import schedule
import pymongo
def repeatfun():
    price, time1, status, time2=live.getlivedata()
    if status=='OPEN' or status=='Open' or status=='open':
        mycol.insert_one({"Date":time1,"close":price})
    print("Data updated")
    time.sleep(30)
    combined_data= mycol.find().sort([('_id', 1)])    
    dataframe=pd.DataFrame(columns=["Date", "close"])
    for i in combined_data:
        dataframe=  dataframe.append({"Date":i["Date"], "close":i["close"]}, ignore_index=True)
    dataframe=dataframe.iloc[12:,:]
    y_test, predictions= predictor.Predictor_Main(dataframe)
    mycol2=mydb["predicted_stock_prices"]
    latest_pred=mycol2.find().sort([('_id', -1)]).limit(1)
    print(latest_pred.count())
    if(latest_pred.count()>=1 and (not latest_pred[0]["Date"]==time1)):
        if(type(predictions)==float):
            mycol2.insert_one({"Date": time2, "Predicted": predictions})
        if (type(predictions)==list):
            mycol2.insert_one({"Date": time2, "Predicted": predictions[0]})
    if(latest_pred.count()==0):
        if(type(predictions)==float):
            mycol2.insert_one({"Date": time2, "Predicted": predictions})
        if (type(predictions)==list):
            mycol2.insert_one({"Date": time2, "Predicted": predictions[0]})
live=importlib.import_module('fetchlivedata')
last2=importlib.import_module('getlast2yearsdataanddumptodatabase')
predictor=importlib.import_module('Predictstocks')
reviewscorer=importlib.import_module('sentiment_main')
start1=int(time.time())
myclient = pymongo.MongoClient("mongodb://localhost:27017/Stock_predictor")
mydb=myclient["Stock_predictor"]
mycol=mydb["stock_prices"]
count=mycol.count()
last2_data=[]
print(count)
if count<200:
    last2_data=last2.getdata2years()
    print(len(last2_data))
    for i in reversed(last2_data):
        if i[0]=='time':
            continue
        if i[0]=='1' or i[0]=='2' or i[0]==1 or i[0]==2 or i[0]=='3' or i[0]=='4' or i[0]==3 or i[0]==4 or i[0]=='5' or i[0]=='6' or i[0]==5 or i[0]==6 or i[0]=='7' or i[0]=='8' or i[0]==7 or i[0]==8 or i[0]=='9' or i[0]==9:
            continue
        mycol.insert_one({"Date":i[0], "close": i[1]})
reviewscorer.add_review_score_to_db()
repeatfun()
end1=int(time.time())
print(end1-start1)
schedule.every(15*60).seconds.do(repeatfun)
schedule.every(15*60).seconds.do(reviewscorer.add_review_score_to_db)
while 1:
    schedule.run_pending()