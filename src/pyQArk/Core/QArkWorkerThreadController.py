# -*- coding: utf-8 -*-
from pyQArk import QArkConfig

if QArkConfig.QARK_QT_THREADING_MECHANISM == QArkConfig.QARK_QT_THREADING_QTHREAD_SUBCLASSING:
    from pyQArk.Core.QArkWorkerThreadController_QThreadSubclassing import QArkWorkerThreadController_QThreadSubclassing
    QArkWorkerThreadController = QArkWorkerThreadController_QThreadSubclassing

elif QArkConfig.QARK_QT_THREADING_MECHANISM == QArkConfig.QARK_QT_THREADING_EVENT_DRIVEN:
    from pyQArk.Core.QArkWorkerThreadController_EventDriven import QArkWorkerThreadController_EventDriven
    QArkWorkerThreadController = QArkWorkerThreadController_EventDriven

