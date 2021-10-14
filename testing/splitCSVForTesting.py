import argparse
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
parser.add_argument('-d', '--divide')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter filename (including \'.csv\'): ')
if args.divide:
    divide = args.divide
else:
    divide = input('Enter the number to divide the spreadsheet by: ')


df = pd.read_csv(filename)
total_rows = len(df.index)
print(total_rows)
x = total_rows/int(divide)
x = round(x)
print(x)
current_row = 0
loop = 0
while total_rows > 0:
    loop = loop + 1
    total_rows = total_rows - x
    print('sheet {}: rows {}-{}'.format(loop, current_row, (current_row+x)))
    current_row = current_row + x
    newDF = pd.DataFrame()
    newDF = newDF.append((df.iloc[(current_row - x):current_row]),
                         ignore_index=True, sort=True)
    newDF.to_csv('graphicPictorial_media_'+(str(loop)).zfill(2)+'.csv', index=False)
