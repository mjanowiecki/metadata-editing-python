import pandas as pd
import argparse
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter first filename (including \'.csv\'): ')


df_1 = pd.read_csv(filename, header=0)
print(df_1.columns)

columnsToCombine = ['desc518', 'color', 'desc508', 'desc511']

for column in columnsToCombine:
    df_1[column] = df_1[column].astype(str)

df_1['combined'] = df_1[columnsToCombine].agg(' '.join, axis=1)

dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')
filename = filename[:-4]
df_1.to_csv(filename+'_mergedColum'+dt+'.csv')
