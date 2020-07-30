import requests
from bs4 import BeautifulSoup
def get_covid_info():
    url = "http://ncov.mohw.go.kr/"

    res = requests.get(url)

    soup = BeautifulSoup(res.text, 'lxml')

    info = soup.select('.liveNum li span.num')
    print(info)
    

    results = {
        '확진환자' : int(info[0].text.replace(',','').replace('(누적)','')),
        '완치' : int(info[1].text.replace(',','')),
        '치료중' : int(info[2].text.replace(',','')),
        '사망' : int(info[3].text.replace(',',''))
    }
    return results

print(get_covid_info())