import os
import csv

 month = 0

csvpath = os.path.join('Resources', 'budget_data.csv')
with open(csvpath, "r") as csvfile:   
    csvreader = csv.reader(csvfile, delimiter=",")

    header = next(csvreader)
   
    

    