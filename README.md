NLP: Chatbot for Customer Support
Description
Developed an NLP-based chatbot to automate customer support queries, understanding natural language input, identifying user intent, and providing relevant responses or escalating to human agents.

Technologies
Python

TensorFlow

Hugging Face

Flask

Key Contributions
Intent Classification: Implemented using pre-trained transformer models.

Named Entity Recognition (NER): Leveraged Hugging Face models for accurate entity detection.

Web Integration: Integrated the chatbot into a web application using Flask.

Performance: Achieved 90% accuracy in intent detection, reducing customer support response time by 40%.

Installation and Setup
Clone the repository:

bash

Copy
git clone https://github.com/sid7shetty/chatbot-customer-support.git
cd chatbot-customer-support
Create a virtual environment:

bash

Copy
python -m venv venv
source venv/bin/activate  # For Windows use `venv\Scripts\activate`
Install dependencies:

bash

Copy
pip install flask tensorflow transformers tf-keras
Run the Flask app:

bash

Copy
python app.py
Access the application: Open your browser and go to http://127.0.0.1:5000.

Usage
Enter your message in the input box.

Click 'Send' to receive a response from the chatbot based on intent classification and entity recognition.

Contributing
Feel free to fork the repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.
