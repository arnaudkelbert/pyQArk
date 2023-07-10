# -*- coding: utf-8 -*-
import unittest
import os
from pyQArk import QArkConfig

import PyQt5.uic as uic

class QArkUiCompiler( object ):

    @classmethod
    def autoname(cls, uifile):
        """
        Construct the name of the python file containing the ui class definitino
        according to pyQArk naming convention.

        Args:
            uifile: input ui file

        Returns:
            str: the name of the python file

        """
        s_path = os.path.normpath(os.path.abspath(uifile))
        # Automatic file naming depending on PyQt generation
        s_basename = os.path.splitext(os.path.basename(s_path))[0]
        pyfile = os.path.join(os.path.dirname(s_path), 'Ui_{}.py'.format(s_basename))
        return pyfile

    @classmethod
    def compile(cls, uifile, pyfile='auto', **kwargs):
        s_path = os.path.normpath(os.path.abspath(uifile))
        isfp = False
        if pyfile == 'auto':
            pyfile = cls.autoname(uifile)
        else:
            try:
                pyfile.seek(0)
            except AttributeError:
                isfp = False
            else:
                isfp = True
        if not isfp:
            try:
                # compileUi file-object opening mode can made the
                # writing fail : 'wb' for python 2, 'w' for python 3
                with open(pyfile,'wb') as fp:
                    cls.compileUi(s_path, fp, **kwargs)
            except TypeError:
                with open(pyfile,'w') as fp:
                    cls.compileUi(s_path, fp, **kwargs)
        else:
            # pyfile is already a file pointer
            cls.compileUi(s_path, pyfile, **kwargs)

    @classmethod
    def compileUi(cls, uifile, pyfile, **kwargs):
        """
        Call uic compile

        Args:
            uifile: input ui file
            pyfile: path of file object for the compiled file
            **kwargs: uic.compile parameters

        Returns:
            None
        """
        uic.compileUi(uifile, pyfile, **kwargs)

class QArkUiCompilerTest(unittest.TestCase):

    def test_me(self):
        QArkUiCompiler.compile(os.path.join(QArkConfig.QARK_ROOT_DIR, 'Tests', 'TestUi.ui'))

if __name__ == '__main__':
    unittest.main()