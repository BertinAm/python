def word_length(mort):
    count = 0
    for mor in mort:
        if len(mor) == 5:
            count += 1
    return(count)
print(word_length(["john","james","marie","peter","bertin","goddy"]))