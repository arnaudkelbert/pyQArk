# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
# 
#
# Tests.test_dynamicAdd
# 
#
# @author : Arnaud Kelbert
# @date : Nov 21, 2014
# @version : 0.1
#-----------------------------------------------------------------------
import sys, os
from PyQt4 import QtGui, QtCore
    
count = 1
 
S_GIF='/home/kelberta/sentinel2_2/ASTERIX/extern/pyQArk/pyQArk/Media/loader.gif'
 
class Main(QtGui.QMainWindow):
 
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.initUI()
 
    def initUI(self):
 
        centralwidget = QtGui.QWidget()
 
        self.label = QtGui.QLabel(self)
        self.movie = QtGui.QMovie(S_GIF)
	
	print os.path.exists(S_GIF)
	print QtGui.QMovie.supportedFormats()
        print self.movie.isValid()
	
        self.label.setMovie(self.movie)
        self.movie.start()
        
        self.msg = QtGui.QLabel('Please wait...')
    
       
 
        self.grid = QtGui.QGridLayout()
         
        self.grid.addWidget(self.label,0,0)
        self.grid.addWidget(self.msg,1,0)
 
        centralwidget.setLayout(self.grid)
 
        self.setCentralWidget(centralwidget)
 
 
    #---------Window settings --------------------------------
         
        self.setGeometry(300,300,280,170)
        self.setWindowTitle("")
        self.setWindowIcon(QtGui.QIcon(""))
        self.setStyleSheet("background-color:")
        self.show()



def main():
    app = QtGui.QApplication(sys.argv)
    main = Main()
    main.show()
 
    sys.exit(app.exec_())
 
if __name__ == "__main__":
    main()


    


    
