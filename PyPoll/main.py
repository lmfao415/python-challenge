import os
import csv #import dependencies

csvpath = os.path.join('Resources', 'election_data.csv')
with open(csvpath, "r") as csvfile:   
    csvreader = csv.reader(csvfile, delimiter=",") #read csv file

    header = next(csvreader) #save/skip csv header
    candidates ={} #set a dictionary to hold candidates and votes
    total_votes = 0
    
    for row in csvreader:  #read through each row in csv file
        if row[2] not in candidates:  #adds candidate to dictionary if not included already
            candidates[row[2]] = 0
        candidates[row[2]] +=1 #updates the amount of votes a candidate has
        total_votes += 1 #calculates the number of total votes

print(f"Election Results") # prints the results to terminal
print(f"-------------------------")
print(f"Total Votes: {total_votes}")
print(f"-------------------------")
for x in candidates:  #goes through candidates dictionary and reports values
    print(f"{x}: {(candidates[x] / total_votes*100):0,.3f}% ({candidates[x]})")
print(f"-------------------------")
print(f"Winner: {max(candidates, key=candidates.get)}") #reports the candidate with the highest number of votes
print(f"-------------------------")

output_path = os.path.join("analysis", "election_results") #prints reults to txt file
with open(output_path, 'w', newline='') as txtfile:
    txtfile.write(f"Election Results\n------------------------------- \n")
    txtfile.write(f"Total Votes: {total_votes}\n-------------------------------\n")
    for x in candidates: #goes through candidates dictionary and reports values
        txtfile.write(f"{x}: {(candidates[x] / total_votes*100):0,.3f}% ({candidates[x]})\n") 
    txtfile.write(f"Winner: {max(candidates, key=candidates.get)}\n") #reports the candidate with the highest number of votes
    txtfile.write(f"-------------------------------\n")
   

