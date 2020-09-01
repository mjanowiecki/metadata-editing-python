import pandas as pd
import argparse
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter filename (including \'.csv\'): ')

df = pd.read_csv(filename, header=0)

# Get unique names.
unique_1 = df.people.unique()
unique_2 = df.corporate.unique()

unique_1 = list(unique_1)
unique_2 = list(unique_2)

names = []
for x in unique_1:
    x = str(x)
    x = x.split('|')
    for name in x:
        if name:
            if name not in names:
                names.append(name)
for x in unique_2:
    x = str(x)
    x = x.split('|')
    for name in x:
        if name:
            if name not in names:
                names.append(name)


names = sorted(names)
url_prefix = 'https://catalyst.library.jhu.edu/catalog/bib_'

newdict = {}
for x in names:
    for index, value in df.people.iteritems():
        value = str(value)
        if x in value:
            data = newdict.get(x)
            valuetoadd = df.at[index, 'bib']
            valuetoadd = url_prefix+str(valuetoadd)
            if data:
                data.append(valuetoadd)
                newdict[x] = data
            else:
                newdict[x] = [valuetoadd]
    for index, value in df.corporate.iteritems():
        value = str(value)
        if x in value:
            data = newdict.get(x)
            valuetoadd = df.at[index, 'bib']
            valuetoadd = url_prefix+str(valuetoadd)
            if data and valuetoadd:
                data.append(valuetoadd)
                newdict[x] = data
            elif valuetoadd:
                newdict[x] = [valuetoadd]
            else:
                pass

new_list_flat = []
for k, v in newdict.items():
    print(type(v))
    v_first = v[0]
    print(v_first)
    v_first = str(v_first)
    baby_list = [k, v_first]
    new_list_flat.append(baby_list)

frame = pd.DataFrame(new_list_flat)


print(frame.head)
dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')
frame.to_csv(path_or_buf='uniqueNamesToEdit_'+dt+'.csv')
