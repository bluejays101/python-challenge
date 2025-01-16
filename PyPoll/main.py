import csv
 
filename = "Resources/election_data.csv"
output_filename = "analysis/pypoll_election_results.txt"
 
candidates = dict()
 
total_votes = 0

output_str = ""
 
with open(filename) as f:
  reader = csv.reader(f)
  next(reader)
  for id, county, candidate in reader:
    if candidate not in candidates:
      candidates[candidate] = 1
    else:
      candidates[candidate] += 1
    total_votes += 1
 

output_str += 'Election results:\n'
output_str += '-' * 50 + '\n'
output_str += f'Total Votes: {total_votes}\n'
output_str += '-' * 50 + '\n'
 

for candidate in candidates.keys():
  output_str += candidate + ": "
  output_str += "%0.3f" % (int(candidates[candidate]) / total_votes * 100.0) + "% "
  output_str += "(" + str(candidates[candidate]) + ")" + '\n'
 
 
output_str += '-' * 50 + '\n'

winner_votes = 0


for candidate in candidates:
  if candidates[candidate] > winner_votes:
    winner_votes = candidates[candidate]
    winner = candidate
 

output_str += f'Winner: {winner}\n'
output_str += '-' * 50 + '\n'
 

print(output_str)
 

with open(output_filename, 'w') as f:
  f.write(output_str)
