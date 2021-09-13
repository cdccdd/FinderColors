from rgb2hls import rgb2hls, hls2rgb
from rgb2ryb import rgb2ryb, ryb2rgb

def clas_thiad_rgb(r, g, b):
    col = (r, g, b)
    HLS = rgb2hls(col)
    HLS1 = (((HLS[0]*360 + 120)%360)/360, HLS[1], HLS[2])
    HLS2 = (((HLS[0]*360 - 120)%360)/360, HLS[1], HLS[2])
    HLS1 = hls2rgb(HLS1)
    HLS2 = hls2rgb(HLS2)
    return HLS1, HLS2

def clas_thiad_ryb(r, g, b):
    col = (r, g, b)
    transfer_to_ryb = rgb2ryb(col)
    r = transfer_to_ryb[0]
    y = transfer_to_ryb[1]
    b = transfer_to_ryb[2]
    new_col1 = [b, r, y]
    new_col2 = [y, b, r]
    return new_col1, new_col2







if __name__ =='__main__':
    print(clas_thiad_rgb(255, 255, 0))
    print(clas_thiad_ryb(44, 227, 3))
