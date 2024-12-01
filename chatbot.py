   # Importing necessary libraries
import nltk
import random
import spacy
from nltk.corpus import wordnet

nltk.download("punkt")
nltk.download("wordnet")

nlp = spacy.load("en_core_web_sm")

  # Declaring responses of chatbot
responses={
    "greeting": ["Hello! How can I assist you today?", "Hi there! How can I help you?", "Hey! What can I do for you?"],
    "farewell": ["Goodbye! Have a great day!", "Bye! Take care!", "See you soon!"],
    "thank_you": ["You're welcome!", "No problem!", "Happy to help!"],
    "how": ["I am great, how are you doing.","I am absolutely right.","I am good."],
    "who": ["I am a chatbot made for your conversation.","I am chatbot develope by Nadia Taj.","I am chatbot your friend."],
    'language':["I am developed in Python language.",'My source code is python.',"python is my developing language."],
    "programmer":["Nadia Taj is my programmer.","I was developed by Nadia Taj.","Nadia Taj cretaed me."],
    "education":["I am application i can not get education ."," Humans are present to feed information.","I am educated by default."],
    "unknown": ["I'm not sure I understand. Could you rephrase?", "I'm here to help, but I need more information.", "Can you clarify?"],
}

intents = {
    "greeting": ["hello", "hi", "hey", "greetings"],
    "farewell": ["bye", "goodbye", "see you"],
    "thank_you": ["thanks", "thank you", "appreciate"],
    "how" : ["how","whats","how"],
    "who" :["who","who","who"],
    'language': ['which','language','what'],
    'programmer':['who develop','who is','who create'],
    "education": ['education','knowledge','qualification']
}

# Tokenize and find synonyms for a word using NLTK
def get_synonyms(word):
    synonyms = set()
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.add(lemma.name().lower())
    return synonyms


# Expand intents with synonyms
expanded_intents = {}
for intent, keywords in intents.items():
    expanded_keywords = set(keywords)
    for word in keywords:
        expanded_keywords.update(get_synonyms(word))
    expanded_intents[intent] = expanded_keywords


# Match user input to an intent
def get_intent(user_input):
    doc = nlp(user_input.lower())
    tokens = [token.text for token in doc]
    for intent, keywords in expanded_intents.items():
        if any(token in keywords for token in tokens):
            return intent
    return "unknown"

# Chatbot function
def chatbot():
    print("Chatbot: Hi! I'm your assistant. Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye! Have a great day!")
            break
        intent = get_intent(user_input)
        response = random.choice(responses[intent])
        print(f"Chatbot: {response}")


# Run the chatbot
if __name__ == "__main__":
    chatbot()