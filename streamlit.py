import streamlit as st
import pandas as pd
import functions.getAverage as average
import functions.common as common
import functions.getAttribute as attribute
import functions.potential as potential
import uuid

st.set_page_config(layout="wide")
fifa_15_players = pd.read_csv('players_15.csv', usecols= ['player_url', 'long_name', 'player_positions', 'overall', 'potential', 'age', 'club_name', 'league_name', 'attacking_finishing', 'passing', 'defending', 'short_name'])
eng_league = "English Premier League"
compared_team = "Chelsea"
crystal_plc = "Crystal Palace"

#Average player rate by role
average.getAveragePlayerOverallRateByTeam(common.getTeamByLeagueAndName(eng_league, crystal_plc, fifa_15_players), uuid.uuid1())

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

#FINISHING and name sorted
Crystal_finishing_list = attribute.getTeam(crystal_finishing_name, crystal_finishing)
Compared_finishing_list = attribute.getTeam(compared_finishing_name, compared_finishing)
st.pyplot(attribute.displayMainAttributeByRole(Crystal_finishing_list, Compared_finishing_list, 'Strikers from strongest to weakest', 'Finishing attribute value', 'Finishing attributes difference between Crystal Palace and Chelsea', uuid.uuid1()))

#PASSING and name sorted
Crystal_passing_list = attribute.getTeam(crystal_passing_name, crystal_passing)
Compared_passing_list = attribute.getTeam(compared_passing_name, compared_passing)
st.pyplot(attribute.displayMainAttributeByRole(Crystal_passing_list, Compared_passing_list, 'Midfields from strongest to weakest', 'Passing attribute value', 'Passing attributes difference between Crystal Palace and Chelsea', uuid.uuid1()))

#DEFENDING and name sorted
Crystal_defending_list = attribute.getTeam(crystal_defending_name, crystal_defending)
Compared_defending_list = attribute.getTeam(compared_defending_name, compared_defending)
st.pyplot(attribute.displayMainAttributeByRole(Crystal_defending_list, Compared_defending_list, 'Backs from strongest to weakest', 'Defending attribute value', 'Defending attributes difference between Crystal Palace and Chelsea', uuid.uuid1()))


#Potential 
potential_list_compared = common.getPlayersAttributes('potential',common.getTeamByLeagueAndName(eng_league, compared_team, fifa_15_players), [])
overall_list_compared = common.getPlayersAttributes('overall',common.getTeamByLeagueAndName(eng_league, compared_team, fifa_15_players), [])

potential_list_crystal = common.getPlayersAttributes('potential',common.getTeamByLeagueAndName(eng_league, crystal_plc, fifa_15_players),[])
overall_list_crystal = common.getPlayersAttributes('overall',common.getTeamByLeagueAndName(eng_league, crystal_plc, fifa_15_players), [])

name_list_compared = common.getPlayersAttributes('short_name',common.getTeamByLeagueAndName(eng_league, compared_team, fifa_15_players), [])
name_list_crystal = common.getPlayersAttributes('short_name',common.getTeamByLeagueAndName(eng_league, crystal_plc, fifa_15_players), [])

difference_compared = potential.calcPotentialOverallDiff(potential_list_compared, overall_list_compared, [])
difference_crystal = potential.calcPotentialOverallDiff(potential_list_crystal, overall_list_crystal, [])

potential.format_name_list(name_list_crystal)
potential.listDescendingOrder(difference_crystal)
potential.listDescendingOrder(difference_compared)

potential.getPotentialsHistogram(difference_crystal, difference_compared, crystal_plc, compared_team)