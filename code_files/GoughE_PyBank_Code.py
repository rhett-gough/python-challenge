# Import modules
import os
import csv

# file path
budget_data = os.path.join("..", "Starter_Code", "PyBank", "Resources", "budget_data.csv")

# Financial analysis variables
total_months = 0
previous_profloss = 0
monthly_profloss_changes = []
greatest_increase = ["", 0]
greatest_decrease = ["", 0]
total_profloss = 0

# Read the file
with open(budget_data) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # add headers
    csv_header = next(csv_reader)

    # loop through the file
    for row in csv_reader:
        
        # track totals
        total_months = total_months + 1
        total_profloss = total_profloss + int(row[1])

        # track Prof/Loss change
        profloss_change = int(row[1]) - previous_profloss

        # Reset previous Prof/Loss
        previous_profloss = int(row[1])

        # Create a list of all of the Prof/Loss changes
        monthly_profloss_changes.append(profloss_change)

        # Caluclate greatest increase
        if (profloss_change > greatest_increase[1]):
            greatest_increase[0] = row[0]
            greatest_increase[1] = profloss_change

        # Calculate greatest decrease
        if (profloss_change < greatest_decrease[1]):
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = profloss_change

# Remove first item in Prof/Loss change list
# ".pop(0)" code provided by GeeksforGeeks <https://www.geeksforgeeks.org/python-removing-first-element-of-list/>
monthly_profloss_changes.pop(0)

# Calculate average profloss change
average_profloss_change = sum(monthly_profloss_changes) / len(monthly_profloss_changes)

# Setup what I'll be printing in a variable
# Code for "\n" provided by Pythontutorial.net <https://www.pythontutorial.net/python-basics/python-write-text-file/>
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_profloss}\n"
    f"Average Change: ${round(average_profloss_change,2)}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
    )

# Print the results in terminal
print(output)

# Text file path
financial_txt = os.path.join("..", "output", "financial_analysis.txt")

# Print the results in a text file
# Code for printing as text file provided by Pythontutorial.net <https://www.pythontutorial.net/python-basics/python-write-text-file/>
with open(financial_txt, "w") as txtfile:
    txtfile.write(output)