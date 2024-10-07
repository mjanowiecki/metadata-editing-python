import pandas as pd
import argparse
from datetime import datetime
import csv

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
parser.add_argument('-id', '--identifier')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter filename (including \'.csv\'): ')
if args.identifier:
    identifier = args.identifier
else:
    identifier = input('Enter name of identifier columns: ')

dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')

df_1 = pd.read_csv(filename, header=0, dtype='str')

# List of column headers with multiple values to collect
valueList = ['holding_id', 'item_pid', 'new_barcode',
             'call_number', 'copy', 'internal_note', 'item_number',
             'status', 'copy_number']
for value in valueList:
    # Aggregate + sort new values by identifier.
    pivoted = pd.pivot_table(df_1, index=[identifier], values=value,
                             aggfunc=lambda x: list(set(list(x))))
    print(pivoted.sort_values(ascending=True, by=identifier).head())

    # Turn pivot table into dataframe.
    new_value = pd.DataFrame(pivoted)
    new_value = new_value.reset_index()
    new_value[value] = new_value[value].apply(lambda x: '|'.join(str(v) for v in x))
    print(new_value.columns)
    print(new_value.head)
    new_value.to_csv(value+'AggregatedBy'+identifier+'_'+dt+'.csv', index=False, quoting=csv.QUOTE_ALL)
