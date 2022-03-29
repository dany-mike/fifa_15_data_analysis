from bs4 import BeautifulSoup
import requests

# importing the libraries
from bs4 import BeautifulSoup
import requests

url="https://sofifa.com/?r=150059&set=true&offset=0"

# Make a GET request to fetch the raw HTML content
html_content = requests.get(url).text

# Parse the html content
soup = BeautifulSoup(html_content, "lxml")

players_table = soup.find('table')
players_table_data = players_table.tbody.find_all('tr')

for player in players_table_data:
    player_total = player.find_all(class_="bp3-tag")[2].text
    player_value = player.find_all(class_="col-vl")[0].text
    player_weekly_salary = player.find_all(class_="col-wg")[0].text
    # print(player_weekly_salary)
    # print(player_value)
    # print(player_total)