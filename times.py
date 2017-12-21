import read
import dateutil.parser
import datetime

df = read.load_data()

hour_part = " "

def get_hour(x):
    hour_part =dateutil.parser.parse(x).hour  
    return hour_part

hour_values = df['submission_time'].apply(get_hour)

print(hour_values.value_counts().head(2))

