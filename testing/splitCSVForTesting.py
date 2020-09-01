import argparse
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter filename (including \'.csv\'): ')


df = pd.read_csv(filename)
total_rows = len(df.index)
print(total_rows)
x = total_rows/10
x = round(x)
current_row = 0
while total_rows > 0:
    total_rows = total_rows - x
    current_row = current_row + x
    print(current_row - x)
    print(current_row)
    newDF = pd.DataFrame()
    newDF = newDF.append((df.iloc[(current_row - x):current_row]),
                         ignore_index=True, sort=True)
    newDF.to_csv(path_or_buf='test'+str(current_row)+'.csv', index=False)
