from rgb2hls import rgb2hls, hls2rgb
from rgb2ryb import rgb2ryb, ryb2rgb
from complement_color import complement

def squer_rgb(r, g, b):
    col = (r, g, b)
    HLS = rgb2hls(col)
    HLS1 = (((HLS[0]*360 + 90)%360)/360, HLS[1], HLS[2])
    HLS2 = (((HLS[0]*360 - 90)%360)/360, HLS[1], HLS[2])
    HLS3 = complement(r, g, b)
    HLS1 = hls2rgb(HLS1)
    HLS2 = hls2rgb(HLS2)

    return HLS1, HLS2, list(HLS3)

def squer_ryb(r, g, b):
    col = (r, g, b)
    pass







if __name__ =='__main__':
    print(squer_rgb(255, 0, 0))
    print(squer_ryb(44, 227, 3))
