from flask import Flask, request, jsonify
import os
import together

app = Flask(__name__)

# Initialize the Together API
together_api = together.Together(api_key=os.environ["TOGETHER_API_KEY"])

# Define a function to handle chatbot responses
def handle_response(message):
    response = together_api.get_response(message)
    return response

# Define a route for the chatbot API
@app.route("/chat", methods=["POST"])
def chat():
    message = request.json["message"]
    response = handle_response(message)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
