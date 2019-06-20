import os
import csv
total_vote=0
candidate_list=[]
unique_candidate=[]
vote_per_candidate=[]
percent_vote=[]
candidate_votes=0
organized_candidate_list=[]

csvpath=os.path.join("election_data.csv")
with open(csvpath,newline="") as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    csv_header=next(csvfile)
    print(f"Header:{csv_header}")

    for row in csvreader:
        total_vote=total_vote+1
        candidate_list.append(row[2])
    for candidate in set(candidate_list):
        unique_candidate.append(candidate) #unique_candidate=[khan] 
        # print(candidate)
        candidate_votes = candidate_list.count(candidate) #2218231
        candidate_vote_percentage = candidate_votes/total_vote #63
        unique_candidate.append(round(candidate_vote_percentage, 2)) #unique_candidate=[khan,63]
        unique_candidate.append(candidate_votes) #unique_candidate=[khan,63,2218231]
        print(unique_candidate)
        unique_candidate=[]
        # organized_candidate_list.append(unique_candidate) #organized_candidate_list = [[khan, 63, 2218231]]




    # print(organized_candidate_list)
# for candy in organized_candidate_list:
#     print(candy[0], ": ", candy[1], "(", candy[2], ")")

    # print(total_vote)
    # print(unique_candidate)
    # print(vote_per_candidate)
    # print(percent_vote)
    