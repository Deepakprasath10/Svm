from flask import Flask, render_template, request
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
import joblib
import os

app = Flask(__name__)

# Load and preprocess data
df = pd.read_csv("spam.csv")
df = df[['label', 'text']]
df['label'] = df['label'].map({'ham': 0, 'spam': 1})

X = df['text']
y = df['label']

# Vectorization
vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X)

# Train SVM model
model = LinearSVC()
model.fit(X_vec, y)

# Save model/vectorizer
joblib.dump(model, 'svm_model.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    email = request.form.get('feedback', '')
    if not email.strip():
        return "Empty input", 400

    vectorizer = joblib.load('vectorizer.pkl')
    model = joblib.load('svm_model.pkl')

    email_vec = vectorizer.transform([email])
    prediction = model.predict(email_vec)[0]

    result = "Spam" if prediction == 1 else "Not Spam"
    return render_template('result.html', prediction=result, email=email)

if __name__ == '__main__':
    app.run(debug=True)
