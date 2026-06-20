# Phishing URL Detection Model

## Overview
This project focuses on building a machine learning model to detect phishing URLs and protect users from malicious sites. Using Natural Language Processing (NLP) techniques, the model analyzes the lexical features of URLs to classify them as either legitimate or phishing.

## Tech Stack & Libraries
- **Language:** Python
- **Backend framework:** `Flask`
- **Frontend UI:** `HTML5`, `Tailwind CSS` (Dark Mode UI)
- **Data Manipulation:** `pandas`, `numpy`
- **Natural Language Processing:** `nltk` (RegexpTokenizer, SnowballStemmer)
- **Machine Learning:** `scikit-learn` (Logistic Regression, Multinomial Naive Bayes)
- **Data Visualization:** `matplotlib`, `seaborn`, `wordcloud`

## Dataset
The model gets trained on `phishing_site_urls.csv`, which contains a collection of URLs mapped to their respective labels (e.g., safe/malicious).

## Methodology & Workflow
1. **Data Preprocessing:** 
   - Extracting words from URLs using tokenization (`RegexpTokenizer`).
   - Normalizing the extracted words using stemming (`SnowballStemmer`) to reduce words to their root forms.
2. **Exploratory Data Analysis (EDA):**
   - Generating **Word Clouds** to visually identify the most frequent terms used in phishing versus legitimate URLs.
3. **Feature Extraction:**
   - Transforming text data into numerical format using **Bag of Words / CountVectorizer**, extracting the core features needed for the models to learn.
4. **Model Training & Evaluation:**
   - Splitting data into Training and Testing sets (80/20 split).
   - Training multiple classification algorithms, particularly **Logistic Regression** and **Multinomial Naive Bayes**.
   - Evaluating results using `classification_report` and `confusion_matrix` to look at precision, recall, and overall accuracy.
5. **Model Serialization:**
   - Saving the trained model using `pickle` for quick deployment and future inferences without retraining.
6. **Web Application Deployment:**
   - Built a sleek, intuitive, dark-themed UI using **Tailwind CSS**.
   - Integrated the serialized ML model with a **Flask** backend to instantly evaluate inputted URLs and dynamically return safety alerts.

## How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Pranjal-Garg-21/phishing_websites_detector.git
   cd phishing_emails
   ```

2. **Activate the environment:**
   ```bash
   source env/bin/activate  # On Linux/Mac
   # For Windows: .\env\Scripts\activate
   ```

3. **Run the Web Application:**
   ```bash
   python app.py
   ```
   *Open `http://127.0.0.1:5000/` in your browser to interact with the model via the modern UI.*

4. **(Optional) Explore the ML Model Notebook:**
   ```bash
   jupyter notebook Phishing_emails_detection_model.ipynb
   ```

##  Key Takeaways 
- **End-to-End Pipeline & Deployment:** Demonstrated a full lifecycle—from raw CSV data ingestion and NLP processing to model serialization and live deployment via a Flask Web App.
- **Modern UI/UX Implementation:** Built an intuitive, dynamic interface with Tailwind CSS that elegantly communicates predictions to end-users.
- **NLP Proficiency:** Effectively applied tokenization, stemming, and vectorization to unstructured string/URL data.
- **Data Science Foundations:** Handled train-test splitting and robust evaluation of model performance using standard validation metrics (Confusion Matrix, Precision, Recall).
