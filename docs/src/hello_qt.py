from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication,QWidget,QPushButton,QMainWindow
from PySide6 import __version__
def click_call():
    print("被点击",__version__)

def click_call_2(e):print("～～～",e),

app = QApplication([])
window = QMainWindow()
window.setWindowTitle("Qt程序中文测试")
window.setFixedSize(QSize(400,300))
button = QPushButton("点击我😯")
button.setCheckable(True)
button.clicked.connect(click_call)
button.clicked.connect(click_call_2)
window.setCentralWidget(button)
window.show()
app.exec()