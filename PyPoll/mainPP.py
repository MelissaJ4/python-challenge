import os
import csv

election_data_csv = os.path.join('Resources', 'election_data.csv')

# Needed variables for csv
total_votes = 0
max_votes = 0

# Open and read csv
with open(election_data_csv, encoding='UTF-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
  
# Read but skip the header row first 
    csv_header = next(csv_file)

# Create an open dictionary for candidates-unknown names
    candidate_votes = {}    
# Total number of votes cast
# A complete list of candidates who received votes-tracking candidate names
# The total number of votes each candidate won

    for row in csv_reader:
        # To track voting total and total votes per candidate
        total_votes +=1
        name = (row[2])
        # if loop to look for names and then add a vote once name is found
        # keys function explained by instructor before class on 4/16
        if name in candidate_votes.keys():
            candidate_votes[name] += 1
        else:
            candidate_votes[name]=1

# The percentage of votes each candidate won
    for name in candidate_votes:
        votes_percentage = (candidate_votes[name])/total_votes

# The winner of the election based on popular vote
    #candidate with max_percentage?
# winner = max(candidate_votes[name])

# Print the result

election_summary = "Election Results"
election_summary = "----------------------------------------------------------\n"
election_summary +=f"Total votes= {total_votes}\n"
election_summary = "----------------------------------------------------------\n"
for name in candidate_votes.keys():
    election_summary+=f'{name} {candidate_votes[name]} {votes_percentage}\n'
election_summary = "----------------------------------------------------------\n"
# election_summary =f'"Winner" + {winner}\n'
print("Election Results")
print (election_summary)

# Export to text file 
#output = os.path.join('Analysis', 'Election_results')
#with open(output, "w", newline='') as datafile:
    #writer = csv.writer(datafile) 

    #print("Election Results", file=datafile)
    #print(bank_summary, file=datafile)