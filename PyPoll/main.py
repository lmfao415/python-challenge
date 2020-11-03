import os
import csv
total_votes = 0

csvpath = os.path.join('Resources', 'election_data.csv')
with open(csvpath, "r") as csvfile:   
    csvreader = csv.reader(csvfile, delimiter=",")

    header = next(csvreader)
    
    for row in csvreader:
        total_votes += 1


print(f"Total Votes : {total_votes}")
