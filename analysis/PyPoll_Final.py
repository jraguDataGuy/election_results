#Add our dependencies
import csv
import os
#Assign a variable to load a file from a path
file_to_load = os.path.join("Module 3 - Python","election_results","Resources","election_results.csv")
#Assign a variable to ave the file to a path
file_to_save = os.path.join("Module 3 - Python","election_results","analysis","election_analysis.txt")
#Open the election results and read the file
with open (file_to_load)as election_data:
    #To do: read and analyze the data here.
    #Read the file object with the reader function
    file_reader = csv.reader(election_data)
    #Read and Print Header Row
    headers = next(file_reader)
    print(headers)
