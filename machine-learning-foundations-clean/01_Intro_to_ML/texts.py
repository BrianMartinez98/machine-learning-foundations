from sklearn.feature_extraction.text import CountVectorizer

positive_texts = [
    "I love this city",
    "This movie is amazing",
    "I am very happy",
    "The food was excellent",
    "This is a great experience",
    "I enjoyed the concert",
    "The weather is beautiful",
    "This product works well",
    "I feel fantastic",
    "The service was wonderful"
]

negative_texts = [
    "I hate this place",
    "This movie is terrible",
    "I am very sad",
    "The food was awful",
    "This is a bad experience",
    "I disliked the concert",
    "The weather is horrible",
    "This product does not work",
    "I feel miserable",
    "The service was poor"
]

training_texts = positive_texts + negative_texts

text_counter = CountVectorizer()
text_training = text_counter.fit_transform(training_texts)
