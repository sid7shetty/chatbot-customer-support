from flask import Flask, request, jsonify, render_template
from transformers import pipeline

app = Flask(__name__)

# Load pre-trained model for intent classification and NER
intent_pipeline = pipeline('text-classification', model='distilbert-base-uncased-finetuned-sst-2-english')
ner_pipeline = pipeline('ner', model='dbmdz/bert-large-cased-finetuned-conll03-english')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']
    intents = intent_pipeline(user_input)
    entities = ner_pipeline(user_input)

    response = {
        'intents': intents,
        'entities': entities,
        'response': generate_response(intents, entities)
    }

    return jsonify(response)

def generate_response(intents, entities):
    if intents[0]['label'] == 'POSITIVE':
        return "I'm glad to hear that! How can I assist you further?"
    else:
        return "I'm sorry to hear that. How can I assist you?"

if __name__ == '__main__':
    app.run(debug=True)
