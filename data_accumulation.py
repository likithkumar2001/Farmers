
def web_scrapping():
    import requests
    from bs4 import BeautifulSoup
    import re
    url = "https://mausam.imd.gov.in/imd_latest/contents/districtwisewarnings.php"
    html = requests.get(url)
    html.close()
    soup_day = BeautifulSoup(html.content, 'html.parser')
    data =str(soup_day.find_all('script')[7])
    return(data)

def data_cleaning(data):
    import json
    from bs4 import BeautifulSoup
    import re
    data=re.sub(r"^\s+|\s+$", "", data)
    data = data.replace("\n","")
    text = '\[(.*?)\]'
    data = "["+ re.findall(text,data)[0] +"]"
    data_json = json.loads(data)
    for i in range(len(data_json)):
        data_json[i]['info']=data_json[i]['info'].replace("</br>"," ")
        data_json[i].pop('color', None)
        data_json[i].pop('balloonText', None)
        data_json[i]['id']=int(data_json[i]['id'])
        y = data_json[i]['info']
        y = BeautifulSoup(y, 'html.parser')
        data_json[i]['info'] = y.text
        p = data_json[i]['info'].split('Time of issue:')
        x= p[0].lstrip()
        x= x.replace("/"," per ")
        x = x.replace("mm"," milli meter ")
        x = x.replace("hr"," hour ")
        x = x.replace("<"," less then ")
        x = x.replace(">", " greater then ")
        x = x.replace("-", " to ")
        x = x.replace("kmph", " kilometer per hour ")      
        data_json[i]['Message']=x.rstrip()
        data_json[i]['Type'] = data_json[i]['Message'].split(':')[0]
        if(len(p)>1):
            time = p[1].split('Valid upto:')
            x = time[0].rstrip()
            x = x.lstrip()
            x=x.split(" ")
            data_json[i]['Date of issue'] = x[0]
            data_json[i]['Time of issue'] = float(x[1])/100
            x = time[1].rstrip()
            x = x.lstrip()
            x = x.split("Hrs")
            data_json[i]['Valid upto'] = float(x[0])/100
        data_json[i].pop('info', None)
    return(data_json)


def store_data(info):
    import urllib
    from pymongo import MongoClient
    import dns
    uri = 'mongodb+srv://likith:'+  urllib.parse.quote("Rp-iA@c6!Nq45c4") +'@cluster0.ms0ap.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
    client = MongoClient( uri )
    db = client.weather
    data = db.data
    x = data.delete_many({})
    result = data.insert_many(info)
    client.close()

data = web_scrapping();
info = data_cleaning(data);
store_data(info);
