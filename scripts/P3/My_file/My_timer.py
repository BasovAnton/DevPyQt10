
import psutil
import requests
from PySide2 import QtCore, QtWidgets


class MyTimer(QtCore.QThread):
    timeLeftSignal = QtCore.Signal(int)

    def setTimer(self, count):
        self.__timerCount = count

    def run(self):
        self.status = True

        while self.status:
            if not self.__timerCount == 0:
                self.__timerCount -= 1
                time.sleep(1)
                self.timeLeftSignal.emit(self.__timerCount)
            else:
                self.status = False