
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt

from subprocess import check_output

df = pd.read_csv('C:/Users/IBM_ADMIN/PycharmProjects/Python1/data/redditworldnews.csv')

from wordcloud import WordCloud, STOPWORDS

word_string=" ".join(df['title'].str.lower())
wordcloud = WordCloud(stopwords=STOPWORDS,
                          background_color='white',
                      max_words=300
                         ).generate(word_string)

plt.clf()
plt.imshow(wordcloud)
plt.axis('off')
plt.show()

