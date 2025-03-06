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
    identifier = input('Enter name of identifier column: ')

dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')

df = pd.read_csv(filename, header=0, dtype='str')

# List of column headers with multiple values to collect.
valueList = ['columnName1', 'columnName2']

for value in valueList:
    # Aggregate and sort new values by identifier.
    pivoted = pd.pivot_table(df, index=[identifier], values=value,
                             aggfunc=lambda x: list(set(list(x))))
    print(pivoted.sort_values(ascending=True, by=identifier).head())

    # Turn pivot table into dataframe.
    new_value = pd.DataFrame(pivoted)
    new_value = new_value.reset_index()
    new_value[value] = new_value[value].apply(lambda x: '|'.join(str(v) for v in x))
    print(new_value.columns)
    print(new_value.head)
    new_filename = value+'AggregatedBy'+identifier+'_'+dt+'.csv'
    new_value.to_csv(new_filename, index=False, quoting=csv.QUOTE_ALL)
