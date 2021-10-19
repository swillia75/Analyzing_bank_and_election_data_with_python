#Import os

import os

#import csv to read file

import csv

# Path to collect data from the Resources folder

PyPoll_csv = os.path.join("Resources", "election_data.csv")

vote_count = 0  
vote_list = []
candidatelist = []
candidate_votes = [0, 0, 0, 0]
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
        vote_list.append(candidate)

    #for candidate in vote_list:

        if candidate not in candidatelist:
            candidatelist.append(candidate)

            
               
    print(vote_count)          
    print(candidatelist)
    
   

        # for candidate_name in vote_list:
        #     #print(candidate_name)

        #     if candidate_name not in candidate_list:
        #         candidate_list.append(candidate_name)

            # if candidate_name == candidate_list[0]:
            #     candidate_votes[0] += 1

            # elif candidate_name == candidate_list[1]:
            #     candidate_votes[1] += 1

            # elif candidate_name == candidate_list[2]:
            #     candidate_votes[2] += 1

    #         else:
    #             pass
            
    # print(candidate_list) 
    #print(candidate_votes)       
            
                
            #total number of votes for each candidate

            #else:
            #   candidate_index = candidate_list.index(candidate_names)
            #   

    #  #percentage of votes for each candidate
    
        #print(vote_list)
    #print(candidate_votes)
          
#     vote_percentage = list()
    
#     for votes in vote_count:

#         #Format vote_percentage
             
#         vote_percent = "{:.2%}".format(float(votes / total_votes))
#         vote_percentage.append(vote_percent)       
        
  
#         #winner of election based on popular vote

#         winner = candidate_list[0]

# #print out to terminal

# print("Election Results")
# print("---------------------------------")
# print("Total votes:" + "  " + str(total_votes))
# print("---------------------------------") 
# print(candidate_list[0] + "  " + (vote_percentage[0])+ " " + "(" + str(vote_count[0]) + ")")
# print(candidate_list[1] + "  " + (vote_percentage[1])+ " " + "(" + str(vote_count[1]) + ")")
# print(candidate_list[2] + "  " + (vote_percentage[2])+ " " + "(" + str(vote_count[2]) + ")")
# print(candidate_list[3] + "  " + (vote_percentage[3])+ " " + "(" + str(vote_count[3]) + ")")
# print("---------------------------------")
# print(("Winner:") + "   " + winner)

# #export to text file

# print("Election Results", file=open("PyPoll analysis/output.txt", "a"))
# print("---------------------------------", file=open("PyPoll analysis/output.txt", "a"))
# print("Total votes:" + "  " + str(total_votes), file=open("PyPoll analysis/output.txt", "a"))
# print("---------------------------------", file=open("PyPoll analysis/output.txt", "a")) 
# print(candidate_list[0] + "  " + (vote_percentage[0])+ " " + "(" + str(vote_count[0]) + ")", file=open("PyPoll analysis/output.txt", "a"))
# print(candidate_list[1] + "  " + (vote_percentage[1])+ " " + "(" + str(vote_count[1]) + ")", file=open("PyPoll analysis/output.txt", "a"))
# print(candidate_list[2] + "  " + (vote_percentage[2])+ " " + "(" + str(vote_count[2]) + ")", file=open("PyPoll analysis/output.txt", "a"))
# print(candidate_list[3] + "  " + (vote_percentage[3])+ " " + "(" + str(vote_count[3]) + ")", file=open("PyPoll analysis/output.txt", "a"))
# print("---------------------------------", file=open("PyPoll analysis/output.txt", "a"))
# print(("Winner:") + "   " + winner, file=open("PyPoll analysis/output.txt", "a"))
# print("---------------------------------", file=open("PyPoll analysis/output.txt", "a"))