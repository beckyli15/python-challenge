import os
import csv
csvpath=os.path.join("budget_data.csv")
total_row=0
total_amount=0
prev=867884
change=0
difference_total=0
change_list=[]
date_change_list=[]

with open(csvpath,newline="") as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    csv_header=next(csvfile)
    print(f"Header:{csv_header}")
    
    for row in csvreader:
        total_row=total_row+1
        total_amount += int(row[1])
        change = int(row[1]) - prev
        prev = int(row[1])
        difference_total += change
       
        date_change_list=[change,row[0]]
        change_list.append(date_change_list)
       
        Greatest_Increase= max(change_list)
        Greatest_Decrease= min(change_list)

    average_change= difference_total/(total_row-1)    
        
        
    print("============")
    print("Total Months " + str(total_row))
    print("Total: " + str(total_amount))
    print("Average Change: " + str(average_change))
    print(f"Greatest Increase in Profits: {Greatest_Increase}")
    print(f"Greatest Decrease in Profits: {Greatest_Decrease}")
  
    
    
