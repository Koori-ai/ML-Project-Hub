import streamlit as st

st.set_page_config(page_title="Bedrock RAG Demo", layout="wide")

st.title("📄 Bedrock RAG Q&A Demo")
st.markdown("Ask questions about a document using LLMs.")

query = st.text_input("🔍 Ask a question:")

if query:
    st.write(f"Searching for: *{query}*")
    # Placeholder - later we'll connect to Bedrock or LangChain
    st.success("LLM response placeholder goes here")
