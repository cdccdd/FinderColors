
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

def analog_thiad_rgb(r, g, b):
    HLS = rgb2hls((r, g, b))
    HLS1 = (((HLS[0] * 360 + 30) % 360) / 360, HLS[1], HLS[2])
    HLS2 = (((HLS[0] * 360 - 30) % 360) / 360, HLS[1], HLS[2])
    return hls2rgb(HLS1), hls2rgb(HLS2)

def analog_thiad_ryb(r, g, b):
    h, l, s = rgb2hryb(r, g, b)
    h1 = (h + 30/360) % 1.0
    h2 = (h - 30/360) % 1.0
    return hryb2rgb(h1, l, s), hryb2rgb(h2, l, s)
