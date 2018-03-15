#runs once on training data
def train:
    total = 0
    num_spam = 0
    for email in train_data:
        if email.label == SPAM :
            num_spam += 1
        total += 1
        processEmail(email.body, email.label)
    p_A = num_spam/float(total)
    p_notA = (total-num_spam)/(float(total))



#counts the number of times a particular word occurs in an email
def processEmail(body, label):
    for word in body:
        if label == SPAM :
            trainpostitive[word] = trainpositive.get(word, 0) + 1
            postive_total += 1
        else :
            trainnegative[word] = trainnegative.get(word, 0) + 1
            negative_total += 1


            
#gives the conditional probability p(B_i | A_x)
def conditional_word(word, spam):
    if spam:
        return (trainpostive[word].get(word,0)+alpha)/(float)(positive_total+alpha*numwords)
    return (trainnegative[word].get(word,0)+alpha)./(float)(negative_total+alpha*numwords)



#in order to get conditional probability p(B | A_x) i.e for an entire email, we simply take the product of p(B_i | A_x) value for every word in the email
def conditional_email(body, spam):
    result = 1
    for word in body:
        result *= conditional_word(word, spam)
    return result



#classifies whether an email is spam or not
def classify(email):
    is_Spam = p_A * conditional_email(email, True) # P( A | B )
    not_Spam = p_notA * conditional_email(email, False) # P( notA | B )
    return is_Spam > not_Spam
        
