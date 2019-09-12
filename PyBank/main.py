import os
import csv
from pathlib import Path 

budget_data = os.path.join("Resources", "budget_data.csv")

#The net total amount of "Profit/Losses" over the entire period
with open(budget_data, 'r') as f:
  next(f) #skips the first row
  total = 0
  for row in csv.reader(f):
    total += float(row[1])
  

#Import data as a list - The total number of months included in the dataset
results = [0]
with open(budget_data, newline='') as inputfile:
    next(inputfile)
    for row in csv.reader(inputfile):
        results.append(row[0])


 #The average of the changes in "Profit/Losses" over the entire period
# with open(budget_data, 'a') as mn:
#     reader = csv.reader(mn)
#     next(reader) #skip the header
#     total = 0
#     the_numbers = [float(row[1]) for row in reader]
#     average = sum(the_numbers) / len(the_numbers)
    
#     print(average)

# Print the Results

print("Financial Analyses")
print("----------------------------")
print(f"Total Months: {len(results)} ")
print(f"Total: ${(total)}")
print(f"Average Change: ")
print(f"Greatest Increase in Profits: ")
print(f"Greatest Decrease in Profits: ")

# export a text file with the result
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




