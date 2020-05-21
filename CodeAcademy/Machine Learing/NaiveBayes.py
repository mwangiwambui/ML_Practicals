# NYBD (Neo York Bot Department) wants to analyze how Neo Yorkers are talking to one another so that they can determine who is being negative.
#
# They have built a Naive Bayes classifier that predicts whether an intercepted text is good or bad, based on the frequency that a word is used in a good training example or a bad one.
#
# Run the code to see if the model classifies the sentence "This hot dog was awful!" as a negative sentiment.

from texts import text_counter, text_training
# TODO : CHECK ON THIS IMPORT FOR TEXTS
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

intercepted_text = "This hot dog was awful!"

text_counts = text_counter.transform([intercepted_text])

text_classifier = MultinomialNB()

text_labels = [0] * 1000 + [1] * 1000

text_classifier.fit(text_training, text_labels)

final_pos = text_classifier.predict_proba(text_counts)[0][1]

final_neg = text_classifier.predict_proba(text_counts)[0][0]

if final_pos > final_neg:
  print("The text is positive.")
else:
  print("The text is negative.")
