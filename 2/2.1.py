import sys
from PyQt5.QtWidgets import QApplication,QWidget
app = QApplication(sys.argv)
mywin = QWidget() # 实例化一个窗口小部件
mywin.setWindowTitle('Hello world!') # 设置窗口标题
mywin.show() #显示窗口
sys.exit(app.exec())
