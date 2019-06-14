import csv
import os

# Variable declarations
candidates = {"Khan":0, "Correy":0, "Li":0, "O'Tooley":0}

with open("election_data.csv") as file:
    votes = csv.reader(file, delimiter=',')

    # Pop the csv header off
    csv_header = next(votes)

    # Determine the amount of votes each candidate received
    for row in votes:
        if row[2] == "Khan":
            candidates["Khan"] += 1
        elif row[2] == "Correy":
            candidates["Correy"] += 1
        elif row[2] == "Li":
            candidates["Li"] += 1
        elif row[2] == "O'Tooley":
            candidates["O'Tooley"] += 1

Khan = candidates["Khan"]
Correy = candidates["Correy"]
Li = candidates["Li"]
OTooley = candidates["O'Tooley"]
Total_Votes = Khan + Correy + Li + OTooley

# A function to format our change list as a fancy string
#def printChange(changeList):
#    return f"{changeList[0]} (${changeList[1]})"

# The output is a multiline string

output = f"""Election Results
----------------------------
Total Votes: {Total_Votes}
----------------------------
Khan: {(Total_Votes / Khan) * 100} ({Khan})
Correy: {(Total_Votes / Correy) * 100} ({Correy})
Li: {(Total_Votes / Li) * 100} ({Li})
OTooley: {(Total_Votes / OTooley) * 100} ({OTooley})
----------------------------
Winner: {max(candidates)}"""

# Open the output file
with open("pyPoll.txt", "w") as outputFile:
    # Write the output to the output file
    outputFile.write(output)

# Print the output to the console
print(output)
