from texts import text_counter, text_training
from sklearn.naive_bayes import MultinomialNB

intercepted_text = "I love New York."

text_counts = text_counter.transform([intercepted_text])

text_classifier = MultinomialNB()

text_labels = [1] * 10 + [0] * 10

text_classifier.fit(text_training, text_labels)

final_pos = text_classifier.predict_proba(text_counts)[0][1]

final_neg = text_classifier.predict_proba(text_counts)[0][0]

if final_pos > final_neg:
    print("The text is positive.")
else:
    print("The text is negative.")

print("Positive probability:", final_pos)
print("Negative probability:", final_neg)
