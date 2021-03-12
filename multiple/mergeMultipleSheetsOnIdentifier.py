import pandas as pd
import argparse
from datetime import datetime
import os

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--directory')
parser.add_argument('-c', '--columnName')
args = parser.parse_args()

if args.directory:
    directory = args.directory
else:
    directory = input('Enter directory: ')

if args.columnName:
    columnName = args.columnName
else:
    columnName = input('Enter column to merge on: ')


def makeDataFrame(frame, filename):
    frame = pd.read_csv(filename, index_col=0)
    frames.append(frame)


frames = []
for count, filename in enumerate(os.listdir(directory)):
    filename = directory + "/" + filename
    if filename.endswith('.csv'):
        makeDataFrame("df_{}".format(count), filename)

frame_count = len(frames)
print(frame_count)

merged = []
for count, frame in enumerate(frames):
    if count == 0:
        new_df = pd.merge(frame, frames[count+1], how='outer', on=columnName)
        merged.append(new_df)
    elif count == 1:
        pass
    else:
        new_df = pd.merge(merged[0], frame, how='outer', on=columnName)
        merged[0] = new_df

print(merged[0])
mergedFrame = merged[0]
print(mergedFrame.columns)
print(mergedFrame.head)
dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')
mergedFrame.to_csv('mergedMultiple_'+dt+'.csv', index=False)
