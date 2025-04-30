import colorsys


def rgb2hls(input_color):
    r = input_color[0]
    g = input_color[1]
    b = input_color[2]

    hls1 = colorsys.rgb_to_hls(r / 255, g / 255, b / 255)
    hls1 = list(hls1)
    return hls1
    # print(hls1)

    # print(f"Мой цвет по HLS {hls1}")


def hls2rgb(input_color):
    h = input_color[0]
    lightness = input_color[1]
    s = input_color[2]
    # def int_r(num):
    #     num = int(num + (0.5 if num > 0 else -0.5))
    #     return num

    final_color1 = colorsys.hls_to_rgb(h, lightness, s)
    final_color1 = list(final_color1)
    final_color = list(map(lambda x: x * 255, final_color1))
    return final_color

    # print(f"Мой цвет по RGB {final_color}")
