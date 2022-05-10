def getTeamByLeagueAndName(league, name, fifa_15_players):
    english_premier_league_players = fifa_15_players.loc[fifa_15_players['league_name'] == league]
    returned_team = english_premier_league_players.loc[english_premier_league_players['club_name'] == name]
    return returned_team

def getUniqueRolesByTeam(team):
    positions_team = team['player_positions']
    positions_list = []

    for position in positions_team:
        position = list(position.split(','))[0]
        positions_list.append(position)
    return list(dict.fromkeys(positions_list))
