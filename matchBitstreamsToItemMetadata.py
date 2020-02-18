import argparse
from datetime import datetime
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
parser.add_argument('-f2', '--file2')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter filename (including \'.csv\'): ')
if args.file2:
    filename2 = args.file2
else:
    filename2 = input('Enter 2nd filename (including \'.csv\'): ')

df = pd.read_csv(filename)
df_2 = pd.read_csv(filename2)

df['handle'] = df['dc.identifier.uri'].copy()
df.handle = df.handle.str.replace('http://jhir.library.jhu.edu/handle/', '')
print(df.handle)

new_df = pd.merge(df_2, df, how='left', on='handle')


print(new_df.columns)
print(new_df.head(10))

dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')

new_df.to_csv(path_or_buf='remediatedBitstreams_'+dt+'.csv', index=False)
