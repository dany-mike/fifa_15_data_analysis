import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

st.set_page_config(layout="wide")
fifa_15_players = pd.read_csv('players_15.csv', usecols= ['player_url', 'long_name', 'player_positions', 'overall', 'potential', 'age', 'club_name', 'league_name', 'attacking_finishing', 'passing', 'defending', 'short_name'])
eng_league = "English Premier League"
compared_team = "Chelsea"
crystal_plc = "Crystal Palace"

def getTeamByLeagueAndName(league, name):
    english_premier_league_players = fifa_15_players.loc[fifa_15_players['league_name'] == league]
    returned_team = english_premier_league_players.loc[english_premier_league_players['club_name'] == name]
    return returned_team

def addPositionbyRoleAndTeam(main_position, unique_role, team,  position_index, position_list, desired_position):
    overall_team = team['overall']
    if main_position == unique_role and main_position == desired_position:
        for overall_index, overall in enumerate(overall_team):
            if overall_index == position_index:
                position_list.append(overall)

def roundValue(value):
    return round(value)

def getUniqueRolesByTeam(team):
    positions_team = team['player_positions']
    positions_list = []

    for position in positions_team:
        position = list(position.split(','))[0]
        positions_list.append(position)
    return list(dict.fromkeys(positions_list))

def getAveragePlayerOverallRateByTeam(team):
    GK = []
    CB = []
    RB = []
    LB = []
    CDM = []
    CM = []
    RM = []
    LM = []
    CAM = []
    ST = []
    positions_team = team['player_positions']
    for position_index, position in enumerate(positions_team):
        main_position = list(position.split(','))[0]
        for unique_role in getUniqueRolesByTeam(team):
            addPositionbyRoleAndTeam(main_position, unique_role, team, position_index, GK, 'GK')
            addPositionbyRoleAndTeam(main_position, unique_role, team, position_index, CB, 'CB')
            addPositionbyRoleAndTeam(main_position, unique_role, team, position_index, RB, 'RB')
            addPositionbyRoleAndTeam(main_position, unique_role, team, position_index, LB, 'LB')
            addPositionbyRoleAndTeam(main_position, unique_role, team, position_index, CDM, 'CDM')
            addPositionbyRoleAndTeam(main_position, unique_role, team, position_index, CM, 'CM')
            addPositionbyRoleAndTeam(main_position, unique_role, team, position_index, RM, 'RM')
            addPositionbyRoleAndTeam(main_position, unique_role, team, position_index, LM, 'LM')
            addPositionbyRoleAndTeam(main_position, unique_role, team, position_index, CAM, 'CAM')
            addPositionbyRoleAndTeam(main_position, unique_role, team, position_index, ST, 'ST')
    overrall_average_position_list = []
    overrall_average_position_list.append(roundValue(Average(GK)))
    overrall_average_position_list.append(roundValue(Average(CB)))
    overrall_average_position_list.append(roundValue(Average(RB)))
    overrall_average_position_list.append(roundValue(Average(LB)))
    overrall_average_position_list.append(roundValue(Average(CDM)))
    overrall_average_position_list.append(roundValue(Average(CM)))
    overrall_average_position_list.append(roundValue(Average(RM)))
    overrall_average_position_list.append(roundValue(Average(LM)))
    overrall_average_position_list.append(roundValue(Average(CAM)))
    overrall_average_position_list.append(roundValue(Average(ST)))
    x=[formatPlayerRole('GK', len(GK), -0.25), formatPlayerRole('CB', len(CB), 0.8), formatPlayerRole('RB', len(RB), 1.8), formatPlayerRole('LB', len(LB), 2.8), formatPlayerRole('CDM', len(CDM), 3.8), formatPlayerRole('CM', len(CM), 4.8), formatPlayerRole('RM', len(RM), 5.8), formatPlayerRole('LM', len(LM), 6.8), formatPlayerRole('CAM', len(CAM), 7.8), formatPlayerRole('ST', len(ST), 8.8)]
    std_y=[getStd(GK), getStd(CB), getStd(RB), getStd(LB), getStd(CDM), getStd(CM), getStd(RM), getStd(LM), getStd(CAM), getStd(ST)]
    y= overrall_average_position_list 
    fig = plt.figure(1, 2)
    plt.xlabel("Quantity of players main roles")
    plt.ylabel("Player overall rate value")
    plt.title("Crystal Palace average player overall rate value by player roles")
    plt.errorbar(x, y, yerr=std_y, fmt="o", color="r")
    plt.bar(x,y)
    col1, col2, = st.columns([9, 1])
    with col1:
        st.pyplot(fig)

    with col2:
        st.image("https://static.streamlit.io/examples/dog.jpg")
   

def getStd(my_list):
    return np.std(my_list)

def Average(lst):
    return sum(lst) / len(lst)

def formatPlayerRole(role, quantity, position=1):
    plt.text(position, 75, "N={}".format(quantity), fontsize = 6)
    return "{}".format(role)

getAveragePlayerOverallRateByTeam(getTeamByLeagueAndName(eng_league, crystal_plc))



