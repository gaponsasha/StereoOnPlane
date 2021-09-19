from PyQt5.Qt import *
import math


class Drawer(QWidget):  # окно с отрисовкой
    def __init__(self, figure, feature, f_width, f_height):
        # figure - id фигуры; feature - набор вычесленных характеристик
        # f_width - совокупная длина фигуры по оси x, в см
        # f_height - совокупная длина фигуры по оси y, в см
        QWidget.__init__(self)
        self.setAttribute(Qt.WA_StaticContents)
        self.figure = figure
        self.feature = feature
        self.im_width = 500
        self.im_height = 500
        factor_width = (self.im_width - 10) / f_width
        factor_height = (self.im_height - 10) / f_height
        # задаем коэфициент изменения для линейных характеристик,
        if factor_height > factor_width:
            self.coefficient = factor_width  # умножая на него сразу получим нужный размер параметра в пикселях
        else:
            self.coefficient = factor_height
        self.myPenWidth = 5
        self.myPenColor = Qt.black
        self.image = QImage(self.im_width, self.im_height, QImage.Format_RGB32)
        self.path = QPainterPath()
        self.image.fill(Qt.white)

    def saveImage(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save Image", "",
                                                  "PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*) ")
        if filePath == "":
            return
        self.image.save(filePath)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawImage(event.rect(), self.image, self.rect())
        p = QPainter(self.image)
        if self.figure == 'cub':
            self.paint_cub(p)
        elif self.figure == 'par_r':
            self.paint_par_r(p)
        elif self.figure == 'par_s':
            self.paint_par_s(p)
        elif self.figure == 'par_i':
            self.paint_par_i(p)
        elif self.figure == 'pri_sr':
            self.paint_pri_sr(p)
        # other figures
        elif self.figure == 'pyr_r':
            self.paint_pyr_r(p)
        # other figures
        elif self.figure == 'con_full_less':
            self.paint_con_full_less(p)
        elif self.figure == 'con_full_more':
            self.paint_con_full_more(p)
        elif self.figure == 'con_trun_less':
            self.paint_con_trun_less(p)
        elif self.figure == 'con_trun_more':
            self.paint_con_trun_more(p)
        elif self.figure == 'cyl':
            self.paint_cyl(p)
        elif self.figure == 'ico':
            self.paint_ico(p)
        elif self.figure == 'oct':
            self.paint_oct(p)
        elif self.figure == 'dod':
            self.paint_dod(p)
        self.update()

    def paint_cub(self, p):
        cub_side = round(self.feature[0] * self.coefficient)
        p.drawRect(5, 5 + cub_side, cub_side, cub_side)
        p.drawRect(5 + cub_side, 5, cub_side, cub_side)
        p.drawRect(5 + cub_side, 5 + cub_side, cub_side, cub_side)
        p.drawRect(5 + cub_side, 5 + 2 * cub_side, cub_side, cub_side)
        p.drawRect(5 + 2 * cub_side, 5 + cub_side, cub_side, cub_side)
        p.drawRect(5 + 3 * cub_side, 5 + cub_side, cub_side, cub_side)

    def paint_par_r(self, p):
        a = round(self.feature[0] * self.coefficient)
        b = round(self.feature[1] * self.coefficient)
        c = round(self.feature[2] * self.coefficient)
        p.drawRect(5, 5 + a, a, c)
        p.drawRect(5 + a, 5, b, a)
        p.drawRect(5 + a, 5 + a, b, c)
        p.drawRect(5 + a, 5 + a + c, b, a)
        p.drawRect(5 + a + b, 5 + a, a, c)
        p.drawRect(5 + 2 * a + b, 5 + a, b, c)

    def paint_par_s(self, p):
        a = round(self.feature[0] * self.coefficient)
        b = round(self.feature[1] * self.coefficient)
        c = round(self.feature[2] * self.coefficient)
        h = round(self.feature[3] * self.coefficient)
        a_eps = round(self.feature[4] * self.coefficient)
        p.drawRect(5, 5 + h, b, c)
        p.drawRect(5 + b, 5 + h, a, c)
        p.drawRect(5 + b + a, 5 + h, b, c)
        p.drawRect(5 + 2 * b + a, 5+h, a, c)
        points_1 = [QPoint(5 + b, 5 + h), QPoint(5 + b + a_eps, 5), QPoint(5 + b + a_eps + a, 5),
                    QPoint(5 + b + a, 5 + h)]
        poly1 = QPolygon(points_1)
        p.drawPolygon(poly1)
        points_2 = [QPoint(5 + b, 5 + h + c), QPoint(5 + b + a_eps, 5 + 2 * h + c),
                    QPoint(5 + b + a_eps + a, 5 + 2 * h + c), QPoint(5 + b + a, 5 + h + c)]
        poly2 = QPolygon(points_2)
        p.drawPolygon(poly2)

    def paint_par_i(self, p):
        a = round(self.feature[0] * self.coefficient)
        h1 = round(self.feature[3]*self.coefficient)
        h2 = round(self.feature[4]*self.coefficient)
        h4 = round(self.feature[5]*self.coefficient)
        h5 = round(self.feature[6]*self.coefficient)
        h6 = round(self.feature[7]*self.coefficient)
        w1 = round(self.feature[8]*self.coefficient)
        w2 = round(self.feature[9]*self.coefficient)
        w4 = round(self.feature[10]*self.coefficient)
        w5 = round(self.feature[11]*self.coefficient)
        w6 = round(self.feature[12]*self.coefficient)
        points1 = [QPoint(5, 5+2*h1+h2), QPoint(5+w1, 5+h1+h2), QPoint(5+w1+a, 5+h1+h2), QPoint(5+a, 5+2*h1+h2)]
        poly1 = QPolygon(points1)
        p.drawPolygon(poly1)
        points2 = [QPoint(5+w1, 5+h1+h2), QPoint(5+w1+w2, 5+h1), QPoint(5+w1+w2+a, 5+h1), QPoint(5+w1+a, 5+h1+h2)]
        poly2 = QPolygon(points2)
        p.drawPolygon(poly2)
        points3 = [QPoint(5+w1+w2, 5+h1), QPoint(5+w2, 5), QPoint(5+w2 + a, 5), QPoint(5+w1+w2+a, 5+h1)]
        poly3 = QPolygon(points3)
        p.drawPolygon(poly3)
        points4 = [QPoint(5+w1 + a, 5+h1+h2), QPoint(5+w1+w2+a, 5+h1), QPoint(5+w1+w2+w4+a, 5+h1+h4), QPoint(5+w1 + w4 + a, 5+h1+h2+h4)]
        poly4 = QPolygon(points4)
        p.drawPolygon(poly4)
        points5 = [QPoint(5+w1 + w4+a, 5+h1+h2+h4), QPoint(5+w1+w2+w4+a, 5+h1+h4), QPoint(5+w1+w2+w4+w5 + a, 5+h1+h4+h5), QPoint(5+w1+w4+w5+a, 5+h1+h2+h4+h5)]
        poly5 = QPolygon(points5)
        p.drawPolygon(poly5)
        points6 = [QPoint(5+w1+w4+w5+a, 5+h1+h2+h4+h5), QPoint(5+w1+w2+w4+w5+a, 5+h1+h4+h5), QPoint(5+w1+w2+w4+w5+w6+a, 5+h1+h4+h5-h6), QPoint(5+w1+w4+w5+w6+a, 5+h1+h2+h4+h5-h6)]
        poly6 = QPolygon(points6)
        p.drawPolygon(poly6)

    def paint_pri_sr(self, p):
        n = self.feature[0]
        a = round(self.feature[1]*self.coefficient)
        c = round(self.feature[2]*self.coefficient)
        angle = self.feature[3]
        h = round(self.feature[4]*self.coefficient)
        for i in range(n):
            p.drawRect(5+a*i, 5+h, a, c)
        points1 = []
        points2 = []
        x1 = 5+a
        y1 = 5+h
        x2 = 5+2*a
        y2 = 5+h+c
        points1.append(QPoint(x1, y1))
        points2.append(QPoint(x2, y2))
        for i in range(1, n+1):
            angle_i = math.radians(angle*i - 180*(i-1))
            x1 = round(x1 + a*math.cos(angle_i))
            y1 = round(y1 - a*math.sin(angle_i))
            x2 = round(x2 - a*math.cos(angle_i))
            y2 = round(y2 + a*math.sin(angle_i))
            points1.append(QPoint(x1, y1))
            points2.append(QPoint(x2, y2))
        poly1 = QPolygon(points1)
        poly2 = QPolygon(points2)
        p.drawPolygon(poly1)
        p.drawPolygon(poly2)

    def paint_pri_ir(self, p):
        pass

    def paint_pri_sw(self, p):
        pass

    def paint_pri_iw(self, p):
        pass

    def paint_pyr_r(self, p):
        n = self.feature[0]
        a = self.feature[1]*self.coefficient
        angle_base = self.feature[2]
        l = self.feature[3]*self.coefficient
        h_side = self.feature[4]*self.coefficient
        f_height = self.feature[5]*self.coefficient
        f_width = self.feature[6]*self.coefficient
        points_base = []
        xi = 5+f_width/2-a/2
        yi = 5+f_height-h_side
        points_base.append(QPoint(round(xi), round(yi)))
        angles = []
        for i in range(1, n):
            angle_i = angle_base*i-math.pi*(i-1)
            angles.append(angle_i)
            xi = xi + a*math.cos(angle_i)
            yi = yi - a*math.sin(angle_i)
            points_base.append(QPoint(round(xi), round(yi)))
        angles.append(angle_base*n-math.pi*(n-1))
        poly = QPolygon(points_base)
        p.drawPolygon(poly)
        for i in range(n):
            if i == n-1:
                point1 = points_base[n-1]
                point2 = points_base[0]
            else:
                point1 = points_base[i]
                point2 = points_base[i+1]
            angle_i = math.pi+math.acos(a/2/l)+angles[i]
            point3 = QPoint(round(point1.x()-l*math.cos(angle_i)), round(point1.y()+l*math.sin(angle_i)))
            triangle = QPolygon([point1, point3, point2])
            p.drawPolygon(triangle)

    def paint_pyr_s(self, p):
        pass

    def paint_con_full_less(self, p):
        h1 = round(self.feature[0]*self.coefficient)
        w1 = round(self.feature[1]*self.coefficient)
        l = round(self.feature[2]*self.coefficient)
        r = round(self.feature[3]*self.coefficient)
        start_angle = self.feature[4]
        angle = self.feature[5]
        p.drawLine(5, 5+h1, 5+w1, 5)
        p.drawLine(5, 5+h1, 5+w1, 5+2*h1)
        p.drawArc(5-l, 5+h1-l, 2*l, 2*l, start_angle*16, angle*16)
        p.drawEllipse(5+l, 5+h1-r, 2*r, 2*r)

    def paint_con_full_more(self, p):
        h1 = round(self.feature[0] * self.coefficient)
        w1 = round(self.feature[1] * self.coefficient)
        l = round(self.feature[2] * self.coefficient)
        r = round(self.feature[3] * self.coefficient)
        start_angle = self.feature[4]
        angle = self.feature[5]
        p.drawLine(5 + w1, 5 + l, 5, 5 + h1)
        p.drawLine(5 + w1, 5 + l, 5, 5 + 2*l - h1)
        p.drawArc(5 + w1 - l, 5, 2*l, 2*l, start_angle*16, angle*16)
        p.drawEllipse(5 + l + w1, 5 + l - r, 2*r, 2*r)

    def paint_con_trun_less(self, p):
        r = round(self.feature[0]*self.coefficient)
        h1 = round(self.feature[1]*self.coefficient)
        w1 = round(self.feature[2]*self.coefficient)
        h2 = round(self.feature[3]*self.coefficient)
        w2 = round(self.feature[4]*self.coefficient)
        R = round(self.feature[5]*self.coefficient)
        l_cut = round(self.feature[6]*self.coefficient)
        l_full = round(self.feature[7]*self.coefficient)
        start_angle = self.feature[8]
        angle = self.feature[9]
        shift = l_cut-2*r
        p.drawArc(5-l_cut-shift, 5+h1-l_cut, 2*l_cut, 2*l_cut, start_angle*16, angle*16)
        p.drawLine(5+w2-shift, 5+h1-h2, 5+w1-shift, 5)
        p.drawArc(5-l_full-shift, 5+h1-l_full, 2*l_full, 2*l_full, start_angle*16, angle*16)
        p.drawLine(5+w2-shift, 5+h1+h2, 5+w1-shift, 5+2*h1)
        p.drawEllipse(5, 5+h1-r, 2*r, 2*r)
        p.drawEllipse(5+l_full-shift, h1-R, 2*R, 2*R)

    def paint_con_trun_more(self, p):
        w0 = round(self.feature[0]*self.coefficient)
        h1 = round(self.feature[1]*self.coefficient)
        w2 = round(self.feature[2]*self.coefficient)
        h2 = round(self.feature[3]*self.coefficient)
        r = round(self.feature[4]*self.coefficient)
        R = round(self.feature[5]*self.coefficient)
        l_cut = round(self.feature[6]*self.coefficient)
        l_full = round(self.feature[7]*self.coefficient)
        start_angle = self.feature[8]
        angle = self.feature[9]
        p.drawLine(5+w2, 5+h2, 5, 5+h1)
        p.drawArc(5+w0-l_full, 5, 2*l_full, 2*l_full, start_angle*16, angle*16)
        p.drawLine(5, 5+2*l_full-h1, 5+w2, 5+2*l_full-h2)
        p.drawArc(5+w0-l_cut, 5+l_full-l_cut, 2*l_cut, 2*l_cut, start_angle*16, angle*16)
        p.drawEllipse(5+w0+l_cut-2*r, 5+l_full-r, 2*r, 2*r)
        p.drawEllipse(5+w0+l_full, l_full-R, 2*R, 2*R)

    def paint_cyl(self, p):
        d = round(self.feature[0]*self.coefficient)
        h = round(self.feature[1]*self.coefficient)
        c = math.ceil(self.feature[2]*self.coefficient)
        p.drawEllipse(5, 5, d, d)
        p.drawEllipse(5, 5+d+h, d, d)
        p.drawRect(5, 5+d, c, h)

    def paint_dod(self, p):
        a = round(self.feature[0]*self.coefficient)
        angle = self.feature[1]
        xi1 = round(self.feature[2]*self.coefficient)
        yi1 = round(self.feature[3]*self.coefficient)
        xi2 = 2*xi1 + 2*a + a*math.sin(angle-math.pi/2)
        yi2 = yi1 -a*math.cos(angle-math.pi/2)
        points1 = [QPoint(5+xi1, 5+yi1)]
        points2 = [QPoint(5+xi2, 5+yi2)]
        for i in range(1, 6):
            angle_i = angle*i - math.pi*(i-1)
            xj1 = xi1
            yj1 = yi1
            xj2 = xi2
            yj2 = yi2
            points1_1 = [QPoint(5 + xj1, 5 + yj1)]
            points2_1 = [QPoint(5 + xj2, 5 + yj2)]
            for j in range(1, 6):
                angle_j = -angle_i - angle * j - math.pi * j
                xj1 = round(xj1 - a * math.cos(angle_j))
                yj1 = round(yj1 - a * math.sin(angle_j))
                points1_1.append(QPoint(5 + xj1, 5 + yj1))
                xj2 = round(xj2 - a * math.cos(angle_j))
                yj2 = round(yj2 + a * math.sin(angle_j))
                points2_1.append(QPoint(5 + xj2, 5 + yj2))
            poly1_1 = QPolygon(points1_1)
            p.drawPolygon(poly1_1)
            poly2_1 = QPolygon(points2_1)
            p.drawPolygon(poly2_1)
            xi1 = round(xi1 + a*math.cos(angle_i))
            yi1 = round(yi1 - a*math.sin(angle_i))
            points1.append(QPoint(5+xi1, 5+yi1))
            xi2 = round(xi2 + a * math.cos(angle_i))
            yi2 = round(yi2 + a * math.sin(angle_i))
            points2.append(QPoint(5 + xi2, 5 + yi2))
        poly1 = QPolygon(points1)
        p.drawPolygon(poly1)
        poly2 = QPolygon(points2)
        p.drawPolygon(poly2)

    def paint_oct(self, p):
        w1 = round(self.feature[0]*self.coefficient)
        h1 = round(self.feature[1]*self.coefficient)
        points = [QPoint(5+w1, 5+3*h1), QPoint(5, 5+2*h1), QPoint(5+w1, 5+h1)]
        poly = QPolygon(points)
        p.drawPolygon(poly)
        points = [QPoint(5 +w1, 5 + 3*h1), QPoint(5 + w1, 5 +h1), QPoint(5 + 2*w1, 5 + 2*h1)]
        poly = QPolygon(points)
        p.drawPolygon(poly)
        points = [QPoint(5 + w1, 5 + 3*h1), QPoint(5 + 2*w1, 5 + 2*h1), QPoint(5 + 2*w1, 5 + 4*h1)]
        poly = QPolygon(points)
        p.drawPolygon(poly)
        points = [QPoint(5 + w1, 5 + 3*h1), QPoint(5 + 2*w1, 5 + 4*h1), QPoint(5 + w1, 5 + 5*h1)]
        poly = QPolygon(points)
        p.drawPolygon(poly)
        points = [QPoint(5, 5 + 2*h1), QPoint(5, 5), QPoint(5 + w1, 5 + h1)]
        poly = QPolygon(points)
        p.drawPolygon(poly)
        points = [QPoint(5 + w1, 5 + h1), QPoint(5 + 2*w1, 5), QPoint(5 + 2*w1, 5 + 2*h1)]
        poly = QPolygon(points)
        p.drawPolygon(poly)
        points = [QPoint(5 + 2*w1, 5 + 2*h1), QPoint(5 + 3*w1, 5 + 3*h1), QPoint(5 + 2*w1, 5 + 4*h1)]
        poly = QPolygon(points)
        p.drawPolygon(poly)
        points = [QPoint(5 + 2*w1, 5 + 4*h1), QPoint(5 + 2*w1, 5 + 6*h1), QPoint(5 + w1, 5 + 5*h1)]
        poly = QPolygon(points)
        p.drawPolygon(poly)

    def paint_ico(self, p):
        w = round(self.feature[0]*self.coefficient)
        h = round(self.feature[1]*self.coefficient)
        for i in range(5):
            poly = QPolygon([QPoint(5+2*w*i, 5+h), QPoint(5+w+2*w*i, 5),  QPoint(5+ 2*w+2*w*i, 5+h)])
            p.drawPolygon(poly)
            poly = QPolygon([QPoint(5 + 2 * w * i, 5 + h), QPoint(5 + w + 2 * w * i, 5+2*h), QPoint(5 + 2 * w + 2 * w * i, 5 + h)])
            p.drawPolygon(poly)
            poly = QPolygon([QPoint(5 + 3*w+2 * w * i, 5 + 2*h), QPoint(5 + w + 2 * w * i, 5 + 2 * h), QPoint(5 + 2 * w + 2 * w * i, 5 + h)])
            p.drawPolygon(poly)
            poly = QPolygon([QPoint(5 + 3 * w + 2 * w * i, 5 + 2 * h), QPoint(5 + w + 2 * w * i, 5 + 2 * h), QPoint(5 + 2 * w + 2 * w * i, 5 + 3*h)])
            p.drawPolygon(poly)

    def sizeHint(self):
        return QSize(self.im_width, self.im_height)
