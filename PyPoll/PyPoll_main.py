#Import os
import os
#import csv to read file
import csv

# Path to collect data from the Resources folder
PyPoll_csv = os.path.join("Resources", "election_data.csv")

# track vote count
vote_count = [0,0,0,0]

# Open the CSV
with open(PyPoll_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
#reader header
    csv_header = next(csvfile)
    
    #total number of votes cast
    poll_list = list(csvreader)
    total_votes = int(len(poll_list))
   
   
    #complete list of candidates receving votes
     
    candidate_list = list()
    vote_count = [0,0,0,0]
    for row in poll_list:

        candidate_names = str(row[2])

        if candidate_names not in candidate_list:
           candidate_list.append(candidate_names)
            
        #total number of votes for each candidate

        else:
            candidate_index = candidate_list.index(candidate_names)
            vote_count[candidate_index] += 1

     #percentage of votes for each candidate     
    vote_percentage = list()
    
    for votes in vote_count:

        #Format vote_percentage
             
        vote_percent = "{:.2%}".format(float(votes / total_votes))
        vote_percentage.append(vote_percent)       
        
  
        #winner of election based on popular vote
        winner = candidate_list[0]
#print out
print("Election Results", file=open("PyPoll analysis/output.txt", "a"))
print("---------------------------------", file=open("PyPoll analysis/output.txt", "a"))
print("Total votes:" + "  " + str(total_votes), file=open("PyPoll analysis/output.txt", "a"))
print("---------------------------------", file=open("PyPoll analysis/output.txt", "a")) 
print(candidate_list[0] + "  " + (vote_percentage[0])+ " " + "(" + str(vote_count[0]) + ")", file=open("PyPoll analysis/output.txt", "a"))
print(candidate_list[1] + "  " + (vote_percentage[1])+ " " + "(" + str(vote_count[1]) + ")", file=open("PyPoll analysis/output.txt", "a"))
print(candidate_list[2] + "  " + (vote_percentage[2])+ " " + "(" + str(vote_count[2]) + ")", file=open("PyPoll analysis/output.txt", "a"))
print(candidate_list[3] + "  " + (vote_percentage[3])+ " " + "(" + str(vote_count[3]) + ")", file=open("PyPoll analysis/output.txt", "a"))
print("---------------------------------", file=open("PyPoll analysis/output.txt", "a"))
print(("Winner:") + "   " + winner, file=open("PyPoll analysis/output.txt", "a"))
print("---------------------------------", file=open("PyPoll analysis/output.txt", "a"))