# Coffee Store ChatBOT

Coffee Store ChatBOT is a simple chatbot application built using Python and Tkinter. It simulates a conversation with a chatbot in a coffee shop setting, allowing users to interact with the chatbot to inquire about various aspects of the coffee shop. The chatbot takes its spirit from the legendary persona Çaycı Hüseyin in the famous Turkish TV series "Çocuklar Duymasın".

## Project Components

### Training Data

The training data for the chatbot is provided in the `intents.json` file. This file contains sequences categorized under different tags, each representing various conversation topics. Each tag includes patterns of user queries and relevant responses.

### Neural Network Implementation

To generate correct responses, a basic neural network model is implemented using PyTorch. The model architecture can be found in either the `ChatBOT.ipynb` notebook or the `model.py` file. PyTorch framework is utilized throughout the AI model's implementation and training process.

### Natural Language Processing (NLP)

Python's NLTK library is employed for basic natural language processing tasks. The preprocessing pipeline involves tokenization, converting text to lowercase and stemming, excluding punctuation characters, and creating a bag of words representation.

1. **Tokenization**: Breaking down the text into individual words or tokens.
2. **Lowercasing and Stemming**: Converting the text to lowercase and reducing words to their root form to normalize variations.
3. **Excluding Punctuation Characters**: Removing punctuation marks from the text to focus on the meaningful words.
4. **Bag of Words Representation**: Converting the processed text into a numerical representation using a bag of words model.

These preprocessing steps help in transforming the raw text data into a format that can be effectively utilized by the neural network model.

### Data Preparation

The `train_utils.py` script is developed to prepare the training data from the raw `intents.json` file. This script processes the data and generates the necessary format for training the neural network model.

### Model Training

Since the dataset is relatively simple and small, no further model fine-tuning is required after training the neural network.

### Graphical User Interface (GUI)

To enhance user experience and accessibility, a basic graphical user interface (GUI) is implemented in `gui.py`. The responses generated by the neural network model are connected to the GUI application via the `chat.py` script.

## Example Dialogues

Here are some examples of the dialogues supported by the Coffee Shop ChatBOT:

<img src="https://github.com/oguz-deniz/Teknofest24/assets/98212476/9fdf0117-8596-47ed-ada6-e8268d634f78" alt="Ekran Görüntüsü (205)" width="400" height="523"> 
<img src="https://github.com/oguz-deniz/Teknofest24/assets/98212476/8124bca7-293d-403b-a94a-cd23b3ead1ba" alt="Ekran Görüntüsü (205)" width="400">

## Conclusion

The Coffee Shop ChatBOT project combines basic natural language processing techniques, neural network implementation, and GUI development to create an interactive chatbot application for coffee shop-related inquiries. The project aims to be a good example of a basic software that provides a user-friendly and engaging experience for customers seeking information about a coffee shop's offerings and services.



