import numpy as np; #linear algebra

array1 = np.array([1, 2, 3]);
print(array1[1] ** 3);

name = raw_input ("What is your name?")
quest = raw_input ("What is your quest?")
color = raw_input ("What is your favorite color?")

print "Ah, so your name is %s, your quest is %s, " \
      "and your favorite color is %s." % (name, quest, color)

bool_one = not True

bool_two = not 3**4 < 4**3

bool_three = not 10 % 3 <= 10 % 2

bool_four = not 3**2 + 4**2 != 5**2

bool_five = not not False

print bool_one;
print bool_two;
print bool_five;

number=-55;
print abs(number)

import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)


df = pd.read_csv(r'C:\Users\IBM_ADMIN\PycharmProjects\Python1\data\redditworldnews.csv')
# Any results you write to the current directory are saved as output.

import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, random_color_func

word_string=" ".join(df['title'].str.lower())
wordcloud = WordCloud(stopwords=STOPWORDS,background_color= '#ff8080',max_words=300).generate(word_string)

plt.clf()
plt.imshow(wordcloud)
plt.axis ('off')
plt.show()






