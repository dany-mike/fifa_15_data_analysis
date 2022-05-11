import matplotlib.pyplot as plt
import streamlit as st

def getPotentialsHistogram(difference_crystal, difference_compared, crystal_plc, compared_team):
    # Crystal palace histogram
    fig, ax = plt.subplots(figsize =(15, 9))
    ax.hist(difference_crystal, bins = [0, 5, 10, 15, 20])

    plt.xlabel("Potential")
    plt.ylabel("Number of players")
    plt.title("Distribution of the potential of the {} players".format(crystal_plc))

    # Show plot
    st.pyplot(fig)


    fig, ax = plt.subplots(figsize =(15, 9))
    ax.hist(difference_compared, bins = [0, 5, 10, 15, 20])

    plt.xlabel("Potential")
    plt.ylabel("Number of players")
    plt.title("Distribution of the potential of the {} players".format(compared_team))

    # Show plot
    st.pyplot(fig)

    

def calcPotentialOverallDiff(potential_list, overall_list, difference):
    zip_object = zip(potential_list, overall_list)
    
    for potential_i, overall_i in zip_object:
        if potential_i > overall_i: 
            difference.append(potential_i-overall_i)
    return difference

def listDescendingOrder(list_values):
    return list_values.sort(reverse=True)

def format_name_list(list_name):
    formatted_list = []
    for el in list_name:
        formatted_list.append(el[:4])
    return formatted_list

def displayPotentialList(team_name, dictionary_potential):
    option = st.selectbox(
        '{} players potential'.format(team_name),
        [[0, 5], [5, 10], [10, 15], [15, 20], [20, 25]])

    for key in dictionary_potential:
        if dictionary_potential[key] >= option[0] and dictionary_potential[key] <= option[1]:
            st.write('{}: '.format(key), dictionary_potential[key])