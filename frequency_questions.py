#!/Users/local/bin/ python

import os
import csv
import sys
import pandas as pd
from pattern.es import lemma
from gensim import corpora, models, similarities
from collections import defaultdict
import logging
import scipy.sparse as sp
import numpy as np
from numpy import array
from itertools import chain
flatten = chain.from_iterable
from nltk import word_tokenize
from gensim.corpora.dictionary import Dictionary
from gensim.models.ldamodel import LdaModel
from gensim.models.tfidfmodel import TfidfModel
import PIL
from os import path
import matplotlib.pyplot as plt
from PIL import Image
from sklearn.decomposition import PCA
from scipy.cluster.hierarchy import linkage, dendrogram
from scipy.spatial.distance import pdist, squareform
import networkx as nx
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import Normalizer
from math import factorial, cos, e
from scipy import *
from scipy.spatial.distance import pdist, squareform
import itertools
import pyLDAvis.gensim
import json
from nltk import word_tokenize
import warnings
import IPython
from gensim.models.coherencemodel import CoherenceModel
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
import re
import string
import nltk
from nltk import FreqDist
from numpy import *
import collections
'''
data = loadtxt('/Users/suchinaparihar/Desktop/np3.txt',dtype=float,usecols=(0,)) #loading 1st column of csv file into array named data.
print data
plt.hist(data)
plt.show()

'''
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

documents = []
common = []



with open('/Users/suchinaparihar/Desktop/Questions.csv', 'r') as csvfile:
    df = pd.read_csv(csvfile)
    names = df['OwnerUserId']

#We start with documents represented as strings
for line in names:
    #line=line.strip('\n')
    documents.append(line)

#counter=collections.Counter(documents)
#print(counter)

documents = nltk.FreqDist(documents)
common = documents.most_common()
#word_features = list(common.values())

#common.to_csv(r'/Users/sumeetparihar/Desktop/np4.txt', header=None, index=None, sep=' ', mode='a')
#print common
#print word_features



x_val = [x[0] for x in common]
z = []
z = np.arange(len(x_val))
#print x_val
y_val = [x[1] for x in common]
#print y_val
#plt.plot(x_val,y_val)
plt.plot(y_val,z)
plt.xlabel('Number of posted questions')
plt.ylabel('Number of developers')
#plt.xscale('log')
plt.yscale('log')
#p.set_xlim([1.0,10.0])
#p.set_ylim([0.0,10.0])
plt.show()





