import argparse
import pandas as pd
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter filename (including \'.csv\'): ')

df = pd.read_csv(filename)

# List of columns that need to be completed.
column_list = []


# If any of the columns has a value (not nan), row is added to newData.
newData = []
for index, data in df.iterrows():
    for column in column_list:
        if pd.notna(data.get(column)):
            newData.append(data)
            break

df_2 = pd.DataFrame(newData)

print(df_2)

dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')
df_2.to_csv('inProgressAndCompletedRows'+dt+'.csv')
