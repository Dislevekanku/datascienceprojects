import streamlit as st
import requests
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from PyPDF2 import PdfReader
import docx
import io
from io import StringIO

# Inline CSS for better styling
st.markdown(
    """
    <style>
        .title {
            font-size: 32px;
            color: #4CAF50;
            font-weight: bold;
            text-align: center;
        }
        .subtitle {
            font-size: 20px;
            color: #2196F3;
            text-align: center;
        }
        .button {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px 20px;
            text-align: center;
            font-size: 16px;
            cursor: pointer;
            border-radius: 5px;
        }
        .button:hover {
            background-color: #45a049;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Load BERT model for semantic similarity
@st.cache_resource
def load_bert_model():
    return SentenceTransformer('all-MiniLM-L6-v2')

bert_model = load_bert_model()

# Function to extract text from PDF
def extract_text_from_pdf(uploaded_file):
    try:
        pdf_reader = PdfReader(uploaded_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        if not text.strip():
            st.error("No text could be extracted from the PDF. Please upload a valid resume.")
        return text.strip()
    except Exception as e:
        st.error(f"Error reading PDF: {e}")
        return ""

# Function to extract text from DOCX
def extract_text_from_docx(uploaded_file):
    try:
        doc = docx.Document(uploaded_file)
        text = "\n".join([para.text for para in doc.paragraphs])
        return text.strip()
    except Exception as e:
        st.error(f"Error reading DOCX file: {e}")
        return ""

# Function to extract text from TXT
def extract_text_from_txt(uploaded_file):
    try:
        text = uploaded_file.getvalue().decode("utf-8")
        return text.strip()
    except Exception as e:
        st.error(f"Error reading TXT file: {e}")
        return ""

# Function to extract text from a job description URL
def extract_text_from_url(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all(['p', 'div'])
        text = " ".join([para.get_text(strip=True) for para in paragraphs if para.get_text(strip=True)])
        if not text.strip():
            st.error("Failed to extract meaningful text. The page might be empty or protected.")
        return text.strip()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching job description: {e}")
        return ""
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
        return ""

# Function to generate a word cloud
def generate_wordcloud(text, title):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis('off')
    plt.title(title, fontsize=16)
    plt.show()
    st.pyplot(plt)

# Function to calculate semantic similarity using BERT
def calculate_semantic_similarity(resume_text, job_description_text):
    try:
        embeddings = bert_model.encode([resume_text, job_description_text])
        similarity = cosine_similarity([embeddings[0]], [embeddings[1]])
        return round(similarity[0][0] * 100, 2)
    except Exception as e:
        st.error(f"Error calculating similarity with BERT: {e}")
        return 0

# Streamlit App
st.markdown('<h1 class="title">Resume vs Job Description Matching App</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Upload your resume and provide the job description URL for matching</p>', unsafe_allow_html=True)

uploaded_file = st.file_uploader("Upload your resume (PDF, TXT, or DOCX)", type=["pdf", "txt", "docx"])
resume_text = ""

# Process resume file
if uploaded_file:
    file_type = uploaded_file.type
    if file_type == "application/pdf":
        resume_text = extract_text_from_pdf(uploaded_file)
    elif file_type == "text/plain":
        resume_text = extract_text_from_txt(uploaded_file)
    elif file_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        resume_text = extract_text_from_docx(uploaded_file)

    if resume_text:
        st.text_area("Extracted Resume Text", resume_text, height=200)

# Enter job description URL
job_desc_url = st.text_input("Enter the job description URL:")

# Button for matching process
if st.button("Calculate Match", help="Click to calculate the semantic similarity"):
    if resume_text and job_desc_url:
        job_description_text = extract_text_from_url(job_desc_url)
        if job_description_text:
            st.text_area("Extracted Job Description Text", job_description_text, height=200)

            # Generate Word Clouds
            st.subheader("Word Clouds")
            st.write("Visualize the key terms in the resume and job description.")
            generate_wordcloud(resume_text, "Resume Word Cloud")
            generate_wordcloud(job_description_text, "Job Description Word Cloud")

            # Calculate Similarity and Show Pie Chart
            similarity_score = calculate_semantic_similarity(resume_text, job_description_text)
            st.subheader("Semantic Similarity Score")
            st.success(f"Semantic Similarity Score: {similarity_score}%")

            # Pie Chart
            labels = ["Match", "Mismatch"]
            sizes = [similarity_score, 100 - similarity_score]
            colors = ["#4CAF50", "#FF5733"]
            plt.figure(figsize=(6, 6))
            plt.pie(sizes, labels=labels, colors=colors, autopct="%1.1f%%", startangle=90, textprops={"fontsize": 14})
            plt.title("Resume Match Percentage", fontsize=16)
            st.pyplot(plt)
    else:
        st.error("Please upload a valid resume and enter a job description URL.")
