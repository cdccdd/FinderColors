"""Функция принимает кортедж из 3х элементов RGB. пример: my_color = (0, 255, 0)"""


# Преобразуйте красно-зелено-синюю систему в красно-желто-синюю систему.
def rgb2ryb(x):
    red = x[0]
    green = x[1]
    blue = x[2]
    # Убрать белизну с цвета.
    white = min(red, green, blue)
    red -= white
    green -= white
    blue -= white
    mg = max(red, green, blue)
    # Получите желтый из красного + зеленого.
    yellow = min(red, green)
    red -= yellow
    green -= yellow
    # Если это неудачное преобразование сочетает синий и зеленый, то разрежьте каждый пополам, чтобы сохранить максимальный диапазон значения.
    if blue+green !=0 :
        blue /= 2
        green /= 2
    # Перераспределите оставшийся зеленый цвет.
    yellow += green
    blue += green
    # Нормализовать до значений.
    my = max(red, yellow, blue)
    if my !=0 :
        n = mg / my
        red *= n
        yellow *= n
        blue *= n
    # Добавьте белый цвет обратно.
    red += white
    yellow += white
    blue += white
    # И верните RYB, набранный соответствующим образом.
    return int(red), int(yellow), int(blue)

# Преобразуйте красно-желто-синюю систему в красно-зелено-синюю систему.
def ryb2rgb(x):
    red = x[0]
    yellow = x[1]
    blue = x[2]

    white = min(red, yellow, blue)
    red -= white
    yellow -= white
    blue -= white
    my = max(red, yellow, blue)

    green = min(yellow, blue)
    yellow -= green
    blue -= green

    if blue+green !=0 :
        blue *= 2
        green *= 2

    red += yellow
    green += yellow

    mg = max(red, green, blue)
    if mg !=0 :
        n = my / mg
        red *= n
        green *= n
        blue *= n

    red += white
    green += white
    blue += white

    return int(red), int(green), int(blue)
