import httpx
from flask import Flask
from os.path import exists
from bs4 import BeautifulSoup


app = Flask(__name__)

def skills():
    headers = {'User-agent': 'Mozilla/5.0'}
    if not exists('skill_result.html'):
        skill_list = httpx.get(url='https://poedb.tw/us/Active_Skill_Gems', headers=headers).text
        with open('skill_result.html', 'w', encoding='utf-8') as f:
            f.write(skill_list)
    else:
        with open('skill_result.html', 'r', encoding='utf-8') as f:
            skill_list = f.read()
    url = []
    names = []
    soup = BeautifulSoup(skill_list, features="html.parser").find_all('tbody')[0]
    skill_name = soup.find_all_next('a', class_='itemclass_gem')
    skill_url = soup.find_all_next('a')
    for i in skill_url:
        if not i['href'] in url:
            url.append(i['href'])

    for i in skill_name:
        if not i.get_text() in names:
            names.append(i.get_text())

    """with open('skill_prety', 'w') as f:
        f.write('\n'.join((('poedb.tw' + str(u) + ', ' + str(n)) for u,n in zip(url[:306], names))))"""


    print('\n'.join((('poedb.tw' + str(u) + ', ' + str(n)) for u,n in zip(url[:306], names))))



@app.route('/')
def index():
    pass


if __name__ == '__main__':
    skills()
    #app.run()