from rgb2hls import rgb2hls, hls2rgb
from rgb2ryb import rgb2ryb, ryb2rgb
import colorsys


def clas_thiad_rgb(r, g, b):
    col = (r, g, b)
    HLS = rgb2hls(col)
    HLS1 = (((HLS[0] * 360 + 120) % 360) / 360, HLS[1], HLS[2])
    HLS2 = (((HLS[0] * 360 - 120) % 360) / 360, HLS[1], HLS[2])
    HLS1 = hls2rgb(HLS1)
    HLS2 = hls2rgb(HLS2)
    return HLS1, HLS2


def clas_thiad_ryb(r, g, b):
    # Переводим в RYB
    ryb = rgb2ryb((r, g, b))
    r, y, b = ryb

    # Нормализуем к диапазону [0, 1]
    r, y, b = [x / 255.0 for x in (r, y, b)]

    # Переводим RYB в HSV через условный круг
    h = (colorsys.rgb_to_hsv(r, y, b)[0] * 360)
    h1 = (h + 120) % 360
    h2 = (h - 120) % 360

    # Цвета на триаде в RYB
    ryb1 = colorsys.hsv_to_rgb(h1 / 360, 1, 1)
    ryb2 = colorsys.hsv_to_rgb(h2 / 360, 1, 1)

    # Возврат к 0–255 и RYB → RGB
    ryb1 = tuple(int(x * 255) for x in ryb1)
    ryb2 = tuple(int(x * 255) for x in ryb2)

    rgb1 = ryb2rgb(ryb1)
    rgb2 = ryb2rgb(ryb2)

    return rgb1, rgb2


if __name__ == "__main__":
    print(clas_thiad_rgb(255, 255, 0))
    print(clas_thiad_ryb(255, 255, 0))
