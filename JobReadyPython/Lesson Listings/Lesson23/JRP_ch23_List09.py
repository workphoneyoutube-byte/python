def tokenize_review(review):
    if type(review) != dict:
        raise Exception("Review must be a dictionary")
    new_review = review.copy()
    words= tokenize(new_review[TEXT_KEY])
    new_review[WORDS_KEY] = words
    return new_review
