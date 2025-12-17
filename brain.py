import json
import random
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC

class Brain:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.classifier = SVC(kernel='linear', probability=True)
        self.tags = []
        self.load_and_train()

    def load_and_train(self):
        with open('data/intents.json', 'r') as file:
            data = json.load(file)

        training_sentences = []
        training_labels = []
        self.responses = {}

        for intent in data['intents']:
            self.responses[intent['tag']] = intent['responses']
            for pattern in intent['patterns']:
                training_sentences.append(pattern)
                training_labels.append(intent['tag'])

        print("Training AI Model...")
        vectors = self.vectorizer.fit_transform(training_sentences)
        self.classifier.fit(vectors, training_labels)
        print("Model Trained Successfully!")

    def predict(self, text):
        vector = self.vectorizer.transform([text])
        prediction = self.classifier.predict(vector)[0]
        return prediction

    def get_response(self, tag):
        return random.choice(self.responses[tag])

if __name__ == "__main__":
    ai = Brain()
    test_text = input("Enter command: ")
    tag = ai.predict(test_text)
    print(f"Predicted Intent: {tag}")