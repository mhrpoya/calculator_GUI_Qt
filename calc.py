from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_view(object):
    def setupUi(self, view):
        view.setObjectName("view")
        view.resize(333, 595)
        view.setStyleSheet("QMainWindow#view{\n"
"    background-color: #436F91;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(view)
        self.centralwidget.setStyleSheet("QWidget#centralwidget{\n"
"    background-color: #436F91;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_otp = QtWidgets.QLabel(self.centralwidget)
        self.lbl_otp.setGeometry(QtCore.QRect(10, 10, 311, 81))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.lbl_otp.setFont(font)
        self.lbl_otp.setStyleSheet("QLabel#lbl_otp{\n"
"    background-color: white;\n"
"}")
        self.lbl_otp.setFrameShape(QtWidgets.QFrame.Box)
        self.lbl_otp.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lbl_otp.setLineWidth(2)
        self.lbl_otp.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_otp.setIndent(10)
        self.lbl_otp.setObjectName("lbl_otp")
        self.btn_prs = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press("%"))
        self.btn_prs.setGeometry(QtCore.QRect(10, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.btn_prs.setFont(font)
        self.btn_prs.setStyleSheet("QPushButton#btn_prs{\n"
"    background-color: white;\n"
"}\n"
"\n"
"QPushButton#btn_prs:hover{\n"
"    background-color: gray;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton#btn_prs:pressed{\n"
"    background-color: white;\n"
"}")
        self.btn_prs.setObjectName("btn_prs")
        self.btn_clr = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press("C"))
        self.btn_clr.setGeometry(QtCore.QRect(90, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.btn_clr.setFont(font)
        self.btn_clr.setStyleSheet("QPushButton#btn_clr{\n"
"    background-color: white;\n"
"}\n"
"\n"
"QPushButton#btn_clr:hover{\n"
"    background-color: gray;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton#btn_clr:pressed{\n"
"    background-color: white;\n"
"}")
        self.btn_clr.setObjectName("btn_clr")
        self.btn_div = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press("/"))
        self.btn_div.setGeometry(QtCore.QRect(250, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.btn_div.setFont(font)
        self.btn_div.setStyleSheet("QPushButton#btn_div{\n"
"    background-color: white;\n"
"}\n"
"\n"
"QPushButton#btn_div:hover{\n"
"    background-color: gray;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton#btn_div:pressed{\n"
"    background-color: white;\n"
"}")
        self.btn_div.setObjectName("btn_div")
        self.btn_flsh = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.remove())
        self.btn_flsh.setGeometry(QtCore.QRect(170, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.btn_flsh.setFont(font)
        self.btn_flsh.setStyleSheet("QPushButton#btn_flsh{\n"
"    background-color: white;\n"
"}\n"
"\n"
"QPushButton#btn_flsh:hover{\n"
"    background-color: gray;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton#btn_flsh:pressed{\n"
"    background-color: white;\n"
"}")
        self.btn_flsh.setObjectName("btn_flsh")
        self.btn_mul = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press("*"))
        self.btn_mul.setGeometry(QtCore.QRect(250, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.btn_mul.setFont(font)
        self.btn_mul.setStyleSheet("QPushButton#btn_mul{\n"
"    background-color: white;\n"
"}\n"
"\n"
"QPushButton#btn_mul:hover{\n"
"    background-color: gray;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton#btn_mul:pressed{\n"
"    background-color: white;\n"
"}")
        self.btn_mul.setObjectName("btn_mul")
        self.btn9 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press("9"))
        self.btn9.setGeometry(QtCore.QRect(170, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.btn9.setFont(font)
        self.btn9.setStyleSheet("QPushButton#btn9{\n"
"    background-color: white;\n"
"}\n"
"\n"
"QPushButton#btn9:hover{\n"
"    background-color: gray;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton#btn9:pressed{\n"
"    background-color: white;\n"
"}")
        self.btn9.setObjectName("btn9")
        self.btn7 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press("7"))
        self.btn7.setGeometry(QtCore.QRect(10, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.btn7.setFont(font)
        self.btn7.setStyleSheet("QPushButton#btn7{\n"
"    background-color: white;\n"
"}\n"
"\n"
"QPushButton#btn7:hover{\n"
"    background-color: gray;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton#btn7:pressed{\n"
"    background-color: white;\n"
"}")
        self.btn7.setObjectName("btn7")
        self.btn8 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press("8"))
        self.btn8.setGeometry(QtCore.QRect(90, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.btn8.setFont(font)
        self.btn8.setStyleSheet("QPushButton#btn8{\n"
"    background-color: white;\n"
"}\n"
"\n"
"QPushButton#btn8:hover{\n"
"    background-color: gray;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton#btn8:pressed{\n"
"    background-color: white;\n"
"}")
        self.btn8.setObjectName("btn8")
        self.btn_sub = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press("-"))
        self.btn_sub.setGeometry(QtCore.QRect(250, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.btn_sub.setFont(font)
        self.btn_sub.setStyleSheet("QPushButton#btn_sub{\n"
"    background-color: white;\n"
"}\n"
"\n"
"QPushButton#btn_sub:hover{\n"
"    background-color: gray;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton#btn_sub:pressed{\n"
"    background-color: white;\n"
"}")
        self.btn_sub.setObjectName("btn_sub")
        self.btn6 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press("6"))
        self.btn6.setGeometry(QtCore.QRect(170, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.btn6.setFont(font)
        self.btn6.setStyleSheet("QPushButton#btn6{\n"
"    background-color: white;\n"
"}\n"
"\n"
"QPushButton#btn6:hover{\n"
"    background-color: gray;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton#btn6:pressed{\n"
"    background-color: white;\n"
"}")
        self.btn6.setObjectName("btn6")
        self.btn4 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press("4"))
        self.btn4.setGeometry(QtCore.QRect(10, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.btn4.setFont(font)
        self.btn4.setStyleSheet("QPushButton#btn4{\n"
"    background-color: white;\n"
"}\n"
"\n"
"QPushButton#btn4:hover{\n"
"    background-color: gray;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton#btn4:pressed{\n"
"    background-color: white;\n"
"}")
        self.btn4.setObjectName("btn4")
        self.btn5 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press("5"))
        self.btn5.setGeometry(QtCore.QRect(90, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.btn5.setFont(font)
        self.btn5.setStyleSheet("QPushButton#btn5{\n"
"    background-color: white;\n"
"}\n"
"\n"
"QPushButton#btn5:hover{\n"
"    background-color: gray;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton#btn5:pressed{\n"
"    background-color: white;\n"
"}")
        self.btn5.setObjectName("btn5")
        self.btn_plus = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press("+"))
        self.btn_plus.setGeometry(QtCore.QRect(250, 380, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.btn_plus.setFont(font)
        self.btn_plus.setStyleSheet("QPushButton#btn_plus{\n"
"    background-color: white;\n"
"}\n"
"\n"
"QPushButton#btn_plus:hover{\n"
"    background-color: gray;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton#btn_plus:pressed{\n"
"    background-color: white;\n"
"}")
        self.btn_plus.setObjectName("btn_plus")
        self.btn3 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press("3"))
        self.btn3.setGeometry(QtCore.QRect(170, 380, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.btn3.setFont(font)
        self.btn3.setStyleSheet("QPushButton#btn3{\n"
"    background-color: white;\n"
"}\n"
"\n"
"QPushButton#btn3:hover{\n"
"    background-color: gray;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton#btn3:pressed{\n"
"    background-color: white;\n"
"}")
        self.btn3.setObjectName("btn3")
        self.btn1 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press("1"))
        self.btn1.setGeometry(QtCore.QRect(10, 380, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.btn1.setFont(font)
        self.btn1.setStyleSheet("QPushButton#btn1{\n"
"    background-color: white;\n"
"}\n"
"\n"
"QPushButton#btn1:hover{\n"
"    background-color: gray;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton#btn1:pressed{\n"
"    background-color: white;\n"
"}")
        self.btn1.setObjectName("btn1")
        self.btn2 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press("2"))
        self.btn2.setGeometry(QtCore.QRect(90, 380, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.btn2.setFont(font)
        self.btn2.setStyleSheet("QPushButton#btn2{\n"
"    background-color: white;\n"
"}\n"
"\n"
"QPushButton#btn2:hover{\n"
"    background-color: gray;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton#btn2:pressed{\n"
"    background-color: white;\n"
"}")
        self.btn2.setObjectName("btn2")
        self.btn_eq = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.math())
        self.btn_eq.setGeometry(QtCore.QRect(250, 470, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.btn_eq.setFont(font)
        self.btn_eq.setStyleSheet("QPushButton#btn_eq{\n"
"    background-color: white;\n"
"}\n"
"\n"
"QPushButton#btn_eq:hover{\n"
"    background-color: gray;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton#btn_eq:pressed{\n"
"    background-color: white;\n"
"}")
        self.btn_eq.setObjectName("btn_eq")
        self.btn_pnt = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.dot())
        self.btn_pnt.setGeometry(QtCore.QRect(170, 470, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.btn_pnt.setFont(font)
        self.btn_pnt.setStyleSheet("QPushButton#btn_pnt{\n"
"    background-color: white;\n"
"}\n"
"\n"
"QPushButton#btn_pnt:hover{\n"
"    background-color: gray;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton#btn_pnt:pressed{\n"
"    background-color: white;\n"
"}")
        self.btn_pnt.setObjectName("btn_pnt")
        self.btn_pm = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.plus_minus())
        self.btn_pm.setGeometry(QtCore.QRect(10, 470, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.btn_pm.setFont(font)
        self.btn_pm.setStyleSheet("QPushButton#btn_pm{\n"
"    background-color: white;\n"
"}\n"
"\n"
"QPushButton#btn_pm:hover{\n"
"    background-color: gray;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton#btn_pm:pressed{\n"
"    background-color: white;\n"
"}")
        self.btn_pm.setObjectName("btn_pm")
        self.btn0 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press("0"))
        self.btn0.setGeometry(QtCore.QRect(90, 470, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.btn0.setFont(font)
        self.btn0.setStyleSheet("QPushButton#btn0{\n"
"    background-color: white;\n"
"}\n"
"\n"
"QPushButton#btn0:hover{\n"
"    background-color: gray;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton#btn0:pressed{\n"
"    background-color: white;\n"
"}")
        self.btn0.setObjectName("btn0")
        view.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(view)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 333, 26))
        self.menubar.setObjectName("menubar")
        view.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(view)
        self.statusbar.setObjectName("statusbar")
        view.setStatusBar(self.statusbar)

        self.retranslateUi(view)
        QtCore.QMetaObject.connectSlotsByName(view)

    def press(self, press):
        if press == "C":
            self.lbl_otp.setText("0")
        else:
            if self.lbl_otp.text() == "0":
                self.lbl_otp.setText("")
            self.lbl_otp.setText(f"{self.lbl_otp.text()}{press}")

    def dot(self):
        screen = self.lbl_otp.text()
        if screen[-1] == ".":
            pass
        else:
            self.lbl_otp.setText(f"{screen}")

    def remove(self):
        screen = self.lbl_otp.text()
        screen = screen[:-1]
        self.lbl_otp.setText(screen)

    def plus_minus(self):
        screen = self.lbl_otp.text()
        if "-" in screen:
            self.lbl_otp.setText(screen.replace("-", ""))
        else:
            self.lbl_otp.setText(f"-{screen}")

    def math(self):
        screen = self.lbl_otp.text()
        try:
            answer = eval(screen)
            self.lbl_otp.setText(str(answer))
        except:
            self.lbl_otp.setText("Error")


    def retranslateUi(self, view):
        _translate = QtCore.QCoreApplication.translate
        view.setWindowTitle(_translate("view", "MainWindow"))
        self.lbl_otp.setText(_translate("view", "0"))
        self.btn_prs.setText(_translate("view", "%"))
        self.btn_clr.setText(_translate("view", "C"))
        self.btn_div.setText(_translate("view", "/"))
        self.btn_flsh.setText(_translate("view", "<<"))
        self.btn_mul.setText(_translate("view", "x"))
        self.btn9.setText(_translate("view", "9"))
        self.btn7.setText(_translate("view", "7"))
        self.btn8.setText(_translate("view", "8"))
        self.btn_sub.setText(_translate("view", "-"))
        self.btn6.setText(_translate("view", "6"))
        self.btn4.setText(_translate("view", "4"))
        self.btn5.setText(_translate("view", "5"))
        self.btn_plus.setText(_translate("view", "+"))
        self.btn3.setText(_translate("view", "3"))
        self.btn1.setText(_translate("view", "1"))
        self.btn2.setText(_translate("view", "2"))
        self.btn_eq.setText(_translate("view", "="))
        self.btn_pnt.setText(_translate("view", "."))
        self.btn_pm.setText(_translate("view", "+/-"))
        self.btn0.setText(_translate("view", "0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    view = QtWidgets.QMainWindow()
    ui = Ui_view()
    ui.setupUi(view)
    view.show()
    sys.exit(app.exec_())
