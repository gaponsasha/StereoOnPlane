from PyQt5.QtWidgets import *
import drawer_jpg
import drawer_pdf
import get


# диалговое окно отображается, если нельзя отрисовать фигуру
class D_empty(QDialog):
    def __init__(self, d_text):
        QDialog.__init__(self)
        self.setGeometry(400, 400, 50, 20)
        self.setWindowTitle('Help')
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        label = QLabel(d_text)
        self.layout.addWidget(label, 0, 0, 1, 1)


# диалоговое окно с отрисовкой развертки. До отрисовки - подсчет параметров
class D_draw(QDialog):
    def __init__(self, figure, feature, f_width, f_height):
        QWidget.__init__(self)
        self.setWindowTitle('Paint')
        btn_save_jpg = QPushButton("Сохранить изображение в JPG (фигура будет масштабирована)")
        btn_save_pdf = QPushButton("Сохранить изображение в PDF A4 (сохраняя реальные размеры)")
        draw_f = drawer_jpg.Drawer(figure, feature, f_width, f_height)
        self.setGeometry(200, 200, 530, 600)
        self.layout = QGridLayout()  # сеточный макет
        self.setLayout(self.layout)  # устанавливаем этот способ отображения
        self.layout.addWidget(btn_save_jpg, 0, 0, 1, 1)
        self.layout.addWidget(btn_save_pdf, 1, 0, 1, 1)
        self.layout.addWidget(draw_f, 2, 0, 1, 1)

        btn_save_jpg.clicked.connect(lambda: draw_f.saveImage())
        btn_save_pdf.clicked.connect(lambda: self.savePDFA4(figure, feature, f_width, f_height))

    def savePDFA4(self, figure, feature, f_width, f_height):
        a4_width = 21-2
        a4_height = 29.7-2
        if f_width > a4_width:  # проверка, вмещается ли развертка на лист
            if f_height > a4_width:
                get.showdialog('Невозможно сохранить pdf.\nРазвертка не вмещается на лист A4.')
                return
            elif f_width > a4_height:
                get.showdialog('Невозможно сохранить pdf.\nРазвертка не вмещается на лист A4.')
                return
            else:
                change_orientation = True
        elif f_height > a4_height:
            get.showdialog('Невозможно сохранить pdf.\nРазвертка не вмещается на лист A4.')
            return
        else:
            change_orientation = False
        filePath, _ = QFileDialog.getSaveFileName(self, "Save Image", "",
                                                  "PDF(*.pdf)")
        # if file path is blank return back
        if filePath == "":
            return
        drawer_pdf.saveA4(filePath, figure, feature, change_orientation)




