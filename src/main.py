import os
import requests

if __name__=='__main__':
    key = os.environ['OWM_API_KEY']
    url = f'https://api.openweathermap.org/data/2.5/forecast?lat=12.9669&lon=77.739831&appid={key}'
    res = requests.get(url)
    print(res.json())