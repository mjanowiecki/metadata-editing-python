import pandas as pd
import argparse
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
    frame = pd.read_csv(filename)
    frames.append(frame)


frames = []
chart = {}
for count, filename in enumerate(os.listdir(directory)):
    filename = directory + "/" + filename
    if filename.endswith('.csv'):
        makeDataFrame("df_{}".format(count), filename)
        chart[filename] = count

frame_count = len(frames)
print(frame_count)
print(chart)


merged = {}
for count, frame in enumerate(frames):
    idList = frame['uri'].to_list()
    for id in idList:
        if merged.get(id) is None:
            merged[id] = str(count)
        else:
            value = merged[id]
            value = value+'|'+str(count)
            merged[id] = value

df = pd.DataFrame.from_dict(merged, orient='index')
print(df.head)

df.to_csv('compareIds.csv')
