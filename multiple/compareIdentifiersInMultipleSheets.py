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


def make_data_frame(frame_name, name_file):
    frame_name = pd.read_csv(name_file)
    frames.append(frame_name)


frames = []
chart = {}
for count, filename in enumerate(os.listdir(directory)):
    print(count)
    filename = directory + "/" + filename
    if filename.endswith('.csv'):
        make_data_frame("df_{}".format(count), filename)
        chart[filename] = count

frame_count = len(frames)
print(frame_count)
print(chart)


merged = {}
for count, frame in enumerate(frames):
    idList = frame[columnName].to_list()
    for identifier in idList:
        if merged.get(identifier) is None:
            merged[identifier] = str(count)
        else:
            value = merged[identifier]
            value = value+'|'+str(count)
            merged[identifier] = value

df = pd.DataFrame.from_dict(merged, orient='index')
print(df.head)

df.to_csv('compareIds.csv')