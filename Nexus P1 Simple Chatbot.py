import random

class SimpleChatbot:
    def __init__(self):
        self.previous_context = {}

    def greet(self):
        return "Hello! I'm your simple chatbot. How can I help you today?"

    def farewell(self):
        return "Goodbye! If you have more questions, feel free to ask later."

    def respond_to_question(self, question):
        if "how are you" in question.lower():
            return "I'm just a computer program, but thanks for asking!"
        elif "your name" in question.lower():
            return "You can call me Chatbot."
        elif "weather" in question.lower():
            return "I'm sorry, I don't have real-time information. You may want to check a weather website."
        elif "joke" in question.lower():
            return "Why don't scientists trust atoms? Because they make up everything!"
        elif "bye" in question.lower():
            return self.farewell()
        else:
            return "I'm not sure how to respond to that. Can you ask me something else?"

    def ask_user_questions(self):
        questions = ["What's your favorite color?", "Do you enjoy programming?", "Have you been on any vacations recently?"]
        user_responses = {}

        for question in questions:
            user_input = input(question + " ")
            user_responses[question] = user_input

        return user_responses

    def chat(self):
        print(self.greet())

        for _ in range(3):
            user_responses = self.ask_user_questions()
            self.previous_context.update(user_responses)

            print("\nLet me think about that...")
            for question, user_response in user_responses.items():
                print(f"You mentioned '{user_response}' when I asked: {question}")

            print("\nResponding to your input...")
            response = self.respond_to_question(random.choice(list(user_responses.values())))
            print(response)

        print(self.farewell())

if __name__ == "__main__":
    chatbot = SimpleChatbot()
    chatbot.chat()
