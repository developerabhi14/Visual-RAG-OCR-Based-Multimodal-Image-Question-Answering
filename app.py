import streamlit as st
from core.ocr import extract_text_from_image
from core.embed_store import embed_and_store
from core.retriever import get_relevant_context_from_query
from core.qa_generator import generate_answer
from core.voice_output import speak_text

st.set_page_config(page_title="Visual RAG Assistant", layout="centered")
st.title("🖼️ Visual Question Answering Agent")

# Initialize session state
if "question" not in st.session_state:
    st.session_state.question = ""
if "response" not in st.session_state:
    st.session_state.response = ""

uploaded_image = st.file_uploader("📤 Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_image:
    st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)

    with st.spinner("🔍 Extracting text from image..."):
        extracted_text = extract_text_from_image(uploaded_image)
        st.success("✅ Text Extracted")
        st.text_area("📝 Extracted Text", extracted_text, height=200)

        # Store embeddings to persistent DB
        embed_and_store(extracted_text)

        # Take user's question
        user_query = st.text_input("💬 Ask a question about the image")

        if user_query:
            with st.spinner("🔎 Retrieving relevant context..."):
                context = get_relevant_context_from_query(user_query)

            with st.spinner("💡 Generating answer..."):
                answer = generate_answer(user_query, context)

            st.markdown("### 🤖 Answer:")
            st.write(answer)
            speak_text(answer)

