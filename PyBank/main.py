import os
import csv


total_months = 0
total = 0



csvpath = os.path.join('Resources', 'budget_data.csv')
with open(csvpath, "r") as csvfile:   
    csvreader = csv.reader(csvfile, delimiter=",")

    header = next(csvreader)
   
    for row in csvreader:
        total_months += 1
        total = total + int(row[1])

print(f"Total Months: {total_months}")
print(f"Total Profit: ${total:0,.2f}")

    