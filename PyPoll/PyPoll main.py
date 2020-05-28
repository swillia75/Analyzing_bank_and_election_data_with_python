import os
import csv

# Path to collect data from the Resources folder
PyPoll_csv = os.path.join("Resources","election_data.csv")

with open(PyPoll_csv) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    if row in csvreader:
        print(row[0])