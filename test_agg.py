import pandas as pd

# Sample dataset
data = {
    'ASS_ID': [1, 1, 1, 2, 2, 3],
    'ScreeID': ['a', 'b', 'c', 'a', 'b', 'c'],
    'entity_id': ['profile1', 'profile2', 'profile3', 'profile4', 'profile5', 'profile6']
}

df = pd.DataFrame(data)

print(df.head())

# Group by ASS_ID and aggregate entity_id into sets based on ScreeID
result = df.groupby('ASS_ID').apply(lambda group: {
    scree_id: set(group.loc[group['ScreeID'] == scree_id, 'entity_id'])
    for scree_id in group['ScreeID'].unique()
}).reset_index()

# Expand the dictionary into separate columns for each ScreeID
result.columns = ['ASS_ID', 'aggregated']
result = pd.concat([result.drop(columns='aggregated'), result['aggregated'].apply(pd.Series)], axis=1)

# Fill missing columns with empty sets (if any ScreeID is missing for a given ASS_ID)
for scree_id in ['a', 'b', 'c']:
    if scree_id not in result.columns:
        result[scree_id] = set()

print(result)
