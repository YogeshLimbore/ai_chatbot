from flask import Flask, render_template, request

app = Flask(__name__)

class Chatbot:
    def __init__(self):
        self.questions = {
            "1": {"question": "What is your name?", "answer": "My name is Chatbot."},
            "2": {"question": "How old are you?", "answer": "I am just a computer program."},
            "3": {"question": "Where are you from?", "answer": "I exist in the digital world."},
            "4": {"question": "how we can fill information in basic information portal?", "answer": "we can fill it by click on profile section and fill it."}
            # Add more questions and answers as needed
        }

    def get_options(self):
        options = []
        for key, value in self.questions.items():
            options.append({"key": key, "question": value['question']})
        return options

    def get_answer(self, question_key):
        return self.questions.get(question_key, {}).get('answer', "Sorry, I don't have an answer to that question.")

    def recognize_question(self, user_input):
        # Check for exact match first
        if user_input in self.questions:
            return self.questions[user_input]["answer"]
        else:
            # Check for keyword matching
            matched_questions = []
            for key, value in self.questions.items():
                if user_input.lower() in value['question'].lower():
                    matched_questions.append({"key": key, "question": value['question']})
            return matched_questions

# Instantiate the chatbot
chatbot = Chatbot()

@app.route('/api/chatbot', methods=['GET', 'POST'])
def index():
    response = None
    matched_questions = []
    if request.method == 'POST':
        user_input = request.form['message']
        matched_questions = chatbot.recognize_question(user_input)
    elif request.method == 'GET' and 'question_key' in request.args:
        question_key = request.args.get('question_key')
        response = chatbot.get_answer(question_key)
    return render_template('index.html', matched_questions=matched_questions, response=response)

if __name__ == '__main__':
    app.run(debug=True)
