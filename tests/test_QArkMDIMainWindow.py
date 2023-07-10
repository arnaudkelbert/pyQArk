import sys
import unittest
from PyQt5 import QtWidgets, QtCore

from pyQArk.MainWindows.QArkMDIMainWindow.QArkMDIMainWindow import QArkMDIMainWindow

class MainUI(QArkMDIMainWindow):

    def __init__(self, _s_logDir):
        """Constructeur"""
        super(MainUI, self).__init__(_s_logDir)

    def initUiComponents(self):
        super(MainUI, self).initUiComponents()

    def initUiSplitter(self):
        super(MainUI, self).initUiSplitter()

    def afterShow(self):
        t_sizes = self.ui_qSplitter.sizes()
        self.ui_qSplitter.setSizes([sum(t_sizes) - 60, 60])
        self.ui_qSplitter.updateGeometry()

    def createActions(self):
        """
        """
        super(MainUI, self).createActions()

    def createMenus(self):
        """
        """
        self.addActionMenu('FILE_MENU', 'File', None, ('QUIT_ACTION',))

TEST_CLASS = QArkMDIMainWindow
class QArkMDIMainWindowTest(unittest.TestCase):
    """
    Test
    """
    def test_widget(self):
        print(TEST_CLASS)
        o_app = QtWidgets.QApplication(sys.argv)
        o_mainWindow = MainUI(_s_logDir='./log')
        o_mainWindow.setWindowTitle(self.__class__.__name__+'.test_widget')
        o_mainWindow.show()
        o_mainWindow.afterShow()
        o_app.exec_()

if __name__ == '__main__':
    unittest.main()