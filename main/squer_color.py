from rgb2hls import rgb2hls, hls2rgb
from rgb2ryb import rgb2ryb, ryb2rgb
from complement_color import complement_rgb, complement_ryb

def squer_rgb(r, g, b):
    col = (r, g, b)
    HLS = rgb2hls(col)
    HLS1 = (((HLS[0]*360 + 90)%360)/360, HLS[1], HLS[2])
    HLS2 = (((HLS[0]*360 - 90)%360)/360, HLS[1], HLS[2])
    HLS3 = complement_rgb(r, g, b)
    HLS1 = hls2rgb(HLS1)
    HLS2 = hls2rgb(HLS2)

    return HLS1, HLS2, list(HLS3)

def squer_ryb(r, g, b):
    col = (r, g, b)
    my_ryb = rgb2ryb(col)
    HLS = rgb2hls(my_ryb)
    HLS1 = (((HLS[0]*360 + 90)%360)/360, HLS[1], HLS[2])
    HLS2 = (((HLS[0]*360 - 90)%360)/360, HLS[1], HLS[2])
    HLS3 = complement_ryb(my_ryb[0], my_ryb[1], my_ryb[2])
    HLS1 = hls2rgb(HLS1)
    HLS2 = hls2rgb(HLS2)
    col1, col2 = ryb2rgb(HLS1), ryb2rgb(HLS2)
    return col1, col2, list(HLS3)







if __name__ =='__main__':
    print(squer_rgb(255, 0, 0))
    print(squer_ryb(44, 227, 3))
