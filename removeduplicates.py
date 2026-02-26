sentence = "Python is a great great language to learn Python"
words = sentence.split()
unique_words = dict.fromkeys(words) 


result_sentence = ' '.join(unique_words.keys())
print("Original sentence:", sentence)
print("Sentence after removing duplicates:", result_sentence)