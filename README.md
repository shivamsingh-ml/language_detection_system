# Language Detection System

This project implements a document language identification system in **Python**, built from scratch using statistical n-gram modeling techniques. It supports five languages: English, Spanish, French, German, and Italian.

The goal was to design and implement a method to identify the language of a given document without relying on prebuilt models or external APIs. The approach is based on classical natural language processing (NLP) methods.

To evaluate robustness, the custom model is also compared against the widely used `langdetect` library.

---

## ✨ Features
- Character-level n-gram modeling
- Custom training and prediction logic implemented from scratch
- Evaluation with confusion matrix and per-language accuracies
- Comparative analysis with the `langdetect` library
- Jupyter notebooks for testing, benchmarking, and analysis

---

## 🚀 Getting Started

### Prerequisites
Ensure you have Python 3.7+ installed. Install the required libraries:

```bash
pip install pandas numpy matplotlib scikit-learn langdetect
```

---

## 📄 How to Use

### Language Model Training & Prediction
The main logic is in `language_detector.py`:
- Preprocess text data from the `/languages/` folder
- Train n-gram frequency models for each language
- Compare document input against these models using similarity measures

Run notebooks in `/notebooks/` to:
- Test custom model predictions (`language_detector_testing.ipynb`)
- Evaluate performance and compare with `langdetect` (`evaluation.ipynb`)

---

## 📚 Project Structure
```
language_detector_task/
|— language_detector.py        # Core logic for language detection
|— languages/                  # Sample text files per language
|    |— en.txt
|    |— es.txt
|    ...
|— figures/                   # Model evaluation plots
|    |— cm.png                  # Confusion matrix
|    |— per_language_accuracies.png
|    ...
|— notebooks/                 # Jupyter notebooks for analysis
|    |— evaluation.ipynb         # Includes langdetect comparison
|    |— language_detector_testing.ipynb
|— Report.pdf                 # Project documentation and methodology
```

---

## 🔹 Methodology
This project implements a character n-gram language model approach, inspired by:
- Cavnar, W. B., & Trenkle, J. M. (1994). *N-Gram-Based Text Categorization*.

Languages are modeled using frequency profiles of n-grams, and predictions are made by comparing unknown text profiles against trained language models.

The model’s accuracy and robustness were benchmarked against the `langdetect` library to assess performance on realistic text inputs.
