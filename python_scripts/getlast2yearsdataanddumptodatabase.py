def getdata2years():
    import pandas as pd
    import csv
    import time
    import requests
    import numpy as np
    api_key1 = "41SG6MXSCEV9EJOQ"
    api_key2 = "QGVON3TNFI6O8HN6"
    api_key3 = "LQ3QY16BHN0DAGP9"
    api_key4="XJKC5WIK7M58YPLT"
    api_key5="79Q3KL78TDZF52NB"
    data = []
    counter = 0
    for i in range(1, 6, 1):
        CSV_URL = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol=MSFT&interval=15min&slice=year1month' + str(i)+'&apikey='+api_key1
        with requests.Session() as s:
            download = s.get(CSV_URL)
            decoded_content = download.content.decode('utf-8')
            cr = csv.reader(decoded_content.splitlines(), delimiter=',')
            my_list = list(cr)
            for row in my_list:
                counter += 1
                data.append(row)
    print(len(data))
    time.sleep(60)
    counter = 0
    for i in range(6, 11, 1):
        CSV_URL = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol=MSFT&interval=15min&slice=year1month' + str(i)+'&apikey='+api_key2
        with requests.Session() as s:
            download = s.get(CSV_URL)
            decoded_content = download.content.decode('utf-8')
            cr = csv.reader(decoded_content.splitlines(), delimiter=',')
            my_list = list(cr)
            for row in my_list:
                counter += 1
                data.append(row)
    print(len(data))
    time.sleep(60)
    counter = 0
    CSV_URL = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol=MSFT&interval=15min&slice=year1month' + str(11)+'&apikey='+api_key3
    with requests.Session() as s:
        download = s.get(CSV_URL)
        decoded_content = download.content.decode('utf-8')
        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        my_list = list(cr)
        for row in my_list:
            counter += 1
            data.append(row)
    print(len(data))
    counter = 0
    CSV_URL = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol=MSFT&interval=15min&slice=year1month' + str(12)+'&apikey='+api_key3
    with requests.Session() as s:
        download = s.get(CSV_URL)
        decoded_content = download.content.decode('utf-8')
        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        my_list = list(cr)
        for row in my_list:
            counter += 1
            data.append(row)
    print(len(data))
    time.sleep(60)
    counter = 0
    for i in range(1, 6, 1):
        CSV_URL = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol=MSFT&interval=15min&slice=year2month' + str(i)+'&apikey='+api_key4
        with requests.Session() as s:
            download = s.get(CSV_URL)
            decoded_content = download.content.decode('utf-8')
            cr = csv.reader(decoded_content.splitlines(), delimiter=',')
            my_list = list(cr)
            for row in my_list:
                counter += 1
                data.append(row)
    print(len(data))
    time.sleep(60)
    counter = 0
    for i in range(6, 11, 1):
        CSV_URL = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol=MSFT&interval=15min&slice=year2month' + str(i)+'&apikey='+api_key5
        with requests.Session() as s:
            download = s.get(CSV_URL)
            decoded_content = download.content.decode('utf-8')
            cr = csv.reader(decoded_content.splitlines(), delimiter=',')
            my_list = list(cr)
            for row in my_list:
                counter += 1
                data.append(row)
    print(len(data))
    time.sleep(60)
    counter = 0
    CSV_URL = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol=MSFT&interval=15min&slice=year2month' + str(11)+'&apikey='+api_key3
    with requests.Session() as s:
        download = s.get(CSV_URL)
        decoded_content = download.content.decode('utf-8')
        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        my_list = list(cr)
        for row in my_list:
            if counter == 0:
                counter = 1
                continue
            counter += 1
            data.append(row)
    print(len(data))
    counter = 0
    CSV_URL = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol=MSFT&interval=15min&slice=year2month' + str(12)+'&apikey='+api_key3
    with requests.Session() as s:
        download = s.get(CSV_URL)
        decoded_content = download.content.decode('utf-8')
        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        my_list = list(cr)
        for row in my_list:
            if counter == 0:
                counter = 1
                continue
            counter += 1
            data.append(row)
    return data