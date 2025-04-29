# Incomplete
# Goal: Experimentation
# Eg: Choose which version of web page is better
# Ranking changes in search results
# Changes in user interface
# Changes in recommendation engine
# Baseline comparison
# Time for adapting the new experience
# Not useful: Recommendation of apartments - frequency of visits, impact on referrals
# Clear control and metrics
# Control vs Experiment group
# More data points (but less resolution)
# Make decision based upon the experimentation (metrics)
# Customer funnel


# When to use A/B Testing
# Movie recommendation engine: new ranking algorithm


# Other techniques - if A/B testing is not possible
# Use of logs over the time - analyze the pattern and behavior
# User experience research (lot more details from few users), Focus groups, Surveys, Human evaluation, qualitative feedback
# Redo of entire site - hard to run a control experimentation

# Example

# Steps 
# Choose a metric - eg Click through rate, click through probability
# Click through rate = number of clicks / number of page views
# Click through probability = number of unique visitors who click / number of unique visitors
# visitors = 1000, unique clicks = 100, Click through P = 10%
# Review statistics
# Binomial distribution, CI, Hypothesis testing
# Bell curve/Normal distribution, Slightly different than Binomail distribution, Click-success/No-click - failure
# 
# Design an experiment
# Analyze the results
# Make a decision

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