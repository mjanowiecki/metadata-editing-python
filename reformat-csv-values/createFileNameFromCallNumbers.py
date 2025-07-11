"""Creates a unique filename based on an item's call number."""

import pandas as pd
import argparse
import re
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter first filename (including \'.csv\'): ')


def remove_space(x):
    x = x.group()
    x = x.lstrip()
    return x


df = pd.read_csv(filename, header=0)

item_list = []
for index, row in df.iterrows():
    row = row
    print("")
    call_num = row['call_number']
    extra = row['extra']
    if pd.notna(call_num):
        call_num = call_num.strip()
        print(call_num)
        # Convert no. 1 to no1
        call_num = re.sub(r'(\sno)\.[\s+\S](\d)', r'\1\2', call_num)
        # Convert c. 1 to c1
        call_num = re.sub(r'(\bc)\.[\s+\S](\d)', r'\1\2', call_num)
        # Convert v. 1 to v1
        call_num = re.sub(r'(\bv)\.[\s+\S](\d)', r'\1\2', call_num)
        # Remove leading whitespace for single character by itself
        call_num = re.sub(r'(\s\w\s)', remove_space, call_num)
        call_num = call_num.replace(" ", "_")
        call_num = call_num.replace(".", "_")
        call_num = call_num.replace(":", "_")
        call_num = call_num.replace("?", "u")
        call_num = call_num.replace("__", "_")
        call_num = call_num.replace("-_", "_")
        call_num = call_num.replace("_-", "_")
        if pd.notna(extra):
            print(call_num+"_"+extra)
            row['filename'] = call_num+"_"+extra
        else:
            print(call_num)
            row['filename'] = call_num
    item_list.append(row)

dt = datetime.now().strftime('%Y-%m-%d%H.%M.%S')
df_1 = pd.DataFrame.from_records(item_list)
df_1.to_csv(filename+'_'+dt+'.csv', index=False)
