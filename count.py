import read
from collections import Counter
import re

df = read.load_data()
string = " "
words_num = 100

for headline in df['headline']:
    headline = str(headline).lower()
    string = string + headline
  
words = re.findall(r'\w+', string)

top_words = Counter(words).most_common(words_num)

print(top_words)
