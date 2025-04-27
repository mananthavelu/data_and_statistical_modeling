import streamlit as st
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqGeneration
import torch

def load_model():
    """Load the summarization model and tokenizer."""
    model_name = "facebook/bart-large-cnn"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqGeneration.from_pretrained(model_name)
    return model, tokenizer

def generate_summary(text, model, tokenizer, max_length=130, min_length=30):
    """Generate a summary of the input text."""
    inputs = tokenizer(text, return_tensors="pt", max_length=1024, truncation=True)
    summary_ids = model.generate(
        inputs["input_ids"],
        max_length=max_length,
        min_length=min_length,
        length_penalty=2.0,
        num_beams=4,
        early_stopping=True
    )
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

def main():
    st.title("Text Summarization App")
    st.write("Enter your text below to generate a summary.")

    # Load model
    @st.cache_resource
    def load_cached_model():
        return load_model()

    model, tokenizer = load_cached_model()

    # Text input
    text_input = st.text_area("Enter your text here:", height=200)

    # Summary parameters
    col1, col2 = st.columns(2)
    with col1:
        max_length = st.slider("Maximum summary length", 50, 200, 130)
    with col2:
        min_length = st.slider("Minimum summary length", 10, 100, 30)

    if st.button("Generate Summary"):
        if text_input:
            with st.spinner("Generating summary..."):
                summary = generate_summary(text_input, model, tokenizer, max_length, min_length)
                st.subheader("Generated Summary:")
                st.write(summary)
        else:
            st.warning("Please enter some text to summarize.")

if __name__ == "__main__":
    main() 