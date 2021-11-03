from bs4 import BeautifulSoup
import requests
import datetime


def getSoup(url):
    html_content = requests.get(url).text
    result = BeautifulSoup(html_content, "html5lib")
    return result

def getRanking():
    months = {1: 'january', 2: 'february', 3: 'march', 4: 'april', 5: 'may',
              6: 'june', 7: 'july', 8: 'august', 9: 'september', 10: 'october', 11: 'november', 12: 'december'}
    date = datetime.date.today()
    day = date.day - 1
    num_month = date.month
    year = date.year

    url = f'https://www.hltv.org/ranking/teams/{year}/{months[num_month]}/{day}'

    soup = getSoup(url)
    head = soup.find('div', class_='regional-ranking-header').get_text('regional-ranking-header')
    ranks = soup.find('div', class_='ranking').find_all('div', class_='ranked-team standard-box')

    result = head+'\n'
    for rank in ranks:
        team_pos = rank.find('div',class_='bg-holder').find('span').get_text()
        team_logo = rank.find('div',class_='bg-holder').find('span', class_='team-logo').find('img').get('title')
        team_score = rank.find('div',class_='bg-holder').find('span', class_='points').get_text()
        result += f'{team_pos} {team_logo} {team_score} \n'
    return result

print(getRanking())







# soup = getSoup("https://www.hltv.org/matches/2352506/virtuspro-vs-faze-pgl-major-stockholm-2021")
# print(getTeams(soup))