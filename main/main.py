# grid использует воображаемую сетку, place использует пиксели, pack использует центры сторон и распологается по середине
import tkinter as tk
from tkinter import colorchooser
from tkinter import ttk
import os
import sys
from PIL import ImageTk, Image
from complement_color import complement_rgb, complement_ryb
from rgb2hex import rgb_to_hex
from rgb2ryb import rgb2ryb
from rgb2cmyk import rgb2cmyk
from rgb2hls import rgb2hls, hls2rgb
from ColorsName import ColorsName
from classic_thiada_color import clas_thiad_rgb, clas_thiad_ryb
from analog_thiada_color import analog_thiad_rgb, analog_thiad_ryb
from contrast_thiada_color import contr_thiad_rgb, contr_thiad_ryb
from squer_color import squer_rgb, squer_ryb

# Получаем абсолютный путь к директории проекта
if getattr(sys, "frozen", False):
    # Если программа запущена как исполняемый файл
    current_dir = os.path.dirname(sys.executable)
else:
    # Если программа запущена как скрипт
    current_dir = os.path.dirname(os.path.abspath(__file__))

print("Текущая директория скрипта:", current_dir)

# Формируем абсолютные пути к директориям
base_dir = os.path.dirname(current_dir)  # поднимаемся на уровень выше
image_dir = os.path.join(base_dir, "Image")
text_dir = os.path.join(base_dir, "Text_files")

print("Базовая директория:", base_dir)
print("Путь к изображениям:", image_dir)
print("Путь к текстовым файлам:", text_dir)

# Проверяем существование директорий и файлов
print("\nПроверка директорий и файлов:")
print(f"Директория Image существует: {os.path.exists(image_dir)}")
print(f"Директория Text_files существует: {os.path.exists(text_dir)}")

title_gif_path = os.path.join(image_dir, "title.gif")
print(f"Файл title.gif существует: {os.path.exists(title_gif_path)}")
if os.path.exists(title_gif_path):
    print(f"Размер файла title.gif: {os.path.getsize(title_gif_path)} байт")

try:
    print("\nПопытка загрузки изображения...")
    test_image = Image.open(title_gif_path)
    print("Изображение успешно загружено")
    test_image.verify()
    print("Изображение верифицировано")
except Exception as e:
    print(f"Ошибка при загрузке изображения: {str(e)}")


def clear_frame(frame):
    # Удаляем все виджеты из фрейма
    for widget in frame.winfo_children():
        widget.destroy()


def ReturningColorRGB(selec, rgb, ryb, rgb2=None, ryb2=None):
    # Очищаем фрейм перед добавлением новых элементов
    clear_frame(frame_result)

    if (selec[0][0] + selec[0][1] + selec[0][2]) > 383 or max(
        selec[0][0], selec[0][1], selec[0][2]
    ) - min(selec[0][0], selec[0][1], selec[0][2]) > 230:
        text_fg = "black"
    else:
        text_fg = "white"
    text_in_label = (
        "Выбранный цвет\n"
        + "RGB: "
        + str(list(map(int, selec[0])))
        + "\nhex: "
        + str(selec[1])
        + "\nCMYK: "
        + str(rgb2cmyk(selec[0][0], selec[0][1], selec[0][2]))
        + "\nRYB"
        + str(rgb2ryb(selec[0]))
        + "\nЦвет: "
        + ColorsName(selec[1])
    )
    l_color = tk.Label(
        frame_result,
        text=text_in_label,
        bg=selec[1],
        justify="left",
        fg=text_fg,
        height=6,
        width=50,
        anchor="w",
        relief="ridge",
        bd=9,
    )
    l_color.place(x=0, y=0)

    if (rgb[0] + rgb[1] + rgb[2]) > 383 or max(rgb[0], rgb[1], rgb[2]) - min(
        rgb[0], rgb[1], rgb[2]
    ) > 230:
        text_fdg = "black"
    else:
        text_fdg = "white"
    hexG = rgb_to_hex(int(rgb[0]), int(rgb[1]), int(rgb[2]))
    text_in_label_g = (
        "Для программ и печати(RGB/CMYK)\n"
        + "RGB: "
        + str(list(map(int, rgb)))
        + "\nhex: "
        + hexG
        + "\nCMYK: "
        + str(rgb2cmyk(rgb[0], rgb[1], rgb[2]))
        + "\nRYB"
        + str(rgb2ryb(rgb))
        + "\nЦвет: "
        + ColorsName(hexG)
    )
    l_color_g = tk.Label(
        frame_result,
        text=text_in_label_g,
        bg=hexG,
        justify="left",
        fg=text_fdg,
        height=6,
        width=50,
        anchor="w",
        relief="ridge",
        bd=9,
    )
    l_color_g.place(x=0, y=110)

    if rgb2 is not None:
        if (rgb2[0] + rgb2[1] + rgb2[2]) > 383 or max(rgb2[0], rgb2[1], rgb2[2]) - min(
            rgb2[0], rgb2[1], rgb2[2]
        ) > 230:
            text_fdg2 = "black"
        else:
            text_fdg2 = "white"
        hexG2 = rgb_to_hex(int(rgb2[0]), int(rgb2[1]), int(rgb2[2]))
        text_in_label_g2 = (
            "Для программ и печати(RGB/CMYK)\n"
            + "RGB: "
            + str(list(map(int, rgb2)))
            + "\nhex: "
            + hexG2
            + "\nCMYK: "
            + str(rgb2cmyk(rgb2[0], rgb2[1], rgb2[2]))
            + "\nRYB"
            + str(rgb2ryb(rgb2))
            + "\nЦвет: "
            + ColorsName(hexG2)
        )
        l_color_g2 = tk.Label(
            frame_result,
            text=text_in_label_g2,
            bg=hexG2,
            justify="left",
            fg=text_fdg2,
            height=6,
            width=50,
            anchor="w",
            relief="ridge",
            bd=9,
        )
        l_color_g2.place(x=370, y=110)

    if (ryb[0] + ryb[1] + ryb[2]) > 383 or max(ryb[0], ryb[1], ryb[2]) - min(
        ryb[0], ryb[1], ryb[2]
    ) > 230:
        text_fdy = "black"
    else:
        text_fdy = "white"
    hexY = rgb_to_hex(int(ryb[0]), int(ryb[1]), int(ryb[2]))
    text_in_label_y = (
        "Для художников(RYB)\n"
        + "RGB: "
        + str(list(map(int, ryb)))
        + "\nhex: "
        + hexY
        + "\nCMYK: "
        + str(rgb2cmyk(ryb[0], ryb[1], ryb[2]))
        + "\nRYB"
        + str(rgb2ryb(ryb))
        + "\nЦвет: "
        + ColorsName(hexY)
    )
    l_color_y = tk.Label(
        frame_result,
        text=text_in_label_y,
        bg=hexY,
        justify="left",
        fg=text_fdy,
        height=6,
        width=50,
        anchor="w",
        relief="ridge",
        bd=9,
    )
    l_color_y.place(x=0, y=220)

    if ryb2 is not None:
        if (ryb2[0] + ryb2[1] + ryb2[2]) > 383 or max(ryb2[0], ryb2[1], ryb2[2]) - min(
            ryb2[0], ryb2[1], ryb2[2]
        ) > 230:
            text_fdy2 = "black"
        else:
            text_fdy2 = "white"
        hexY2 = rgb_to_hex(int(ryb2[0]), int(ryb2[1]), int(ryb2[2]))
        text_in_label_y2 = (
            "Для художников(RYB)\n"
            + "RGB: "
            + str(list(map(int, ryb2)))
            + "\nhex: "
            + hexY2
            + "\nCMYK: "
            + str(rgb2cmyk(ryb2[0], ryb2[1], ryb2[2]))
            + "\nRYB"
            + str(rgb2ryb(ryb2))
            + "\nЦвет: "
            + ColorsName(hexY2)
        )
        l_color_y2 = tk.Label(
            frame_result,
            text=text_in_label_y2,
            bg=hexY2,
            justify="left",
            fg=text_fdy2,
            height=6,
            width=50,
            anchor="w",
            relief="ridge",
            bd=9,
        )
        l_color_y2.place(x=370, y=220)

    if rgb2 == None:
        l_clear_bg = tk.Frame(frame_result, width=740, height=335, bg="#f0f0f0")
        l_clear_bg.place(x=370, y=0)
    else:
        l_clear_bg = tk.Frame(frame_result, width=740, height=335, bg="#f0f0f0")
        l_clear_bg.place(x=740, y=0)


def ReturningColorRGB4recta(selec1, selec2, rgb1, rgb2, ryb1, ryb2):
    # Очищаем фрейм перед добавлением новых элементов
    clear_frame(frame_result)

    if (selec1[0][0] + selec1[0][1] + selec1[0][2]) > 383 or max(
        selec1[0][0], selec1[0][1], selec1[0][2]
    ) - min(selec1[0][0], selec1[0][1], selec1[0][2]) > 230:
        text_fg1 = "black"
    else:
        text_fg1 = "white"
    text_in_label1 = (
        "Выбранный цвет\n"
        + "RGB: "
        + str(list(map(int, selec1[0])))
        + "\nhex: "
        + str(selec1[1])
        + "\nCMYK: "
        + str(rgb2cmyk(selec1[0][0], selec1[0][1], selec1[0][2]))
        + "\nRYB"
        + str(rgb2ryb(selec1[0]))
        + "\nЦвет: "
        + ColorsName(selec1[1])
    )
    l_color1 = tk.Label(
        frame_result,
        text=text_in_label1,
        bg=selec1[1],
        justify="left",
        fg=text_fg1,
        height=6,
        width=50,
        anchor="w",
        relief="ridge",
        bd=9,
    )
    l_color1.place(x=0, y=0)

    if (selec2[0][0] + selec2[0][1] + selec2[0][2]) > 383 or max(
        selec2[0][0], selec2[0][1], selec2[0][2]
    ) - min(selec2[0][0], selec2[0][1], selec2[0][2]) > 230:
        text_fg2 = "black"
    else:
        text_fg2 = "white"
    text_in_label2 = (
        "Выбранный цвет\n"
        + "RGB: "
        + str(list(map(int, selec2[0])))
        + "\nhex: "
        + str(selec2[1])
        + "\nCMYK: "
        + str(rgb2cmyk(selec2[0][0], selec2[0][1], selec2[0][2]))
        + "\nRYB"
        + str(rgb2ryb(selec2[0]))
        + "\nЦвет: "
        + ColorsName(selec2[1])
    )
    l_color2 = tk.Label(
        frame_result,
        text=text_in_label2,
        bg=selec2[1],
        justify="left",
        fg=text_fg2,
        height=6,
        width=50,
        anchor="w",
        relief="ridge",
        bd=9,
    )
    l_color2.place(x=370, y=0)

    if (rgb1[0] + rgb1[1] + rgb1[2]) > 383 or max(rgb1[0], rgb1[1], rgb1[2]) - min(
        rgb1[0], rgb1[1], rgb1[2]
    ) > 230:
        text_fdg1 = "black"
    else:
        text_fdg1 = "white"
    hexG1 = rgb_to_hex(int(rgb1[0]), int(rgb1[1]), int(rgb1[2]))
    text_in_label_g1 = (
        "Для программ и печати(RGB/CMYK)\n"
        + "RGB: "
        + str(list(map(int, rgb1)))
        + "\nhex: "
        + hexG1
        + "\nCMYK: "
        + str(rgb2cmyk(rgb1[0], rgb1[1], rgb1[2]))
        + "\nRYB"
        + str(rgb2ryb(rgb1))
        + "\nЦвет: "
        + ColorsName(hexG1)
    )
    l_color_g1 = tk.Label(
        frame_result,
        text=text_in_label_g1,
        bg=hexG1,
        justify="left",
        fg=text_fdg1,
        height=6,
        width=50,
        anchor="w",
        relief="ridge",
        bd=9,
    )
    l_color_g1.place(x=0, y=110)

    if (rgb2[0] + rgb2[1] + rgb2[2]) > 383 or max(rgb2[0], rgb2[1], rgb2[2]) - min(
        rgb2[0], rgb2[1], rgb2[2]
    ) > 230:
        text_fdg2 = "black"
    else:
        text_fdg2 = "white"
    hexG2 = rgb_to_hex(int(rgb2[0]), int(rgb2[1]), int(rgb2[2]))
    text_in_label_g2 = (
        "Для программ и печати(RGB/CMYK)\n"
        + "RGB: "
        + str(list(map(int, rgb2)))
        + "\nhex: "
        + hexG2
        + "\nCMYK: "
        + str(rgb2cmyk(rgb2[0], rgb2[1], rgb2[2]))
        + "\nRYB"
        + str(rgb2ryb(rgb2))
        + "\nЦвет: "
        + ColorsName(hexG2)
    )
    l_color_g2 = tk.Label(
        frame_result,
        text=text_in_label_g2,
        bg=hexG2,
        justify="left",
        fg=text_fdg2,
        height=6,
        width=50,
        anchor="w",
        relief="ridge",
        bd=9,
    )
    l_color_g2.place(x=370, y=110)

    if (ryb1[0] + ryb1[1] + ryb1[2]) > 383 or max(ryb1[0], ryb1[1], ryb1[2]) - min(
        ryb1[0], ryb1[1], ryb1[2]
    ) > 230:
        text_fdy1 = "black"
    else:
        text_fdy1 = "white"
    hexY1 = rgb_to_hex(int(ryb1[0]), int(ryb1[1]), int(ryb1[2]))
    text_in_label_y1 = (
        "Для художников(RYB)\n"
        + "RGB: "
        + str(list(map(int, ryb1)))
        + "\nhex: "
        + hexY1
        + "\nCMYK: "
        + str(rgb2cmyk(ryb1[0], ryb1[1], ryb1[2]))
        + "\nRYB"
        + str(rgb2ryb(ryb1))
        + "\nЦвет: "
        + ColorsName(hexY1)
    )
    l_color_y1 = tk.Label(
        frame_result,
        text=text_in_label_y1,
        bg=hexY1,
        justify="left",
        fg=text_fdy1,
        height=6,
        width=50,
        anchor="w",
        relief="ridge",
        bd=9,
    )
    l_color_y1.place(x=0, y=220)

    if (ryb2[0] + ryb2[1] + ryb2[2]) > 383 or max(ryb2[0], ryb2[1], ryb2[2]) - min(
        ryb2[0], ryb2[1], ryb2[2]
    ) > 230:
        text_fdy2 = "black"
    else:
        text_fdy2 = "white"
    hexY2 = rgb_to_hex(int(ryb2[0]), int(ryb2[1]), int(ryb2[2]))
    text_in_label_y2 = (
        "Для художников(RYB)\n"
        + "RGB: "
        + str(list(map(int, ryb2)))
        + "\nhex: "
        + hexY2
        + "\nCMYK: "
        + str(rgb2cmyk(ryb2[0], ryb2[1], ryb2[2]))
        + "\nRYB"
        + str(rgb2ryb(ryb2))
        + "\nЦвет: "
        + ColorsName(hexY2)
    )
    l_color_y2 = tk.Label(
        frame_result,
        text=text_in_label_y2,
        bg=hexY2,
        justify="left",
        fg=text_fdy2,
        height=6,
        width=50,
        anchor="w",
        relief="ridge",
        bd=9,
    )
    l_color_y2.place(x=370, y=220)

    l_clear_bg = tk.Frame(frame_result, width=740, height=335, bg="#f0f0f0")
    l_clear_bg.place(x=740, y=0)


def ReturningColorRGB4sque(selec, rgb1, rgb2, rgb3, ryb1, ryb2, ryb3):
    # Очищаем фрейм перед добавлением новых элементов
    clear_frame(frame_result)

    if (selec[0][0] + selec[0][1] + selec[0][2]) > 383 or max(
        selec[0][0], selec[0][1], selec[0][2]
    ) - min(selec[0][0], selec[0][1], selec[0][2]) > 230:
        text_fg = "black"
    else:
        text_fg = "white"
    text_in_label = (
        "Выбранный цвет\n"
        + "RGB: "
        + str(list(map(int, selec[0])))
        + "\nhex: "
        + str(selec[1])
        + "\nCMYK: "
        + str(rgb2cmyk(selec[0][0], selec[0][1], selec[0][2]))
        + "\nRYB"
        + str(rgb2ryb(selec[0]))
        + "\nЦвет: "
        + ColorsName(selec[1])
    )
    l_color = tk.Label(
        frame_result,
        text=text_in_label,
        bg=selec[1],
        justify="left",
        fg=text_fg,
        height=6,
        width=50,
        anchor="w",
        relief="ridge",
        bd=9,
    )
    l_color.place(x=0, y=0)

    if (rgb1[0] + rgb1[1] + rgb1[2]) > 383 or max(rgb1[0], rgb1[1], rgb1[2]) - min(
        rgb1[0], rgb1[1], rgb1[2]
    ) > 230:
        text_fdg1 = "black"
    else:
        text_fdg1 = "white"
    hexG1 = rgb_to_hex(int(rgb1[0]), int(rgb1[1]), int(rgb1[2]))
    text_in_label_g1 = (
        "Для программ и печати(RGB/CMYK)\n"
        + "RGB: "
        + str(list(map(int, rgb1)))
        + "\nhex: "
        + hexG1
        + "\nCMYK: "
        + str(rgb2cmyk(rgb1[0], rgb1[1], rgb1[2]))
        + "\nRYB"
        + str(rgb2ryb(rgb1))
        + "\nЦвет: "
        + ColorsName(hexG1)
    )
    l_color_g1 = tk.Label(
        frame_result,
        text=text_in_label_g1,
        bg=hexG1,
        justify="left",
        fg=text_fdg1,
        height=6,
        width=50,
        anchor="w",
        relief="ridge",
        bd=9,
    )
    l_color_g1.place(x=0, y=110)

    if (rgb2[0] + rgb2[1] + rgb2[2]) > 383 or max(rgb2[0], rgb2[1], rgb2[2]) - min(
        rgb2[0], rgb2[1], rgb2[2]
    ) > 230:
        text_fdg2 = "black"
    else:
        text_fdg2 = "white"
    hexG2 = rgb_to_hex(int(rgb2[0]), int(rgb2[1]), int(rgb2[2]))
    text_in_label_g2 = (
        "Для программ и печати(RGB/CMYK)\n"
        + "RGB: "
        + str(list(map(int, rgb2)))
        + "\nhex: "
        + hexG2
        + "\nCMYK: "
        + str(rgb2cmyk(rgb2[0], rgb2[1], rgb2[2]))
        + "\nRYB"
        + str(rgb2ryb(rgb2))
        + "\nЦвет: "
        + ColorsName(hexG2)
    )
    l_color_g2 = tk.Label(
        frame_result,
        text=text_in_label_g2,
        bg=hexG2,
        justify="left",
        fg=text_fdg2,
        height=6,
        width=50,
        anchor="w",
        relief="ridge",
        bd=9,
    )
    l_color_g2.place(x=370, y=110)

    if (rgb3[0] + rgb3[1] + rgb3[2]) > 383 or max(rgb3[0], rgb3[1], rgb3[2]) - min(
        rgb3[0], rgb3[1], rgb3[2]
    ) > 230:
        text_fdg3 = "black"
    else:
        text_fdg3 = "white"
    hexG3 = rgb_to_hex(int(rgb3[0]), int(rgb3[1]), int(rgb3[2]))
    text_in_label_g3 = (
        "Для программ и печати(RGB/CMYK)\n"
        + "RGB: "
        + str(list(map(int, rgb3)))
        + "\nhex: "
        + hexG2
        + "\nCMYK: "
        + str(rgb2cmyk(rgb3[0], rgb3[1], rgb3[2]))
        + "\nRYB"
        + str(rgb2ryb(rgb3))
        + "\nЦвет: "
        + ColorsName(hexG3)
    )
    l_color_g3 = tk.Label(
        frame_result,
        text=text_in_label_g3,
        bg=hexG3,
        justify="left",
        fg=text_fdg3,
        height=6,
        width=50,
        anchor="w",
        relief="ridge",
        bd=9,
    )
    l_color_g3.place(x=740, y=110)

    if (ryb1[0] + ryb1[1] + ryb1[2]) > 383 or max(ryb1[0], ryb1[1], ryb1[2]) - min(
        ryb1[0], ryb1[1], ryb1[2]
    ) > 230:
        text_fdy1 = "black"
    else:
        text_fdy1 = "white"
    hexY1 = rgb_to_hex(int(ryb1[0]), int(ryb1[1]), int(ryb1[2]))
    text_in_label_y1 = (
        "Для художников(RYB)\n"
        + "RGB: "
        + str(list(map(int, ryb1)))
        + "\nhex: "
        + hexY1
        + "\nCMYK: "
        + str(rgb2cmyk(ryb1[0], ryb1[1], ryb1[2]))
        + "\nRYB"
        + str(rgb2ryb(ryb1))
        + "\nЦвет: "
        + ColorsName(hexY1)
    )
    l_color_y1 = tk.Label(
        frame_result,
        text=text_in_label_y1,
        bg=hexY1,
        justify="left",
        fg=text_fdy1,
        height=6,
        width=50,
        anchor="w",
        relief="ridge",
        bd=9,
    )
    l_color_y1.place(x=0, y=220)

    if (ryb2[0] + ryb2[1] + ryb2[2]) > 383 or max(ryb2[0], ryb2[1], ryb2[2]) - min(
        ryb2[0], ryb2[1], ryb2[2]
    ) > 230:
        text_fdy2 = "black"
    else:
        text_fdy2 = "white"
    hexY2 = rgb_to_hex(int(ryb2[0]), int(ryb2[1]), int(ryb2[2]))
    text_in_label_y2 = (
        "Для художников(RYB)\n"
        + "RGB: "
        + str(list(map(int, ryb2)))
        + "\nhex: "
        + hexY2
        + "\nCMYK: "
        + str(rgb2cmyk(ryb2[0], ryb2[1], ryb2[2]))
        + "\nRYB"
        + str(rgb2ryb(ryb2))
        + "\nЦвет: "
        + ColorsName(hexY2)
    )
    l_color_y2 = tk.Label(
        frame_result,
        text=text_in_label_y2,
        bg=hexY2,
        justify="left",
        fg=text_fdy2,
        height=6,
        width=50,
        anchor="w",
        relief="ridge",
        bd=9,
    )
    l_color_y2.place(x=370, y=220)

    if (ryb3[0] + ryb3[1] + ryb3[2]) > 383 or max(ryb3[0], ryb3[1], ryb3[2]) - min(
        ryb3[0], ryb3[1], ryb3[2]
    ) > 230:
        text_fdy3 = "black"
    else:
        text_fdy3 = "white"
    hexY3 = rgb_to_hex(int(ryb3[0]), int(ryb3[1]), int(ryb3[2]))
    text_in_label_y3 = (
        "Для художников(RYB)\n"
        + "RGB: "
        + str(list(map(int, ryb3)))
        + "\nhex: "
        + hexY3
        + "\nCMYK: "
        + str(rgb2cmyk(ryb3[0], ryb3[1], ryb3[2]))
        + "\nRYB"
        + str(rgb2ryb(ryb3))
        + "\nЦвет: "
        + ColorsName(hexY3)
    )
    l_color_y3 = tk.Label(
        frame_result,
        text=text_in_label_y3,
        bg=hexY3,
        justify="left",
        fg=text_fdy3,
        height=6,
        width=50,
        anchor="w",
        relief="ridge",
        bd=9,
    )
    l_color_y3.place(x=740, y=220)


def opposite():
    color = colorchooser.askcolor(title="Выберите цвет")
    if color[1] is not None:
        rgb_hex = color[1]
        rgb_color = list(map(int, color[0]))
        ryb_color = rgb2ryb(rgb_color)
        rgb_comp = complement_rgb(rgb_color[0], rgb_color[1], rgb_color[2])
        ryb_comp = complement_ryb(ryb_color[0], ryb_color[1], ryb_color[2])
        ReturningColorRGB(color, rgb_comp, ryb_comp)


def ClassThiada():
    color = colorchooser.askcolor(title="Выберите цвет")
    if color[1] is not None:
        rgb_color = list(map(int, color[0]))
        ryb_color = rgb2ryb(rgb_color)
        rgb_comp1, rgb_comp2 = clas_thiad_rgb(rgb_color[0], rgb_color[1], rgb_color[2])
        ryb_comp1, ryb_comp2 = clas_thiad_ryb(ryb_color[0], ryb_color[1], ryb_color[2])
        print(color, rgb_comp1, ryb_comp1, rgb_comp2, ryb_comp2)
        ReturningColorRGB(color, rgb_comp1, ryb_comp1, rgb_comp2, ryb_comp2)


def AnalogThiada():
    color = colorchooser.askcolor(title="Выберите цвет")
    if color[1] is not None:
        rgb_color = list(map(int, color[0]))
        ryb_color = rgb2ryb(rgb_color)
        rgb_comp1, rgb_comp2 = analog_thiad_rgb(rgb_color[0], rgb_color[1], rgb_color[2])
        ryb_comp1, ryb_comp2 = analog_thiad_ryb(ryb_color[0], ryb_color[1], ryb_color[2])
        ReturningColorRGB(color, rgb_comp1, ryb_comp1, rgb_comp2, ryb_comp2)


def ContrasThiada():
    color = colorchooser.askcolor(title="Выберите цвет")
    if color[1] is not None:
        rgb_color = list(map(int, color[0]))
        ryb_color = rgb2ryb(rgb_color)
        rgb_comp1, rgb_comp2 = contr_thiad_rgb(rgb_color[0], rgb_color[1], rgb_color[2])
        ryb_comp1, ryb_comp2 = contr_thiad_ryb(ryb_color[0], ryb_color[1], ryb_color[2])
        ReturningColorRGB(color, rgb_comp1, ryb_comp1, rgb_comp2, ryb_comp2)


def Rectangle():
    color1 = colorchooser.askcolor(title="Выберите цвет")
    color2 = colorchooser.askcolor(title="Выберите цвет")
    if color1[1] is not None and color2[1] is not None:
        rgb_color1 = list(map(int, color1[0]))
        rgb_color2 = list(map(int, color2[0]))
        ryb_color1 = rgb2ryb(rgb_color1)
        ryb_color2 = rgb2ryb(rgb_color2)
        ReturningColorRGB4recta(color1, color2, rgb_color1, rgb_color2, ryb_color1, ryb_color2)


def Sque():
    color = colorchooser.askcolor(title="Выберите цвет")
    if color[1] is not None:
        rgb_color = list(map(int, color[0]))
        ryb_color = rgb2ryb(rgb_color)
        rgb_comp1, rgb_comp2, rgb_comp3 = squer_rgb(rgb_color[0], rgb_color[1], rgb_color[2])
        ryb_comp1, ryb_comp2, ryb_comp3 = squer_ryb(ryb_color[0], ryb_color[1], ryb_color[2])
        ReturningColorRGB4sque(color, rgb_comp1, rgb_comp2, rgb_comp3, ryb_comp1, ryb_comp2, ryb_comp3)


"""ГЛАВНОЕ ОКНО"""

window = tk.Tk()
window.title("Finder Colors")
window.geometry("1224x768")

frame_title = tk.Frame(window, width=1224, height=50, bg="#f0f0f0")
frame_title.place(relwidth=1, height=90)

frame_methods = tk.Frame(window, width=1224, height=100, bg="#f0f0f0")
frame_methods.place(y=90, relwidth=1, height=350)

frame_result = tk.Frame(window, width=1224, height=100, bg="#f0f0f0")
frame_result.place(y=350, relwidth=1, height=400)

"""РАСПОЛОЖЕНИЕ ТИТУЛА"""
frameCnt = 60
title_gif = [
    tk.PhotoImage(
        file=os.path.join(image_dir, "title.gif"), format="gif -index %i" % (i)
    )
    for i in range(frameCnt)
]


def update(ind):
    frame = title_gif[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    l_title_name.configure(image=frame)
    window.after(100, update, ind)


l_title_name = tk.Label(frame_title)
l_title_name.pack()
window.after(0, update, 0)

l_title_descrip = tk.Label(
    frame_title, text="программа для подбора цветов и генерации цветовых схем"
)
l_title_descrip.pack()

"""РАСПОЛОЖЕНИЕ МЕТОДОВ"""
image_opposite = ImageTk.PhotoImage(
    Image.open(os.path.join(image_dir, "opposite.jpeg")).resize((120, 130))
)
l_opposite = tk.Label(frame_methods, image=image_opposite)
l_opposite.place(x=0, y=0)
radbut_opposite = tk.Button(frame_methods, text="Выбери меня", command=opposite)
radbut_opposite.place(x=0, y=140)

image_classic_thiada = ImageTk.PhotoImage(
    Image.open(os.path.join(image_dir, "classic_thiada.jpeg")).resize((120, 130))
)
l_classic_thiada = tk.Label(frame_methods, image=image_classic_thiada)
l_classic_thiada.place(x=120, y=0)
radbut_classic_thiada = tk.Button(
    frame_methods, text="Выбери меня", command=ClassThiada
)
radbut_classic_thiada.place(x=120, y=140)

image_analog_thriada = ImageTk.PhotoImage(
    Image.open(os.path.join(image_dir, "analog_thriada.jpeg")).resize((120, 130))
)
l_analog_thriada = tk.Label(frame_methods, image=image_analog_thriada)
l_analog_thriada.place(x=240, y=0)
radbut_analog_thriada = tk.Button(
    frame_methods, text="Выбери меня", command=AnalogThiada
)
radbut_analog_thriada.place(x=240, y=140)

image_contrast_thriada = ImageTk.PhotoImage(
    Image.open(os.path.join(image_dir, "contrast_thriada.jpeg")).resize((120, 130))
)
l_contrast_thriada = tk.Label(frame_methods, image=image_contrast_thriada)
l_contrast_thriada.place(x=360, y=0)
radbut_contrast_thriada = tk.Button(
    frame_methods, text="Выбери меня", command=ContrasThiada
)
radbut_contrast_thriada.place(x=360, y=140)

image_rectangle = ImageTk.PhotoImage(
    Image.open(os.path.join(image_dir, "rectangle.jpeg")).resize((120, 130))
)
l_rectangle = tk.Label(frame_methods, image=image_rectangle)
l_rectangle.place(x=480, y=0)
radbut_rectangle = tk.Button(frame_methods, text="Выбери меня", command=Rectangle)
radbut_rectangle.place(x=480, y=140)

image_square = ImageTk.PhotoImage(
    Image.open(os.path.join(image_dir, "square.jpeg")).resize((120, 130))
)
l_square = tk.Label(frame_methods, image=image_square)
l_square.place(x=600, y=0)
radbut_square = tk.Button(frame_methods, text="Выбери меня", command=Sque)
radbut_square.place(x=600, y=140)

window.mainloop()
