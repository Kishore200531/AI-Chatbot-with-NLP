# AI-Chatbot-with-NLP

Company: CODTECH IT SOLUTIONS

Name: UDATA JOSEPH KISHORE

Intern ID: CTIS7316

Domain: PYTHON PROGRAMMING

Duration: 4 Weeks

Mentor: NEELA SANTOSH KUMAR

Task Description:

I've used Pycharm for programming. Task Title: AI Chatbot with NLP. In this code I've imported the required libraries - random (To generate random responses), nltk (NLP library), PorterStemmer from nltk.stem (For converting to root form). And then I've selected some data to train the AI chatbot along with their responses like greetings - responses, farewells - farewell_responses, questions - question_responses, small_talk - small_talk_responses. And then I've downloaded required resources from nltk library (punkt and punkt_tab) for tokenization of the sentences provided by user. And then for converting the words/tokens into their root form I've used PorterStemmer() as stemmer variable. And then I've mapped the intent categories to their corresponding response categories using INTENT_RESPONSE_MAP. And for preprocessing I've defined a function preprocess() with the argument sentence. The preprocess is used to tokenize the sentence using word_tokenize() method from nltk library and then the return statement consists of the tokens that are converted to their root form using stemmer.stem() method. And then I've defined get_response() function for getting response to the user query. This function takes an argument user_input and the user_input is preprocessed that means converted into root form of tokens and it is stored in processed_input variable. And for checking that pattern of user_input is present in the mapping categories (intent_category, response_category) in INTENT_RESPONSE_MAP.items(). And then the pattern is proprocessed and stored in processed_pattern. If the processed_input is present in the processed_pattern that means if the user_input is present in intent_category then return the random response for that input using random.choice() method. If the user query (user_input) does not present in the intent category (unknown inputs) then I've returned a default message saying "Sorry, I'm unable to understand that. Could you please try again?". And then I've defined chat() function for building a chatting interface (Interactive Communication Interface) in which a starting default message from the chatbot is shown saying "Chatbot: Hello, I'm your friendly chatbot. Type 'exit' to end conversation." And then I've used an infinite while loop which runs till the user types 'exit'. And then the input query from the user is represented by "You:", where user have to type their query/question to the chatbot. This user query is stripped using strip() method for removing unnecessary spaces. And then if the user query matches any of the intent category the chatbot gives the responses randomly from the response category using get_response() function that is defined to generate the response for any intent/query provided by the user. If the user type 'exit' the chatbot will say "Chatbot: Goodbye, see you later!" and then the infinite while loop will be stopped/breaked. And then for executing the chatbot I've called the main method using,
if __name__ == "__main__":
    chat()

Dataflow of the Code:

User input -> tokenization using nltk -> stemming with PorterStemmer -> intent matching by predefined patterns -> mapped response selection from dataset(data) -> printing chatbot reply -> loop continues until exit

Here I've used very few data and their responses for creating a chatbot. You can increase the size of the data by adding more intent and response categories for making the chatbot more trained and informative for many user queries. Even you can prefer to load the dataset in another file and can import the data from that file for easy manipulation (adding, deleting, updating) of data in the dataset.

Output:

<img width="1919" height="1076" alt="Image" src="https://github.com/user-attachments/assets/5afa952a-ba64-4d92-ad3b-535b3f3965f5" />
