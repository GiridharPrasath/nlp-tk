import urllib.request
from bs4 import BeautifulSoup
import pandas as pd 
from sklearn.model_selection import train_test_split
import nltk
from nltk.corpus import stopwords
from nltk.classify import SklearnClassifier

from wordcloud import WordCloud,STOPWORDS
import matplotlib.pyplot as plt
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib','inline')

url = "https://en.wikipedia.org/wiki/Football"
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,'html5lib')
for script in soup(["script", "style"]):
    script.extract()

text = soup.get_text()

lines = (line.strip() for line in text.splitlines())
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
text = '\n'.join(chunk for chunk in chunks if chunk)

from subprocess import check_output
f=open('foot.txt','wb')
f.write(text.encode("utf-8"))
data = pd.read_fwf('foot.txt')
data = data['Football - Wikipedia']
def wordcloud_draw(data, color = 'black'):
    words =" ".join(data)
    cleaned_word = " ".join([word for word in words.split()
                            if '123' not in word
                                and not word.startswith('\t')
                                and not word.startswith('\n')
                                and word != 'RT'
                            ])
    wordcloud = WordCloud(stopwords=STOPWORDS,
                      background_color=color,
                      width=2500,
                      height=2000
                     ).generate(cleaned_word)
    plt.figure(1,figsize=(13, 13))
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()

wordcloud_draw(data)
