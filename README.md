# Text Summarization Application

This is a simple text summarization application that uses the BART model from Facebook to generate concise summaries of input text. The application provides a user-friendly interface using Streamlit and allows users to customize the length of the generated summaries.

## Features

- Interactive web interface
- Customizable summary length
- Uses state-of-the-art BART model for summarization
- Real-time summary generation
- Cached model loading for better performance

## Installation

1. Clone this repository
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the application:
```bash
streamlit run text_summarizer.py
```

2. Open your web browser and navigate to the URL shown in the terminal (typically http://localhost:8501)
3. Enter your text in the text area
4. Adjust the maximum and minimum summary length using the sliders
5. Click "Generate Summary" to get your summary

## Requirements

- Python 3.7+
- See requirements.txt for package dependencies

## Notes

- The first run will download the BART model, which might take a few minutes depending on your internet connection
- The model works best with texts between 100 and 1000 words
- Longer texts will be truncated to 1024 tokens

Data and Statistical modelling - refresher (work in progress)
  1. Descriptive statistics
  2. Measures of central tendency
     * mean
     * median
     * mode
  3. Measures of spread / Dispersion
     * range
     * inter quartile range
     * variance
     * standard deviation
  4. Shape and outliers analysis
  5. Sampling distributions
  6. Central limit theorem
  7. Binomial distribution & Normal distribution
  8. Hypothesis testing
  9. A/B Testing
  10. Variance, Covariance, Correlation
  11. Linear regression
  12. Feed forward neural network (FFNN)
  13. Neural networks implementation using PyTorch
  14. Transformers
  15. LLM Simple use case
  16. Expanded use case for LLM
  17. Fine tuning an LLM
  18. Supervised Fine Tuning (SFT)
  19. Reinforcement Learning with Human Feedback (RLHF)
  20. Distillation
  21. Distrinited training
  22. Multi model fine tuning
  23. Q learning