import argparse
from datetime import datetime
import pandas as pd
import ast

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter first filename (including \'.csv\'): ')

df = pd.read_csv(filename)


count = 0
bitlist = []
for index, data in df.iterrows():
    bit = data['bitstreams']
    handle = data['JHIR']
    handle = handle.replace('http://jhir.library.jhu.edu/handle/', '')
    if pd.notna(bit):
        bit = ast.literal_eval(bit)
        if isinstance(bit, list):
            bit_count = len(bit)
            print(bit_count)
            count = count + bit_count
            for b in bit:
                bitlist.append({'bitstream': b, 'handle': handle})
print(count)

dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')
df_1 = pd.DataFrame(bitlist)
df_1.to_csv(filename+'_'+dt+'.csv', index=False)
