import os
import csv
from pathlib import Path 

election_data = os.path.join("Resources", "election_data.csv")


#The total number of votes cast
with open(election_data, 'r') as f:
  next(f) #skips the first row
  total = 0
  for row in csv.reader(f):
    total += float(row[1])

#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.






# Print the Election Results
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {(total)}")
print(f"----------------------------")
print(f"Khan: ")
print(f"Correy: ")
print(f"Li: )")
print(f"O'Tooley: ")
print(f"----------------------------")
print(f"Winner: ")
print(f"----------------------------")

# export a text file with the result
output_file = Path("Election_Summary.txt")

with open(output_file,"w") as file:

# Write methods to print to Elections_Results_Summary 
    file.write(f"Election Results")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Total Votes: ")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Khan: ")
    file.write("\n")
    file.write(f"Correy: ")
    file.write("\n")
    file.write(f"Li: ")
    file.write("\n")
    file.write(f"O'Tooley: ")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Winner: ")
    file.write("\n")
    file.write(f"----------------------------")