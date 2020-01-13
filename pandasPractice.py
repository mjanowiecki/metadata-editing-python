pivoted = pd.pivot_table(df, index=['dc.subject'], values='uri', aggfunc=lambda x: ','.join(str(v) for v in x))


pivoted = pd.pivot_table(df, index='dc.subject', values='uri', aggfunc='count')

pivoted.sort_values(ascending=False, by='uri').head()

df.shape
df.shape[0]
df.shape[1]

df[(df['dc.subject']=='marine') | (df['dc.subject']=='wave')]


df[df['dc.subject']=='wave']
