# I worked with another student, Chelsea Cullen, over Zoom on 4/14 and we worked through the steps together.
#Instructor and TA gave steps for finding average before class on 4/15

import os
import csv

budget_data_csv = os.path.join('Resources', 'budget_data.csv')


# Needed variables similar to VBA set-up
total_months = 0
total_profits = 0
current_profit = 0
previous_month = 0
max_value = float('-inf')
max_date = None
min_value = float("inf")
min_date = None
total_change_in_profit = 0
is_first_row = True

# Open and read csv
with open(budget_data_csv, encoding='UTF-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
  
# Read but skip the header row first 
    csv_header = next(csv_file)

# Loop to find the total number of months included in the dataset.
# Net total amount of "Profit/Losses" over entire period...VBA stock market similarity?
 
    for row in csv_reader:
        last_month_profit = current_profit
        total_months += 1
        current_profit = float(row[1]) 
        total_profits += current_profit
        
  
# Used XPert Learning Assistant to find an example structure. Sort of helpful-wanted to use Pandas
 
# The greatest increase in profits (date and amount) over the entire period
# if > or < number before

        date = row[0]
        change_in_profit = current_profit - last_month_profit

# Finding the change in profits between dates. Need if/else to ignore the first row since no change/not starting at 0
# Account for the first row technically at 0/no change yet
        if not is_first_row:
            total_change_in_profit += change_in_profit
        else: 
            is_first_row = False

# The greatest increase in profits (date and amount) over the entire period         

        if change_in_profit > max_value:
            max_value = change_in_profit
            max_date = date

# The greatest decrease in profits (date and amount) over the entire period
        date = row[0]
        if change_in_profit < min_value:
            min_value = change_in_profit
            min_date = date

# The changes in "Profit/Losses" over entire period and then average the changes 
# Average has to be one less month than the total months since no change in first row
    average = total_change_in_profit/(total_months-1)
    
# Combining it together for final summary.  Used similar format as the state/student grad example from 4/11 class
# https://stackoverflow.com/questions/53162/how-can-i-do-a-line-break-line-continuation-in-python-split-up-a-long-line-of 
    bank_summary = "Financial Analysis"
    bank_summary = "-----------------------------------------------------\n"
    bank_summary+=f'Total months= {total_months}\n'
    bank_summary+=f'Total= ${total_profits}\n'
    bank_summary+=f'Average= ${average}\n'
    bank_summary+=f'Greatest Increase in Profits= {max_date}  (${max_value})\n'
    bank_summary+=f'Greatest Decrease in Profits= {min_date}  (${min_value})\n'

# Export to text file 
output = os.path.join('Analysis', 'Bank_analysis')
with open(output, "w", newline='') as datafile:
    writer = csv.writer(datafile) 

    print("Financial Analysis", file=datafile)
    print(bank_summary, file=datafile)



