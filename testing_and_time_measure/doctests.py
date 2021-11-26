"""Смотреть детальные результаты тестов через python ./doctests.py -v
-v Обязательно в конце!!!
Здесь наверху тоже можно писать тесты
>>> check_word("sasd c") == True
True
"""

a = ["a", "b", "c"]
b = ['good']

def check_word(text):
    """
    >>> check_word("asd") == True
    True
    >>> check_word("good bad") == False
    True
    """
    splitted_text = text.split()
    if not any(word in splitted_text for word in b):
        return True
    for word in splitted_text:
        if word in a:
            return True
    return False

if __name__ == "__main__":
    import doctest
    doctest.testmod()