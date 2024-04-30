import nltk
import numpy as np
# nltk.download('punkt') # To be able to use pretrained string tokenizer
from nltk.stem.porter import PorterStemmer

stemmer = PorterStemmer()

def tokenize(sentence):
    return nltk.word_tokenize(sentence)

def stem(word):
    word = word.lower()
    return stemmer.stem(word)

def apply_bag_of_words(tokenized_sentence, all_words):
    tokenized_sentence = [stem(w) for w in tokenized_sentence]

    bow = np.zeros(len(all_words), dtype=np.float32)
    for idx, w in enumerate(all_words):
        if w in tokenized_sentence:
            bow[idx] = 1.0

    return bow

sentence = ["hello","how","are","you"]
all_words = ["hi","hello","I","you","bye","thank","cool"]
bow = apply_bag_of_words(sentence, all_words)
#print(bow)

"""
a = "How much do you bench brother?"
print(a)
a = tokenize(a)
print("tokenized:",a)
stemmed = [stem(w) for w in a]
print(stemmed)"""
