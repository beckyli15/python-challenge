import os
import csv
csvpath=os.path.join("budget_data.csv")
total_row=0
total_amount=0
prev=867884
difference=0
difference_total=0

with open(csvpath,newline="") as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    csv_header=next(csvfile)
    print(f"Header:{csv_header}")
    
    for row in csvreader:
        total_row=total_row+1
        total_amount += int(row[1])
        diff = int(row[1]) - prev
        prev = int(row[1])
        difference_total += diff
        
        
   
    print(max(diff["Profit/Losses"]))
    print("============")
    print(total_row)
    print(total_amount)
    print(difference_total/(total_row-1))
    
