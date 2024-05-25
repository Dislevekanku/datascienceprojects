# Project Description:
This project implements a simple language model using Flask and NLTK (Natural Language Toolkit). The language model predicts the next word in a sentence based on n-gram statistics and includes functionalities for data preprocessing, model implementation, testing, and evaluation.

# Key Features:

<li>Data collection from the Gutenberg corpus using NLTK.</li>
<li>Text preprocessing including lowercase conversion and special character removal.</li>
<li>Tokenization of text into words.</li>
<li>Generation of n-grams and calculation of their frequencies.</li>
<li>Implementation of Laplace smoothing to handle zero probabilities.</li>
<li>Prediction of the next word given a sequence of words.</li>
<li>Generation of sentences based on specified prefix and length.</li>
<li>Testing and evaluation of the model's performance using perplexity metrics.</li>
<li>Development of a user-friendly web interface with Flask to interact with the language model.</li>

# Usage:

Clone the repository.
Install the required dependencies listed in the requirements.txt file.
Run the Flask server using python app.py.
Access the web interface at http://localhost:5000 in your browser.
Enter a prefix, specify the desired length of the generated sentence, and choose the n-gram model to generate text and view perplexity metrics.