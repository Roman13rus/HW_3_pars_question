import requests
import json
import time
from pprint import pprint

class Parser:  #Создаем класс принимающий 1 параметр -тег
    
    def __init__(self, tags):
        self.tags = tags

    def colletor(self, URL):  #Создаем метод поиска принимающий URL 
        # преобразование даты в unix формат
        fromdate = int(time.mktime(time.strptime('2023-03-03 00:00:00', '%Y-%m-%d %H:%M:%S')))
        todate = int(time.mktime(time.strptime('2023-03-06 22:00:00', '%Y-%m-%d %H:%M:%S')))

        params = {'tagged':self.tags,'fromdate':fromdate,'todate': todate,'page':25,'order':'asc',
                   'sort':'creation','site':'stackoverflow'}
        response = requests.get(URL, params=params)
        print(response.status_code)
        data = response.json()
        if response:
            result = len(data["items"])
            print(f'Всего по данному тегу найдено {result} вопросов.')
            pprint(data)
            
        return data

    def writer(self):                       #функция для записи результатов ответа сайта(при необходимости)
        with open('parser_data.json', 'w') as file:
            json.dump(self.colletor(URL),file, ensure_ascii = False, indent=2)

        #print(response.content)
        


pars = Parser(['Python'])
URL = 'https://api.stackexchange.com/2.3/questions'
#pars.colletor(URL) 
pars.writer()
