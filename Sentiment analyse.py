# -*- coding: utf-8 -*-
"""
Created on Thu May  9 11:48:47 2019

@author: Stephanie
"""
import pandas as pd
import matplotlib.pyplot as plt
#matplotlib inline  
import nltk
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import LancasterStemmer, WordNetLemmatizer, PorterStemmer
from wordcloud import WordCloud, STOPWORDS
from textblob import TextBlob