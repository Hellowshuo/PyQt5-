import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QVBoxLayout
# 创建一个类，这个类继承了QWidget
class Mywin(QWidget):
    def __init__(self):
        super(Mywin, self).__init__()
        button = QPushButton("OK") #实例化一个按钮控件
        layout = QVBoxLayout(self) #实例化一个水平布局
        layout.addWidget(button) #在软件布局中添加按钮控件
        self.setLayout(layout) #将这个类设置为水平布局


app = QApplication(sys.argv)
mywin = Mywin() # 实例化一个窗口小部件
mywin.setWindowTitle('Hello world!') # 设置窗口标题
mywin.show() #显示窗口
sys.exit(app.exec())