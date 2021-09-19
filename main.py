import math
import sys

from PyQt5.Qt import *


import get


def button_click():
    if not screen.all_edits_fill():
        get.showdialog('Не все поля заполнены.')
    elif screen.figure == 'par' and screen.wrong_angle_180():  # проверяем для фигур с параллелепипедом в основании
        get.showdialog('Вы ввели слишком большой угол.\nВведите угол < 180.')
    elif screen.figure == 'con_full' and screen.no_exist_triangle():
        get.showdialog('Невозможно построить конус.\nВторое измерение должно быть меньше l.')
    elif screen.figure == 'con_trun' and screen.no_exist_triangle():
        get.showdialog('Невозможно построить усеченный конус.\nРазность между радиусами должна быть меньше l.')
    elif screen.f_char == 'pyr_r' and screen.no_exist_triangle():
        get.showdialog('Невозможно построить пирамиду.\nh/l должно быть больше.')
    else:  # если все условия для фигур введены правильно и все поля заполнены
        get.show_draw(screen)


class Window(QWidget):
    # инициализация начального окна-ввода условий
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("StereoOnPlane")  # имя окна
        # размеры окна
        self.w = 700
        self.h = 350
        self.setGeometry(300, 300, self.w, self.h)
        self.layout = QGridLayout()  # сеточный макет
        self.setLayout(self.layout)  # устанавливаем этот способ отображения
        self.edits = []  # все поля ввода
        self.row = 0  # количество заполненных строк сетки
        self.l0()
        self.l1()  # отрисовка первого блока
        # стартовый вид приложения-1 фигура
        self.figure = 'cub'
        self.f_char = 's'
        self.l3_cub_s()

    # начальные инструкции перед вводом параметров
    def l0(self):
        label0 = QLabel(
            "Последовательно выбирайте характеристики для развертки.\n Длины вводите в сантиметрах, углы-в градусах.")
        label0.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(label0, 0, 0, 1, 12)

    # блок выбор пользователем фигуры
    def l1(self):
        # подсказка пользователю
        label1_1 = QLabel("Выберите фигуру:")
        self.layout.addWidget(label1_1, 1, 0, 1, 6)
        # выпадающий список фигур
        combox1_1 = QComboBox()
        combox1_1.addItems(
            ['Куб', 'Параллелепипед', 'Призма', 'Пирамида', 'Конус', 'Цилиндр', 'Правильный многогранник'])
        self.layout.addWidget(combox1_1, 1, 6, 1, 6)
        combox1_1.currentIndexChanged.connect(lambda: self.l2(combox1_1.currentIndex()))

    # блок с кнопкой. Обработка результатов
    def l4_b(self):
        # заполним пустые столбцы
        if self.row != 11:
            label4 = QLabel()
            self.layout.addWidget(label4, self.row, 0, 11 - self.row, 12)
        b = QPushButton("Построить развертку")
        b.clicked.connect(button_click)
        self.layout.addWidget(b, 11, 0, 1, 12)

    # блок выбора набора вводимых характеристик
    def l2(self, ci):
        self.clean(3)  # очищаем 2-4 блок от элементов с предыдущего шага
        self.clean_edits(0)  # очистим предыдущий набор полей для ввода
        if ci == 0:  # переходим к отрисовке 2 блока в зависимости от выбранной фигуры
            self.l2_cub()
        elif ci == 1:
            self.l2_par()
        elif ci == 2:
            self.l2_pri()
        elif ci == 3:
            self.l2_pyr()
        elif ci == 4:
            self.l2_con()
        elif ci == 5:
            self.l2_cyl()
        elif ci == 6:
            self.l2_poly_reg()

    # для каждой фигуры
    def l2_cub(self):  # куб
        self.figure = 'cub'
        self.l3_cub()  # сразу ввод стороны, нет выбора хар-к

    def l2_par(self):  # параллелепипед
        self.figure = 'par'
        label2_1 = QLabel("Какой параллелепипед нужно построить:")
        self.layout.addWidget(label2_1, 2, 0, 1, 6)
        combox2_1 = QComboBox()
        combox2_1.addItems(['Прямоугольный', 'Прямой', 'Наклонный'])
        combox2_1.currentIndexChanged.connect(lambda: self.l3_par(combox2_1.currentIndex()))
        self.layout.addWidget(combox2_1, 2, 6, 1, 6)
        label2_2 = QLabel("Введите стороны фигуры:")
        self.layout.addWidget(label2_2, 3, 0, 1, 12)
        self.l3_par_r()

    def l2_pri(self):  # призма
        self.figure = 'pri'
        label2_1 = QLabel("Какую призму нужно построить:")
        self.layout.addWidget(label2_1, 2, 0, 1, 6)
        combox2_1 = QComboBox()
        combox2_1.addItems(['Прямую, правильную']) #  , 'Прямую, неправильную', 'Наклонную, правильную', 'Наклонную, неправильную'])
        self.layout.addWidget(combox2_1, 2, 6, 1, 6)
        combox2_1.currentIndexChanged.connect(lambda: self.l3_pri(combox2_1.currentIndex()))
        label3_1 = QLabel("Выберите количество сторон основания призмы (3-10):")
        self.layout.addWidget(label3_1, 3, 0, 1, 6)
        self.spin3_1 = QSpinBox()
        self.spin3_1.setMinimum(3)
        self.spin3_1.setMaximum(10)
        self.spin3_1.valueChanged.connect(lambda: self.l3_pri(combox2_1.currentIndex()))
        self.layout.addWidget(self.spin3_1, 3, 6, 1, 6)
        self.l3_pri_sr()

    def l2_pyr(self):  # пирамида
        self.figure = 'pyr'
        label2_1 = QLabel("Какую пирамиду нужно построить:")
        self.layout.addWidget(label2_1, 2, 0, 1, 6)
        combox2_1 = QComboBox()
        combox2_1.addItems(['Правильную']) #  , 'Прямоугольную'])
        self.layout.addWidget(combox2_1, 2, 6, 1, 6)
        combox2_1.currentIndexChanged.connect(lambda: self.l3_pyr(combox2_1.currentIndex()))
        self.l3_pyr_r()

    def l2_con(self):  # конус
        label2_2 = QLabel("Вид конуса:")
        self.layout.addWidget(label2_2, 2, 0, 1, 6)
        combox2_2 = QComboBox()
        combox2_2.addItems(['Прямой', 'Усеченный'])
        self.layout.addWidget(combox2_2, 2, 6, 1, 6)
        combox2_2.currentIndexChanged.connect(lambda: self.l2_con_ch(combox2_2.currentIndex()))
        self.l2_con_full()

    def l2_con_ch(self, ci):
        self.clean(5)
        self.clean_edits(0)
        if ci == 0:
            self.l2_con_full()
        elif ci == 1:
            self.l2_con_trun()


    def l2_con_full(self):
        self.figure = 'con_full'
        label2_1 = QLabel("Характеристики, по которым\nбудет строиться конус:")
        self.layout.addWidget(label2_1, 3, 0, 1, 6)
        combox2_1 = QComboBox()
        combox2_1.addItems(['По образующей и радиусу', 'По высоте и радиусу', 'По высоте и образующей'])
        self.layout.addWidget(combox2_1, 3, 6, 1, 6)
        combox2_1.currentIndexChanged.connect(lambda: self.l3_con_full(combox2_1.currentIndex()))
        self.l3_con_full_lr()

    def l2_con_trun(self):
        self.figure = 'con_trun'
        label2_1 = QLabel("Характеристики, по которым\nбудет строиться усеченный конус:")
        self.layout.addWidget(label2_1, 3, 0, 1, 6)
        combox2_1 = QComboBox()
        combox2_1.addItems(['По образующей и радиусам', 'По высоте и радиусам'])
        self.layout.addWidget(combox2_1, 3, 6, 1, 6)
        combox2_1.currentIndexChanged.connect(lambda: self.l3_con_trun(combox2_1.currentIndex()))
        self.l3_con_trun_lr()

    def l2_cyl(self):  # цилиндр
        self.figure = 'cyl'
        label2_1 = QLabel("Выберите характеристики,\nпо которым будет строиться цилиндр:")
        self.layout.addWidget(label2_1, 2, 0, 1, 6)
        combox2_1 = QComboBox()
        combox2_1.addItems(['По высоте и радиусу', 'По высоте и длине окружности'])
        self.layout.addWidget(combox2_1, 2, 6, 1, 6)
        combox2_1.currentIndexChanged.connect(lambda: self.l3_cyl(combox2_1.currentIndex()))
        self.l3_cyl_hr()

    def l2_poly_reg(self):  # правильные многогранники
        self.figure = 'poly_reg'
        self.f_char = 'poly_reg_tet'
        label2_1 = QLabel("Выберите правильный многогранник:")
        self.layout.addWidget(label2_1, 2, 0, 1, 6)
        combox2_1 = QComboBox()
        combox2_1.addItems(['Тетраэдр', 'Гексаэдр', 'Октаэдр', 'Додекаэдр', 'Икосаэдр'])
        self.layout.addWidget(combox2_1, 2, 6, 1, 6)
        combox2_1.currentIndexChanged.connect(lambda: self.l3_poly_reg(combox2_1.currentIndex()))
        label3_1 = QLabel("Введите сторону фигуры:")
        self.layout.addWidget(label3_1, 3, 0, 1, 6)
        edit3_1 = QLineEdit()
        edit3_1.setInputMask('00.00')
        self.layout.addWidget(edit3_1, 3, 6, 1, 6)
        self.edits.append(edit3_1)
        self.row = 4
        self.l4_b()

    # блок ввода характеристик
    # куб
    def l3_cub(self):
        self.l3_cub_s()  # без выбора, сразу отрисовка по стороне

    def l3_cub_s(self):  # куб по стороне
        self.f_char = 'cub_s'
        label3_1 = QLabel("Введите сторону a:")
        self.layout.addWidget(label3_1, 2, 0, 1, 6)
        edit3_1 = QLineEdit()
        edit3_1.setInputMask('00.00')
        self.layout.addWidget(edit3_1, 2, 6, 1, 6)
        self.edits.append(edit3_1)
        self.row = 3
        self.l4_b()

    # параллелеограм
    def l3_par(self, ci):
        self.clean(6)
        self.clean_edits(0)
        if ci == 0:
            self.l3_par_r()
        elif ci == 1:
            self.l3_par_s()
        elif ci == 2:
            self.l3_par_i()

    def l3_par_r(self):  # прямоугольный параллелепипед
        self.f_char = 'par_r'
        label3_1 = QLabel("Сторона-длина a:")
        self.layout.addWidget(label3_1, 4, 0, 1, 2)
        edit3_1 = QLineEdit()
        edit3_1.setInputMask('00.00')
        self.layout.addWidget(edit3_1, 4, 2, 1, 2)
        self.edits.append(edit3_1)
        label3_2 = QLabel("Сторона-ширина b:")
        self.layout.addWidget(label3_2, 4, 4, 1, 2)
        edit3_2 = QLineEdit()
        edit3_2.setInputMask('00.00')
        self.layout.addWidget(edit3_2, 4, 6, 1, 2)
        self.edits.append(edit3_2)
        label3_3 = QLabel("Сторона-высота c:")
        self.layout.addWidget(label3_3, 4, 8, 1, 2)
        edit3_3 = QLineEdit()
        edit3_3.setInputMask('00.00')
        self.layout.addWidget(edit3_3, 4, 10, 1, 2)
        self.edits.append(edit3_3)
        self.row = 5
        self.l4_b()

    def l3_par_s(self):
        self.f_char = 'par_s'
        label3_1 = QLabel("Сторона основания a:")
        self.layout.addWidget(label3_1, 4, 0, 1, 2)
        edit3_1 = QLineEdit()
        edit3_1.setInputMask('00.00')
        self.layout.addWidget(edit3_1, 4, 2, 1, 2)
        self.edits.append(edit3_1)
        label3_2 = QLabel("Сторона основания b:")
        self.layout.addWidget(label3_2, 4, 4, 1, 2)
        edit3_2 = QLineEdit()
        edit3_2.setInputMask('00.00')
        self.layout.addWidget(edit3_2, 4, 6, 1, 2)
        self.edits.append(edit3_2)
        label3_3 = QLabel("Сторона-высота c:")
        self.layout.addWidget(label3_3, 4, 8, 1, 2)
        edit3_3 = QLineEdit()
        edit3_3.setInputMask('00.00')
        self.layout.addWidget(edit3_3, 4, 10, 1, 2)
        self.edits.append(edit3_3)
        label3_4 = QLabel("Введите один из углов основания:")
        self.layout.addWidget(label3_4, 5, 0, 1, 4)
        edit3_4 = QLineEdit()
        edit3_4.setInputMask('000')
        self.layout.addWidget(edit3_4, 5, 4, 1, 2)
        self.edits.append(edit3_4)
        self.row = 6
        self.l4_b()

    def l3_par_i(self):
        self.f_char = 'par_i'
        label3_1 = QLabel("Сторона a:")
        self.layout.addWidget(label3_1, 4, 0, 1, 2)
        edit3_1 = QLineEdit()
        edit3_1.setInputMask('00.00')
        self.layout.addWidget(edit3_1, 4, 2, 1, 2)
        self.edits.append(edit3_1)
        label3_2 = QLabel("Сторона b:")
        self.layout.addWidget(label3_2, 4, 4, 1, 2)
        edit3_2 = QLineEdit()
        edit3_2.setInputMask('00.00')
        self.layout.addWidget(edit3_2, 4, 6, 1, 2)
        self.edits.append(edit3_2)
        label3_3 = QLabel("Сторона c:")
        self.layout.addWidget(label3_3, 4, 8, 1, 2)
        edit3_3 = QLineEdit()
        edit3_3.setInputMask('00.00')
        self.layout.addWidget(edit3_3, 4, 10, 1, 2)
        self.edits.append(edit3_3)
        label3_0 = QLabel("Введите по одному из углов для граней, образованных ребрами:")
        self.layout.addWidget(label3_0, 5, 0, 1, 12)
        label3_4 = QLabel("Угол между a и b:")
        self.layout.addWidget(label3_4, 6, 0, 1, 2)
        edit3_4 = QLineEdit()
        edit3_4.setInputMask('000')
        self.layout.addWidget(edit3_4, 6, 2, 1, 2)
        self.edits.append(edit3_4)
        label3_5 = QLabel("Угол между a и c:")
        self.layout.addWidget(label3_5, 6, 4, 1, 2)
        edit3_5 = QLineEdit()
        edit3_5.setInputMask('000')
        self.layout.addWidget(edit3_5, 6, 6, 1, 2)
        self.edits.append(edit3_5)
        label3_6 = QLabel("Угол между b и c:")
        self.layout.addWidget(label3_6, 6, 8, 1, 2)
        edit3_6 = QLineEdit()
        edit3_6.setInputMask('000')
        self.layout.addWidget(edit3_6, 6, 10, 1, 2)
        self.edits.append(edit3_6)
        self.row = 7
        self.l4_b()

    # призма
    def l3_pri(self, ci):
        self.clean(7)
        self.clean_edits(0)
        if ci == 0:
            self.l3_pri_sr()
        elif ci == 1:
            self.l3_pri_sw()
        elif ci == 2:
            self.l3_pri_ir()
        elif ci == 3:
            self.l3_pri_iw()

    def l3_pri_sr(self):
        self.f_char = 'pri_sr'
        label3_2 = QLabel("Введите сторону основания a:")
        self.layout.addWidget(label3_2, 4, 0, 1, 3)
        edit3_2 = QLineEdit()
        edit3_2.setInputMask('00.00')
        self.layout.addWidget(edit3_2, 4, 3, 1, 3)
        self.edits.append(edit3_2)
        label3_3 = QLabel("Введите высоту фигуры h:")
        self.layout.addWidget(label3_3, 4, 6, 1, 3)
        edit3_3 = QLineEdit()
        edit3_3.setInputMask('00.00')
        self.layout.addWidget(edit3_3, 4, 9, 1, 3)
        self.edits.append(edit3_3)
        self.row = 5
        self.l4_b()

    def l3_pri_sw(self):
        self.f_char = 'pri_sw'
        cou_s = self.spin3_1.value()
        edits3 = []
        r = 5
        c = 0
        label0 = QLabel("Введите стороны основания:")
        self.layout.addWidget(label0, 4, 0, 1, 6)
        for i in range(0, cou_s):
            label = QLabel(f"Сторона a{i + 1}:")
            self.layout.addWidget(label, r, c, 1, 2)
            edit = QLineEdit()
            edit.setInputMask('00.00')
            edits3.append(edit)
            self.layout.addWidget(edits3[i], r, c + 2, 1, 2)
            c += 4
            if c == 12:
                c = 0
                r += 1
        if c != 0:
            r += 1
        self.edits = self.edits + edits3
        label3_3 = QLabel("Введите высоту фигуры h:")
        self.layout.addWidget(label3_3, r, 0, 1, 3)
        edit3_3 = QLineEdit()
        edit3_3.setInputMask('00.00')
        self.layout.addWidget(edit3_3, r, 3, 1, 3)
        self.edits.append(edit3_3)
        self.row = r + 1
        self.l4_b()

    def l3_pri_ir(self):
        self.f_char = 'pri_ir'
        label3_2 = QLabel("Введите сторону основания a:")
        self.layout.addWidget(label3_2, 4, 0, 1, 3)
        edit3_2 = QLineEdit()
        edit3_2.setInputMask('00.00')
        self.layout.addWidget(edit3_2, 4, 3, 1, 3)
        self.edits.append(edit3_2)
        self.combox3_3 = QComboBox()
        self.combox3_3.addItems(['Введите высоту фигуры h:', 'Введите боковое ребро b:'])
        self.layout.addWidget(self.combox3_3, 4, 6, 1, 3)
        edit3_3 = QLineEdit()
        edit3_3.setInputMask('00.00')
        self.layout.addWidget(edit3_3, 4, 9, 1, 3)
        self.edits.append(edit3_3)
        label3_4 = QLabel("Фигура наклонена относительно:")
        self.layout.addWidget(label3_4, 5, 0, 1, 3)
        self.combox3_4 = QComboBox()
        self.combox3_4.addItems(['Стороны основания:', 'Угла основания:'])
        self.layout.addWidget(self.combox3_4, 5, 3, 1, 3)
        label3_5 = QLabel("Введите угол наклона фигуры\n относительно основания:")
        self.layout.addWidget(label3_5, 5, 6, 1, 3)
        edit3_5 = QLineEdit()
        edit3_5.setInputMask('000')
        self.layout.addWidget(edit3_5, 5, 9, 1, 3)
        self.edits.append(edit3_5)
        self.row = 6
        self.l4_b()

    def l3_pri_iw(self):
        self.f_char = 'pri_iw'
        cou_s = self.spin3_1.value()
        edits3 = []
        r = 5
        c = 0
        label0 = QLabel("Введите стороны основания:")
        self.layout.addWidget(label0, 4, 0, 1, 6)
        for i in range(0, cou_s):
            label = QLabel(f"Сторона a{i + 1}:")
            self.layout.addWidget(label, r, c, 1, 2)
            edit = QLineEdit()
            edit.setInputMask('00.00')
            edits3.append(edit)
            self.layout.addWidget(edits3[i], r, c + 2, 1, 2)
            c += 4
            if c == 12:
                c = 0
                r += 1
        if c != 0:
            r += 1
        self.edits = self.edits + edits3
        self.combox3_3 = QComboBox()
        self.combox3_3.addItems(['Введите высоту h:', 'Введите бок.ребро b:'])
        self.layout.addWidget(self.combox3_3, r, 0, 1, 3)
        edit3_3 = QLineEdit()
        edit3_3.setInputMask('00.00')
        self.layout.addWidget(edit3_3, r, 3, 1, 3)
        self.edits.append(edit3_3)
        r += 1
        label3_4 = QLabel("Выберите № стороны, относительно\nкоторой наклонена фигура:")
        self.layout.addWidget(label3_4, r, 0, 1, 4)
        self.spin3_4 = QSpinBox()
        self.spin3_4.setMinimum(1)
        self.spin3_4.setMaximum(cou_s)
        self.layout.addWidget(self.spin3_4, r, 4, 1, 2)
        label3_5 = QLabel("Введите угол наклона фигуры\n относительно этой стороны:")
        self.layout.addWidget(label3_5, r, 6, 1, 3)
        edit3_5 = QLineEdit()
        edit3_5.setInputMask('000')
        self.layout.addWidget(edit3_5, r, 9, 1, 3)
        self.edits.append(edit3_5)
        self.row = r + 1
        self.l4_b()

    # пирамида
    def l3_pyr(self, ci):
        self.clean(5)
        self.clean_edits(0)
        if ci == 0:
            self.l3_pyr_r()
        elif ci == 1:
            self.l3_pyr_s()

    def l3_pyr_r(self):
        self.f_char = 'pyr_r'
        label3_1 = QLabel("Выберите количество\nсторон основания (3-10):")
        self.layout.addWidget(label3_1, 3, 0, 1, 5)
        self.spin3_1 = QSpinBox()
        self.spin3_1.setMinimum(3)
        self.spin3_1.setMaximum(10)
        self.layout.addWidget(self.spin3_1, 3, 5, 1, 1)
        label3_2 = QLabel("Введите сторону основания a:")
        self.layout.addWidget(label3_2, 4, 0, 1, 3)
        edit3_2 = QLineEdit()
        edit3_2.setInputMask('00.00')
        self.layout.addWidget(edit3_2, 4, 3, 1, 3)
        self.edits.append(edit3_2)
        self.combox3_2 = QComboBox()
        self.combox3_2.addItems(['Введите высоту фигуры h:', 'Введите боковое ребро l:'])
        self.layout.addWidget(self.combox3_2, 4, 6, 1, 3)
        edit3_2 = QLineEdit()
        edit3_2.setInputMask('00.00')
        self.layout.addWidget(edit3_2, 4, 9, 1, 3)
        self.edits.append(edit3_2)
        self.row = 5
        self.l4_b()

    def l3_pyr_s(self):
        self.f_char = 'pyr_s'
        label3_1 = QLabel("Выберите количество\nсторон основания (3-10):")
        self.layout.addWidget(label3_1, 3, 0, 1, 5)
        self.spin3_1 = QSpinBox()
        self.spin3_1.setMinimum(3)
        self.spin3_1.setMaximum(10)
        self.spin3_1.valueChanged.connect(self.l3_pyr_s_s)
        self.layout.addWidget(self.spin3_1, 3, 5, 1, 1)
        self.l3_pyr_s_s()

    def l3_pyr_s_s(self):
        self.clean(7)
        self.clean_edits(0)
        cou_s = self.spin3_1.value()
        r = 5
        c = 0
        edits3 = []
        label0 = QLabel('Введите стороны основания:')
        self.layout.addWidget(label0, 4, 0, 1, 12)
        for i in range(cou_s):
            label = QLabel(f"Сторона a{i + 1}:")
            self.layout.addWidget(label, r, c, 1, 2)
            edit = QLineEdit()
            edit.setInputMask('00.00')
            edits3.append(edit)
            self.layout.addWidget(edits3[i], r, c + 2, 1, 2)
            c += 4
            if c == 12:
                c = 0
                r += 1
        if c != 0:
            r += 1
        self.edits = self.edits + edits3
        label3_2 = QLabel("Выберите № стороны основания,\nс которой образован прямой угол:")
        self.layout.addWidget(label3_2, r, 0, 1, 3)
        self.spin3_2 = QSpinBox()
        self.spin3_2.setMinimum(1)
        self.spin3_2.setMaximum(cou_s)
        self.layout.addWidget(self.spin3_2, r, 3, 1, 3)
        label3_3 = QLabel("Введите высоту h:")
        self.layout.addWidget(label3_3, r, 6, 1, 3)
        edit3_3 = QLineEdit()
        edit3_3.setInputMask('00.00')
        self.layout.addWidget(edit3_3, r, 9, 1, 3)
        self.edits.append(edit3_3)
        self.row = r + 1
        self.l4_b()

    # конус
    def l3_con_full(self, ci):
        self.clean(7)
        self.clean_edits(0)
        if ci == 0:
            self.l3_con_full_lr()
        elif ci == 1:
            self.l3_con_full_hr()
        elif ci == 2:
            self.l3_con_full_lh()

    def l3_con_full_lr(self):  # конус по образующей и радиусу
        self.f_char = 'con_lr'
        label3_1 = QLabel("Введите образующую l:")
        self.layout.addWidget(label3_1, 4, 0, 1, 3)
        edit3_1 = QLineEdit()
        edit3_1.setInputMask('00.00')
        self.layout.addWidget(edit3_1, 4, 3, 1, 3)
        self.edits.append(edit3_1)
        label3_2 = QLabel("Введите радиус r:")
        self.layout.addWidget(label3_2, 4, 6, 1, 3)
        edit3_2 = QLineEdit()
        edit3_2.setInputMask('00.00')
        self.layout.addWidget(edit3_2, 4, 9, 1, 3)
        self.edits.append(edit3_2)
        self.row = 5
        self.l4_b()

    def l3_con_full_hr(self):  # конус по высоте и радиусу
        self.f_char = 'con_hr'
        label3_1 = QLabel("Введите высоту h:")
        self.layout.addWidget(label3_1, 4, 0, 1, 3)
        edit3_1 = QLineEdit()
        edit3_1.setInputMask('00.00')
        self.layout.addWidget(edit3_1, 4, 3, 1, 3)
        self.edits.append(edit3_1)
        label3_2 = QLabel("Введите радиус r:")
        self.layout.addWidget(label3_2, 4, 6, 1, 3)
        edit3_2 = QLineEdit()
        edit3_2.setInputMask('00.00')
        self.layout.addWidget(edit3_2, 4, 9, 1, 3)
        self.edits.append(edit3_2)
        self.row = 5
        self.l4_b()

    def l3_con_full_lh(self):  # конус по высоте и образующей
        self.f_char = 'con_lh'
        label3_2 = QLabel("Введите образующую l:")
        self.layout.addWidget(label3_2, 4, 0, 1, 3)
        edit3_2 = QLineEdit()
        edit3_2.setInputMask('00.00')
        self.layout.addWidget(edit3_2, 4, 3, 1, 3)
        self.edits.append(edit3_2)
        label3_1 = QLabel("Введите высоту h:")
        self.layout.addWidget(label3_1, 4, 6, 1, 3)
        edit3_1 = QLineEdit()
        edit3_1.setInputMask('00.00')
        self.layout.addWidget(edit3_1, 4, 9, 1, 3)
        self.edits.append(edit3_1)
        self.row = 5
        self.l4_b()

    #  усеченный конус
    def l3_con_trun(self, ci):
        self.clean(7)
        self.clean_edits(0)
        if ci == 0:
            self.l3_con_trun_lr()
        elif ci == 1:
            self.l3_con_trun_hr()

    def l3_con_trun_lr(self):
        self.f_char = 'con_lr'
        label3_1 = QLabel("Введите образующую l:")
        self.layout.addWidget(label3_1, 4, 0, 1, 3)
        edit3_1 = QLineEdit()
        edit3_1.setInputMask('00.00')
        self.layout.addWidget(edit3_1, 4, 3, 1, 3)
        self.edits.append(edit3_1)
        label3_2 = QLabel("Введите радиус меньшего основания r:")
        self.layout.addWidget(label3_2, 5, 0, 1, 3)
        edit3_2 = QLineEdit()
        edit3_2.setInputMask('00.00')
        self.layout.addWidget(edit3_2, 5, 3, 1, 3)
        self.edits.append(edit3_2)
        label3_3 = QLabel("Введите радиус большего основания R:")
        self.layout.addWidget(label3_3, 5, 6, 1, 3)
        edit3_3 = QLineEdit()
        edit3_3.setInputMask('00.00')
        self.layout.addWidget(edit3_3, 5, 9, 1, 3)
        self.edits.append(edit3_3)
        self.row = 6
        self.l4_b()

    def l3_con_trun_hr(self):
        self.f_char = 'con_hr'
        label3_1 = QLabel("Введите высоту h:")
        self.layout.addWidget(label3_1, 4, 0, 1, 3)
        edit3_1 = QLineEdit()
        edit3_1.setInputMask('00.00')
        self.layout.addWidget(edit3_1, 4, 3, 1, 3)
        self.edits.append(edit3_1)
        label3_2 = QLabel("Введите радиус меньшего основания r:")
        self.layout.addWidget(label3_2, 5, 0, 1, 3)
        edit3_2 = QLineEdit()
        edit3_2.setInputMask('00.00')
        self.layout.addWidget(edit3_2, 5, 3, 1, 3)
        self.edits.append(edit3_2)
        label3_3 = QLabel("Введите радиус большего основания R:")
        self.layout.addWidget(label3_3, 5, 6, 1, 3)
        edit3_3 = QLineEdit()
        edit3_3.setInputMask('00.00')
        self.layout.addWidget(edit3_3, 5, 9, 1, 3)
        self.edits.append(edit3_3)
        self.row = 6
        self.l4_b()

    # цилиндр
    def l3_cyl(self, ci):
        self.clean(5)  # очищаем 3-4 блок от элементов с предыдущего шага
        self.clean_edits(0)
        if ci == 0:
            self.l3_cyl_hr()
        elif ci == 1:
            self.l3_cyl_hc()

    def l3_cyl_hr(self):  # цилиндр по высоте и радиусу
        self.f_char = 'cyl_hr'
        label3_1 = QLabel("Введите высоту h:")
        self.layout.addWidget(label3_1, 3, 0, 1, 3)
        edit3_1 = QLineEdit()
        edit3_1.setInputMask('00.00')
        self.layout.addWidget(edit3_1, 3, 3, 1, 3)
        self.edits.append(edit3_1)
        label3_2 = QLabel("Введите радиус r:")
        self.layout.addWidget(label3_2, 3, 6, 1, 3)
        edit3_2 = QLineEdit()
        edit3_2.setInputMask('00.00')
        self.layout.addWidget(edit3_2, 3, 9, 1, 3)
        self.edits.append(edit3_2)
        self.row = 4
        self.l4_b()

    def l3_cyl_hc(self):
        self.f_char = 'cyl_hc'
        label3_1 = QLabel("Введите высоту h:")
        self.layout.addWidget(label3_1, 3, 0, 1, 3)
        edit3_1 = QLineEdit()
        edit3_1.setInputMask('00.00')
        self.layout.addWidget(edit3_1, 3, 3, 1, 3)
        self.edits.append(edit3_1)
        label3_2 = QLabel("Введите длину окружности c:")
        self.layout.addWidget(label3_2, 3, 6, 1, 3)
        edit3_2 = QLineEdit()
        edit3_2.setInputMask('00.00')
        self.layout.addWidget(edit3_2, 3, 9, 1, 3)
        self.edits.append(edit3_2)
        self.row = 4
        self.l4_b()

    # правильные многогранники
    def l3_poly_reg(self, ci):
        if ci == 0:
            self.f_char = 'poly_reg_tet'
        elif ci == 1:
            self.f_char = 'poly_reg_gec'
        elif ci == 2:
            self.f_char = 'poly_reg_oct'
        elif ci == 3:
            self.f_char = 'poly_reg_dod'
        elif ci == 4:
            self.f_char = 'poly_reg_ico'

    # очистка блоков от элементов  прошлых шагов
    def clean(self, start_el):
        l_cou = self.layout.count()
        for i in reversed(range(start_el, l_cou)):
            self.layout.itemAt(i).widget().setParent(None)

    # очистка хранилища полей ввода
    def clean_edits(self, el):
        l_e = len(self.edits)
        for i in reversed(range(el, l_e)):
            self.edits.pop(i)

    # проверка, заполнены ли все поля
    def all_edits_fill(self):
        for i in self.edits:
            if i.text() == '' or i.text() == '.':
                return False
        return True

    # проверяем, ввели ли ошибочный угол
    def wrong_angle_180(self):
        if self.f_char == 'par_s':
            if int(self.edits[3].text()) >= 180:
                return True
        if self.f_char == 'par_i':
            for i in range(3, 6):
                if int(self.edits[i].text()) >= 180:
                    return True
        return False

    def no_exist_triangle(self):
        if self.figure == 'con_full':
            if self.f_char == 'con_hr':
                return False
            else:
                l = float(self.edits[0].text())
                r = float(self.edits[1].text())
                if l <= r:
                    return True
                else:
                    return False
        if self.figure == 'con_trun':
            if self.f_char == 'con_hr':
                return False
            else:
                l = float(self.edits[0].text())
                r = float(self.edits[1].text())
                R = float(self.edits[2].text())
                if l <= math.fabs(R-r):
                    return True
                else:
                    return False
        if self.f_char == 'pyr_r':
            n = self.spin3_1.value()
            a = float(self.edits[0].text())
            if self.combox3_2.currentIndex() == 0:
                return False
            if self.combox3_2.currentIndex() == 1:
                l = float(self.edits[1].text())
                R = a / (2 * math.sin(math.pi / n))
                if l <= R or l <= a / 2:
                    return True
                else:
                    return False


app = QApplication(sys.argv)  # создает приложение
screen = Window()  # инициируем окно
screen.show()  # включаем егго видимость

sys.exit(app.exec_())  # условие завершения работы программы - закрытие окна приложения
