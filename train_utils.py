import json
import numpy as np
from nltk_utils import tokenize, stem, apply_bag_of_words

def get_train_data():

    with open('intents.json','r') as f:
        intents = json.load(f)

    all_words = []
    tags = []
    xy = []

    for intent in intents['intents']:
        tag = intent['tag']
        tags.append(tag)
        for pattern in intent['patterns']:
            w = tokenize(pattern)
            all_words.extend(w)
            xy.append((w,tag))

    ignore_words = ["?","!",".",",",";"]
    all_words = [stem(w) for w in all_words if w not in ignore_words]
    all_words = sorted(set(all_words)) # set(all_words) used to remove duplicates
    tags = sorted(set(tags))
    #print(all_words)
    print("the tags:",tags)
    print("number of tags:",len(tags))

    X_train = []
    y_train = []

    for (pattern_sequence, tag) in xy:
        bow = apply_bag_of_words(pattern_sequence, all_words)
        X_train.append(bow)

        label = tags.index(tag)
        y_train.append(label) # We will use CrossEntropyLoss, thus our label should not be one-hot-vector.

    X_train = np.array(X_train)
    y_train = np.array(y_train)

    return X_train, y_train, all_words, tags
