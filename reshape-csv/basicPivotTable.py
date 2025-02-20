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
    column1 = input('Enter column to aggregate ')

if args.column2:
    column2 = args.column2
else:
    column2 = input('Enter column to pivot: ')


dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')

df = pd.read_csv(filename, header=0)
print(df.head)

# original
# column1   column2
# 001       Smith, Jane
# 002       Smith, Ed
# 002       Austen, Jane
# 003       Smith, Ed

# new
# column2       column1
# Austen, Jane  002
# Smith, Ed     002|003
# Smith, Jane   001

newColumns = ''
pivot = pd.pivot_table(df, index=column2,
                       values=column1,
                       aggfunc=lambda x: '|'.join(str(v) for v in x))

df_p = pd.DataFrame(pivot)
df_p = df_p.reset_index()
print(df_p.head)

df_p.to_csv('pivotedBy'+column2+'_'+dt+'.csv', index=False, quoting=csv.QUOTE_ALL)
