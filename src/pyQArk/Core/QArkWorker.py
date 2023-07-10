# -*- coding: utf-8 -*-
from pyQArk import QArkConfig

if QArkConfig.QARK_QT_THREADING_MECHANISM == QArkConfig.QARK_QT_THREADING_QTHREAD_SUBCLASSING:
    from pyQArk.Core.QArkWorker_QThreadSubclassing import QArkWorker_QThreadSubclassing
    QArkWorker = QArkWorker_QThreadSubclassing

elif QArkConfig.QARK_QT_THREADING_MECHANISM == QArkConfig.QARK_QT_THREADING_EVENT_DRIVEN:
    from pyQArk.Core.QArkWorker_EventDriven import QArkWorker_EventDriven
    QArkWorker = QArkWorker_EventDriven

