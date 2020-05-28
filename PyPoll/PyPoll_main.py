#Import os
import os
#import csv to read file
import csv

# Path to collect data from the Resources folder
PyPoll_csv = os.path.join("Resources", "election_data.csv")

# Open the CSV
with open(PyPoll_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")