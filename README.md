# Spam_filter
This is an implementation of a Naive Bayesian Classifier written in Python. The utility uses statistical methods to classify documents, based on the words that appear within them. A common application for this type of software is in email spam filters.

The utility must first be 'trained' using large numbers of pre-classified documents, during the training phase a database is populated with information about how often certain words appear in each type of document. Once training is complete, unclassified documents can be submitted to the classifier which will return a value between 0 and 1, indicating the probablity that the document belongs to one class of document rather than another.

## Bayes Theorem:
![image](https://user-images.githubusercontent.com/32382556/36624422-c5967612-18c3-11e8-99a5-1566e536fe7d.png)

## Laplace Smoothing:
If a word in the email we're classifying isn't in the training set, we have added a smoothing factor. This is best exemplified in the modified code below where smoothing factor alpha is added:

```
#gives the conditional probability p(B_i | A_x)
def conditional_word(word, spam):
    if spam:
        return (trainpostive[word].get(word,0)+alpha)/(float)(positive_total+alpha*numwords)
    return (trainnegative[word].get(word,0)+alpha)./(float)(negative_total+alpha*numwords)
```
## Features:
- Performed filtering of spam emails.
- Bag of words model.
- Naive Bayes written from scratch.
- Laplace smoothing to handle unknown words.

## Results:
- Enhanced the overall test accuracy to 97%
- False positive rate - 0.5% (Only 5 mails falsely classified as spam for every ~2000 mails).

## References:
- https://hackernoon.com/how-to-build-a-simple-spam-detecting-machine-learning-classifier-4471fe6b816e
