import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, confusion_matrix

# 1. Sample short reviews dataset
reviews = [
    "I love this product", "This is amazing", "Absolutely fantastic!", 
    "I hate this", "Worst experience ever", "Really bad product", 
    "Excellent quality", "Not worth the money", "Totally disappointed", 
    "Highly recommend", "Terrible service", "I am very happy", 
    "Awful experience", "Very satisfied", "Waste of time"
]

labels = [1,1,1, 0,0,0, 1,0,0, 1,0,1, 0,1,0]  # 1=Positive, 0=Negative

# 2. Convert text to Bag of Words
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(reviews)

# 3. Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.3, random_state=42)

# 4. Train Naive Bayes model
nb = MultinomialNB()
nb.fit(X_train, y_train)

# 5. Predictions and probabilities
y_pred = nb.predict(X_test)
y_proba = nb.predict_proba(X_test)

# 6. Evaluation
print("Classification Report:\n", classification_report(y_test, y_pred, target_names=["Negative","Positive"]))

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=["Neg","Pos"], yticklabels=["Neg","Pos"])
plt.title("Confusion Matrix")
plt.show()

# 7. Visualize probability outputs for test reviews
for review, prob in zip(np.array(reviews)[[i for i in range(len(labels)) if i not in X_train.indices]], y_proba):
    print(f"Review: '{review}'")
    print(f"Predicted Probabilities -> Negative: {prob[0]:.2f}, Positive: {prob[1]:.2f}\n")

# 8. Analyse Misclassifications
for r, true, pred in zip(np.array(reviews)[np.array(y_test)==0], y_test, y_pred):
    if true != pred:
        print(f"Misclassified Review: '{r}' | True: {true}, Predicted: {pred}")
