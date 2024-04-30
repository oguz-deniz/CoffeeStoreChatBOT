import random
import json
import torch
from model import NeuralNet
from nltk_utils import apply_bag_of_words, tokenize

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intents.json','r') as f:
        intents = json.load(f)

FILEPATH = "chatBOT_model.pth"
model_info = torch.load(FILEPATH)
input_size = model_info["input_size"]
hidden_size = model_info["hidden_size"]
output_size = model_info["output_size"]
all_words = model_info["all_words"]
tags = model_info["tags"]
model_state_dict = model_info["model_state_dict"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state_dict)
model.eval()

def get_response(message):

    sentence = tokenize(message)
    X = apply_bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device) # Convert numpy array to tensor

    output = model(X)
    _, predicted = torch.max(output, dim=1)
    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]

    if prob.item() > 0.75:
        for intent in intents["intents"]:
            if tag == intent["tag"]:
                return random.choice(intent['responses'])
   
    return "I don't understand"
