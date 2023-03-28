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

# needed for word normalization
import pymorphy2

# FOR README - stopwords and punkt

def format_text():
    f = open('text-for-analys/2.Гарри_Поттер_и_Тайная_комната.txt', 'r', encoding='utf-8')
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
    morph = pymorphy2.MorphAnalyzer()
    

    noun_tokens = []
    adjf_tokens = []
    verb_tokens = []

    # Get normalize for of current word
    for token in text_tokens:
        p = morph.parse(str(token))[0]

        if "NOUN" in p.tag:
            noun_tokens.append(p.normal_form)

        elif "ADJF" in p.tag or "ADJS" in p.tag:
            adjf_tokens.append(p.normal_form)

        elif "VERB" in p.tag or "INFN" in p.tag:
            verb_tokens.append(p.normal_form)

    # Function for split type of words
    def text_cloud(tokens):
        text = nltk.Text(tokens)

        # Countiong words by the popularity
        tdist = FreqDist(text)

        # Formation stop words and scrubbing them
        stop_words = stopwords.words("russian")
        text_tokens = [token.strip() for token in tokens if token not in stop_words]
    
        text = nltk.Text(text_tokens)
        tdist_sw = FreqDist(text)
        #print(tdist_sw.most_common(10))

        stop_words.extend(['это', 'всё', 'который', 'сказать', 'свой', 'еще', 'её', 'видеть', 'говорить', 'думать', 'сказать', 'весь', 'мочь', 'знать', 'хотеть'])
        text_tokens = [token.strip() for token in text_tokens if token not in stop_words]
        text = nltk.Text(text_tokens)
        fdist_sw = FreqDist(text)

        # Picture rendering
        text_raw = " ".join(text)
        wordcloud = WordCloud(width=1600, height=800).generate(text_raw)
        plt.figure( figsize=(20,10), facecolor='k')
        plt.imshow(wordcloud)
        plt.axis("off")
        plt.tight_layout(pad=0)
        plt.show()
    
    text_cloud(noun_tokens)
    text_cloud(adjf_tokens)
    text_cloud(verb_tokens)
    

if __name__ == "__main__":
    format_text()
