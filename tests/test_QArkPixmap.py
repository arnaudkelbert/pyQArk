import sys
import unittest
from PyQt5 import QtWidgets, QtGui

from pyQArk.Image.QArkPixmap import QArkPixmap
from pyQArk.Image.QArkHistogramEqualization import QArkHistogramEqualization
from pyQArk.Image.QArkColorMapManager import QArkColorMapManager
import numpy as np

TEST_CLASS = QArkPixmap
class QArkPixmapTest(unittest.TestCase):
    """
    Test
    """
    class _ControllerWidget(QtWidgets.QWidget):
        def __init__(self, parent):
            super(self.__class__, self).__init__(parent)
            self.initUi()

        def initUi(self):
            self.o_layout = QtWidgets.QVBoxLayout(self)

            L=400
            C=400
            t_data = np.arange(L*C).reshape((L,C))/(L*C)*255
            t_data = t_data.astype(int)
            pixmap = QArkPixmap()
            pixmap.initFromGreyData(_t_data=t_data, _o_colorMap=QArkColorMapManager().getColorMap('GREY'))
            self.o_widget = QtWidgets.QLabel()
            self.o_widget.setPixmap(pixmap.getPixmap())
            self.o_layout.addWidget(self.o_widget)

            #Test QPixmap directly
            import os
            from pyQArk import QArkConfig
            s_img = os.path.join(QArkConfig.QARK_ROOT_DIR, 'Tests', 'pixmap.png')
            #o_image2 = QtGui.QImage('./pixmap_grey.png')
            o_image2 = QtGui.QImage(s_img)
            #o_image2 = QtGui.QImage('./pixmap.jpg')
            o_pixmap2 = QtGui.QPixmap.fromImage(o_image2)
            self.o_widget2 = QtWidgets.QLabel()
            self.o_widget2.setPixmap(o_pixmap2)
            self.o_layout.addWidget(self.o_widget2)

    def test_widget(self):
        print(TEST_CLASS)
        o_app = QtWidgets.QApplication(sys.argv)
        o_mainWindow = QtWidgets.QDialog()
        o_layout = QtWidgets.QVBoxLayout(o_mainWindow)
        o_widget = self.__class__._ControllerWidget(parent=o_mainWindow)
        o_layout.addWidget(o_widget)
        o_mainWindow.setLayout(o_layout)
        o_mainWindow.setWindowTitle(self.__class__.__name__+'.test_widget')
        o_mainWindow.show()
        o_app.exec_()

if __name__ == '__main__':
    unittest.main()