def longest_word(word):
    new = []
    for b in word:
        c = len(b)
        new.append(c)
    max_word = max(new)
    name = [x for x in word if len(x) == max(new)]
    for x in name:
        continue
    lang_len = [max_word, x]
    return lang_len


lang = ['Java', 'JavaScript', 'Python']
print(longest_word(lang))
