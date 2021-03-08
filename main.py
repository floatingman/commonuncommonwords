def common_and_uncommon_words(sentence1: str, sentence2: str) -> (list, list):
    """A simple function that returns a list of common and uncommon words
    contained within two sentences"""

    # Because uppercase and lowercase words don't match, convert to lowercase
    # and split into a list of words
    sentence1words = sentence1.lower().split()
    sentence2words = sentence2.lower().split()

    # A set is a good data structure to find common and unique values
    sentence1set = set(sentence1words)
    sentence2set = set(sentence2words)

    # Find the intersection of words in each set for common values
    common_words = sentence1set.intersection(sentence1set)
    # Finding the disjunctive union of words in each set for uncommon values
    uncommon_words = sentence1set.symmetric_difference(sentence2set)

    # Since we need to return two arrays, we return a tuple of lists
    # which we con unpack into two variables.
    return list(common_words), list(uncommon_words)


if __name__ == '__main__':
    sentence1 = "This is a sentence that contains some common words"
    sentence2 = "Another sentence that possibly has the same words like this"
    blanksentence2 = ""

    print("Two different sentences")
    common_words, uncommon_words = common_and_uncommon_words(sentence1, sentence2)
    print("Common Words")
    print(common_words)
    print("Uncommon words")
    print(uncommon_words)

    print("One Blank Sentence")
    common_words, uncommon_words = common_and_uncommon_words(sentence1, blanksentence2)
    print("Common Words")
    print(common_words)
    print("Uncommon words")
    print(uncommon_words)

    print("Two Identical Sentences")
    common_words, uncommon_words = common_and_uncommon_words(sentence1, sentence1)
    print("Common Words")
    print(common_words)
    print("Uncommon words")
    print(uncommon_words)
