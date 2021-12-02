def getlivedata():
    import requests
    from bs4 import BeautifulSoup
    from datetime import datetime, timedelta
    HTML=requests.get('https://www.marketwatch.com/investing/stock/msft').text
    data=BeautifulSoup(HTML, 'lxml')
    price=data.find_all('bg-quote', {'class':'value'})[0].text
    time=data.find_all('span', {'class':'timestamp__time'})[0].text[14:].replace(',','').replace('  ',' ').replace(' p.m. EDT','PM').replace(' a.m. EDT','AM').replace(' p.m. EST','PM').replace(' a.m. EST','AM')
    status=data.find_all('div',{'class':'status'})[0].text
    temp=datetime.strptime(time, '%b %d %Y %I:%M%p')
    temp2=temp+timedelta(minutes=18)
    time=temp.strftime("%Y-%m-%d %H:%M:%S")
    time2=temp2.strftime("%Y-%m-%d %H:%M:%S")
    return price, time, status, time2