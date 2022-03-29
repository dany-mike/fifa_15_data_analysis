import csv

#Read first element of the csv
with open('/home/dany/data_analysis/players_stats.csv', 'r') as players_stats:
    reader = csv.reader(players_stats, delimiter=',')
    for row in reader:
        print(row[0])