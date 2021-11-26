import random
import string
data = " ".join("".join(
    random.choices(string.ascii_lowercase, k=8)) for i in range(500000))
bad = ["a", "b", "c"]
good = ['good', "asdgg", "afffs", "sdsdfff"]

def check_word(text):
    spl_text = set(text.split())
    if spl_text.intersection(bad) == set() and spl_text.intersection(good) != set():
        return 'Проверка пройдена'
    return 'Проверка не пройдена'




if __name__ == '__main__':
    assert check_word("asd") == 'Проверка не пройдена', "Mistake"
    assert check_word("good bad") == 'Проверка пройдена', "Mistake"
    assert check_word("good b") == 'Проверка не пройдена', "Mistake"
    assert check_word("sasd c") == 'Проверка не пройдена', "Mistake"
    assert check_word("sasd sdsdfff") == 'Проверка пройдена', "Mistake"

    import timeit
    print(timeit.timeit("check_word(data)",
        setup="from __main__ import check_word, bad, good, data", number=100))