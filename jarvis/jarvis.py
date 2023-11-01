from Brain.AIBrain import ReplyBrain
from Brain.QNA import QuestionAnswer
from Body.Speak import Speak
import sys
Speak("Starting Jarvis : Wait For Few Seconds")
from Body.Listen import MicExecusion
from Main import MaintaskExecution
from jarvisui import Ui_Dialog
from PyQt5 import QtCore , QtWidgets , QtGui
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType
Speak("Starting Jarvis")


class Mainthread(QThread):

    def __init__(self):
        super(Mainthread,self).__init__()

    def run(self):
        self.MainExecusion()

    def MainExecusion(self):

        Speak("Hello Sir")
        Speak("Jarvis is ready to assist you")

        while True:

            self.Data = MicExecusion()
            self.data = str(self.Data)

            self.ValueReturn = MaintaskExecution(self.data)
            if self.ValueReturn==True:
                pass

            elif len(self.data)<3:
                pass

            elif "what" in self.data or "where" in self.data:
                self.Reply = QuestionAnswer(self.data)
                Speak(self.Reply)

            else:
                self.Reply = ReplyBrain(self.data)
                Speak(self.Reply)

startFunction = Mainthread()

class Gui_Start(QMainWindow):

    def __init__(self):
        super().__init__()
        self.Jarvis_ui = Ui_Dialog()
        self.Jarvis_ui.setupUi(self)

        self.Jarvis_ui.pushButton.clicked.connect(self.startFunc)

    def startFunc(self):
        self.Jarvis_ui.movies= QtGui.QMovie("Qualt.gif")
        self.Jarvis_ui.label.setMovie(self.Jarvis_ui.movies)
        self.Jarvis_ui.movies.start()

        timer = QTimer(self)
        timer.timeout.connect(self.showTimeLive)
        timer.start(999)

        startFunction.start()
    
    def showTimeLive(self):
        timee = QTime.currentTime()
        time = timee.toString()
        label_time = "Time :" + time

        self.Jarvis_ui.textBrowser.setText(label_time)

Gui_App = QApplication(sys.argv)
Gui_Jarvis = Gui_Start()
Gui_Jarvis.show()
exit(Gui_App.exec_())