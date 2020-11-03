import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')
with open(csvpath, "r") as csvfile:   
    csvreader = csv.reader(csvfile, delimiter=",")

    header = next(csvreader)
    candidates ={}
    total_votes = 0
    
    for row in csvreader:
        if row[2] not in candidates:
            candidates[row[2]] = 0
        candidates[row[2]] +=1
        total_votes += 1

print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes: {total_votes}")
print(f"-------------------------")
for x in candidates:
    print(f"{x}: {(candidates[x] / total_votes*100):0,.3f}% ({candidates[x]})")

print(f"-------------------------")
print(f"Winner: {max(candidates, key=candidates.get)}")
print(f"-------------------------")

output_path = os.path.join("analysis", "election_results")
with open(output_path, 'w', newline='') as txtfile:
    txtfile.write(f"Election Results\n------------------------------- \n")
    txtfile.write(f"Total Votes: {total_votes}\n-------------------------------\n")
    for x in candidates:
        txtfile.write(f"{x}: {(candidates[x] / total_votes*100):0,.3f}% ({candidates[x]})\n")
    txtfile.write(f"-------------------------------\n")
    txtfile.write(f"Winner: {max(candidates, key=candidates.get)}\n")
    txtfile.write(f"-------------------------------")

