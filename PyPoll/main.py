import os
import csv
total_vote=0
candidate_list=[]
unique_candidate=[]
vote_per_candidate=[]
percent_vote=[]
candidate_votes=0
organized_candidate_list=[]
final_list=[]

csvpath=os.path.join("election_data.csv")
with open(csvpath,newline="") as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    csv_header=next(csvfile)
    print(f"Header:{csv_header}")

    for row in csvreader:
        total_vote=total_vote+1
        candidate_list.append(row[2])
    for candidate in set(candidate_list):
        # print(candidate)
        candidate_votes = candidate_list.count(candidate) #2218231
        candidate_vote_percentage = ((candidate_votes/total_vote)*100)#63
        unique_candidate.append(candidate_votes) #unique_candidate=[khan,63,2218231]
        unique_candidate.append('{:.2f}%'.format(candidate_vote_percentage)) #unique_candidate=[khan,63]
        unique_candidate.append(candidate) #unique_candidate=[khan] 
        # print(unique_candidate)
        # unique_candidate=[]
        organized_candidate_list.append(unique_candidate) #organized_candidate_list = [[khan, 63, 2218231]]
        unique_candidate=[]
       
        # candidate.loc[candidate['candidate_votes'].idxmax(candidate_votes)]

textfile= open("main.txt","w")
for candy in organized_candidate_list:
    per_string = str(candy[1])
    vote_string = str(candy[0])
    line_entry=candy[2] + ": " + per_string + "(" + vote_string + ")\n"
    print(candy[2], ": ", candy[1], "(", candy[0], ")")
    textfile.writelines( line_entry )


winner_line = "Winner: " + max(organized_candidate_list)[2]
print("-------------------------")
print(winner_line)
print("-------------------------")



textfile.writelines(winner_line)

    # print(total_vote)
    # print(unique_candidate)
    # print(vote_per_candidate)
    # print(percent_vote)
    