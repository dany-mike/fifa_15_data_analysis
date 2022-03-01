from bs4 import BeautifulSoup
import requests
import csv

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
    player_name = player.find_all(class_="ellipsis")[0].text
    pos_list = []
    for pos in player.find_all(class_="pos"):
        pos_list.append(pos.text)
    player_positions = pos_list
    player_age = player.find_all(class_="col-ae")[0].text
    player_note = player.find_all(class_="bp3-tag")[0].text
    player_potential = player.find_all(class_="bp3-tag")[1].text
    player_total = player.find_all(class_="bp3-tag")[2].text
    player_club = player.find_all(class_="ellipsis")[1].a.text
    player_value = player.find_all(class_="col-vl")[0].text
    player_weekly_salary = player.find_all(class_="col-wg")[0].text
    player_weekly_salary