# Spam_filter
This is an implementation of a Naive Bayesian Classifier written in Python. The utility uses statistical methods to classify documents, based on the words that appear within them. A common application for this type of software is in email spam filters.

The utility must first be 'trained' using large numbers of pre-classified documents, during the training phase a database is populated with information about how often certain words appear in each type of document. Once training is complete, unclassified documents can be submitted to the classifier which will return a value between 0 and 1, indicating the probablity that the document belongs to one class of document rather than another.

## Bayes Theorem
![image](https://user-images.githubusercontent.com/32382556/36624422-c5967612-18c3-11e8-99a5-1566e536fe7d.png)
