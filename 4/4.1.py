from form import Ui_Form
from PyQt5.QtWidgets import *
import sys


class MyWin(QWidget,Ui_Form):
    """docstring for Mywine"""
    def __init__(self):
        super(MyWin, self).__init__()
        self.setupUi(self)

    def test(self): # 这里test就是槽函数, 当点击按钮时执行 test 函数中的内容, 注意有一个参数为 self
        print('hello world!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywin = MyWin() # 实例化一个窗口小部件
    mywin.setWindowTitle('Hello world!') # 设置窗口标题
    mywin.show() #显示窗口
    sys.exit(app.exec())
