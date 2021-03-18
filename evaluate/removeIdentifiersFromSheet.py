import pandas as pd
import argparse
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')  # Original data
parser.add_argument('-f2', '--file2')
parser.add_argument('-id', '--identifier')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter filename (including \'.csv\'): ')
if args.file2:
    filename2 = args.file2
else:
    filename2 = input('Enter filename (including \'.csv\'): ')
if args.identifier:
    identifier = args.identifier
else:
    identifier = input('Enter name of identifier columns: ')


df_1 = pd.read_csv(filename, header=0)
index = df_1.index
initialCount = len(index)
df_2 = pd.read_csv(filename2, header=0)


unique_2 = df_2[identifier].unique()
unique_2 = list(unique_2)


items = []
count = 0
for index, row in df_1.iterrows():
    print(row)
    uri = row[identifier]
    if uri in unique_2:
        count = count + 1
        pass
    else:
        items.append(row)


frame = pd.DataFrame.from_dict(items)
index = frame.index
endCount = len(index)
rowsRemoved = initialCount - endCount
print('Rows removed: '+str(rowsRemoved))
print('Identifiers found: '+str(count))
print(frame.columns)
print(frame.head)
dt = datetime.now().strftime('%Y-%m-%d')
filename = filename[:-4]
frame.to_csv(filename+'_identifiersRemoved_'+dt+'.csv')
