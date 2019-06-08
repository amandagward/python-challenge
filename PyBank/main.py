import csv
import os
csvPath = os.path.join("Resources", "budget_data.csv")
outputPath = os.path.join("Resources", "output.txt")

# Variable declarations
months = 0
total = 0
amount = 0
lastAmount = 0
change = 0
greatestIncrease = [ "", 0 ]
greatestDecrease = [ "", 0 ]

with open(csvPath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Pop the csv header off
    csv_header = next(csvreader)

    for row in csvreader:
        # Increment the number of months by 1
        months += 1

        amount = int(row[1])

        # Add the month's total to the running total
        total += amount

        # Calculate change in amounts
        change = amount - lastAmount

        # If the current month's change is larger
        # than the greatest change we currently know of
        if change > greatestIncrease[1]:
            # This is the new greatest change we know of
            greatestIncrease = [ row[0], change ]

        # If the current month's change is smaller
        # than the smallest change we currently know of
        if change < greatestDecrease[1]:
            # This is the new smallest change we know of
            greatestDecrease = [ row[0], change ]

        # This month's amount will be last
        # month's amount for the next month
        lastAmount = amount

# A function to format our change list as a fancy string
def printChange(changeList):
    return f"{changeList[0]} (${changeList[1]})"

# The output is a multiline string
output = f"""Financial Analysis
----------------------------
Total Months: {months}
Total: ${total}
Average Charge: ${round(total / months, 2)}
Greatest Increase in Profits: {printChange(greatestIncrease)}
Greatest Decrease in Profits: {printChange(greatestDecrease)}"""

# Open the output file
with open(outputPath, "w") as outputFile:
    # Write the output to the output file
    outputFile.write(output)

# Print the output to the console
print(output)