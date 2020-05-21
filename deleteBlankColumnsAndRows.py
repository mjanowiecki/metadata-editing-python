
import pandas as pd

filename = 'agentSpreadsheet.csv'

df = pd.read_csv(filename)
df = df.dropna(axis=0, how='all')
df = df.dropna(axis=1, how='all')

df.to_csv(path_or_buf='fixed.csv', index=False)
