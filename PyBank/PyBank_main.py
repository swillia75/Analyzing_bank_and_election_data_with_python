# assign initial variables
date = str(dates[0])
profit = long(profits_losses[1])
date_list = []

#assignn values to max/min counters
max_profit = 0
max_losses = 0

#import os
import os

#import csv to read file
import csv

# Path to collect data from the Resources folder
PyBank_csv = os.path.join("Resources","budget_data.csv")

# Open the CSV
with open(PyBank_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

 #Total months in dataset
total_months = len(date_list)

#The net total amount "profits/losses" over entire period
total = sum(row[1])

#The average of changes in "profits/losses" over entire period
average_change = average(row[1])

#The greatest increase in profits (date and amount) over entire period
if (row[1]) > max_profit:
    max_profit = row[1]
    max_profit_date = row[0]

#The greatest decrease in losses (date and amount) over entire period
    Elif (row[1]) < max_profit
    max_losses = row[1]
    min_losses_date = row[0]
   
        
    #Final analysis printout
    print("Financial Analysis")
    print("------------------------------------")
    print("Total Months:" + "  " + int(total_months))
    print("Total:" + "  " + long(total))
    print("Average Change:" + "  " + float(average_change))
    print("Greatest increase in Profits:" + "  " + str(row[0]) + long(profits)
    print("Greatest decrease in Profits:" + "  " + str(row[0]) + long(profits)