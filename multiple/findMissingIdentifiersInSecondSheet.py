import pandas as pd
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
parser.add_argument('-f2', '--file2')
parser.add_argument('-id', '--identifier')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter first (original) filename (including \'.csv\'): ')
if args.file2:
    filename2 = args.file2
else:
    filename2 = input('Enter second (new) filename (including \'.csv\'): ')
if args.id:
    identifier = args.id
else:
    identifier = input('Enter name of identifier columns: ')


df = pd.read_csv(filename)
df_2 = pd.read_csv(filename2)

# Get list of identifiers.
id_1 = df[identifier].to_list()
id_2 = df_2[identifier].to_list()

# Prints any duplicate identifiers in files.
duplicates = df[identifier].duplicated()
for index, item in duplicates.items():
    if item:
        print(index, item)

duplicates_2 = df_2[identifier].duplicated()
for index, item in duplicates_2.items():
    if item:
        print(index, item)

# Finds any identifers in file 1, but missing from file 2.
missing = set(id_1) - set(id_2)
print(len(missing))
print(missing)


# Creates dictionary of missing identifiers information using file 1.
new_dict = []
for index, data in df.iterrows():
    for k, v in data.items():
        if k == identifier:
            if v in missing:
                new_dict.append(data)

# Prints dictionary of missing info to csv.
newDF = pd.DataFrame.from_dict(new_dict)
newDF.to_csv(path_or_buf='notFound.csv', index=False)
