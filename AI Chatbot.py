import random
import nltk
from nltk.stem import PorterStemmer

data = {
    "greetings": ["hello", "hi", "hey", "what's up", "yo", "good morning", "good afternoon", "good evening"],
    "responses": ["Hello!", "Hi there!", "Hey!", "Greetings!", "How can I help you!", "Nice to see you!", "Hi, how are you?", "Hey, what's going on?"],
    "farewells": ["bye", "goodbye", "see you later", "take care", "farewell", "have a good day", "catch you later"],
    "farewell_responses": ["Bye!", "Goodbye!", "See You Later!", "Take Care!", "Have a Great Day!", "Bye! Comeback soon.", "Farewell!"],
    "questions": ["how are you", "who are you", "what's your name", "what can you do", "who created you", "what's the weather today"],
    "question_responses": ["I'm just a chatbot, but I'm doing great!", "I'm your friendly chatbot!", "I can answer questions and chat with you.", "I'm a chatbot created by a developer."],
    "small_talk": ["tell me a joke", "what's new", "how's it going", "what are you up to"],
    "small_talk_responses": ["Why don't scientists trust atoms? Because they make up everything!", "Not much, just here to chat with you!", "It's going well, thanks for asking!"]
}

#Download required resources
nltk.download('punkt') #Helps to tokenize
nltk.download('punkt_tab')

stemmer = PorterStemmer() #Convert words to their root form

#Map intent categories to their corresponding response categories
INTENT_RESPONSE_MAP = {"greetings" : "responses", "farewells" : "farewell_responses", "questions" : "question_responses", "small_talk" : "small_talk_responses"}

def preprocess(sentence):
    tokens = nltk.word_tokenize(sentence.lower())
    return {stemmer.stem(token) for token in tokens}

def get_response(user_input):
    processed_input = preprocess(user_input)
    #Check for all pattern categories
    for intent_category, response_category in INTENT_RESPONSE_MAP.items():
        for pattern in data[intent_category]:
            processed_pattern = preprocess(pattern)
            if all(word in processed_input for word in processed_pattern):
                return random.choice(data[response_category])

    #Fall back for unknown inputs
    return "Sorry, I'm unable to understand that. Could you please try again?"

def chat():
    print("Chatbot: Hello, I'm your friendly chatbot. Type 'exit' to end conversation.")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye, see you later!")
            break
        response = get_response(user_input)
        print(f"Chatbot: {response}")

#To execute the Chatbot
if __name__ == "__main__":
    chat()