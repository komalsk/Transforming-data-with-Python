import pandas as pd

df = pd.read_csv("hn_stories.csv", header=None)

df.columns = ['submission_time', 'upvote', 'url', 'headline']

domains = df['url'].value_counts()

#print(domains.head(2))

for name, row in domains.items():
    print("{0}: {1}".format(name, row))