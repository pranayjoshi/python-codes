def avg_word(sentence):   
    words = sentence.split()
    average = sum(len(word) for word in words) / len(words)
    print(average)
