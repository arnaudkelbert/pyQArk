# -*- coding: utf-8 -*-
from pyQArk import QArkConfig

if QArkConfig.QARK_QT_THREADING_MECHANISM == QArkConfig.QARK_QT_THREADING_QTHREAD_SUBCLASSING:
    from pyQArk.Core.QArkWorkerThread_QThreadSubclassing import QArkWorkerThread_QThreadSubclassing
    QArkWorkerThread = QArkWorkerThread_QThreadSubclassing
else:
    QArkWorkerThread = None
