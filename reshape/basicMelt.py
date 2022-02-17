import pandas as pd

filename = ''
df_1 = pd.read_csv(filename, header=0)

df_1 = df_1.melt(id_vars=['local_identifier'])
print(df_1.head)
df_1.to_csv('melted_.csv')
