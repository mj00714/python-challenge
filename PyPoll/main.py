# import the moudles
import os
import csv

# set the path for the PyPoll file (run from the Python-Challenge directory)
election_data = os.path.join('PyPoll/Resources/election_data.csv')

total_votes = {}


# open the csv file with the proper encoding
with open(election_data, encoding='UTF-8') as election_data:
    csvreader = csv.reader(election_data, delimiter=",")
    # print CSV reader as a test
    # print(csvreader)

    # add a header row to the CSV file
    election_data_header = next(csvreader)
    # print the header as a check
    # print(f'CSV Header: {election_data_header}')

    # set the reader to the first row for all of the variables
    # first_row = next(csvreader) -- don't need this

    # count the number of votes for each candidate
    for row in csvreader:
        # define the candidate column
        candidate = row[2]
        # if the candidate is not in the list, add their name
        if candidate not in total_votes:
            total_votes[candidate] = 1
        # if the candidate is already in the list, add a vote
        else: total_votes[candidate] += 1

# print the votes as a check
# for index, value in total_votes.items():
#     print(f'{index}: {value} votes')

vote_count = total_votes.values()
total_votes_cast = sum(vote_count)
# check the total vote count
# print(f'Total Votes Cast: {total_votes_cast}')

# calculate the percentages, by candidate


# printout of the analysis
print('')
print(f'Election Results')
print('-----------------------------------------')
print(f'Total Votes: {total_votes_cast}')
print('-----------------------------------------')
for index, value in total_votes.items():
    print(f'{index}: {value / total_votes_cast:.3%} ({value})')
print('-----------------------------------------')
print(f'Winner: {max(total_votes, key=total_votes.get)}')
print('-----------------------------------------')

# create a txt file and export the data

output_path = os.path.join('PyPoll/analysis/analysis_data.txt')
with open(output_path, "w", newline='') as datafile:
    datafile.write(
    'Election Results\n'
    f'-----------------------------------------\n'
    f'Total Votes: {total_votes_cast}\n'
    f'-----------------------------------------\n')
    for index, value in total_votes.items():
        datafile.write(f'{index}: {value / total_votes_cast:.3%} ({value})\n')
    datafile.write(f'-----------------------------------------\n'
    f'Winner: {max(total_votes, key=total_votes.get)}\n'
    '-----------------------------------------')