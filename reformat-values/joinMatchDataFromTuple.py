import argparse
import pandas as pd
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
parser.add_argument('-f2', '--file2')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter first filename (including \'.csv\'): ')
if args.file2:
    filename2 = args.file2
else:
    filename2 = input('Enter second filename (including \'.csv\'): ')

df_1 = pd.read_csv(filename, header=0)
df_2 = pd.read_csv(filename2, header=0)

df_1.match1 = df_1.match1.str.lstrip('(')
df_1.match1 = df_1.match1.str.rstrip(')')
df_1.match2 = df_1.match2.str.lstrip('(')
df_1.match2 = df_1.match2.str.rstrip(')')


m1 = df_1.match1.str.rsplit(pat=',', n=1, expand=True)
m1['title1'] = m1[0]
m1['ratio1'] = m1[1]
m2 = df_1.match2.str.rsplit(pat=',', n=1, expand=True)
m2['title2'] = m2[0]
m2['ratio2'] = m2[1]
little = m1.join(m2, rsuffix='_2')


df_1 = df_1.join(little)


df_1.title1 = df_1['title1'].str.strip("'")
df_1.title1 = df_1.title1.str.strip("'")
df_1.title2 = df_1.title2.str.strip("'")
df_1.title2 = df_1['title2'].str.strip('"')

df_1.to_csv('matchesSeperatedIntoColumns.csv', index=False)

unique1 = df_1.title1.unique()
unique2 = df_1.title2.unique()
all = list(unique1)+list(unique2)
all = list(set(all))


combined = []

for index, row in df_2.iterrows():
    row = dict(row)
    if row.get('title') in all:
        combined.append(row)
    else:
        pass

df_3 = pd.DataFrame(combined)
dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')
df_3.to_csv('marcSubset.csv', index=False)
