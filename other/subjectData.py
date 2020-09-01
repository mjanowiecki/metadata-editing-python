import pandas as pd
import argparse
import csv
import re

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter filename (including \'.csv\'): ')


with open(filename) as itemMetadataFile:
    itemMetadata = csv.DictReader(itemMetadataFile)
    for row in itemMetadata:
        newSubject = row['newSubject']
        newKey = row['newKey']
        if newKey == 'dc.subject.mesh':
            if '--' in newSubject:
                print(newSubject)
        elif newKey == 'dc.subject':
            match = re.findall(r'(\s[A-Z][a-z]){1,}', newSubject)
            if match:
                print(newSubject)
            if '--' in newSubject:
                print(newSubject)


# df = pd.read_csv(filename, header=0)
#
#
# unique_1 = df.newSubject.unique()
# unique_2 = df.newKey.unique()
# values = df.newSubject.value_counts()
# print(unique_2)
#
#
# notControlled = df.loc[df['newKey'] == 'dc.subject']
# fast = df.loc[df['newKey'] == 'dc.subject.fast']
# mesh = df.loc[df['newKey'] == 'dc.subject.mesh']
# print(notControlled.head)
# print(fast.head)
# print(mesh.head)
#
# # mesh['uri'] = mesh['uri'].str.split(',')
# # mesh.reset_index()
# # mesh = mesh.explode('uri')
# # print(mesh.head)
#
#
# #
# # mesh.to_csv(path_or_buf='explodedMESH.csv')
