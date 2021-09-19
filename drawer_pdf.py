from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.lib.pagesizes import A4, portrait
import math


def saveA4(f_name, figure, feature, change_orientation):
    can = canvas.Canvas(f_name, bottomup=0)
    can.setPageSize(portrait(A4))
    if figure == 'cub':
        paint_cub(can, feature, change_orientation)
    elif figure == 'par_r':
        paint_par_r(can, feature, change_orientation)
    elif figure == 'par_s':
        paint_par_s(can, feature, change_orientation)
    elif figure == 'par_i':
        paint_par_i(can, feature, change_orientation)
    elif figure == 'pri_sr':
        paint_pri_sr(can, feature, change_orientation)
    elif figure == 'pyr_r':
        paint_pyr_r(can, feature, change_orientation)
    elif figure == 'con_full_less':
        paint_con_full_less(can, feature, change_orientation)
    elif figure == 'con_full_more':
        paint_con_full_more(can, feature, change_orientation)
    elif figure == 'con_trun_less':
        paint_con_trun_less(can, feature, change_orientation)
    elif figure == 'con_trun_more':
        paint_con_trun_more(can, feature, change_orientation)
    elif figure == 'cyl':
        paint_cyl(can, feature, change_orientation)
    elif figure == 'ico':
        paint_ico(can, feature, change_orientation)
    elif figure == 'oct':
        paint_oct(can, feature, change_orientation)
    elif figure == 'dod':
        paint_dod(can, feature, change_orientation)
    can.showPage()
    can.save()


def paint_cub(can, feature, change_orientation):
    cub_side = feature[0]
    points_x = [0, cub_side, cub_side, cub_side, 2*cub_side, 3*cub_side]
    points_y = [cub_side, 0, cub_side, 2*cub_side, cub_side, cub_side]
    if not change_orientation:
        p_cube(can, points_x, points_y, cub_side)
    else:
        p_cube(can, points_y, points_x, cub_side)


def p_cube(can, x, y, cub_side):
    can.rect((1+x[0])*cm, (1 + y[0])*cm, cub_side*cm, cub_side*cm)
    can.rect((1 + x[1])*cm, (1+y[1])*cm, cub_side*cm, cub_side*cm)
    can.rect((1 + x[2])*cm, (1 + y[2])*cm, cub_side*cm, cub_side*cm)
    can.rect((1 + x[3])*cm, (1 + y[3])*cm, cub_side*cm, cub_side*cm)
    can.rect((1 + x[4])*cm, (1 + y[4])*cm, cub_side*cm, cub_side*cm)
    can.rect((1 + x[5])*cm, (1 + y[5])*cm, cub_side*cm, cub_side*cm)


def paint_par_r(can, feature, change_orientation):
    a = feature[0]
    b = feature[1]
    c = feature[2]
    points_x = [0, a, a, a, a+b, 2*a+b]
    points_y = [a, 0, a, a+c, a, a]
    size_x = [a, b, b, b, a, b]
    size_y = [c, a, c, a, c, c]
    if not change_orientation:
        p_par_r(can, points_x, points_y, size_x, size_y)
    else:
        p_par_r(can, points_y, points_x, size_y, size_x)


def p_par_r(can, x, y, s_x, s_y):
    can.rect((1+x[0])*cm, (1 + y[0])*cm, s_x[0]*cm, s_y[0]*cm)
    can.rect((1+x[1])*cm, (1 + y[1])*cm, s_x[1]*cm, s_y[1]*cm)
    can.rect((1+x[2])*cm, (1 + y[2])*cm, s_x[2]*cm, s_y[2]*cm)
    can.rect((1+x[3])*cm, (1 + y[3])*cm, s_x[3]*cm, s_y[3]*cm)
    can.rect((1+x[4])*cm, (1 + y[4])*cm, s_x[4]*cm, s_y[4]*cm)
    can.rect((1+x[5])*cm, (1 + y[5])*cm, s_x[5]*cm, s_y[5]*cm)


def paint_par_s(can, feature, change_orientation):
    a = feature[0]
    b = feature[1]
    c = feature[2]
    h = feature[3]
    a_eps = feature[4]
    points_x = [0, b, b+a, 2*b+a, b, b+a_eps, b+a_eps+a, b+a, b, b+a_eps, b+a_eps+a, b+a]
    points_y = [h, h, h, h, h, 0, 0, h, h+c, 2*h+c, 2*h+c, h+c]
    size_x = [b, a, b, a]
    size_y = [c, c, c, c]
    if not change_orientation:
        p_par_s(can, points_x, points_y, size_x, size_y)
    else:
        p_par_s(can, points_y, points_x, size_y, size_x)


def p_par_s(can, x, y, s_x, s_y):
    can.rect((1+x[0])*cm, (1+y[0])*cm, s_x[0]*cm, s_y[0]*cm)
    can.rect((1+x[1])*cm, (1+y[1])*cm, s_x[1]*cm, s_y[1]*cm)
    can.rect((1+x[2])*cm, (1+y[2])*cm, s_x[2]*cm, s_y[2]*cm)
    can.rect((1+x[3])*cm, (1+y[3])*cm, s_x[3]*cm, s_y[3]*cm)
    poly1 = can.beginPath()
    poly1.moveTo((1+x[4])*cm, (1+y[4])*cm)
    poly1.lineTo((1+x[5])*cm, (1+y[5])*cm)
    poly1.lineTo((1+x[6])*cm, (1+y[6])*cm)
    poly1.lineTo((1+x[7])*cm, (1+y[7])*cm)
    poly1.lineTo((1+x[4])*cm, (1+y[4])*cm)
    poly1.close()
    can.drawPath(poly1)
    poly2 = can.beginPath()
    poly2.moveTo((1+x[8])*cm, (1+y[8])*cm)
    poly2.lineTo((1+x[9])*cm, (1+y[9])*cm)
    poly2.lineTo((1+x[10])*cm, (1+y[10])*cm)
    poly2.lineTo((1+x[11])*cm, (1+y[11])*cm)
    poly2.lineTo((1+x[8])*cm, (1+y[8])*cm)
    poly2.close()
    can.drawPath(poly2)


def paint_par_i(can, feature, change_orientation):
    a = feature[0]
    h1 = feature[3]
    h2 = feature[4]
    h4 = feature[5]
    h5 = feature[6]
    h6 = feature[7]
    w1 = feature[8]
    w2 = feature[9]
    w4 = feature[10]
    w5 = feature[11]
    w6 = feature[12]
    points_x = [0, w1, w1+a, a, w1, w1+w2, w1+w2+a, w1+a, w1+w2, w2, w2 + a, w1+w2+a, w1 + a, w1+w2+a, w1+w2+w4+a, w1 + w4 + a, w1 + w4+a, w1+w2+w4+a, w1+w2+w4+w5 + a, w1+w4+w5+a, w1+w4+w5+a, w1+w2+w4+w5+a, w1+w2+w4+w5+w6+a, w1+w4+w5+w6+a]
    points_y = [2*h1+h2, h1+h2, h1+h2, 2*h1+h2, h1+h2, h1, h1, h1+h2, h1, 0, 0, h1, h1+h2, h1, h1+h4, h1+h2+h4, h1+h2+h4, h1+h4, h1+h4+h5, h1+h2+h4+h5, h1+h2+h4+h5, h1+h4+h5, h1+h4+h5-h6, h1+h2+h4+h5-h6]
    if not change_orientation:
        p_par_i(can, points_x, points_y)
    else:
        p_par_i(can, points_y, points_x)


def p_par_i(can, x, y):
    for i in range(6):
        poly1 = can.beginPath()
        poly1.moveTo((1+x[0+4*i])*cm, (1+y[0+4*i])*cm)
        poly1.lineTo((1+x[1+4*i])*cm, (1+y[1+4*i])*cm)
        poly1.lineTo((1 + x[2+4*i])*cm, (1 + y[2+4*i]) * cm)
        poly1.lineTo((1 + x[3+4*i])*cm, (1 + y[3+4*i]) * cm)
        poly1.lineTo((1 + x[0+4*i])*cm, (1 + y[0+4*i]) * cm)
        poly1.close()
        can.drawPath(poly1)


def paint_pri_sr(can, feature, change_orientation):
    n = feature[0]
    a = feature[1]
    c = feature[2]
    angle = feature[3]
    h = feature[4]
    points_x = []
    points_y = []
    size_x = []
    size_y = []
    for i in range(n):
        points_x.append(a*i)
        points_y.append(h)
        size_x.append(a)
        size_y.append(c)
    x1 = a
    y1 = h
    x2 = 2 * a
    y2 = h + c
    points_x.append(x1)
    points_y.append(y1)
    for i in range(1, n):
        angle_i = math.radians(angle * i - 180 * (i - 1))
        x1 = x1 + a * math.cos(angle_i)
        y1 = y1 - a * math.sin(angle_i)
        points_x.append(x1)
        points_y.append(y1)
    points_x.append(x2)
    points_y.append(y2)
    for i in range(1, n):
        angle_i = math.radians(angle * i - 180 * (i - 1))
        x2 = x2 - a * math.cos(angle_i)
        y2 = y2 + a * math.sin(angle_i)
        points_x.append(x2)
        points_y.append(y2)
    if not change_orientation:
        p_pri_sr(can, points_x, points_y, size_x, size_y, n)
    else:
        p_pri_sr(can, points_y, points_x, size_y, size_x, n)


def p_pri_sr(can, x, y, s_x, s_y, n):
    for i in range(n):
        can.rect((1+x[i])*cm, (1+y[i])*cm, s_x[i]*cm, s_y[i]*cm)
    for i in range(1, 3):
        poly = can.beginPath()
        poly.moveTo((1+x[n*i])*cm, (1+y[n*i])*cm)
        for j in range(1, n):
            poly.lineTo((1+x[n*i+j])*cm, (1+y[n*i+j])*cm)
        poly.lineTo((1+x[n*i])*cm, (1+y[n*i])*cm)
        poly.close()
        can.drawPath(poly)


def paint_pri_ir(can, feature, change_orientation):
    pass


def paint_pri_sw(can, feature, change_orientation):
    pass


def paint_pri_iw(can, feature, change_orientation):
    pass


def paint_pyr_r(can, feature, change_orientation):
    n = feature[0]
    a = feature[1]
    angle_base = feature[2]
    l = feature[3]
    h_side = feature[4]
    f_height = feature[5]
    f_width = feature[6]
    points_x= []
    points_y = []
    points_base = []
    xi = f_width / 2 - a / 2
    yi = f_height - h_side
    points_x.append(xi)
    points_y.append(yi)
    angles = []
    for i in range(1, n):
        angle_i = angle_base * i - math.pi * (i - 1)
        angles.append(angle_i)
        xi = xi + a * math.cos(angle_i)
        yi = yi - a * math.sin(angle_i)
        points_x.append(xi)
        points_y.append(yi)
    angles.append(angle_base * n - math.pi * (n - 1))
    for i in range(n):
        if i == n - 1:
            x1 = points_x[n-1]
            y1 = points_y[n-1]
            x2 = points_x[0]
            y2 = points_y[0]
        else:
            x1 = points_x[i]
            y1 = points_y[i]
            x2 = points_x[i+1]
            y2 = points_y[i+1]
        angle_i = math.pi + math.acos(a / 2 / l) + angles[i]
        points_x.append(x1)
        points_y.append(y1)
        points_x.append(x1 - l * math.cos(angle_i))
        points_y.append(y1 + l * math.sin(angle_i))
        points_x.append(x2)
        points_y.append(y2)
    if not change_orientation:
        p_pyr_r(can, points_x, points_y, n)


def p_pyr_r(can, x, y, n):
    poly = can.beginPath()
    poly.moveTo((1+x[0])*cm, (1+y[0])*cm)
    for i in range(1, n):
        poly.lineTo((1+x[i])*cm, (1+y[i])*cm)
    poly.lineTo((1+x[0])*cm, (1+y[0])*cm)
    poly.close()
    can.drawPath(poly)
    for i in range(n):
        poly = can.beginPath()
        poly.moveTo((1+x[n+3*i])*cm, (1+y[n+3*i])*cm)
        poly.lineTo((1+x[n+3*i+1])*cm, (1+y[n+3*i+1])*cm)
        poly.lineTo((1 + x[n + 3 * i + 2]) * cm, (1 + y[n + 3 * i + 2]) * cm)
        poly.lineTo((1+x[n+3*i])*cm, (1+y[n+3*i])*cm)
        poly.close()
        can.drawPath(poly)


def paint_pyr_s(can, feature, change_orientation):
    pass


def paint_con_full_less(can, feature, change_orientation):
    h1 = feature[0]
    w1 = feature[1]
    l = feature[2]
    r = feature[3]
    start_angle = feature[4]
    angle = feature[5]
    points_x = [w1, 0, w1, -l, 2 * l, l, 2 * r]
    points_y = [0, h1, 2 * h1, h1 - l, 2 * l, h1 - r, 2 * r]
    if not change_orientation:
        angles = [-start_angle, -angle]
        p_con_full_less(can, points_x, points_y, angles)
    else:
        angles = [90-start_angle-angle, angle]
        p_con_full_less(can, points_y, points_x, angles)


def p_con_full_less(can, x, y, angles):
    path = can.beginPath()
    path.moveTo((1+x[0])*cm, (1+y[0])*cm)
    path.lineTo((1+x[1])*cm, (1+y[1])*cm)
    path.lineTo((1 + x[2]) * cm, (1 + y[2]) * cm)
    path.arcTo((1+x[3])*cm, (1+y[3])*cm, (1+x[3]+x[4])*cm, (1+y[3]+y[4])*cm, angles[0], angles[1])
    path.ellipse((1 + x[5]) * cm, (1 + y[5]) * cm, x[6] * cm, y[6]*cm)
    path.close()
    can.drawPath(path)


def paint_con_full_more(can, feature, change_orientation):
    h1 = feature[0]
    w1 = feature[1]
    l = feature[2]
    r = feature[3]
    start_angle = feature[4]
    angle = feature[5]
    points_x = [0, w1, 0, w1-l, 2*l, l+w1, 2*r]
    points_y = [h1, l, 2*l-h1, 0, 2*l, l-r, 2*r]
    if not change_orientation:
        angles = [-start_angle, -angle]
        p_con_full_more(can, points_x, points_y, angles)
    else:
        angles = [90-start_angle-angle, angle]
        p_con_full_more(can, points_y, points_x, angles)


def p_con_full_more(can, x, y, angles):
    path = can.beginPath()
    path.moveTo((1+x[0])*cm, (1+y[0])*cm)
    path.lineTo((1+x[1])*cm, (1+y[1])*cm)
    path.lineTo((1+x[2])*cm, (1+y[2])*cm)
    path.arcTo((1+x[3])*cm, (1+y[3])*cm, (1+x[3]+x[4])*cm, (1+y[3]+y[4])*cm, angles[0], angles[1])
    path.ellipse((1+x[5])*cm, (1+y[5])*cm, x[6]*cm, y[6]*cm)
    path.close()
    can.drawPath(path)


def paint_con_trun_less(can, feature, change_operation):
    r = feature[0]
    h1 = feature[1]
    w1 = feature[2]
    h2 = feature[3]
    w2 = feature[4]
    R = feature[5]
    l_cut = feature[6]
    l_full = feature[7]
    start_angle = feature[8]
    angle = feature[9]
    shift = l_cut - 2 * r
    points_x = [w1-shift, w2-shift, -l_cut-shift, -shift+l_cut, w1-shift, -l_full-shift, l_full-shift, 0, 2*r, l_full-shift, 2*R]
    points_y = [0, h1-h2, h1-l_cut, h1+l_cut, 2*h1, h1-l_full, h1+l_full, h1-r, 2*r, h1-R, 2*R]
    if not change_operation:
        angles = [start_angle, angle, -start_angle, -angle]
        p_con_trun_less(can, points_x, points_y, angles)
    else:
        angle = [90+start_angle+angle, -angle, 90-start_angle-angle, angle]
        p_con_trun_less(can, points_y, points_x, angle)


def p_con_trun_less(can, x, y, angles):
    path = can.beginPath()
    path.moveTo((1+x[0])*cm, (1+y[0])*cm)
    path.lineTo((1+x[1])*cm, (1+y[1])*cm)
    path.arcTo((1+x[2])*cm, (1+y[2])*cm, (1+x[3])*cm, (1+y[3])*cm, angles[0], angles[1])
    path.lineTo((1+x[4])*cm,(1+y[4])*cm)
    path.arcTo((1+x[5])*cm, (1+y[5])*cm, (1+x[6])*cm, (1+y[6])*cm, angles[2], angles[3])
    path.ellipse((1+x[7])*cm, (1+y[7])*cm, (x[8])*cm, (y[8])*cm)
    path.ellipse((1+x[9])*cm, (1+y[9])*cm,(x[10])*cm, (y[10])*cm)
    path.close()
    can.drawPath(path)


def paint_con_trun_more(can, feature, change_operation):
    w0 = feature[0]
    h1 = feature[1]
    w2 = feature[2]
    h2 = feature[3]
    r = feature[4]
    R = feature[5]
    l_cut = feature[6]
    l_full = feature[7]
    start_angle = feature[8]
    angle = feature[9]
    points_x = [0, w2, w0-l_cut, w0+l_cut, 0, w0-l_full, w0+l_full, w0+l_cut-2*r, 2*r, w0+l_full, 2*R]
    points_y = [2*l_full-h1, 2*l_full-h2, l_full-l_cut, l_full+l_cut, h1, 0, 2*l_full, l_full-r, 2*r, l_full-R, 2*R]
    if not change_operation:
        angles = [-start_angle, -angle, start_angle, angle]
        p_con_trun_more(can, points_x, points_y, angles)
    else:
        angles = [90-start_angle-angle, angle, 90+start_angle+angle, -angle]
        p_con_trun_more(can, points_y, points_x, angles)


def p_con_trun_more(can,x, y, angles):
    path = can.beginPath()
    path.moveTo((1+x[0])*cm, (1+y[0])*cm)
    path.lineTo((1+x[1])*cm, (1+y[1])*cm)
    path.arcTo((1+x[2])*cm, (1+y[2])*cm, (1+x[3])*cm, (1+y[3])*cm, angles[0], angles[1])
    path.lineTo((1+x[4])*cm, (1+y[4])*cm)
    path.arcTo((1+x[5])*cm, (1+y[5])*cm, (1+x[6])*cm, (1+y[6])*cm, angles[2], angles[3])
    path.ellipse((1+x[7])*cm, (1+y[7])*cm, (x[8])*cm, (y[8])*cm)
    path.ellipse((1+x[9])*cm, (1+y[9])*cm, (x[10])*cm, (y[10])*cm)
    path.close()
    can.drawPath(path)


def paint_cyl(can, feature, change_orientation):
    d = feature[0]
    h = feature[1]
    c = feature[2]
    points_x = [0, d, 0, 0, c]
    points_y = [0, d, d+h, d, h]
    if not change_orientation:
        p_cyl(can, points_x, points_y)
    else:
        p_cyl(can, points_y, points_x)


def p_cyl(can, x, y):
    cyl = can.beginPath()
    cyl.ellipse((1+x[0])*cm, (1+y[0])*cm, x[1]*cm, y[1]*cm)
    cyl.ellipse((1 + x[2]) * cm, (1 + y[2]) * cm, x[1] * cm, y[1] * cm)
    cyl.close()
    can.drawPath(cyl)
    can.rect((1+x[3])*cm, (1+y[3])*cm, x[4]*cm, y[4]*cm)


def paint_dod(can, feature, change_orientation):
    a = feature[0]
    angle = feature[1]
    xi1 = feature[2]
    yi1 = feature[3]
    xi2 = 2 * xi1 + 2 * a + a * math.sin(angle - math.pi / 2)
    yi2 = yi1 - a * math.cos(angle - math.pi / 2)
    points_x = [[xi1], [xi2]]
    points_y = [[yi1], [yi2]]
    for i in range(1, 6):
        angle_i = angle * i - math.pi * (i - 1)
        xj1 = xi1
        yj1 = yi1
        xj2 = xi2
        yj2 = yi2
        points_x.append([xj1])
        points_x.append([xj2])
        points_y.append([yj1])
        points_y.append([yj2])
        for j in range(1, 6):
            angle_j = -angle_i - angle * j - math.pi * j
            xj1 = xj1 - a * math.cos(angle_j)
            yj1 = yj1 - a * math.sin(angle_j)
            points_x[i*2].append(xj1)
            points_y[i*2].append(yj1)
            xj2 = xj2 - a * math.cos(angle_j)
            yj2 = yj2 + a * math.sin(angle_j)
            points_x[1+i*2].append(xj2)
            points_y[1+i*2].append(yj2)
        xi1 = xi1 + a * math.cos(angle_i)
        yi1 = yi1 - a * math.sin(angle_i)
        points_x[0].append(xi1)
        points_y[0].append(yi1)
        xi2 = xi2 + a * math.cos(angle_i)
        yi2 = yi2 + a * math.sin(angle_i)
        points_x[1].append(xi2)
        points_y[1].append(yi2)
    if not change_orientation:
        p_dod(can, points_x, points_y)
    else:
        p_dod(can, points_y, points_x)


def p_dod(can, x, y):
    for i in range(12):
        poly = can.beginPath()
        poly.moveTo((1+x[i][0])*cm, (1+y[i][0])*cm)
        for j in range(1, 5):
            poly.lineTo((1+x[i][j])*cm, (1+y[i][j])*cm)
        poly.lineTo((1+x[i][j])*cm, (1+y[i][j])*cm)
        poly.close()
        can.drawPath(poly)


def paint_oct(can, feature, change_orientation):
    w1 = feature[0]
    h1 = feature[1]
    points_x = [[w1, 0, w1], [w1, w1, 2*w1], [w1, 2 * w1, 2 * w1], [w1, 2*w1, w1], [0, 0, w1], [w1, 2 * w1, 2 * w1], [2 * w1, 3 * w1, 2 * w1], [2 * w1, 2 * w1, w1]]
    points_y = [[3 * h1, 2 * h1,  h1], [3 * h1, h1, 2 * h1], [3 * h1, 2 * h1, 4 * h1], [3 * h1, 4 * h1, 5 * h1], [2 * h1, 0, h1], [h1, 0, 2*h1], [2 * h1, 3 * h1, 4 * h1], [4 * h1, 6 * h1, 5 * h1]]
    if not change_orientation:
        p_oct(can, points_x, points_y)
    else:
        p_oct(can, points_y, points_x)


def p_oct(can, x, y):
    for i in range(8):
        path = can.beginPath()
        path.moveTo((1+x[i][0])*cm, (1+y[i][0])*cm)
        path.lineTo((1+x[i][1])*cm, (1+y[i][1])*cm)
        path.lineTo((1+x[i][2])*cm, (1+y[i][2])*cm)
        path.lineTo((1+x[i][0])*cm, (1+y[i][0])*cm)
        path.close()
        can.drawPath(path)


def paint_ico(can, feature, change_orientation):
    w = feature[0]
    h = feature[1]
    points_x = []
    points_y = []
    for i in range(5):
        points_x.append([2 * w * i, w + 2 * w * i, 2 * w + 2 * w * i])
        points_y.append([h, 0, h])
        points_x.append([2 * w * i, w + 2 * w * i,  2 * w + 2 * w * i])
        points_y.append([h, 2*h, h])
        points_x.append([3 * w + 2 * w * i, w + 2 * w * i, 2 * w + 2 * w * i])
        points_y.append([2 * h, 2 * h, h])
        points_x.append([3 * w + 2 * w * i, w + 2 * w * i, 2 * w + 2 * w * i])
        points_y.append([2 * h, 2 * h, 3 * h])
    if not change_orientation:
        p_ico(can, points_x, points_y)
    else:
        p_ico(can, points_y, points_x)


def p_ico(can, x, y):
    for i in range(20):
        tr = can.beginPath()
        tr.moveTo((1+x[i][0])*cm, (1+y[i][0])*cm)
        tr.lineTo((1+x[i][1])*cm, (1+y[i][1])*cm)
        tr.lineTo((1+x[i][2])*cm, (1+y[i][2])*cm)
        tr.lineTo((1+x[i][0])*cm, (1+y[i][0])*cm)
        tr.close()
        can.drawPath(tr)

