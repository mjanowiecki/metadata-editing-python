import pandas as pd
import argparse
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter filename (including \'.csv\'): ')

dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')

df = pd.read_csv(filename, header=0)
print(df.head)

pivotIndex = ''
newColumns = ''
newValues = ''
pivot = pd.pivot_table(df, index=pivotIndex, columns=newColumns, values=newValues,
                       aggfunc=lambda x: '|'.join(str(v) for v in x))

df_p = pd.DataFrame(pivot)
df_p = df_p.reset_index()

print(df_p.head)

df_p.to_csv(path_or_buf='pivotedBy'+pivotIndex+'_'+dt+'.csv')
