#Import os

import os

#import csv to read file

import csv

# Path to collect data from the Resources folder

PyPoll_csv = os.path.join("Resources", "election_data.csv")

vote_count = 0  
vote_list = []
candidatelist = []
candidate_votes = {}
vote_percentage = []
# Open the CSV

with open(PyPoll_csv, newline="") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")

    #reader header
    csv_header = next(csvreader)
    
   #Loop through csvreader to get candidate name and votes
    
    for row in csvreader:
        #Add 1 vote to total vote count
        vote_count = vote_count + 1
        # #Add candidate name to candidate list
        candidate = row[2]
        
        if candidate not in candidatelist:
            candidatelist.append(candidate)
            ##choice_index = int(candidate) - 1
    
            candidate_votes[candidate] = 0

        candidate_votes[candidate] = candidate_votes[candidate] + 1
            
               
    print(vote_count)          
    print(candidate_votes)
    print(candidate_votes['Correy'])
    
   

print("Election Results")
print("---------------------------------")
print("Total votes:" + "  " + str(vote_count))
print("---------------------------------") 
print((candidatelist[0]) + "  " + str(((candidate_votes['Khan'])/vote_count)*100) + " " + "(" + str(candidate_votes['Khan']) + ")")
print((candidatelist[1]) + "  " + str(((candidate_votes['Correy'])/vote_count)*100) + " " + "(" + str(candidate_votes['Correy']) + ")")
print((candidatelist[2]) + "  " + str(((candidate_votes['Li'])/vote_count)*100) + " " + "(" + str(candidate_votes['Li']) + ")")
print((candidatelist[3]) + "  " + str(((candidate_votes["O'Tooley"])/vote_count)*100) + " " + "(" + str(candidate_votes["O'Tooley"]) + ")")
print("---------------------------------")
print(("Winner:") + "   " + candidatelist[0])

# #export to text file

#print("Election Results", file=open("PyPoll analysis/output.txt", "a"))
#print("---------------------------------", file=open("PyPoll analysis/output.txt", "a"))
#print("Total votes:" + "  " + str(total_votes), file=open("PyPoll analysis/output.txt", "a"))
#print("---------------------------------", file=open("PyPoll analysis/output.txt", "a")) 
#print(candidate_list[0] + "  " + (vote_percentage[0])+ " " + "(" + str(vote_count[0]) + ")", file=open("PyPoll analysis/output.txt", "a"))
#print(candidate_list[1] + "  " + (vote_percentage[1])+ " " + "(" + str(vote_count[1]) + ")", file=open("PyPoll analysis/output.txt", "a"))
#print(candidate_list[2] + "  " + (vote_percentage[2])+ " " + "(" + str(vote_count[2]) + ")", file=open("PyPoll analysis/output.txt", "a"))
#print(candidate_list[3] + "  " + (vote_percentage[3])+ " " + "(" + str(vote_count[3]) + ")", file=open("PyPoll analysis/output.txt", "a"))
#print("---------------------------------", file=open("PyPoll analysis/output.txt", "a"))
#print(("Winner:") + "   " + winner, file=open("PyPoll analysis/output.txt", "a"))
#print("---------------------------------", file=open("PyPoll analysis/output.txt", "a"))