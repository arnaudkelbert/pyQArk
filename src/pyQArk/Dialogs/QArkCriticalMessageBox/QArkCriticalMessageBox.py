from PyQt5 import QtWidgets
from pyQArk.Dialogs.QArkDialog import QArkDialog

class QArkCriticalMessageBox(QtWidgets.QMessageBox):

    def __init__(self, message, detailedMessage=None, *args, **kwargs):
        QtWidgets.QMessageBox.__init__(self, *args, **kwargs)
        self.setText( message )
        self.setStandardButtons( QtWidgets.QMessageBox.Ok )
        self.setIcon( QtWidgets.QMessageBox.Critical )
        if not detailedMessage is None:
            self.setDetailedText( detailedMessage )

    def exec_(self, _b_centered=True, **kwargs):
        # Reimplemented to get it centered
        if _b_centered:
            QArkDialog.centerDialog( self, **kwargs )
        QtWidgets.QMessageBox.exec_(self, **kwargs)
