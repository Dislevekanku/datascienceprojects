from flask import Flask, request, jsonify, render_template
import nltk
from nltk.corpus import gutenberg
from nltk.tokenize import word_tokenize
import re
from collections import Counter
import math

app = Flask(__name__)

# Download required datasets
nltk.download('gutenberg')
nltk.download('punkt')

# Load the Gutenberg corpus
corpus = gutenberg.raw()

# Preprocessing the text
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    return text

# Preprocess the corpus
cleaned_corpus = preprocess_text(corpus)
# Tokenize the text
tokens = word_tokenize(cleaned_corpus)

# Function to generate n-grams
def generate_ngrams(tokens, n):
    ngrams = zip(*[tokens[i:] for i in range(n)])
    return [" ".join(ngram) for ngram in ngrams]

# Generate n-grams and calculate frequencies
def get_ngram_frequencies(tokens, n):
    ngrams = generate_ngrams(tokens, n)
    ngram_freq = Counter(ngrams)
    n_minus1grams = generate_ngrams(tokens, n-1)
    n_minus1gram_freq = Counter(n_minus1grams)
    return ngram_freq, n_minus1gram_freq

# Calculate probability with Laplace smoothing
def calculate_probability_laplace(word, context, ngram_freq, n_minus1gram_freq, vocab_size, alpha=1):
    ngram = context + " " + word
    return (ngram_freq[ngram] + alpha) / (n_minus1gram_freq[context] + alpha * vocab_size)

# Predict the next word with Laplace smoothing
def predict_next_word_laplace(context, ngram_freq, n_minus1gram_freq, vocab, alpha=1):
    candidates = list(vocab)
    probabilities = [calculate_probability_laplace(candidate, context, ngram_freq, n_minus1gram_freq, len(vocab), alpha) for candidate in candidates]
    return candidates[probabilities.index(max(probabilities))]

# Generate a sentence of a specified length
def generate_sentence(prefix, length, ngram_freq, n_minus1gram_freq, vocab, n):
    sentence = prefix.split()
    for _ in range(length - len(sentence)):
        context = " ".join(sentence[-(n-1):])
        next_word = predict_next_word_laplace(context, ngram_freq, n_minus1gram_freq, vocab)
        if not next_word:
            break
        sentence.append(next_word)
    return " ".join(sentence)

# Calculate perplexity
def calculate_perplexity(test_tokens, n, ngram_freq, n_minus1gram_freq, vocab, alpha=1):
    ngrams = generate_ngrams(test_tokens, n)
    n_minus1grams = generate_ngrams(test_tokens, n-1)
    
    log_prob = 0
    for i, ngram in enumerate(ngrams):
        context = n_minus1grams[i]
        word = ngram.split()[-1]
        prob = calculate_probability_laplace(word, context, ngram_freq, n_minus1gram_freq, len(vocab), alpha)
        log_prob += math.log(prob)
    
    return math.exp(-log_prob / len(ngrams))

# Split the data into train and test sets
split_index = int(0.8 * len(tokens))
train_tokens = tokens[:split_index]
test_tokens = tokens[split_index:]

# Vocabulary
vocab = set(tokens)

# Train bigram model (n=2)
bigram_freq, bigram_n_minus1gram_freq = get_ngram_frequencies(train_tokens, 2)

# Train trigram model (n=3)
trigram_freq, trigram_n_minus1gram_freq = get_ngram_frequencies(train_tokens, 3)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    prefix = data.get('prefix')
    length = int(data.get('length'))
    n = int(data.get('n'))
    
    if not prefix or length <= 0:
        return jsonify({'error': 'Invalid input'})

    if n == 2:
        sentence = generate_sentence(prefix, length, bigram_freq, bigram_n_minus1gram_freq, vocab, 2)
        perplexity = calculate_perplexity(test_tokens, 2, bigram_freq, bigram_n_minus1gram_freq, vocab)
    else:
        sentence = generate_sentence(prefix, length, trigram_freq, trigram_n_minus1gram_freq, vocab, 3)
        perplexity = calculate_perplexity(test_tokens, 3, trigram_freq, trigram_n_minus1gram_freq, vocab)
    
    return jsonify({'sentence': sentence, 'perplexity': perplexity})

if __name__ == '__main__':
    app.run(debug=True)
