"""Collects identifiers from all CSVs in a directory and lists the CSVs where each identifier appears."""

import pandas as pd
import argparse
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
    idList = frame[column_name].to_list()
    for identifier in idList:
        if merged.get(identifier) is None:
            merged[identifier] = str(count)
        else:
            value = merged[identifier]
            value = value+'|'+str(count)
            merged[identifier] = value

new_df = pd.DataFrame.from_dict(merged, orient='index')
print(new_df.head)

new_df.to_csv('compareIds.csv', index=False, quoting=csv.QUOTE_ALL)
