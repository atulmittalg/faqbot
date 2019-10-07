##import nltk
##import urllib.request
##response =  urllib.request.urlopen('https://en.wikipedia.org/wiki/SpaceX')
##html = response.read()
##print(html)
##from bs4 import BeautifulSoup
##soup = BeautifulSoup(html,'html.parser')
##text = soup.get_text(strip = True)
##print(text)
##tokens = [t for t in text.split()]
##print(tokens)
##from nltk.corpus import stopwords
##sr= stopwords.words('english')
##clean_tokens = tokens[:]
##for token in tokens:
##    if token in stopwords.words('english'):
##        
##        clean_tokens.remove(token)
##print(clean_tokens)
##freq = nltk.FreqDist(clean_tokens)
##for key,val in freq.items():
##    print(str(key) + ':' + str(val))
##freq.plot(20, cumulative=False)
from bs4 import BeautifulSoup 
import urllib.request 
import nltk 
from nltk.corpus import stopwords 
response = urllib.request.urlopen('http://php.net/') 
html = response.read() 
soup = BeautifulSoup(html,"html.parser") 
text = soup.get_text(strip=True) 
tokens = [t for t in text.split()] 
clean_tokens = tokens[:] 
sr = stopwords.words('english') 
for token in tokens: 
    if token in stopwords.words('english'): 
        clean_tokens.remove(token) 
freq = nltk.FreqDist(clean_tokens) 
for key,val in freq.items(): 
    print (str(key) + ':' + str(val))

freq.plot(20,cumulative=False)

