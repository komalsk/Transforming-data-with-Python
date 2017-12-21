import pandas as pd

def load_data():
    dataset = pd.read_csv("hn_stories.csv", header=None)
    dataset.columns = ["submission_time",
                      "upvotes",
                      "url",
                      "headline"]
    return dataset
    
temp = load_data()
#print(temp.head(5))
