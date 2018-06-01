"""
For this problem, use the same data set as in the previous problem.

Your task now is to run the greedy algorithm that schedules jobs (optimally) in decreasing order of the ratio (weight/length). In this algorithm, it does not matter how you break ties. You should report the sum of weighted completion times of the resulting schedule --- a positive integer --- in the box below. 
"""

import pandas as pd

jobs_df = pd.read_csv('jobs.txt', sep=" ", skiprows=1, header=None)
jobs_df.columns = ['weight', 'length']

jobs_df['ratio'] = jobs_df['weight'] / jobs_df['length']
jobs_df = jobs_df.sort_values(by=['ratio'], ascending=False)

jobs_df['finishing time'] = jobs_df['length'].cumsum()
jobs_df['weighted average'] = jobs_df['weight'] * jobs_df['finishing time']

print(jobs_df['weighted average'].sum())