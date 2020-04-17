import pandas as pd
import argparse
import os
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--directory')
args = parser.parse_args()

if args.directory:
    directory = args.directory
else:
    directory = input('Enter directory (including \'.csv\'): ')

newDF = pd.DataFrame()
for filename in os.listdir(directory):
    filename = directory + "/" + filename
    df = pd.read_csv(filename)
    handle = filename.replace(directory+'/', '').replace('Metadata.csv', '')
    print(handle)
    df['handle'] = handle
    newDF = newDF.append(df, ignore_index=True, sort=True)


columnNames = list(newDF.columns.values)
for column in columnNames:
    print(column)
    new_df = newDF[[column, 'itemID', 'handle']].copy()
    new_df = new_df.dropna(subset=[column])
    print(new_df.head)
    columnName = column.replace('.', '_')
    dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')
    new_df.to_csv(path_or_buf=columnName+'_'+dt+'.csv', index=False)
