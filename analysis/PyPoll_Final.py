#Add our dependencies
import csv
import os

#Assign a variable to load a file from a path
file_to_load = os.path.join("Module 3 - Python","election_results","Resources","election_results.csv")

#Assign a variable to ave the file to a path
file_to_save = os.path.join("Module 3 - Python","election_results","analysis","election_analysis.txt")

#1. Initialize a total vote counter.
total_votes = 0
#Candidate Options
candidate_options = []

#Empty Dictionary
candidate_votes={}

#Open the election results and read the file

#Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open (file_to_load)as election_data:
    #To do: read and analyze the data here.
    #Read the file object with the reader function
    file_reader = csv.reader(election_data)
    #Read the header row.
    headers = next(file_reader)
    #Print each row in the CSV File.
    for row in file_reader:
        #2. Add to the total vote count
        total_votes += 1
        #Print the candidate name from each row.
        candidate_name = row[2]
        #If candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
        #Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
        #Begin tracking that candidates vote count.
            candidate_votes[candidate_name] = 0
        #Add a vote to that candidate's count   
        candidate_votes[candidate_name] += 1
        #Determine percentage of votes for each candidate
        #1 Interate through candidate list
for candidate_name in candidate_votes:
            #2. Retrieve vote count of a candidate
    votes = candidate_votes[candidate_name]
            #3. Calculate the percentages of votes
    vote_percentage = float(votes) / float(total_votes) * 100
            #4. Print the candidate name and percentage of votes
    #Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count.
    if(votes>winning_count) and (vote_percentage>winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name
    print(f"{candidate_name}:{vote_percentage:.1f}% ({votes:,})\n")
winning_candidate_summary = (
    f"---------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count:{winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"---------------------------\n")
print(winning_candidate_summary)

#Print the total votes
#print(total_votes)
#Print the candidate list.
#print(candidate_options)
#Print the candidate vote dictionary.
#print(candidate_votes)
