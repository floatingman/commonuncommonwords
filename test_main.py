import unittest

from main import common_and_uncommon_words


class TestCommonUncommonWords(unittest.TestCase):
    # Test Data
    sentence1 = "This is a sentence that contains some common words"
    sentence2 = "Another sentence that possibly has the same words like this"
    blanksentence2 = ""
    onewordsentence1 = "Hi"
    onewordsentence2 = "Bye"
    expected_sentence12_commonwords = sorted(['that', 'sentence', 'words', 'this'])
    expected_sentence12_uncommonwords = sorted(
        ['is', 'common', 'has', 'some', 'the', 'possibly', 'another', 'like', 'a', 'same', 'contains'])
    expected_same_sentence = sorted(['common', 'that', 'a', 'contains', 'sentence', 'some', 'is', 'this', 'words'])
    expected_one_blank_sentence = sorted(['a', 'that', 'contains', 'common', 'is', 'this', 'words', 'some', 'sentence'])

    # Helper functions
    def run_function_and_sort_results(self, string1: str, string2: str) -> (list, list):
        """
        :param string1:
        :param string2:
        :return: (list, list)
        Helper function sort results
        """
        common_words, uncommon_words = common_and_uncommon_words(string1, string2)
        return sorted(common_words), sorted(uncommon_words)

    # Tests
    def test_two_different_sentences(self):
        """
        Test with two different sentences
        """
        common_words_sorted, uncommon_words_sorted = self.run_function_and_sort_results(self.sentence1, self.sentence2)
        self.assertEqual(common_words_sorted, self.expected_sentence12_commonwords)
        self.assertEqual(uncommon_words_sorted, self.expected_sentence12_uncommonwords)

    def test_same_sentence(self):
        """
        Test with the same sentences. Common_words array should contain all the words
        and uncommon_words array should be empty
        """
        common_words_sorted, uncommon_words_sorted = self.run_function_and_sort_results(self.sentence1, self.sentence1)
        self.assertEqual(common_words_sorted, self.expected_same_sentence)
        self.assertEqual(len(uncommon_words_sorted), 0)

    def test_one_blank_sentence(self):
        """
        Test with one blank sentence. Uncommon_words array should contain all the words
        and common_words array should be empty
        """
        common_words_sorted, uncommon_words_sorted = self.run_function_and_sort_results(self.sentence1, "")
        self.assertEqual(uncommon_words_sorted, self.expected_one_blank_sentence)
        self.assertEqual(len(common_words_sorted), 0)

    def test_one_word_sentences(self):
        """
        Test one word sentences
        :return:
        """
        common_words_sorted, uncommon_words_sorted = self.run_function_and_sort_results(self.onewordsentence1,
                                                                                        self.onewordsentence2)
        self.assertEqual(len(common_words_sorted), 0)
        self.assertEquals(uncommon_words_sorted, ["bye", "hi"])

    def test_incorrect_arguments_number_of_arguments(self):
        """
        Test with incorrect number of arguments
        """
        with self.assertRaises(TypeError):
            common_words, uncommon_words = common_and_uncommon_words(self.sentence1)

    def test_wrong_type_of_arguments(self):
        """
        Test with the wrong type of arguments
        """
        with self.assertRaises(AttributeError):
            common_words, uncommon_words = common_and_uncommon_words(1, 2)


if __name__ == '__main__':
    unittest.main()
