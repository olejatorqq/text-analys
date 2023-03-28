import string
import re

# nltk necessary for tokenization of words
from nltk import word_tokenize
import nltk

# import statistic
from nltk.probability import FreqDist

# import stopwords
from nltk.corpus import stopwords

# needed to build word clouds
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# FOR README - stopwords and punkt

def format_text():
    f = open('text-for-analys/1.Гаррии_Поттер_и_философский_камень.txt', 'r', encoding='utf-8')
    text = f.read()
    text = text.lower()
    spec_chars = string.punctuation + '«»\t—…’'

    # Cleaning the text from punctuation marks
    text = "".join([ch for ch in text if ch not in spec_chars])
    text = re.sub('\n', ' ', text)

    # Removing numbers from text
    text = "".join([ch for ch in text if ch not in string.digits])
    
    # Tokenization text
    text_tokens = word_tokenize(text)
    text = nltk.Text(text_tokens)

    # Countiong words by the popularity
    tdist = FreqDist(text)

    # Formation stop words and scrubbing them
    stop_words = stopwords.words("russian")
    stop_words.extend(['–', 'это'])
    text_tokens = [token.strip() for token in text_tokens if token not in stop_words]
    
    text = nltk.Text(text_tokens)
    tdist_sw = FreqDist(text)
    #print(tdist_sw.most_common(10))
    
    # Picture rendering
    text_raw = " ".join(text)
    wordcloud = WordCloud(width=1600, height=800).generate(text_raw)
    plt.figure( figsize=(20,10), facecolor='k')
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.show()

    




if __name__ == "__main__":
    format_text()