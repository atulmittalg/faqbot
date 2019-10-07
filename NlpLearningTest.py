import nltk
from nltk.stem import WordNetLemmatizer 
from nltk.stem import PorterStemmer 
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()
for index in range(5): 
    input_sentence = input("Please enter your Query? ")
    words = word_tokenize(input_sentence)
    for word in words:
        if word in stopwords.words('english'):
            words.remove(word)
    print(words)          
    freq = nltk.FreqDist(words) 
    for key,val in freq.items():
        print('using Lemmatization: ' + lemmatizer.lemmatize(str(key)) + '--------' + 'using Stemming : ' + stemmer.stem(str(key)) + '--------- count of the word in the sentence:' + str(val))
