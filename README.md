# AI Text Summarization Tool

## Project Overview

The AI Text Summarization Tool is a web-based application that automatically generates concise summaries from lengthy text documents. The application helps users quickly understand the key points of large amounts of text without reading the entire content.

Built with Python and Streamlit, the tool uses Natural Language Processing (NLP) techniques to analyze text, identify important information, and generate meaningful summaries.

---

## Features

* Generate summaries from long text passages
* Simple and interactive web interface
* Fast text processing and summarization
* Displays original and summarized text
* Word count comparison between original text and summary
* User-friendly design using Streamlit

---

## Technologies Used

* Python
* Streamlit
* NLTK (Natural Language Toolkit)
* Natural Language Processing (NLP)
* Git & GitHub

---

## AI/NLP Model Used

This project uses an **Extractive Text Summarization** approach.

### Process:

1. Text preprocessing

   * Tokenization
   * Stopword removal
   * Text cleaning

2. Sentence scoring

   * Important words are identified using word frequency analysis.
   * Each sentence receives a score based on the significance of the words it contains.

3. Summary generation

   * Top-ranked sentences are selected and combined to create the final summary.

### Libraries Used

* NLTK for tokenization and stopword removal
* Heapq for selecting the highest-scoring sentences

This project does not use a large language model (LLM). Instead, it uses traditional NLP techniques for efficient extractive summarization.

---

## Project Structure

```text
ai_text_summarizer/
│
├── app.py
├── summarizer.py
├── requirements.txt
├── README.md
├── .gitignore
└── venv/
```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/durgabhavaniguntanala/my_vscode.git
```

### Navigate to Project Directory

```bash
cd my_vscode
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Download NLTK Resources

```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```

---

## Usage

Run the Streamlit application:

```bash
streamlit run app.py
```

Open the local URL displayed in the terminal (usually):

```text
http://localhost:8501
```

### Steps

1. Enter or paste text into the input box.
2. Click **Generate Summary**.
3. View the generated summary.
4. Compare original and summarized word counts.

---

## Future Enhancements

* Support for PDF and document uploads
* Abstractive summarization using Transformer models
* Multi-language support
* Summary length customization
* Export summaries to PDF

---

## Learning Outcomes

Through this project, I gained practical experience in:

* Natural Language Processing (NLP)
* Text preprocessing techniques
* Python application development
* Streamlit web application development
* Git and GitHub version control

---

## Author

**Durga Bhavani**

GitHub: https://github.com/durgabhavaniguntanala
# my_vscode
