import pandas as pd
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')  # Original data
parser.add_argument('-f2', '--file2')
parser.add_argument('-id', '--identifier')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter filename (including \'.csv\'): ')
if args.file2:
    filename2 = args.file2
else:
    filename2 = input('Enter filename (including \'.csv\'): ')
if args.id:
    identifier = args.id
else:
    identifier = input('Enter name of identifier columns: ')


df_1 = pd.read_csv(filename, header=0)
df_2 = pd.read_csv(filename2, header=0)

unique_1 = df_1[identifier].unique()
unique_2 = df_2[identifier].unique()
unique_1 = list(unique_1)
unique_2 = list(unique_2)
# not_found = unique_1 - unique_2

# Create dataframe of unique identifier values from file2.
# Add column with information about status of identifiers.
new_df = pd.DataFrame(unique_2, columns=[identifier])
new_df['found'] = 'Skip for now'


frame = pd.merge(df_1, new_df, how='left', on=[identifier],
                 suffixes=('_1', '_2'))

print(frame.columns)
print(frame.head)

# Create updated file1 with column identifying identifiers found in file2.
frame.to_csv(path_or_buf='updated'+filename)
