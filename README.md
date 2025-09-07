# Data science portfolio
Repository containing portfolio of data science projects completed by me for academic, self learning, and hobby purposes. Presented in the form of Jupyter notebooks,

## Setup

Create a virtual environment and install the project dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

Alternatively, you can automate the above steps with:

```bash
make install
```

After setting up the environment, install the pre-commit hooks:

```bash
pre-commit install
```

## Contributing

### Branch Naming
- Use descriptive branch names prefixed with `feature/`, `fix/`, or `docs/`.
- Separate words with hyphens, e.g., `feature/add-model-evaluation`.

### Commit Messages
- Use the imperative mood in the subject line.
- Keep the subject line under 50 characters.

### Pull Requests
- Open PRs against the `main` branch.
- Ensure all checks pass and request at least one review.
- Address review feedback promptly.

## Docker

Build the image:
```bash
docker build -t dsp .
```

Run the container:
```bash
docker run -p 8888:8888 dsp
```

This starts a Jupyter Notebook server at http://localhost:8888.

## Contents
### Machine Learning
  [Predicting Boston Housing Prices:](https://github.com/Dislevekanku/datascienceprojects/blob/703d428e1739dca4832ede708f5880a8aa27b6ff/boston_housing/Boston%20Housing%20price%20prediction.ipynb) Used Linear Regression model to predict the value of houses in the Boston area, Used various statistical tools for analysis. Performed model evaluation by finding the r2 score.

  [Finding Donors for Charity with ML:](https://github.com/Dislevekanku/datascienceprojects/blob/9a5832e9c4cadfbca3f4f50f81c82fc9f29f4d7d/CharityML/Charity%20ML.ipynb) I used three different supervised learning algorithms to build a model that predicts whether an individual makes more than $50,000 to identify likely donors for a fiction non-profit organisation

  [Arrythmia Detection:](https://github.com/Dislevekanku/Arrythmia_detection) This project focuses on detecting arrhythmias using the MIT-BIH (Massachusetts Institute of Technology - Beth Israel Hospital) ECG (Electrocardiogram) dataset. Arrhythmias are irregular heart rhythms that can have serious health implications, and early detection is essential.


  [Building a Simple Language Model with Flask and NLTK](https://github.com/Dislevekanku/datascienceprojects/tree/master/LLM_FLASK) This repository details the implementation, testing, and evaluation of a simple n-gram language model using the NLTK library. The model is designed to predict the next word in a sentence based on the preceding words, using n-gram statistics. We explored both bigram (n=2) and trigram (n=3) models to compare their performance.
