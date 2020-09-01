import pandas as pd
import argparse
import os
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--directory')
args = parser.parse_args()

if args.directory:
    directory = args.directory
else:
    directory = input('Enter directory (including \'.csv\'): ')


newDF = pd.DataFrame()
for filename in os.listdir(directory):
    filename = directory + "/" + filename
    df = pd.read_csv(filename)
    counts = df.count()
    handle = filename.replace(directory+'/', '').replace('Metadata.csv', '')
    print(handle)
    df_count = counts.to_frame()
    df_count = df_count.reset_index()
    df_count['handle'] = handle
    print(df_count.head)
    newDF = newDF.append(df_count, sort=True)

print(newDF.head)
dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')
newDF.to_csv(path_or_buf='countedValues_'+dt+'.csv', index=False)
