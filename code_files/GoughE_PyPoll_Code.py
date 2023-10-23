# import modules
import os
import csv

# file path
poll_data = os.path.join("..", "Starter_Code", "PyPoll", "Resources", "election_data.csv")

# Total vote counter
total_votes = 0

# Dictionary to track votes of each candidate
votes_by_candidate = {}

# List of candidates
candidates = []

# Winning candidate and winning vote count
winner = ""
winner_votes = 0

# Read the csv file
with open(poll_data) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # add headers 
    csv_header = next(csv_reader)

    # loop through the file
    for row in csv_reader:

        # count the total votes
        total_votes = total_votes + 1

        # get the candidate voted for from every row
        candidate_name = row[2]

        # See if the candidate is not the candidate list
        # "not in" code provided by W3docs <https://www.w3docs.com/snippets/python/check-if-something-is-not-in-a-list-in-python.html>
        if candidate_name not in candidates:

            # add them to the candidate list
            candidates.append(candidate_name)

            # give them a vote count
            votes_by_candidate[candidate_name] = 0

        # add a vote to the candidate
        votes_by_candidate[candidate_name] = votes_by_candidate[candidate_name] + 1

# file output path
election_txt = os.path.join("..", "output", "election_results.txt")

# Print the results
# Code for printing as text file provided by Pythontutorial.net <https://www.pythontutorial.net/python-basics/python-write-text-file/>
with open(election_txt, "w") as txtfile:

    # Print the final vote count
    # "\n" code provided by Pythontutorial.net <https://www.pythontutorial.net/python-basics/python-write-text-file/>
    final_counts = (
        f"Election Results\n"
        f"-------------------------\n"
        f"Total Votes {total_votes}\n"
        f"-------------------------\n"
    )

    #print the final vote count in the terminal
    print(final_counts)

    # Save the final vote count in the txt file
    txtfile.write(final_counts)

    # Find out winner by looping through votes_by_candidate
    # Code for looping through dictionary provded by W3Schools <https://www.w3schools.com/python/python_dictionaries_loop.asp>
    for candidate in votes_by_candidate:
    
        # Get the vote counts
        individual_votes = votes_by_candidate[candidate]

        # Calulate percent
        vote_percent = (individual_votes / total_votes) * 100

        # Figure out the winner. If the vote count for a candidate is bigger the winner's votes...
        if individual_votes > winner_votes:

            # Make that the new winner's vote
            winner_votes = individual_votes

            # Make that candidate the winner
            winner = candidate

        # print each candidates vote count
        # ":.3f" code provided by Stack Overflow <https://stackoverflow.com/questions/45310254/fixed-digits-after-decimal-with-f-strings>
        candidate_tally = f"{candidate}: {vote_percent:.3f}% ({individual_votes})\n"

        # print to the terminal
        print(candidate_tally)

        # save to the text file
        txtfile.write(candidate_tally)

    # print the winner
    results = (
        f"-------------------------\n"
        f"Winner: {winner}\n"
        f"-------------------------"
    )

    # print the results to the terminal
    print(results)

    # save the results to the txt file
    txtfile.write(results)