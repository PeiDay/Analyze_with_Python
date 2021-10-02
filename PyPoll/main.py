import os
import csv


# Path for input from the Resources and output to Analysis 
pypoll_csv = os.path.join('Resources','election_data.csv')
pypoll_txt = os.path.join('Analysis','pyPoll_analysis.txt')

print('Election Results')
print('-------------------------------------------')


# Set variables for list for calculations
voterID = []
candidate_list = []
candidate_vote = {}  # set as a dictionary { candidate : vote count }
highest_vote = 0
result = []


# Read the cvs file and get the dictionary key and value
with open(pypoll_csv,'r') as electionPoll:
    PollData = csv.reader(electionPoll, delimiter = ',')
    header = next(PollData)
    # print(header)

    for row in PollData:
        voterID.append(row[0])
        candidate = row[2]
        if candidate not in candidate_list:
            candidate_list.append(candidate)
            candidate_vote[candidate] = 1
            # print(candidate)
        else:
            candidate_vote[candidate] = candidate_vote[candidate] + 1
    # print(candidate_vote)


# Calculate total votes
totalVote = int(len(voterID))
print(f'Total Votes: {totalVote}')
print('-------------------------------------------')
    

# Count votes and percentage for each candidate from dictionary
for candidate in candidate_vote:
    votes_count = candidate_vote.get(candidate)
    vote_rate = (votes_count / totalVote) * 100
    print(f'{candidate} : {vote_rate:.3f}% ({candidate_vote[candidate]})')


    # identify the winner
    if (votes_count > highest_vote):
        highest_vote = votes_count
        winner = candidate

print('-------------------------------------------')
print(f'Winner: {winner}')
print('-------------------------------------------')


with open (pypoll_txt, 'w') as textfile:
    textfile.write('Election Results\n')
    textfile.write('------------------------------------------------\n')
    textfile.write(f'Total Votes: {totalVote}\n')
    textfile.write('------------------------------------------------\n')
    for candidate in candidate_vote:
        votes_count = candidate_vote.get(candidate)
        vote_rate = (votes_count/totalVote) * 100
        textfile.write(f'{candidate} : {vote_rate:.3f}% ({candidate_vote[candidate]})\n')
    textfile.write('------------------------------------------------\n')
    textfile.write(f'Winner: {winner}\n')
    textfile.write('------------------------------------------------\n')
    textfile.close
        