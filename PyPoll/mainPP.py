import os
import csv

election_data_csv = os.path.join('Resources', 'election_data.csv')


# Needed variables similar 
total_votes = 0
candidates = []
Stockham = 0
DeGette = 0
Doane = 0
max_percent = 0

# Open and read csv
with open(election_data_csv, encoding='UTF-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
  
# Read but skip the header row first 
    csv_header = next(csv_file)

# Total number of votes cast
# A complete list of candidates who received votes
# The total number of votes each candidate won

    for row in csv_reader:

        total_votes +=1
        candidates = row[2]
    
        if row[2] == "Stockham":
            Stockham +=1
        elif row[2] == "DeGette":
            DeGette +=1
        else row[2] == "Doane":
            Doane +=1


# The percentage of votes each candidate won
Stockham_percent = Stockham/total_votes*100
DeGette_percent = DeGette/total_votes*100
Doane_percent = Doane/total_votes*100


# The winner of the election based on popular vote
    #candidate with max_percentage?


# Print the result

election_summary = "Election Results"
election_summary = 
"----------------------------------------------------------\n"
election_summary+=f'Total votes= {total_votes}\n'
 