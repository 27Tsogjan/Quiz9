def count_words(text):
    count = 0
    for words in text.split():
        if(words != ""):
            count += 1
    return count

def count_chars(text):
    count = 0
    for char in text:
        if (char != " " and char != ""):
            count += 1
    return count


    
