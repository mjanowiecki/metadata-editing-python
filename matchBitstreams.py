import csv
import argparse
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter filename (including \'.csv\'): ')

handleDict = {}
extDict = {}

dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')
f = csv.writer(open('matchedBitstreams_'+dt+'.csv', 'w', encoding='utf-8'))


with open(filename) as itemMetadataFile:
    itemMetadata = csv.DictReader(itemMetadataFile)
    for row in itemMetadata:
        bitstream = row['bitstream']
        handle = row['handle']
        title = row['title']
        bitext = bitstream.rsplit('.', 1)
        bit = bitext[0]
        ext = bitext[1].lower()
        if handle not in handleDict:
            handleDict[handle] = [bitstream]
            extDict[handle] = [ext]
        elif handle in handleDict:
            value = handleDict.get(handle)
            value.append(bitstream)
            handleDict[handle] = value
            ext_value = extDict[handle]
            if ext not in ext_value:
                ext_value.append(ext)
                extDict[handle] = ext_value
            else:
                pass
        else:
            print('no')


for key, value in extDict.items():
    handle = key
    extensionList = value
    type_count = len(extensionList)
    if type_count > 1:
        value = handleDict.get(handle)
        dict = {}
        for bitstream in value:
            bitext = bitstream.rsplit('.', 1)
            bit = bitext[0]
            ext = bitext[1]
            if ext not in dict:
                dict[ext] = [bit]
            if ext in dict:
                bits = dict.get(ext)
                bits.append(bit)
                dict[ext] = bits
        lists = list(dict.values())
        if "pdf" in dict:
            del dict['pdf']
        if "tfw" in dict:
            del dict['tfw']
        lists = list(dict.values())
        if len(lists) > 1:
            differences = []
            set1 = set(lists[0])
            set2 = set(lists[1])
            difference = set1.symmetric_difference(set2)
            for diff in difference:
                if diff not in differences:
                    differences.append(diff)
            try:
                set3 = set(lists[2])
                difference1 = set2.symmetric_difference(set3)
                difference2 = set1.symmetric_difference(set3)
                for diff in difference1:
                    if diff not in differences:
                        differences.append(diff)
                for diff in difference2:
                    if diff not in differences:
                        differences.append(diff)
            except IndexError:
                pass
            try:
                set4 = set(lists[3])
            except IndexError:
                pass
            if differences:
                print(differences)
                f.writerow([handle]+[differences])
