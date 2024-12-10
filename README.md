# Spam_Email_Detector
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Spam Detector README</title>
</head>
<body>
    <h1>Spam Detector</h1>
    <p>This project is a simple spam detection model built using Python and machine learning libraries.</p>

    <h2>Installation</h2>
    <p>To run this program, you need to have Python installed on your machine. You can download it from <a href="https://www.python.org/downloads/">python.org</a>.</p>
    <p>After installing Python, you need to install the required libraries. You can do this using pip:</p>
    <pre><code>pip install pandas numpy scikit-learn</code></pre>
    <p>Additionally, you will need to install the pickle module, which is included with Python's standard library.</p>

    <h2>Code Explanation</h2>
    <h3>1. Importing Libraries</h3>
    <pre><code>import pandas as pd</code></pre>
    <p>Imports the pandas library for data manipulation and analysis.</p>
    
    <pre><code>import numpy as np</code></pre>
    <p>Imports the numpy library for numerical operations.</p>

    <h3>2. Loading Data</h3>
    <pre><code>data = pd.read_csv("spam (1).csv", encoding = "latin-1")</code></pre>
    <p>Loads the dataset from a CSV file into a pandas DataFrame.</p>

    <h3>3. Data Preprocessing</h3>
    <pre><code>data['Category'] = data['Category'].map({'ham': 0, 'spam': 1})</code></pre>
    <p>Maps the 'ham' and 'spam' categories to numerical values (0 and 1).</p>

    <h3>4. Feature Extraction</h3>
    <pre><code>from sklearn.feature_extraction.text import CountVectorizer</code></pre>
    <p>Imports CountVectorizer for converting text data into a matrix of token counts.</p>

    <h3>5. Splitting Data</h3>
    <pre><code>from sklearn.model_selection import train_test_split</code></pre>
    <p>Imports train_test_split to split the dataset into training and testing sets.</p>

    <h3>6. Model Training</h3>
    <pre><code>from sklearn.naive_bayes import MultinomialNB</code></pre>
    <p>Imports the Multinomial Naive Bayes model for classification.</p>

    <h3>7. Model Evaluation</h3>
    <pre><code>model.score(x_test, y_test)</code></pre>
    <p>Evaluates the model's performance on the test set.</p>

    <h3>8. Saving the Model</h3>
    <pre><code>import pickle</code></pre>
    <p>Imports the pickle module for saving the trained model and vectorizer.</p>

    <pre><code>pickle.dump(model, open('spam123.pkl', 'wb'))</code></pre>
    <p>Saves the trained model to a file named 'spam123.pkl'.</p>

    <pre><code>pickle.dump(cv, open('vec.pkl', 'wb'))</code></pre>
    <p>Saves the CountVectorizer object to a file named 'vec.pkl'.</p>

    <h2>Usage</h2>
    <p>To use the model for predictions, load the saved model and vectorizer, then transform your input data and call the predict method.</p>

    <h2>Conclusion</h2>
    <p>This spam detector can be used to classify messages as spam or ham based on the trained model.</p>
</body>
</html>
