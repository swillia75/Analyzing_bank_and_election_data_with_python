#import os
import os

#import csv to read file
import csv

#define variables


# start counters
total=0
max_profit = 0
max_losses = 0
# Path to collect data from the Resources folder
PyBank_csv = os.path.join("Resources","budget_data.csv")


# Open and read the CSV
with open(PyBank_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #reader header
    csv_header = next(csvfile)

    #create list
    budget_list = list(csvreader)

    
     #Calculate Total months 
    total_months = len(budget_list) 

    #The net total amount "profits/losses" over entire period
    for row in budget_list:
        
        total += int(row[1])
        total_formatted = "${:.0f}".format(total)
       
    #average change for "profits/losses" over entire period
        average_change = (total / total_months)
        average_change_formatted = "${:.2f}".format(average_change)

#The greatest increase in profits (date and amount) over entire period
    
        if (int(row[1])) > max_profit:
            max_profit = int(row[1])
            max_profit_date = str(row[0])
            max_profit_formatted = "${:.0f}".format(max_profit)

         

#The greatest decrease in losses (date and amount) over entire period

        elif (int(row[1])) < max_losses:
            max_losses = int(row[1])
            max_losses_date = str(row[0])
            max_losses_formatted = "${:.0f}".format(max_losses).replace('$-','-$')
  
        
    

    

    #Final analysis printout

    print("Financial Analysis", file=open("PyBank analysis/output.txt", "w"))
    print("------------------------------------", file=open("PyBank analysis/output.txt", "a"))
    print("Total months:"+"  "+ str(total_months), file=open("PyBank analysis/output.txt", "a"))
    print("Total:" + "  " +str(total_formatted), file=open("PyBank analysis/output.txt", "a"))
    print("Average Change:" + "  " + str(average_change_formatted), file=open("PyBank analysis/output.txt", "a"))
    print("Greatest increase in Profits:" + "  " + str(max_profit_date) + " " + "(" + str(max_profit_formatted) + ")", file=open("PyBank analysis/output.txt", "a"))
    print("Greatest decrease in Losses:" + "  " + str(max_losses_date) + " " + "(" + str(max_losses_formatted) + ")", file=open("PyBank analysis/output.txt", "a"))

