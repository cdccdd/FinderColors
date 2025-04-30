from rgb2hls import rgb2hls, hls2rgb
from rgb2ryb import rgb2ryb, ryb2rgb


def contr_thiad_rgb(r, g, b):
    col = (r, g, b)
    HLS = rgb2hls(col)
    HLS1 = (((HLS[0] * 360 + 150) % 360) / 360, HLS[1], HLS[2])
    HLS2 = (((HLS[0] * 360 - 150) % 360) / 360, HLS[1], HLS[2])
    HLS1 = hls2rgb(HLS1)
    HLS2 = hls2rgb(HLS2)
    return HLS1, HLS2


def contr_thiad_ryb(r, g, b):
    col = (r, g, b)
    my_ryb = rgb2ryb(col)
    HLS = rgb2hls(my_ryb)
    HLS1 = (((HLS[0] * 360 + 150) % 360) / 360, HLS[1], HLS[2])
    HLS2 = (((HLS[0] * 360 - 150) % 360) / 360, HLS[1], HLS[2])
    HLS1 = hls2rgb(HLS1)
    HLS2 = hls2rgb(HLS2)
    col1, col2 = ryb2rgb(HLS1), ryb2rgb(HLS2)
    return col1, col2


if __name__ == "__main__":
    print(contr_thiad_rgb(255, 255, 0))
    print(contr_thiad_ryb(44, 227, 3))
