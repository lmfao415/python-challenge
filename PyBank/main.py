import os
import csv

total_months = 0
total_profit = 0

max_value = -999999999
min_value = 999999999
max_month = ""
min_month = ""
last_profit = 0
first_profit = 0
csvpath = os.path.join('Resources', 'budget_data.csv')
with open(csvpath, "r") as csvfile:   
    csvreader = csv.reader(csvfile, delimiter=",")

    header = next(csvreader)
   
    for row in csvreader:
        profit = int(row[1])
        month = row[0]
        if total_months == 0:
            last_profit = profit
            first_profit = profit
        else:
            monthly_change = profit - last_profit
            if monthly_change < min_value:
                min_value = monthly_change
                min_month = month
            if monthly_change > max_value:
                max_value = monthly_change
                max_month = month
            last_profit = profit
        total_months += 1
        total_profit = total_profit + profit
    average_profit_change = (last_profit - first_profit) / (total_months - 1)
print("Financial Analysis")
print("-------------------------------")
print(f"Total Months: {total_months}")
print(f"Total Profit: ${total_profit:0,.2f}")
print(f"Average Monthly Change: ${average_profit_change:0,.2f}")
print(f"Greatest Increase in Monthly Profits: ({max_month} : ${max_value:0,.2f})")
print(f"Greatest Decrease in Monthly Profits: ({min_month} : ${min_value:0,.2f})")

output_path = os.path.join("analysis", "budget_analysis")
with open(output_path, 'w', newline='') as txtfile:
    txtfile.write(f"Financial Analysis\n------------------------------- \n")
    txtfile.write(f"Total Months: {total_months} \n")
    txtfile.write(f"Total Profit: ${total_profit:0,.2f} \n")
    txtfile.write(f"Average Monthly Change: ${average_profit_change:0,.2f} \n")
    txtfile.write(f"Greatest Increase in Monthly Profits: ({max_month} : ${max_value:0,.2f}) \n")
    txtfile.write(f"Greatest Decrease in Monthly Profits: ({min_month} : ${min_value:0,.2f}) \n")



