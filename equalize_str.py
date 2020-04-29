def equalize(str1, str2):
    length = max(len(str1), len(str2))
    word = min(str1, str2)
    extra_long_word = word * (length//len(word) + 1)
    required_string = extra_long_word[:length]
    print(required_string)
