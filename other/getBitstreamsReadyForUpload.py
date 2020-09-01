import csv
import argparse
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
parser.add_argument('-f2', '--file2')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter filename (including \'.csv\'): ')
if args.file2:
    filename2 = args.file2
else:
    filename2 = input('Enter 2nd filename (including \'.csv\'): ')


dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')

f = csv.writer(open('bitstreamsToUpload_'+dt+'.csv', 'w', encoding='utf-8'))

handleDict = {}

with open(filename2) as itemMetadataFile2:
    itemMetadata2 = csv.DictReader(itemMetadataFile2)
    for row in itemMetadata2:
        handle = row['handle']
        bitstream = row['bitstream']
        if handle not in handleDict:
            handleDict[handle] = [bitstream]
        elif handle in handleDict:
            value = handleDict.get(handle)
            value.append(bitstream)
            handleDict[handle] = value

newList = []

with open(filename) as itemMetadataFile:
    itemMetadata = csv.DictReader(itemMetadataFile)
    for row in itemMetadata:
        handle = row['handle']
        item_1 = row['item_1']
        item_2 = row['item_2']
        fin_name = row['final_name'].strip()
        if fin_name != 'NOT MATCH':
            value = handleDict.get(handle)
            for v in value:
                bitext = v.rsplit('.', 1)
                bit = bitext[0]
                ext = bitext[1]
                if item_1 == bit:
                    print(v)
                    newList.append([handle, v, fin_name+'.'+ext])
                elif item_2 == bit:
                    print(v)
                    newList.append([handle, v, fin_name+'.'+ext])
                else:
                    pass

for x in newList:
    print(x)
    f.writerows([x])
