
#The data we need to retrieve.
import csv
#Assign a variable for the file to load and the path
file_to_load = 'Resources/election_results.csv'
#open the election results and read the file
with open(file_to_load) as election_data:
#print the file object
    print(election_data)
#Create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")
open(file_to_save, "w")
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote.
#close the file
election_data.close()