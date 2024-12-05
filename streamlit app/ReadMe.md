# Resume vs Job Description Matching App

## Overview

The "Resume vs Job Description Matching App" is a web application built with Streamlit that helps job seekers analyze how well their resumes match a job description. By uploading a resume (PDF, TXT, or DOCX formats) and providing a job description URL, the app extracts the relevant text from both, calculates the semantic similarity between them, and generates visualizations to help users understand the match percentage.

This app is powered by advanced NLP techniques, utilizing BERT embeddings for semantic similarity calculations, and leverages libraries like BeautifulSoup, PyPDF2, and WordCloud for text extraction and visualization.

## Features

- **Upload Resumes**: Users can upload resumes in PDF, DOCX, or TXT format.
- **Extract Job Description**: Input a job description URL to extract the relevant text.
- **Semantic Similarity**: Calculate the semantic similarity score between the uploaded resume and job description using BERT embeddings.
- **Word Cloud Visualization**: Generate and visualize word clouds for both the resume and the job description to highlight the key terms.
- **Match Percentage**: Display the match percentage in a pie chart to show the similarity between the resume and job description.

## Requirements

To run this app, you'll need the following Python libraries:

- `streamlit`
- `requests`
- `beautifulsoup4`
- `wordcloud`
- `matplotlib`
- `sentence-transformers`
- `scikit-learn`
- `PyPDF2`
- `python-docx`

You can install all required dependencies using the following command:

```bash
pip install streamlit requests beautifulsoup4 wordcloud matplotlib sentence-transformers scikit-learn PyPDF2 python-docx
