from matplotlib.pyplot import title
import streamlit as st

import pandas as pd
import functions.common as common
import functions.getAttribute as attribute
import functions.potential as potential
import uuid
from PIL import Image

with open('styles.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

col1Header, col2Header = st.columns([4, 1])
image = Image.open('logo_crystal_palace.png')

with col1Header:
    st.title('Crystal palace team analysis based on the fifa 15 game')
    st.write("This dashboard has been created to improve Crystal Palace's team recruitment strategy and identify weakness in the team. I got this data from the Kaggle website. The data set exposes the data of all the players of the fifa 15 video game. All the data of this data set come from the sofifa.com website. This site lists statistics of the players of the fifa video games. This dashboard allows you to visualize and compare statistics between crystal palace and other teams of the english football championship")
with col2Header:
    st.image(image, caption='10th Crystal palace')

option = st.selectbox(
    'Premier league teams',
    ['Select team', '1st Chelsea', '2nd Manchester City', '3rd Arsenal', '4th Manchester United', '6th Liverpool', '7th Southampton', '19th Burnley'])

if option != 'Select team':
    fifa_15_players = pd.read_csv('players_15.csv', usecols= ['player_url', 'long_name', 'player_positions', 'overall', 'potential', 'age', 'club_name', 'league_name', 'attacking_finishing', 'passing', 'defending', 'short_name'])
    eng_league = "English Premier League"
    compared_team = option[4:]
    crystal_plc = "Crystal Palace"

    #Get finishing attribute for strikers
    crystal_finishing = attribute.getStrikersAttributeByTeam(common.getTeamByLeagueAndName(eng_league, crystal_plc, fifa_15_players), 'attacking_finishing')
    compared_finishing = attribute.getStrikersAttributeByTeam(common.getTeamByLeagueAndName(eng_league, compared_team, fifa_15_players), 'attacking_finishing')
    crystal_finishing_name = attribute.getStrikersAttributeByTeam(common.getTeamByLeagueAndName(eng_league, crystal_plc, fifa_15_players), 'short_name')
    compared_finishing_name = attribute.getStrikersAttributeByTeam(common.getTeamByLeagueAndName(eng_league, compared_team, fifa_15_players), 'short_name')

    #Get passing attribute for midfields
    crystal_passing = attribute.getMidfieldsAttributeByTeam(common.getTeamByLeagueAndName(eng_league, crystal_plc, fifa_15_players), 'passing')
    compared_passing = attribute.getMidfieldsAttributeByTeam(common.getTeamByLeagueAndName(eng_league, compared_team, fifa_15_players), 'passing')
    crystal_passing_name = attribute.getMidfieldsAttributeByTeam(common.getTeamByLeagueAndName(eng_league, crystal_plc, fifa_15_players), 'short_name')
    compared_passing_name = attribute.getMidfieldsAttributeByTeam(common.getTeamByLeagueAndName(eng_league, compared_team, fifa_15_players), 'short_name')

    #Get defending attribute for backs
    crystal_defending = attribute.getBacksAttributeByTeam(common.getTeamByLeagueAndName(eng_league, crystal_plc, fifa_15_players), 'defending')
    compared_defending = attribute.getBacksAttributeByTeam(common.getTeamByLeagueAndName(eng_league, compared_team, fifa_15_players), 'defending')
    crystal_defending_name = attribute.getBacksAttributeByTeam(common.getTeamByLeagueAndName(eng_league, crystal_plc, fifa_15_players), 'short_name')
    compared_defending_name = attribute.getBacksAttributeByTeam(common.getTeamByLeagueAndName(eng_league, compared_team, fifa_15_players), 'short_name')

    crystal_finishing_sorted = attribute.getTeamName(crystal_finishing_name, crystal_finishing)
    compared_finishing_sorted = attribute.getTeamName(compared_finishing_name, compared_finishing)
    combine_name_finishing = crystal_finishing_sorted + compared_finishing_sorted

    crystal_passing_sorted = attribute.getTeamName(crystal_passing_name, crystal_passing)
    compared_passing_sorted = attribute.getTeamName(compared_passing_name, compared_passing)
    combine_name_passing = crystal_passing_sorted + compared_passing_sorted

    crystal_defending_sorted = attribute.getTeamName(crystal_defending_name, crystal_defending)
    compared_defending_sorted = attribute.getTeamName(compared_defending_name, compared_defending)


    #Potential sorted
    potential_list_compared = common.getPlayersAttributes('potential',common.getTeamByLeagueAndName(eng_league, compared_team, fifa_15_players), [])
    overall_list_compared = common.getPlayersAttributes('overall',common.getTeamByLeagueAndName(eng_league, compared_team, fifa_15_players), [])

    potential_list_crystal = common.getPlayersAttributes('potential',common.getTeamByLeagueAndName(eng_league, crystal_plc, fifa_15_players),[])
    overall_list_crystal = common.getPlayersAttributes('overall',common.getTeamByLeagueAndName(eng_league, crystal_plc, fifa_15_players), [])

    name_list_compared = common.getPlayersAttributes('short_name',common.getTeamByLeagueAndName(eng_league, compared_team, fifa_15_players), [])
    name_list_crystal = common.getPlayersAttributes('short_name',common.getTeamByLeagueAndName(eng_league, crystal_plc, fifa_15_players), [])

    difference_compared = potential.calcPotentialOverallDiff(potential_list_compared, overall_list_compared, [])
    difference_crystal = potential.calcPotentialOverallDiff(potential_list_crystal, overall_list_crystal, [])

    dictionary_potential_crystal = dict(zip(name_list_crystal, difference_crystal))
    dictionary_potential_compared = dict(zip(name_list_compared, difference_compared))

    potential.format_name_list(name_list_crystal)
    potential.listDescendingOrder(difference_crystal)
    potential.listDescendingOrder(difference_compared)

    potential.getPotentialsHistogram(difference_crystal, difference_compared, crystal_plc, compared_team)

    #FINISHING and name sorted
    Crystal_finishing_list = attribute.getTeam(crystal_finishing_name, crystal_finishing)
    Compared_finishing_list = attribute.getTeam(compared_finishing_name, compared_finishing)
    col1Attr, col2Attr, col3Attr = st.columns(3)
    with col1Attr:
        st.pyplot(attribute.displayMainAttributeByRole(Crystal_finishing_list, Compared_finishing_list, 'Strikers from strongest to weakest', 'Value of the finish attribute', 'Finishing stats difference between Crystal Palace and {}'.format(option[4:]), uuid.uuid1(), attribute.formatAttributePlayerName(crystal_finishing_sorted, compared_finishing_sorted), option[4:]))

    #PASSING and name sorted
    Crystal_passing_list = attribute.getTeam(crystal_passing_name, crystal_passing)
    Compared_passing_list = attribute.getTeam(compared_passing_name, compared_passing)
    with col2Attr:
        st.pyplot(attribute.displayMainAttributeByRole(Crystal_passing_list, Compared_passing_list, 'Midfields from strongest to weakest', 'Value of the pass attribute', 'Passing stats difference between Crystal Palace and {}'.format(option[4:]), uuid.uuid1(), attribute.formatAttributePlayerName(crystal_passing_sorted, compared_passing_sorted), option[4:]))

    #DEFENDING and name sorted
    Crystal_defending_list = attribute.getTeam(crystal_defending_name, crystal_defending)
    Compared_defending_list = attribute.getTeam(compared_defending_name, compared_defending)
    with col3Attr:
        st.pyplot(attribute.displayMainAttributeByRole(Crystal_defending_list, Compared_defending_list, 'Backs from strongest to weakest', 'Value of the defence attribute', 'Defending stats difference between Crystal Palace and {}'.format(option[4:]), uuid.uuid1(), attribute.formatAttributePlayerName(crystal_defending_sorted, compared_defending_sorted), option[4:]))

    #Potentials list
    potential.displayPotentialList(compared_team, dictionary_potential_compared)
    potential.displayPotentialList(crystal_plc, dictionary_potential_crystal)