import argparse
from datetime import datetime
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter filename (including \'.csv\'): ')

df = pd.read_csv(filename, header=0)

bitList = []
for index, row in df.iterrows():
    tinyDict = {}
    bitstream = row['bitstream']
    handle = row['handle']
    title = row['title']
    bitext = bitstream.rsplit('.', 1)
    bit = bitext[0]
    ext = bitext[1].lower()

    tinyDict['handle'] = handle
    tinyDict['bitstream'] = bitstream
    tinyDict['bit'] = bit
    tinyDict['ext'] = ext
    bitList.append(tinyDict)

df_bit = pd.DataFrame.from_dict(bitList)
print(df_bit)

frame_1 = df_bit[['handle', 'bit']].copy()
pivot = pd.pivot_table(frame_1, index='handle',
                       values='bit',
                       aggfunc=lambda x: list(x))

df_p = pd.DataFrame(pivot)
df_p = df_p.reset_index()
print(df_p)


frame_2 = df_bit[['handle', 'ext']].copy()
pivot_2 = pd.pivot_table(frame_2, index='handle',
                         values='ext',
                         aggfunc=lambda x: list(x))

df_p2 = pd.DataFrame(pivot_2)
df_p2 = df_p2.reset_index()
print(df_p2)
frame_3 = df_bit[['handle', 'bitstream']].copy()
pivot_3 = pd.pivot_table(frame_3, index='handle',
                         values='bitstream',
                         aggfunc=lambda x: list(x))

df_p3 = pd.DataFrame(pivot_3)
df_p3 = df_p3.reset_index()
print(df_p3)

merged = pd.merge(df_p, df_p2, how='outer', on='handle')
df_merge = pd.merge(merged, df_p3, how='outer', on='handle')
print(df_merge)

lonely = []
for index, row in df_merge.iterrows():
    tiny = {}
    extensions = row['ext']
    handle = row['handle']
    tiny['handle'] = handle
    bits = row['bit']
    type_count = len(extensions)
    if type_count > 1:
        bits = pd.Series(bits)
        counts = bits.value_counts()
        for index, value in counts.items():
            if value > 1:
                matchList = tiny.get('matched')
                if matchList is None:
                    tiny['matched'] = [index]
                else:
                    matchList = matchList
                    matchList.append(index)
                    tiny['matched'] = matchList
            else:
                lonelyList = tiny.get('lonely')
                if lonelyList is None:
                    tiny['lonely'] = [index]
                else:
                    lonelyList = lonelyList
                    lonelyList.append(index)
                    tiny['lonely'] = lonelyList
    else:
        tiny['single'] = bits

    lonely.append(tiny)

bitPairs = pd.DataFrame.from_dict(lonely)
dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')
bitPairs.to_csv('matchedCSV_'+dt+'.csv')
