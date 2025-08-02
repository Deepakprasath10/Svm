## Spam Mail Classifier Web App

A Flask-based web application that uses a trained Machine Learning model to identify whether a given email/message is **Spam** or **Not Spam**.

---

## Features

-  Classifies input text as **Spam** or **Not Spam**
-  Uses a trained **Multinomial Naive Bayes** model
-  Preprocessing includes cleaning, stemming, and vectorization
-  Interactive web interface built with HTML, CSS (modern design)
-  Responsive UI with hover effects and mobile support

---

##  How It Works

1. **Data Collection**: Loads a CSV dataset of labeled spam and ham messages.
2. **Preprocessing**: Removes punctuation, stopwords, and applies stemming.
3. **Vectorization**: Converts text into numeric features using CountVectorizer.
4. **Model Training**: Trains a Multinomial Naive Bayes classifier.
5. **Web App**: User enters a message → Model predicts if it's spam → Displays result.

---

##  Project Structure
```
spam-mail-classifier/
├── static/
│ └── style.css # Modern UI styling
├── templates/
│ └── index.html # HTML frontend
├── spam.csv # Sample dataset
├── spam_classifier_model.pkl # Trained model
├── vectorizer.pkl # Trained CountVectorizer
├── app.py # Flask backend
└── README.md # Project documentation
```
---

##  Setup Instructions

1. **Clone the repository**

```
git clone https://github.com/yourusername/spam-mail-classifier.git
cd spam-mail-classifier
```
Install dependencies
```
pip install -r requirements.txt
```
Run the application
```
python app.py
```
Open in browser

Visit: http://localhost:5000

# Sample Input

Congratulations! You've won a $1000 Walmart gift card. Click here to claim now.
Prediction: 🚫 Spam


## Screenshots
![alt text](<Screenshot 2025-08-02 140353.png>)
![alt text](<Screenshot 2025-08-02 140422.png>)
![alt text](<Screenshot 2025-08-02 140433.png>)

## Future Improvements
Train on a larger dataset

Add user authentication

Support file upload (for .eml or .txt emails)

Create API endpoint for classification