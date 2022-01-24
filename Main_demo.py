import sys

from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow

import win_demo


if __name__ == '__main__':

    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = win_demo.Ui_MainWindow()#UI.py文件名
    ui.setupUi(mainWindow)
    # 窗口标题
    mainWindow.setWindowTitle("湿热一瞬间")
    mainWindow.setPalette(QPalette(QColor(255, 255, 255)))
    # 显示窗口
    mainWindow.show()

    # 进入循环
    sys.exit(app.exec_())



