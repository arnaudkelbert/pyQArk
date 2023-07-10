import sys
from PyQt5 import QtGui, QtCore, QtWidgets
    
count = 1
 
class Main(QtWidgets.QMainWindow):
 
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.initUI()
 
    def initUI(self):
 
        centralwidget = QtWidgets.QWidget()
 
        self.add = QtWidgets.QPushButton("Add")
        self.add.clicked.connect(self.Add)
         
 
        self.grid = QtWidgets.QGridLayout()
         
        self.grid.addWidget(self.add,0,0)
 
        centralwidget.setLayout(self.grid)
 
        self.setCentralWidget(centralwidget)
 
 
    #---------Window settings --------------------------------
         
        self.setGeometry(300,300,280,170)
        self.setWindowTitle("")
        self.setWindowIcon(QtGui.QIcon(""))
        self.setStyleSheet("background-color:")
        self.show()


    def Add(self):
        global count
     
        b = QtWidgets.QPushButton(str(count),self)
        b.clicked.connect(self.Button)
     
        self.grid.addWidget(b,count,0)
     
        count += 1


    def Button(self):
         
        sender = self.sender()
     
        print(sender.text())


def main():
    app = QtWidgets.QApplication(sys.argv)
    main = Main()
    main.show()
 
    sys.exit(app.exec_())
 
if __name__ == "__main__":
    main()


    


    
