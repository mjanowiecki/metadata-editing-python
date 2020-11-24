from datetime import datetime
import argparse
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', help='Enter filename with csv.')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter filename (including \'.csv\'): ')


dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')

df_1 = pd.read_csv(filename, header=0)

fastBase = 'http://id.worldcat.org/fast/'
viafBase = 'http://viaf.org/viaf/'

identifier = df_1.fast_id

uriList = []
for index, value in identifier.items():
    tinyDict = {'index': index}
    if isinstance(value, str):
        if 'fst' in value:
            value = value.lstrip('fst')
            value = value.lstrip('0')
            value = value.strip()
            fastURI = fastBase + value
            tinyDict['fast_id'] = fastURI
            uriList.append(tinyDict)
        elif 'VIAF' in value:
            value = value.strip('VIAF ID:')
            value = value.strip()
            viafURI = viafBase + value
            tinyDict['fast_id'] = viafURI
            uriList.append(tinyDict)
        else:
            pass

new_df = pd.DataFrame.from_records(uriList, index='index')
print(new_df.head)

df_1.update(new_df)


df_1.to_csv(filename+'_'+dt+'.csv', index=False)
