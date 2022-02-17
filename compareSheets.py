import pandas as pd
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--directory')
args = parser.parse_args()

if args.directory:
    directory = args.directory
else:
    directory = input('Enter directory: ')

columns = ['uri', 'print_bib', 'barcode', 'call_number']


def makeDataFrame(frame, complete_filename, file):
    frame = pd.read_csv(complete_filename)
    for c in frame.columns:
        if c not in columns:
            frame = frame.drop(columns=c)
        else:
            pass
    for c in frame.columns:
        if c != 'uri':
            frame = frame.rename(columns={c:'{}_{}'.format(file, c)})
    print(frame)
    frames.append(frame)


frames = []
for count, filename in enumerate(os.listdir(directory)):
    complete_filename = directory + "/" + filename
    file = filename[:-4]
    if complete_filename.endswith('.csv'):
        makeDataFrame("df_{}".format(file), complete_filename, file)

frame_count = len(frames)
print(frame_count)


merged = []
for count, frame in enumerate(frames):
    if count == 0:
        new_df = pd.merge(frame, frames[count+1], how='outer', on='uri')
        merged.append(new_df)
    elif count == 1:
        pass
    else:
        new_df = pd.merge(merged[0], frame, how='outer', on='uri')
        merged[0] = new_df

mergedFrame = merged[0]
mergedFrame = mergedFrame.drop_duplicates(keep='first')
print(mergedFrame.columns)
mergedFrame = mergedFrame.set_index(keys='uri')
mergedFrame = mergedFrame.dropna(axis=0, how='all')
print(mergedFrame.columns)

new_df = []
for index, row in mergedFrame.iterrows():
    bibList = []
    callList = []
    barList = []
    for column in mergedFrame.columns:
        if 'bib' in column:
            value = row[column]
            if pd.notna(value):
                try:
                    value = str(int(value))
                except:
                    value = str(value)
                bibList.append(value)
        elif 'call_number' in column:
            value = row[column]
            if pd.notna(value):
                value = str(value)
                callList.append(value)
        else:
            value = row[column]
            if pd.notna(value):
                value = str(value)
                barList.append(value)
    bibList = set(bibList)
    callList = set(callList)
    barList = set(barList)
    if (len(bibList) > 1) or (len(callList) > 1) or (len(barList) > 1):
        row['bibList'] = bibList
        row['callList'] = callList
        row['barList'] = barList
        new_df.append(row)

new_df = pd.DataFrame.from_dict(new_df)
new_df.to_csv('new.csv')
