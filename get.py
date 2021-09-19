import math
import dialogs


# функция вызывается при нажатии кнопки

# если заполнены не все поля ввода
def showdialog(d_text):
    d = dialogs.D_empty(d_text)
    d.show()
    d.exec_()


# зависимости от id фигуры и набора характеристик находим недостающие величины и строим нужную фигуру
def show_draw(screen):
    global fea, f_height, f_width, figure
    fea = []  # набор характеристик, нужных для развертки.
    # переходим к обработке данных из окна в зависимости от id
    if screen.figure == 'cub':
        find_for_cub(screen)
    elif screen.figure == 'par':
        find_for_par(screen)
    elif screen.figure == 'pri':
        find_for_pri(screen)
    elif screen.figure == 'pyr':
        find_for_pyr(screen)
    elif screen.figure == 'con_full':
        find_for_con_full(screen)
    elif screen.figure == 'con_trun':
        find_for_con_trun(screen)
    elif screen.figure == 'cyl':
        find_for_cyl(screen)
    elif screen.figure == 'poly_reg':
        find_for_poly_reg(screen)
    d = dialogs.D_draw(figure, fea, f_width, f_height)  # вызов диалогового окна
    d.show()
    d.exec_()


# куб
def find_for_cub(screen):
    global fea, f_height, f_width, figure
    side = float(screen.edits[0].text())
    f_height = 3 * side
    f_width = 4 * side
    figure = 'cub'
    fea.append(side)


# параллелепипед
def find_for_par(screen):
    global fea, f_height, f_width, figure
    if screen.f_char == 'par_r':  # прямоугольный
        a = float(screen.edits[0].text())
        b = float(screen.edits[1].text())
        c = float(screen.edits[2].text())
        fea = [a, b, c]
        figure = 'par_r'
        f_height = 2 * a + c
        f_width = 2 * a + 2 * b
    if screen.f_char == 'par_s':  # прямой
        a = float(screen.edits[0].text())
        b = float(screen.edits[1].text())
        c = float(screen.edits[2].text())
        alf = int(screen.edits[3].text())
        angle = min(alf, 180 - alf)
        angle = math.radians(angle)
        h = b * math.sin(angle)
        a_eps = b * math.cos(angle)
        fea = [a, b, c, h, a_eps]
        figure = 'par_s'
        f_height = 2 * h + c
        f_width = 2 * a + 2 * b
    if screen.f_char == 'par_i':
        a = float(screen.edits[0].text())
        b = float(screen.edits[1].text())
        c = float(screen.edits[2].text())
        alf1 = int(screen.edits[3].text())
        alf2 = int(screen.edits[4].text())
        alf3 = int(screen.edits[5].text())
        angle1 = min(alf1, 180 - alf1)
        angle2 = max(alf2, 180 - alf2)
        angle3 = min(alf3, 180 - alf3)
        angle4 = angle2 - angle3
        angle5 = 2 * angle2 - 180
        angle6 = 180 - angle2 - angle3
        angle1 = math.radians(angle1)
        angle2 = math.radians(angle2)
        angle4 = math.radians(angle4)
        angle5 = math.radians(angle5)
        angle6 = math.radians(angle6)
        h1 = b * math.sin(angle1)
        h2 = c * math.sin(angle2)
        h4 = b * math.sin(angle4)
        h5 = a * math.sin(angle5)
        h6 = b * math.sin(angle6)
        w1 = b * math.cos(angle1)
        w2 = -c * math.cos(angle2)
        w4 = b * math.cos(angle4)
        w5 = a * math.cos(angle5)
        w6 = b * math.cos(angle6)
        f_height = max(2 * h1 + h2, h1 + h2 + h4 + h5, h1 + h2 + h4 + h5 - h6)
        f_width = w1 + w2 + w4 + w5 + w6 + a
        fea = [a, b, c, h1, h2, h4, h5, h6, w1, w2, w4, w5, w6]
        figure = 'par_i'


# призма
def find_for_pri(screen):
    global fea, f_height, f_width, figure
    if screen.f_char == 'pri_sr':
        n = screen.spin3_1.value()
        a = float(screen.edits[0].text())
        c = float(screen.edits[1].text())
        angle = (n - 2) * 180 / n
        if n % 2 == 1:
            h = a / 2 / math.sin(math.radians(180 / n))
            h += a / 2 / math.tan(math.radians(180 / n))
        else:
            h = a / math.tan(math.radians(180 / n))
        f_width = n * a
        w = a / 2 / math.sin(math.radians(180 / n))
        if a < w:
            f_width += w - a
        f_height = 2 * h + c
        fea = [n, a, c, angle, h]
        figure = 'pri_sr'


# пирамида
def find_for_pyr(screen):
    global fea, f_height, f_width, figure
    if screen.f_char == 'pyr_r':
        n = screen.spin3_1.value()
        a = float(screen.edits[0].text())
        angle_base = (n - 2) * math.pi / n
        R = a / (2 * math.sin(math.pi / n))
        if screen.combox3_2.currentIndex() == 0:
            h = float(screen.edits[1].text())
            l = math.sqrt(h ** 2 + R ** 2)
        elif screen.combox3_2.currentIndex() == 1:
            l = float(screen.edits[1].text())
        r = a / (2 * math.tan(math.pi / n))
        h_side = math.sqrt(l ** 2 - a ** 2 / 4)
        if n % 4 == 0:
            f_height = 2 * r + 2 * h_side
            f_width = 2 * r + 2 * h_side
        elif n % 2 == 0:
            f_height = 2 * h_side + 2 * r
            n_4 = math.ceil(n / 4)
            f_width = 2 * l * math.fabs(
                math.cos(math.pi + math.acos(a / 2 / l) + angle_base * n_4 - math.pi * (n_4 - 1)))
            f_width += 2 * R
        else:
            n_4 = n // 4
            n_2 = math.floor(n / 2)
            f_height = R + r + h_side + l * math.fabs(math.cos(math.pi - angle_base / 2 - math.acos(a / 2 / l)))
            if n_4 == 0:
                f_width = 2 * l * math.fabs(
                    math.cos(math.pi + math.acos(a / 2 / l) + angle_base * (n_4 + 1) - math.pi * n_4))
                f_width += a
            else:
                w1 = 2 * l * math.fabs(
                    math.cos(math.pi + math.acos(a / 2 / l) + angle_base * (n_4 + 1) - math.pi * (n_4)))
                for i in range(n_4 + 1, n_2 + 1):
                    w1 += 2 * a * math.fabs(math.cos(angle_base * i - math.pi * (i - 1)))
                w2 = 2 * l * math.fabs(
                    math.cos(math.pi + math.acos(a / 2 / l) + angle_base * (n_4) - math.pi * (n_4 - 1)))
                for i in range(1, n_4):
                    w2 += 2 * a * math.fabs(math.cos(angle_base * i - math.pi * (i - 1)))
                w2 += a
                f_width = max(w1, w2)
        fea = [n, a, angle_base, l, h_side, f_height, f_width]
        figure = 'pyr_r'


# конус
def find_for_con_full(screen):
    global fea, f_height, f_width, figure
    if screen.f_char == 'con_lr':
        l = float(screen.edits[0].text())
        r = float(screen.edits[1].text())
    elif screen.f_char == 'con_hr':
        h = float(screen.edits[0].text())
        r = float(screen.edits[1].text())
        l = math.sqrt(h ** 2 + r ** 2)
    elif screen.f_char == 'con_lh':
        l = float(screen.edits[0].text())
        h = float(screen.edits[1].text())
        r = math.sqrt(l ** 2 - h ** 2)
    angle = 2 * math.pi * r / l
    if angle <= math.pi:
        h1 = l * math.sin(angle / 2)
        w1 = l * math.cos(angle / 2)
        f_height = 2 * h1
        f_width = l + 2 * r
        st_angle = - math.degrees(angle / 2)
        fea = [h1, w1, l, r, st_angle, math.degrees(angle)]
        figure = 'con_full_less'
    else:
        angle1 = (angle - math.pi) / 2
        w1 = l * math.sin(angle1)
        h1 = l - l * math.cos(angle1)
        f_width = w1 + l + 2 * r
        f_height = 2 * l
        st_angle = -90 - math.degrees(angle1)
        fea = [h1, w1, l, r, st_angle, math.degrees(angle)]
        figure = 'con_full_more'


# конус усеченный
def find_for_con_trun(screen):
    global fea, f_height, f_width, figure
    if screen.f_char == 'con_lr':
        l = float(screen.edits[0].text())
        r = float(screen.edits[1].text())
        R = float(screen.edits[2].text())
        if r > R:
            i = r
            r = R
            R = r
        l_full = l * R / (R - r)
        l_cut = l_full - l
    elif screen.f_char == 'con_hr':
        h = float(screen.edits[0].text())
        r = float(screen.edits[1].text())
        R = float(screen.edits[2].text())
        if r > R:
            i = r
            r = R
            R = r
        h_full = h * R / (R - r)
        h_cut = h_full - h
        l_full = math.sqrt(h_full ** 2 + R ** 2)
        l_cut = math.sqrt(h_cut ** 2 + r ** 2)
    angle = 2 * math.pi * R / l_full
    if angle <= math.pi:
        h1 = l_full * math.sin(angle / 2)
        w1 = l_full * math.cos(angle / 2)
        h2 = l_cut * math.sin(angle / 2)
        w2 = l_cut * math.cos(angle / 2)
        f_height = 2 * h1
        f_width = max(2 * r, l_cut) + l_full - l_cut + 2 * R
        st_angle = - math.degrees(angle / 2)
        fea = [r, h1, w1, h2, w2, R, l_cut, l_full, st_angle, math.degrees(angle)]
        figure = 'con_trun_less'
    else:
        angle1 = (angle - math.pi) / 2
        w0 = l_full * math.sin(angle1)
        h0 = l_full * math.cos(angle1)
        h1 = l_full-h0
        h2 = l_full- l_cut*math.cos(angle1)
        w2 = w0-l_cut*math.sin(angle1)
        f_width = w0 + l_full + 2 * R
        f_height = 2 * l_full
        st_angle = -90 - math.degrees(angle1)
        fea = [w0, h1, w2, h2, r, R, l_cut, l_full, st_angle, math.degrees(angle)]
        figure = 'con_trun_more'


# цилиндр
def find_for_cyl(screen):
    global fea, f_height, f_width, figure
    figure = 'cyl'
    if screen.f_char == 'cyl_hr':
        h = float(screen.edits[0].text())
        r = float(screen.edits[1].text())
        d = 2 * r
        c = 2 * math.pi * r
        fea = [d, h, c]
    if screen.f_char == 'cyl_hc':
        h = float(screen.edits[0].text())
        c = float(screen.edits[1].text())
        d = c / math.pi
        fea = [d, h, c]
    f_width = c
    f_height = h + 2 * d


# правильные многогранники
def find_for_poly_reg(screen):
    global fea, f_height, f_width, figure
    a = float(screen.edits[0].text())
    if screen.f_char == 'poly_reg_tet':
        n = 3
        angle_base = (n - 2) * math.pi / n
        R = a / (2 * math.sin(math.pi / n))
        l = a
        r = a / (2 * math.tan(math.pi / n))
        h_side = math.sqrt(l ** 2 - a ** 2 / 4)
        n_4 = n // 4
        f_height = R + r + h_side + l * math.fabs(math.cos(math.pi - angle_base / 2 - math.acos(a / 2 / l)))
        f_width = 2 * l * math.fabs(
            math.cos(math.pi + math.acos(a / 2 / l) + angle_base * (n_4 + 1) - math.pi * n_4))
        f_width += a
        fea = [n, a, angle_base, l, h_side, f_height, f_width]
        figure = 'pyr_r'
    elif screen.f_char == 'poly_reg_gec':
        f_height = 3 * a
        f_width = 4 * a
        figure = 'cub'
        fea = [a]
    elif screen.f_char == 'poly_reg_oct':
        w1 = a * math.sin(math.pi / 3)
        h1 = a * math.cos(math.pi / 3)
        f_width = 3 * w1
        f_height = 6 * h1
        fea = [w1, h1]
        figure = 'oct'
    elif screen.f_char == 'poly_reg_dod':
        angle = 3 * math.pi / 5
        r = a / 2 / math.tan(math.pi / 5)
        R = a / 2 / math.sin(math.pi / 5)
        h1 = a * math.sin(angle)
        x1 = 2 * a * math.sin(angle / 2)
        y1 = r + R + h1
        figure = 'dod'
        fea = [a, angle, x1, y1]
        f_height = 2 * r + 2 * R + h1
        f_width = 3 * a + 3 * x1 + a * math.sin(angle - math.pi / 2)
    elif screen.f_char == 'poly_reg_ico':
        w = a / 2
        h = a * math.sin(math.pi / 3)
        fea = [w, h]
        figure = 'ico'
        f_width = 11 * w
        f_height = 3 * h
