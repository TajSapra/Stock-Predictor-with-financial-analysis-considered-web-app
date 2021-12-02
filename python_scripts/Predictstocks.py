def Predictor_Main(df):
    import pandas as pd
    import math
    import numpy as np
    import matplotlib.pyplot as plt
    from sklearn.preprocessing import MinMaxScaler
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import Dense, LSTM
    df.dropna(inplace=True)
    scaler=MinMaxScaler(feature_range=(0, 1))
    dataset=df.filter(['close']).values
    scaled_data=scaler.fit_transform(dataset)
    training_data_len = math.ceil( len(dataset)) 
    train_data = scaled_data[0:training_data_len  , : ]
    x_train=[]
    y_train = []
    for i in range(48,len(train_data)):
        x_train.append(train_data[i-48:i,0])
        y_train.append(train_data[i,0])
    x_train, y_train = np.array(x_train), np.array(y_train)
    x_train = np.reshape(x_train, (x_train.shape[0],x_train.shape[1],1))
    model = Sequential()
    print("shape: ", x_train.shape)
    model.add(LSTM(units=50, return_sequences=True,input_shape=(x_train.shape[1],1)))
    model.add(LSTM(units=50, return_sequences=False))
    model.add(Dense(units=25))
    model.add(Dense(units=15))
    model.add(Dense(units=1))
    model.compile(optimizer='adam', loss='mean_squared_error')
    model.fit(x_train, y_train, epochs=10, batch_size=64)
    test_data = scaled_data[training_data_len - 48: , : ]
    x_test = []
    # y_test =  dataset[training_data_len : , : ]
    x_test.append(test_data[-48:,0])

    x_test = np.array(x_test)
    print(x_test.shape)
    x_test = np.reshape(x_test, (x_test.shape[0],x_test.shape[1],1))
    predictions = model.predict(x_test) 
    predictions = scaler.inverse_transform(predictions)
    predictions=[float(i) for i in predictions]
    # y_test=[float(i) for i in y_test]
    # print("Test: ",y_test)
    print("Predictions: ",predictions)    
    # rmse=np.sqrt(np.mean(((np.array(predictions)- np.array(y_test))**2)))
    # print("RMSE: ",rmse)
    y_test=0
    return y_test, predictions