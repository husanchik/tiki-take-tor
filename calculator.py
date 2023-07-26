import sys

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout 
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton

class Button(QPushButton):
    def __init__(self, text):
        super().__init__(text)
        self.setFixedSize(60,40)
        self.setStyleSheet( "QPushButton::hover"
                     "{"
                     "background-color : lightgreen;"
                     "font-size : 25px;"
                     "}"
        )
class Calc(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("My Calculator")
        self.initUI()
        self.show()

    def initUI(self):
        self.setStyleSheet('background : #FFD93D')
        self.check  = 0
        self.expression = ''
        self.v_box = QVBoxLayout()

        self.h_box1 = QHBoxLayout()
        self.h_box2 = QHBoxLayout()
        self.h_box3 = QHBoxLayout()
        self.h_box4 = QHBoxLayout()
        self.h_box5 = QHBoxLayout()

        self.label_display = QLabel()

        self.edit_display = QLineEdit()
        self.edit_display.setPlaceholderText('0')

        self.btn0 = Button('0')
        self.btn1 = Button('1')
        self.btn2 = Button('2')
        self.btn3 = Button('3')
        self.btn4 = Button('4')
        self.btn5 = Button('5')
        self.btn6 = Button('6')
        self.btn7 = Button('7')
        self.btn8 = Button('8')
        self.btn9 = Button('9')
        self.btn_add = Button('+')
        self.btn_sub = Button('-')
        self.btn_mul = Button('*')
        self.btn_div = Button('/')
        self.btn_eq = Button('=')
        self.btn_bc = Button('<-')
        self.btn_clear = Button('C')
        self.btn_dot = Button('.')
        self.btn_open = Button('(')
        self.btn_close = Button(')')

        self.btn_clear.setStyleSheet( "QPushButton::hover"
                     "{"
                     "background-color : red;"
                     "font-size : 25px"
                     "}")

        self.h_box1.addWidget(self.btn_clear)
        self.h_box1.addWidget(self.btn_bc)
        self.h_box1.addWidget(self.btn_open)
        self.h_box1.addWidget(self.btn_close)

        self.h_box2.addWidget(self.btn7)
        self.h_box2.addWidget(self.btn8)
        self.h_box2.addWidget(self.btn9)
        self.h_box2.addWidget(self.btn_div)
        
        self.h_box3.addWidget(self.btn4)
        self.h_box3.addWidget(self.btn5)
        self.h_box3.addWidget(self.btn6)
        self.h_box3.addWidget(self.btn_mul)

        self.h_box4.addWidget(self.btn1)
        self.h_box4.addWidget(self.btn2)
        self.h_box4.addWidget(self.btn3)
        self.h_box4.addWidget(self.btn_sub)

        self.h_box5.addWidget(self.btn0)
        self.h_box5.addWidget(self.btn_dot)
        self.h_box5.addWidget(self.btn_eq)
        self.h_box5.addWidget(self.btn_add)

        self.v_box.addWidget(self.label_display)
        self.v_box.addWidget(self.edit_display)

        self.v_box.addLayout(self.h_box1)
        self.v_box.addLayout(self.h_box2)
        self.v_box.addLayout(self.h_box3)
        self.v_box.addLayout(self.h_box4)
        self.v_box.addLayout(self.h_box5)

        self.setLayout(self.v_box)

        self.btn0.clicked.connect(lambda : self.on_clicked(self.btn0.text()))
        self.btn1.clicked.connect(lambda : self.on_clicked(self.btn1.text()))
        self.btn2.clicked.connect(lambda : self.on_clicked(self.btn2.text()))
        self.btn3.clicked.connect(lambda : self.on_clicked(self.btn3.text()))
        self.btn4.clicked.connect(lambda : self.on_clicked(self.btn4.text()))
        self.btn5.clicked.connect(lambda : self.on_clicked(self.btn5.text()))
        self.btn6.clicked.connect(lambda : self.on_clicked(self.btn6.text()))
        self.btn7.clicked.connect(lambda : self.on_clicked(self.btn7.text()))
        self.btn8.clicked.connect(lambda : self.on_clicked(self.btn8.text()))
        self.btn9.clicked.connect(lambda : self.on_clicked(self.btn9.text()))
        self.btn_add.clicked.connect(lambda : self.on_clicked(self.btn_add.text()))
        self.btn_sub.clicked.connect(lambda : self.on_clicked(self.btn_sub.text()))
        self.btn_mul.clicked.connect(lambda : self.on_clicked(self.btn_mul.text()))
        self.btn_div.clicked.connect(lambda : self.on_clicked(self.btn_div.text()))
        self.btn_dot.clicked.connect(lambda : self.on_clicked(self.btn_dot.text()))
        self.btn_open.clicked.connect(lambda : self.on_clicked(self.btn_open.text()))
        self.btn_close.clicked.connect(lambda : self.on_clicked(self.btn_close.text()))

        self.btn_bc.clicked.connect(self.backslash)

        self.btn_clear.clicked.connect(self.clear_display)

        self.btn_eq.clicked.connect(self.get_result)

    def on_clicked(self, s):   
        try:
            type(s) == int   
        except AttributeError:
            self.edit_display.setText('faqat raqam kiritng')
        else : 
            self.expression += s
            self.edit_display.setText(self.expression)

    def backslash(self):
        self.expression = self.expression[:-1]
        self.edit_display.setText(self.expression)

    def clear_display(self):
        self.expression = ''
        self.edit_display.clear()
        self.label_display.clear()

    def get_result(self):

        try:
            res = eval(self.expression)

        except SyntaxError:
            res = 'Faqat raqam kiritng: '
        finally :  
            self.check += 1
            self.label_display.setText(str(res))
            if self.check == 2:
                self.label_display.clear()
                self.edit_display.setText(str(res))
                self.expression = str(res)
                self.check = 0



app = QApplication([])

win = Calc()

sys.exit(app.exec_())
