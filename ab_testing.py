import pandas as pd

df = pd.read_csv('homepage_actions.csv')
df.head()

# total number of actions
df.shape

# number of unique users
len(set(df['id']))

# size of control group and experiment group
len(set(df[df['group'] == 'control']['id']))

len(df[df['group'] == 'experiment'])

# duration of this experiment
(min(df['timestamp']),max(df['timestamp']))

# action types in this experiment
df['action'].unique()