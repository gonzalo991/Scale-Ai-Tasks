def length_words(sentence):
    '''
    Function that receives a sentence and returns a dictionary with the words it contains and their lengths.
    Parameters:
        sentence: A string of characters containing a sentence.
    Returns:
        A dictionary with word:length pairs, where words are the words present in the sentence.
    '''
    words = sentence.split()  # Split the sentence into words using whitespace as separator
    lengths = map(len, words)  # Calculate the lengths of the words using the len function
    return dict(zip(words, lengths))  # Create a dictionary by pairing words with their corresponding lengths

print(length_words('Welcome to Python'))  # Example usage of the length_words function