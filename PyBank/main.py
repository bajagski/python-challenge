import os
import csv
from pathlib import Path 

budget_data = os.path.join("Resources", "budget_data.csv")

  

# #Import data as a list - The total number of months included in the dataset
date_results = []
profit_results = []
avg_results = []

with open(budget_data, newline='') as inputfile:
    next(inputfile)

    for row in csv.reader(inputfile):
        date_results.append(row[0])
        profit_results.append(float(row[1]))

#print(len(date_results))

#print(sum(profit_results))

#The average of the changes in "Profit/Losses" over the entire period
    for x in range(len(profit_results)):
      avg_results.append((profit_results[x+1])-profit_results[x]))

print(sum(avg_results)/len(avg_results))
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period

#Print the Results

print("Financial Analyses")
print("----------------------------")
print(f"Total Months: {len(date_results)} ")
print(f"Total: ${(sum(profit_results))}")
print(f"Average Change: ")
print(f"Greatest Increase in Profits: ")
print(f"Greatest Decrease in Profits: ")

# # export a text file with the result
output_file = Path("Output_Summary.txt")

with open(output_file,"w") as file:
    
# Write methods to print to Financial_Analysis_Summary 
    file.write("Financial Analyses")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(results)}")
    file.write("\n")
    file.write(f"Total: ${(total)}")
    file.write("\n")
    file.write(f"Average Change:")
    file.write("\n")
    file.write(f"Greatest Increase in Profits:)")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits:")




