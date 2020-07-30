import requests
from pprint import pprint
from datetime import date, timedelta
import xmltodict
import json

def get_city_data():
    url = "http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson"

    params ={
        'serviceKey':'X/C2kuzSwMAhST4sE+QmInc5Sog/qb9A6sK7aBjcTQOlYCutTj543s9gqsJxT2rh9hEyNlh3fGQT03CBRnMvhQ==',
        'pageNo': '1',
        'numOfRows': '30',
        'startCreatDt' : '20200726',
        'endCreateDt': '20200727',
    }

    res = requests.get(url, params=params)

    dict_data = xmltodict.parse(res.text)

    json_data = json.dumps(dict_data)
    dict_data = json.loads(json_data)
    pprint(dict_data)
    pprint(dict_data["response"]["body"]["items"]["item"][1])
    return dict_data

pprint(get_city_data())