import argparse
from datetime import datetime
import pandas as pd


parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter filename (including \'.csv\'): ')

dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')

metadata = pd.read_csv(filename, dtype='string')

all_items = []
for count, row in metadata.iterrows():
    row = row
    box = row['box']
    folder = row['folder']
    folder = folder.zfill(3)
    title = row['title']
    match_id = box+'_'+folder+'_'+title
    row['match_id'] = match_id
    all_items.append(row)

frame = pd.DataFrame.from_dict(all_items, dtype='string')
frame = frame.drop(columns=['box', 'folder', 'title'])
frame.to_csv('withMatchId_'+filename, index=False)
