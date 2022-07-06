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

dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')
f = csv.writer(open('reformattedNames_'+dt+'.csv', 'w'))
f.writerow([['title']+['names_reformatted']])

suffixes = ["Jr.", "Sr.", "II", "III", "IV"]


def check_for_suffix(name_p1):
    for s in suffixes:
        if s in name_p1:
            suffix = s
            s_len = len(suffix)+1
            name_1 = name_p1[:-s_len]
        else:
            name_1 = name_p1
            suffix = ''
        return suffix, name_1


def check_if_suffix(name_p3):
    for s in suffixes:
        if s == name_p3:
            suffix = name_p3
        else:
            suffix = ''
        return suffix


with open(filename) as itemMetadataFile:
    itemMetadata = csv.DictReader(itemMetadataFile)
    for row in itemMetadata:
        names = row['title']
        n_list = names.split('|')
        new_names = []
        for name in n_list:
            if 0 < name.count(',') < 3:
                name_parts = name.split(',')
                name_p2 = name_parts[0].strip()
                name_p1 = name_parts[1].strip()
                try:
                    name_p3 = name_parts[2].strip()
                    suffix = check_if_suffix(name_p3)
                    if suffix:
                        new_name = name_p1+' '+name_p2+' '+suffix
                        new_names.append(new_name)
                    else:
                        new_name = name_p1+' '+name_p2+' '+name_p3
                        new_names.append(new_name)
                except IndexError:
                    suffix, name_1 = check_for_suffix(name_p1)
                    if suffix:
                        new_name = name_1+' '+name_p2+' '+suffix
                        new_names.append(new_name)
                    else:
                        new_name = name_1+' '+name_p2
                        new_names.append(new_name)
            else:
                name = name.strip()
                new_names.append(name)

        new_string = ', '.join(new_names)
        f.writerow([names]+[new_string])