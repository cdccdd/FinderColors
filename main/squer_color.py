
from rgb2hls import rgb2hls, hls2rgb
from rgb2ryb import rgb2ryb, ryb2rgb
import colorsys

rgb_hues = [0, 60, 120, 180, 240, 300, 360]
ryb_hues = [0, 40, 85, 135, 195, 260, 360]

def interpolate_hue(h, table_in, table_out):
    for i in range(1, len(table_in)):
        if h <= table_in[i]:
            t = (h - table_in[i - 1]) / (table_in[i] - table_in[i - 1])
            return table_out[i - 1] + t * (table_out[i] - table_out[i - 1])
    return table_out[-1]

def rgb2hryb(r, g, b):
    h, l, s = colorsys.rgb_to_hls(r / 255, g / 255, b / 255)
    h_deg = h * 360
    h_ryb = interpolate_hue(h_deg, rgb_hues, ryb_hues) / 360
    return h_ryb, l, s

def hryb2rgb(h, l, s):
    h_deg = h * 360
    h_rgb = interpolate_hue(h_deg, ryb_hues, rgb_hues) / 360
    r, g, b = colorsys.hls_to_rgb(h_rgb, l, s)
    return int(r * 255), int(g * 255), int(b * 255)

def squer_rgb(r, g, b):
    HLS = rgb2hls((r, g, b))
    steps = [0, 90, 180, 270]
    return [hls2rgb((((HLS[0] * 360 + s) % 360) / 360, HLS[1], HLS[2])) for s in steps[1:]]

def squer_ryb(r, g, b):
    h, l, s = rgb2hryb(r, g, b)
    steps = [90/360, 180/360, 270/360]
    return [hryb2rgb((h + s) % 1.0, l, s) for s in steps]
