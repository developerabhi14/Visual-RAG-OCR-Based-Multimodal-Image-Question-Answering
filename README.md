# Visual-RAG: OCR-Based Multimodal Image Question Answering

This project is a lightweight Visual Retrieval-Augmented Generation (RAG) application that allows users to:
- Upload an image (containing text),
- Extract the text via OCR (EasyOCR),
- Embed and store the text (HuggingFace + ChromaDB),
- Ask natural language questions about the image, and
- Receive contextual answers using the **Gemini 1.5 Flash** model.

## 🚀 Features

- 📷 Image-based OCR using EasyOCR
- 📚 Text chunking and embedding using `sentence-transformers`
- 🧠 Contextual retrieval with ChromaDB
- 🤖 Answer generation using Google Gemini API
- 🎯 Accurate answers based on only the content in the image
- 🧵 Streamlit frontend

## 📁 Project Structure

MultimodalRAG/
│
├── app.py # Streamlit frontend
├── .env # API keys and env vars
├── requirements.txt # All dependencies
│
├── core/
│ ├── ocr.py # EasyOCR extraction
│ ├── embed_store.py # Chroma DB & embedding
│ ├── retriever.py # Vector similarity retriever
│ └── qa_generator.py # Gemini API-based generator
│
├── chroma_db_multimodal/ # Persistent vector DB
├── outputs/ # For generated audio (optional)
├── assets/ # Screenshots, logos, GIFs


---

## 🔧 Installation

### 1. Clone the repo

```bash
git clone ## 📁 Project Structure

MultimodalRAG/
│
├── app.py # Streamlit frontend
├── .env # API keys and env vars
├── requirements.txt # All dependencies
│
├── core/
│ ├── ocr.py # EasyOCR extraction
│ ├── embed_store.py # Chroma DB & embedding
│ ├── retriever.py # Vector similarity retriever
│ └── qa_generator.py # Gemini API-based generator
│
├── chroma_db_multimodal/ # Persistent vector DB
├── outputs/ # For generated audio (optional)
├── assets/ # Screenshots, logos, GIFs


---

## 🔧 Installation

### 1. Clone the repo

```bash
git clone https://github.com/developerabhi14/Visual-RAG-OCR-Based-Multimodal-Image-Question-Answering.git
cd Visual-RAG

### 2. Create a virtual environment

python3 -m venv venv
source venv/bin/activate

### 3. Install requirements

pip install -r requirements.txt

### 4. Add your API key

Create a .env file:

GOOGLE_API_KEY=your_gemini_api_key

### 5. Run the App

streamlit run app.py

🧠 Technologies Used

    EasyOCR

    HuggingFace Sentence Transformers

    ChromaDB

    Google Gemini Flash

    LangChain

    Streamlit
