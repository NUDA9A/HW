def upper_case(s):
    """Возвращает строку с заглавными буквами"""
    return s.upper()

def Title_case(s):
    """Возвращает строку в которой каждое слово с заглавной буквы"""
    result = ""
    a = s.split()
    for x in a:
        result += x.title()
    return result
