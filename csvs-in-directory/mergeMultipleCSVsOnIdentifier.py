"""Merges all CSVs in a directory into one big CSV on an identifier column found in all the sheets."""

import pandas as pd
import argparse
from datetime import datetime
import os
import csv

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--directory')
parser.add_argument('-id', '--identifier')
args = parser.parse_args()

if args.directory:
    directory = args.directory
else:
    directory = input('Enter directory: ')
if args.identifier:
    identifier = args.identifier
else:
    identifier = input('Enter name of identifier columns: ')


def make_data_frame(frame_name, name_file):
    frame_name = pd.read_csv(name_file, index_col=0, dtype=object)
    frames.append(frame_name)


frames = []
for count, filename in enumerate(os.listdir(directory)):
    filename = directory + "/" + filename
    if filename.endswith('.csv'):
        make_data_frame("df_{}".format(count), filename)

frame_count = len(frames)
print(frame_count)

merged = []
for count, frame in enumerate(frames):
    if count == 0:
        new_df = pd.merge(frame, frames[count+1], how='outer', on=identifier)
        merged.append(new_df)
    elif count == 1:
        pass
    else:
        new_df = pd.merge(merged[0], frame, how='outer', on=identifier)
        merged[0] = new_df

print(merged[0])
mergedFrame = merged[0]
print(mergedFrame.columns)
print(mergedFrame.head)
dt = datetime.now().strftime('%Y-%m-%d%H.%M.%S')
new_filename = 'mergedMultiple_'+dt+'.csv'
mergedFrame.to_csv(new_filename, quoting=csv.QUOTE_ALL)
