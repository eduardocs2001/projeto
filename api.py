import requests
import json
import csv
from datetime import date
import time


class binace_csv:

    def __init__(self):
        self._file = open('dados.csv', 'w', newline='', encoding='utf-8')
        self._w = csv.writer(self._file)
        self._w.writerow(['longShortRatio', 'timestamp', 'symbol'])

    def tempo(self):
        hj = date.today()
        passado = date.fromordinal(hj.toordinal()-30) # 30 dias atrás
        unix_timestamp = time.mktime(passado.timetuple())
        unix_timestamp_hoje = time.mktime(hj.timetuple())
        salto = 144000
        print(unix_timestamp_hoje, 'hoje')
        print(unix_timestamp, 'inicio')
        dados = [int(unix_timestamp), salto]
        return dados


    def requisita(self):
        dados = self.tempo()
        inicio = dados[0]
        stop = dados[0]
        for x in range(18):
            print(stop)
            stop += dados[1]
            url = f'https://fapi.binance.com/futures/data/globalLongShortAccountRatio?symbol=BTCUSDT&period=5m&start_time={inicio}&end_time={stop}&limit=480'
            inicio = stop
            print(url)
            consulta = requests.get(url)
            dadosjson = json.loads(consulta.content)
            for x in range(len(dadosjson)):
                self._w.writerow([dadosjson[x]['longShortRatio'],dadosjson[x]['timestamp'], dadosjson[x]['symbol']])


a = binace_csv()
a.requisita()