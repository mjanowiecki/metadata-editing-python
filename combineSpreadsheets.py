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
    directory = input('Enter directory: ')

dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')

newDF = pd.DataFrame()
for filename in os.listdir(directory):
    filename = directory + "\\" + filename
    print(filename)
    if filename.endswith('.csv'):
        df = pd.read_csv(filename)
        newDF = newDF.append(df, ignore_index=True, sort=True)

print(newDF.head)

newDF.to_csv(path_or_buf='mergedCSV_'+dt+'.csv', index=False)
