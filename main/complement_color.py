"""
Для импорта ее в код: complement(red, green, blue)
Функция находит комплементарный цветов
Работает с цветовой моделью RGB
"""


def hilo(a, b, c):
    if c < b: b, c = c, b
    if b < a: a, b = b, a
    if c < b: b, c = c, b
    return a + c

def complement(r, g, b):
    k = hilo(r, g, b)
    return tuple(k - u for u in (r, g, b))
