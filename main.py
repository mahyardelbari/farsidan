from hazm import *
from styles.mainwindow import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox 
import sys
import farsi.farsidan
from PyQt5.QtCore import QObject




class screen(QMainWindow):
    def __init__(self):
        super(screen, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('فارسی دان')
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.result_naghsh.setWordWrap(True)
        self.ui.result_bakhsh.setWordWrap(True)
        self.ui.result_fel.setWordWrap(True)
        self.ui.result_mofrad.setWordWrap(True)
        self.ui.result_mani.setWordWrap(True)
        self.ui.result_emla.setWordWrap(True)
        self.ui.lineEdit_fel.setPlaceholderText("رفتم,خوردم,...")
        self.ui.lineEdit_mofrad.setPlaceholderText("دانشمندان,خدایان,...")
        self.ui.lineEdit_mani.setPlaceholderText('بهایم,خلق,...')
        self.ui.lineEdit_paye_emla.setPlaceholderText('اول')
        self.ui.lineEdit_darsa_emla.setPlaceholderText('1,2,3,...')


    
    def on_btn_naghsh_dastory_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(1)
    
    def on_btn_bakhsbandi_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def on_btn_rishe_fel_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def on_btn_mofrad_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(4)
        QMessageBox.information(self, 'توجه', 'کاربر گرامی تشخیص مفرد جمع های مکسر به زودی اضافه خواهد شد\nبا تشکر از صبر شما')
        sender = QObject.sender(self)
        sender.clicked.disconnect()
        self.ui.btn_mofrad.clicked.connect(self.on_btn_mofrad_clicked)
        
    def on_btn_mani_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(5)
        QMessageBox.information(self,"توجه","معنی تمام کلمات از لغت نامه ی دهخدا جمع اوری شده است")
        sender = QObject.sender(self)
        sender.clicked.disconnect()
        self.ui.btn_mani.clicked.connect(self.on_btn_mani_clicked)

    def on_btn_emla_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(6)
        QMessageBox.information(self,"توجه","این بخش به اینترنت و فیلتر شکن نیاز دارد")
        sender = QObject.sender(self)
        sender.clicked.disconnect()
        self.ui.btn_emla.clicked.connect(self.on_btn_emla_clicked)

# back buttons
    def on_back_4_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(0)
    def on_back_1_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(0)
    def on_back_2_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(0)
    def on_back_3_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(0)
    def on_back_5_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(0)
    def on_back_6_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(0)
#naghs
    def on_btn_javab_naghsh_clicked(self):
        farsi.farsidan.naghsh(self)
            
#bakhsh bandi
    def on_btn_javab_bakhsh_clicked(self):
        farsi.farsidan.bakhsh(self)

#rishe fel
    def on_btn_javab_fel_clicked(self):
        farsi.farsidan.rishe_fel(self)

#mofrad 
    def on_btn_javab_mofrad_clicked(self):
        farsi.farsidan.mofrad(self)

#mani
    def on_btn_javab_mani_clicked(self):
        farsi.farsidan.mani(self)


#close event     
    def closeEvent(self, event):
        reply = QMessageBox.question(
            self,
            'تأیید',
            'آیا مطمئن هستید که می خواهید خارج شوید؟',
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()



app = QApplication(sys.argv)
window = screen()
window.show()
sys.exit(app.exec())