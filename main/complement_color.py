"""
Для импорта ее в код: complement(red, green, blue)
Функция находит комплементарный цветов
Работает с цветовой моделью RGB
"""
from rgb2ryb import ryb2rgb
from rgb2hls import rgb2hls, hls2rgb

def hilo(a, b, c):
    if c < b: b, c = c, b
    if b < a: a, b = b, a
    if c < b: b, c = c, b
    return a + c

def complement_rgb(r, g, b):
    k = hilo(r, g, b)
    return tuple(k - u for u in (r, g, b))

def complement_ryb(r, y, b):
    opposite_color_RYB = (255 - r, 255 - y, 255 - b)
    opposite_color_RYB = ryb2rgb(opposite_color_RYB)
    opposite_color_RYB = rgb2hls(opposite_color_RYB)
    if opposite_color_RYB[1] > 0.5: opposite_color_RYB[1] -= 0.5
    opposite_color_RYB = hls2rgb(opposite_color_RYB)
    return opposite_color_RYB
