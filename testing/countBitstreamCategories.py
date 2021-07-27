import pandas as pd
import argparse
from datetime import datetime
import ast

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
parser.add_argument('-c', '--column1')
parser.add_argument('-c2', '--column2')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter filename (including \'.csv\'): ')

dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')

df = pd.read_csv(filename, header=0)

allItems = []
for count, row in df.iterrows():
    row = row
    handle = row['handle']
    lonely = row['lonely']
    matched = row['matched']
    single = row['single']
    if pd.notna(lonely):
        lonely = ast.literal_eval(lonely)
        lonely_count = len(lonely)
        row['lonely_count'] = lonely_count
    if pd.notna(matched):
        matched = ast.literal_eval(matched)
        matched_count = len(matched)
        row['matched_count'] = matched_count
    if pd.notna(single):
        single = ast.literal_eval(single)
        single_count = len(single)
        row['single_count'] = single_count
    allItems.append(row)

updated_df = pd.DataFrame.from_dict(allItems)
dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')
updated_df.to_csv('totalValuesOf_'+dt+'.csv')
