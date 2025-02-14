import pandas as pd
import argparse
from datetime import datetime
import csv

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
parser.add_argument('-c', '--column1')
parser.add_argument('-c2', '--column2')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter filename (including \'.csv\'): ')
if args.column1:
    column1 = args.column1
else:
    column1 = input('Enter column with values to aggregate: ')
if args.column2:
    column2 = args.column2
else:
    column2 = input('Enter column to aggregate by: ')

dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')

df = pd.read_csv(filename, header=0, dtype='str')

# Reshapes sheet indexed by column1 (column2 aggregated)
# --> sheet indexed by column2 (column1 aggregated)

# original
# column1   column2
# Smith, Ed    001|004|005
# Smith, Jane  004

# new
# column2   column1
# 001          Smith, Ed
# 004          Smith, Ed|Smith, Jane
# 005          Smith, Ed

# Explode column2.
df[column2] = df[column2].astype('str')
df[column2] = df[column2].str.strip()
df[column2] = df[column2].str.split('|')
df.reset_index()
df = df.explode(column2)
df[column2] = df[column2].str.strip()
df[column1] = df[column1].str.strip()

# Pivot table, aggregated values associated with column2.
pivoted = pd.pivot_table(df, index=[column2], values=column1,
                         aggfunc=lambda x: '|'.join(str(v) for v in x))


# Create updated_df from pivot table.
updated_df = pd.DataFrame(pivoted)
updated_df = updated_df.reset_index()

updated_df[column1] = updated_df[column1].str.split('|')
updated_df[column1] = updated_df[column1].apply(set)
updated_df[column1] = updated_df[column1].apply(sorted)
updated_df['count'] = updated_df[column1].str.len()
updated_df[column1] = updated_df[column1].str.join('|')


# Create CSV for updated_df.
print(updated_df.columns)
print(updated_df.head)
updated_df.to_csv(column1+'AggregatedBy'+column2+'_'+dt+'.csv', index=False, quoting=csv.QUOTE_ALL)
