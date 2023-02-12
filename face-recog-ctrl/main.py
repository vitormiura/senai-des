from PyQt5 import QtWidgets, uic 
import sys
from gui import gui
import faceDetecEmail as face
import faceDetection as test
import imageTraining as encoding
import userDelete as delete 
import faceShot as shot

class Menu(gui.Ui_MainWindow):
    def __init__(self, menu_principal):
        self.setupUi(menu_principal)
        self.pushButton.clicked.connect(self.newCad)
        self.pushButton_2.clicked.connect(self.rmvCad)
        self.pushButton_3.clicked.connect(self.runEncondings)
        self.pushButton_4.clicked.connect(self.runSys)
        self.pushButton_5.clicked.connect(self.runTest)
        
    def newCad(self):
        shot.shot()
    
    def rmvCad(self):
        delete.delShot()
    
    def runEncondings(self):
        encoding.encoding()

    def runSys(self):
        face.main()

    def runTest(self):
        test.teste()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = QtWidgets.QMainWindow()
    m = Menu(main)
    main.show()
    sys.exit(app.exec_())
