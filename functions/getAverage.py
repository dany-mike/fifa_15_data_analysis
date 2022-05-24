from turtle import color
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import functions.common as common
import functions.helpers as helpers

def getStd(my_list):
    return np.std(my_list)

def Average(lst):
    return sum(lst) / len(lst)

def formatPlayerRole(role, quantity, position=1):
    plt.text(position, 75, "N={}".format(quantity), fontsize = 14)
    return "{}".format(role)

def addPositionbyRoleAndTeam(main_position, unique_role, team,  position_index, position_list, desired_position):
    overall_team = team['overall']
    if main_position == unique_role and main_position == desired_position:
        for overall_index, overall in enumerate(overall_team):
            if overall_index == position_index:
                position_list.append(overall)

def getAveragePlayerOverallRateByTeam(team, unique_id):
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
        for unique_role in common.getUniqueRolesByTeam(team):
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
    overrall_average_position_list.append(helpers.roundValue(Average(GK)))
    overrall_average_position_list.append(helpers.roundValue(Average(CB)))
    overrall_average_position_list.append(helpers.roundValue(Average(RB)))
    overrall_average_position_list.append(helpers.roundValue(Average(LB)))
    overrall_average_position_list.append(helpers.roundValue(Average(CDM)))
    overrall_average_position_list.append(helpers.roundValue(Average(CM)))
    overrall_average_position_list.append(helpers.roundValue(Average(RM)))
    overrall_average_position_list.append(helpers.roundValue(Average(LM)))
    overrall_average_position_list.append(helpers.roundValue(Average(CAM)))
    overrall_average_position_list.append(helpers.roundValue(Average(ST)))
    fig = plt.figure(unique_id, figsize=(8, 5))
    x=[formatPlayerRole('GK', len(GK), -0.25), formatPlayerRole('CB', len(CB), 0.8), formatPlayerRole('RB', len(RB), 1.8), formatPlayerRole('LB', len(LB), 2.8), formatPlayerRole('CDM', len(CDM), 3.8), formatPlayerRole('CM', len(CM), 4.8), formatPlayerRole('RM', len(RM), 5.8), formatPlayerRole('LM', len(LM), 6.8), formatPlayerRole('CAM', len(CAM), 7.8), formatPlayerRole('ST', len(ST), 8.8)]
    std_y=[getStd(GK), getStd(CB), getStd(RB), getStd(LB), getStd(CDM), getStd(CM), getStd(RM), getStd(LM), getStd(CAM), getStd(ST)]
    y= overrall_average_position_list
    plt.xlabel("Player role", fontdict={'fontsize':14})
    plt.xticks(fontsize=13)
    plt.yticks(fontsize=13)
    plt.ylabel("Overall rate value", fontdict={'fontsize':14})
    plt.title("Overall rate by player roles for Crystal Palace players", fontdict={'fontsize':15})
    plt.errorbar(x, y, yerr=std_y, fmt="o", color="#EE4B2B")
    plt.bar(x,y, color="#92B4EC")
    return st.pyplot(fig)
