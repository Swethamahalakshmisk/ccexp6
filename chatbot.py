import nltk
from nltk.chat.util import Chat, reflections

nltk.download('punkt')

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how are you today?",]
    ],
    [
        r"hi|hello|hey",
        ["Hello!", "Hey there!",]
    ],
    [
        r"what is your name ?",
        ["I am a chatbot created to assist you.",]
    ],
    [
        r"how are you ?",
        ["I'm doing great, thanks for asking!", "I'm fine, how about you?"]
    ],
    [
        r"sorry (.*)",
        ["It's okay!", "No problem!"]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that!", "Great!"]
    ],
    [
        r"what can you do ?",
        ["I can chat with you and answer some basic questions.",]
    ],
    [
        r"(.*) (location|city) ?",
        ["I live in the digital world!"]
    ],
    [
        r"how is the weather in (.*)?",
        ["I'm not sure, but you can check it online!",]
    ],
    [
        r"quit",
        ["Bye! Take care.",]
    ]
]

fallbacks = [
    "I'm not sure I understand.",
    "Can you rephrase that?",
    "Sorry, I don't know the answer to that."
]

chatbot = Chat(pairs, reflections)

def start_chatbot():
    print("Hi, I'm a chatbot! Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("Chatbot: Bye! Take care.")
            break
        response = chatbot.respond(user_input)
        if response:
            print(f"Chatbot: {response}")
        else:
            print(f"Chatbot: {fallbacks[0]}")


start_chatbot()
