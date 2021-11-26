import random
import string
data = " ".join("".join(
    random.choices(string.ascii_lowercase, k=8)) for i in range(500000))
bad = ["a", "b", "c"]
good = ['good', "asdgg", "afffs", "sdsdf"]

def check_word(text):
    splitted_text = text.split()
    if not all(word not in splitted_text for word in bad):
        return True
    if not any(word in splitted_text for word in good):
        return True
    return False


if __name__ == '__main__':
    assert check_word("asd") == True, "Mistake"
    assert check_word("good bad") == False, "Mistake"
    assert check_word("good b") == True, "Mistake"
    assert check_word("sasd c") == True, "Mistake"
    assert check_word("sasd sdsdfff") == False, "Mistake"

    import timeit
    print(timeit.timeit("check_word(data)", 
        setup="from __main__ import check_word, bad, good, data", number=100))