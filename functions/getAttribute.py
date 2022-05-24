import functions.common as common
import matplotlib.pyplot as plt
import numpy as np

def getStrikersAttributeByTeam(team, attribute):
    attributes_list = []
    positions_team = team['player_positions']
    for position_index, position in enumerate(positions_team):
        main_position = list(position.split(','))[0]
        for unique_role in common.getUniqueRolesByTeam(team):
            getPlayersAttributesByMainPosition(main_position, unique_role, attribute, position_index, team, 'ST', attributes_list)
    return attributes_list
            
def getMidfieldsAttributeByTeam(team, attribute):
    attributes_list = []
    positions_team = team['player_positions']
    for position_index, position in enumerate(positions_team):
        main_position = list(position.split(','))[0]
        for unique_role in common.getUniqueRolesByTeam(team):
            getPlayersAttributesByMainPosition(main_position, unique_role, attribute, position_index, team, 'CDM', attributes_list)
            getPlayersAttributesByMainPosition(main_position, unique_role, attribute, position_index, team, 'CM', attributes_list)
            getPlayersAttributesByMainPosition(main_position, unique_role, attribute, position_index, team, 'RM', attributes_list)
            getPlayersAttributesByMainPosition(main_position, unique_role, attribute, position_index, team, 'LM', attributes_list)
            getPlayersAttributesByMainPosition(main_position, unique_role, attribute, position_index, team, 'CAM', attributes_list)
    return attributes_list

def getBacksAttributeByTeam(team, attribute):
    attributes_list = []
    positions_team = team['player_positions']
    for position_index, position in enumerate(positions_team):
        main_position = list(position.split(','))[0]
        for unique_role in common.getUniqueRolesByTeam(team):
            getPlayersAttributesByMainPosition(main_position, unique_role, attribute, position_index, team, 'CB', attributes_list)
            getPlayersAttributesByMainPosition(main_position, unique_role, attribute, position_index, team, 'RB', attributes_list)
            getPlayersAttributesByMainPosition(main_position, unique_role, attribute, position_index, team, 'LB', attributes_list)
    return attributes_list

def getAllPlayersAttributeByTeam(team, attribute):
    attributes_list = []
    positions_team = team['player_positions']
    for position_index, position in enumerate(positions_team):
        main_position = list(position.split(','))[0]
        for unique_role in common.getUniqueRolesByTeam(team):
            getPlayersAttributesByMainPosition(main_position, unique_role, attribute, position_index, team, 'ST', attributes_list)
            getPlayersAttributesByMainPosition(main_position, unique_role, attribute, position_index, team, 'CDM', attributes_list)
            getPlayersAttributesByMainPosition(main_position, unique_role, attribute, position_index, team, 'CM', attributes_list)
            getPlayersAttributesByMainPosition(main_position, unique_role, attribute, position_index, team, 'RM', attributes_list)
            getPlayersAttributesByMainPosition(main_position, unique_role, attribute, position_index, team, 'LM', attributes_list)
            getPlayersAttributesByMainPosition(main_position, unique_role, attribute, position_index, team, 'CAM', attributes_list)
            getPlayersAttributesByMainPosition(main_position, unique_role, attribute, position_index, team, 'CB', attributes_list)
            getPlayersAttributesByMainPosition(main_position, unique_role, attribute, position_index, team, 'RB', attributes_list)
            getPlayersAttributesByMainPosition(main_position, unique_role, attribute, position_index, team, 'LB', attributes_list)
    return attributes_list

def getPlayersAttributesByMainPosition(main_position, unique_role, attribute_name, player_index, team, desired_position, attributes_list):
    attribute_team = team[attribute_name]
    if main_position == unique_role and main_position == desired_position:
        for attribute_index, attribute in enumerate(attribute_team):
            if attribute_index == player_index:
                attributes_list.append(attribute)

def sortDictionary(dictionary):
    sorted_values = sorted(dictionary.values(), reverse=True)
    sorted_dict = {}

    for i in sorted_values:
        for k in dictionary.keys():
            if dictionary[k] == i:
                sorted_dict[k] = dictionary[k]
                break
    return sorted_dict

def formatListsToDict(players_name, values_list):
    empty_dict = {}
    for index, el in enumerate(players_name):
        empty_dict[el] = values_list[index]
    return empty_dict

def sortAttributeList(dictionary, list, limit):
    for i in dictionary:
        if len(list) < limit:
            list.append(dictionary[i])
    return list

def sortAttributeListIndex(dictionary, list, limit):
    for key in dictionary.keys():
        if len(list) < limit:
            list.append(key)
    return list

def sortPlayerList(dictionary, list, limit):
    for i in dictionary:
        if len(list) < limit:
            list.append(i)
    return list

def getTeam(name: list, attribute: list):
    sorted_dictionary = sortDictionary(formatListsToDict(name, attribute))

    sorted_attribute_list = []

    team = sortAttributeList(sorted_dictionary, sorted_attribute_list, 3)

    return team

def getTeamName(name: list, attribute: list):
    sorted_dictionary = sortDictionary(formatListsToDict(name, attribute))

    sorted_attribute_list = []

    teamName = sortAttributeListIndex(sorted_dictionary, sorted_attribute_list, 3)

    return teamName

def displayMainAttributeByRole(Crystal: list, Compared_team: list, x_label, y_label, title, id, players_name_list):
    n=3
    r = np.arange(n)
    width = 0.25
    fig = plt.figure(id, figsize=(8, 5))
    plt.bar(r, Crystal, color = '#92B4EC',
            width = width, edgecolor = 'black',
            label='Crystal Palace')
    plt.bar(r + width, Compared_team, color = '#FFE69A',
            width = width, edgecolor = 'black',
            label='Chelsea')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.xticks(r + width/2,players_name_list)
    plt.legend()
    return fig

def formatAttributePlayerName(arr1, arr2):
    arr3 = []
    for i, value in enumerate(arr2):
        arr3.append((arr1[i] +  '\n' + value))
    return arr3