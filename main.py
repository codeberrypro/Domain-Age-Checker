import requests
from bs4 import BeautifulSoup
import fake_useragent
import time

'''
Check only http url, if you want to change url to https do the follows:
 ==>   lines = [line.strip()[12:] for line in file]
'''
user = fake_useragent.UserAgent().random
headers = {
    'user-agent': user
}

# https[12:]  http[11:]
with open('domains') as file:
    lines = [line.strip()[11:] for line in file]

    for domains in lines:
        time.sleep(1)
        url = f'https://www.nic.ru/whois/?searchWord={domains}'
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        try:
            information = soup.find(class_='_3U-mA _23Irb')
            inf = information.text.splitlines()
            for x in inf:
                if 'created:' in x:
                    creation_date = x.split('created:')[-1].strip()
                    creation_date = creation_date[:4]
                    print(f'{domains}: {creation_date}')
                elif 'Creation Date' in x:
                    creation_date = x.split('Creation Date')[-1].strip()
                    creation_date = creation_date[:4]
                    print(f'{domains}: {creation_date}')
        except:
            print(f'{domains}: не удалось проверить')








