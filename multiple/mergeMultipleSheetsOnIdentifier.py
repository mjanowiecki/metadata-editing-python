import pandas as pd
import argparse
from datetime import datetime
import os
import csv

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--directory')
parser.add_argument('-c', '--column_name')
args = parser.parse_args()

if args.directory:
    directory = args.directory
else:
    directory = input('Enter directory: ')

if args.column_name:
    column_name = args.column_name
else:
    column_name = input('Enter column to merge on: ')


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
        new_df = pd.merge(frame, frames[count+1], how='outer', on=column_name)
        merged.append(new_df)
    elif count == 1:
        pass
    else:
        new_df = pd.merge(merged[0], frame, how='outer', on=column_name)
        merged[0] = new_df

print(merged[0])
mergedFrame = merged[0]
print(mergedFrame.columns)
print(mergedFrame.head)
dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')
mergedFrame.to_csv('mergedMultiple_'+dt+'.csv', quoting=csv.QUOTE_ALL)
