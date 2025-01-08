# Simple Chatbot Program


# Importing random module to randomly select responses from a list
import random


# predefined responses for various user inputs using a dictionary to stroe predefined responses
responses = {
    "hello":["Hi, there!", "Hello! How can i help you"],
    "how are you": ["I am just a bot, but I'am doing great"],
    "what is your name": ["I'm Chatbot, your friendly assistant.", "You can call me ChatBot!"],
    "what can you do": ["I can chat with you and answer simple queries.", "I am here to keep you company"],
    "tell me a joke": ["why don't skeletons fight each other? They don't have the guts.", "Why did the scraecrow win an award? Because he was outstanding in his field.", "what do you call fake spaghetti? An impasta!"],
    "bye": ["goodbye!", "See you later"],
    "default": ["I am not sure about that. Can you rephrase?", "Sorry, I didn't catch that."]
}
# "default" key provides a fallback response when no match is found.

# function to generate a response based on the urse input
def chatbot_response(user_input):
    for key in responses.keys():# iterating over each key in the dictionary to check if its in the users input 
        if key in user_input.lower():
            return random.choice(response[key]) #if the key matches return a random response associated with that key
        return random.choice(response["default"]) # if no key matches return a default response
    
print("Chatbot: Hello! Type 'bye' to exit.") # intial greeting when the chatbot starts

# infinite loop to keep the chatbot running until the user exits
while True:
    user_input = input("You: ") # accepting user input
    if user_input.lower() == "bye": # checking if the user wants to exit the chat
        print("Chatbot: Goodbye!")
        break # exit the loop and program when the user types "bye"
    print("Chatbot:", chatbot_response(user_input)) # Displaying the chatbots response to user
    
