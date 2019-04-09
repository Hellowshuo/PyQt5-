from form import Ui_Form
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread, pyqtSignal
import sys
import time

class MyWin(QWidget,Ui_Form):
    """docstring for Mywine"""
    def __init__(self):
        super(MyWin, self).__init__()
        self.setupUi(self)
        self.mythread = MyThread() # 实例化自己建立的任务线程类
        self.mythread.signal.connect(self.callback) #设置任务线程发射信号触发的函数

    def test(self): # 这里test就是槽函数, 当点击按钮时执行 test 函数中的内容, 注意有一个参数为 self
        self.mythread.data = 5 # 这句就是给线程的实例化一个属性给其赋值，在线程里面就可以调用了
        self.mythread.start() # 启动任务线程

    def callback(self,i): # 这里的 i 就是任务线程传回的数据
        self.pushButton.setText(i)

class MyThread(QThread): # 建立一个任务线程类
    signal = pyqtSignal(str) #设置触发信号传递的参数数据类型,这里是字符串
    def __init__(self):
        super(MyThread, self).__init__()

    def run(self): # 在启动线程后任务从这个函数里面开始执行
        print(self.data) # 调用传递过来的数据

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywin = MyWin() # 实例化一个窗口小部件
    mywin.setWindowTitle('Hello world!') # 设置窗口标题
    mywin.show() #显示窗口
    sys.exit(app.exec())
