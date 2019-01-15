
from PyQt5 import * 
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import cv2,os
import numpy as np

class BtnLabel(QLabel):  
    def __init__(self,parent=None):  
        super(BtnLabel,self).__init__(parent)  
        self.if_mouse_press = False
        
        self.Rectangle_list = [0,0,1,1]
        
        self.Draw = "Rectangle"
 
    def mousePressEvent(self, e):
        
        self.Rectangle_list[0] = e.x()
        self.Rectangle_list[1] = e.y()
        print("start",self.Rectangle_list[0],self.Rectangle_list[1])
    def mouseReleaseEvent(self, e): 
        print(u"release")
        if e.button() == Qt.LeftButton:
            print(u"left")
        elif e.button() == Qt.RightButton:
            print(u"right")
        elif e.button() == Qt.MidButton:
            print(u"mid")
            

    def mouseMoveEvent(self, e):
        
        self.Rectangle_list[2] = e.x()-self.Rectangle_list[0]
        self.Rectangle_list[3] = e.y()-self.Rectangle_list[1]
        self.update()
    def paintEvent(self, e):
        
        super(BtnLabel,self).paintEvent(e)
        painter = QPainter(self)
        painter.setPen(QColor(166,66,250))          
        painter.begin(self) 
        #painter.drawLine((0,0),(100,800))
        #painter.drawLine(0,0,800,800)
        #painter.drawLine(self.Line_list[0],self.Line_list[1],self.Line_list[2],self.Line_list[3])
        painter.drawRect(self.Rectangle_list[0],self.Rectangle_list[1],self.Rectangle_list[2],self.Rectangle_list[3])
        #print(self.Line_list[0],self.Line_list[1],self.Line_list[2],self.Line_list[3])    
        painter.end() 
 
     
class MainDialog(QDialog):  
    def __init__(self,parent=None):  
        super(MainDialog,self).__init__(parent)  
        self.resize(1500, 700)
        self.bo=1
        
        self.Draw = "Rectangle"
        
        self.input_label = BtnLabel(self)  
        self.input_label.setGeometry(160, 40, 640, 480)  
        #self.input_label.setStyleSheet("background-color: rgb(255, 255, 255);")
        
        '''
        self.output_label = BtnLabel(self)  
        self.output_label.setGeometry(900, 40, 640, 480)  
        '''
 
 
        #set open file button
        self.open_btn = QPushButton(self)  
        self.open_btn.setObjectName("open_btn")  
        self.open_btn.setGeometry(1, 0, 100, 40)
 
        self.open_btn.setText("open")  
        self.open_btn.clicked.connect(self.on_button_load_clicked) 
 
        #set tailor button
        self.tailor_btn = QPushButton(self)  
        self.tailor_btn.setObjectName("tailor_btn")  
        self.tailor_btn.setGeometry(1, 60, 100, 40)
        self.tailor_btn.setText("tailor")  
        self.tailor_btn.clicked.connect(self.tailor)  
 
        #set save file button
        self.save_btn = QPushButton(self)  
        self.save_btn.setObjectName("save_btn")  
        self.save_btn.setGeometry(1, 120, 100, 40)
 
        self.save_btn.setText("save")  
        self.save_btn.clicked.connect(self.on_button_save_clicked)  
 
        #set add point button
        self.add_point_btn = QPushButton(self)  
        self.add_point_btn.setObjectName("add_point_btn")  
        self.add_point_btn.setGeometry(1, 180, 100, 40)
 
        self.add_point_btn.setText("add sqr")  
        self.add_point_btn.clicked.connect(self.on_button_edit_clicked)  
        
        
        
        #set erase point button
        self.erase_point_btn = QPushButton(self)  
        self.erase_point_btn.setObjectName("erase_point_btn")  
        self.erase_point_btn.setGeometry(1, 240, 100, 40)
 
        self.erase_point_btn.setText("draw sqr")  
        self.erase_point_btn.clicked.connect(self.draw_sqr)  
        
        
        
        
        #set add border button
        self.add_border_btn = QPushButton(self)  
        self.add_border_btn.setObjectName("black")  
        self.add_border_btn.setGeometry(1, 300, 100, 40)
        
        
        self.add_border_btn.setText("black")  
        self.add_border_btn.clicked.connect(self.black)  
        
        #set add border button
        self.white_btn = QPushButton(self)  
        self.white_btn.setObjectName("white")  
        self.white_btn.setGeometry(1, 360, 100, 40)
        
        
        self.white_btn.setText("white")  
        self.white_btn.clicked.connect(self.white) 
        
        '''
        #set result text
        self.text_label = QLabel(self)
        self.text_label.setAlignment(Qt.AlignCenter)  
        self.text_label.setGeometry(1, 360, 140, 100) 
        '''
        
        
    '''
    def open_file(self):
        img = cv2.imread(r"E:\qq\MobileFile\pyqt5 project\111.png")  
        if img is None:  
            print("Error: could not load image" ) 
            os._exit(0)  
          
        size = (int(self.input_label.width()),int(self.input_label.height())) 
        #img = cv2.resize(img, size, interpolation=cv2.INTER_AREA)  
        

        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
        
        #cv2.imshow('img', self.opencv_img)            
        self.QtImg = QImage(img.data, 
                            img.shape[1], 
                            img.shape[0],
                            img.shape[1]*3, 
                            QImage.Format_RGB888)     
        #self.input_label.resize()                                           
        self.input_label.setPixmap(QPixmap.fromImage(self.QtImg))
        print("11")
    '''
    def show_pic(self):
        size = (int(self.input_label.width()),int(self.input_label.height())) 
        #self.opencv_img = cv2.resize(self.opencv_img, size, interpolation=cv2.INTER_AREA) 
        
        
        #cv2.imshow('img', self.opencv_img) 
        if self.bo:
            self.opencv_img = cv2.cvtColor(self.opencv_img, cv2.COLOR_BGR2RGB) 
            self.bo=0 
        
                   
        self.QtImg = QImage(self.opencv_img.data, 
                                                self.opencv_img.shape[1], 
                                                self.opencv_img.shape[0],
                                                self.opencv_img.shape[1]*3, 
                                                QImage.Format_RGB888)
        self.input_label.resize(self.opencv_img.shape[1],self.opencv_img.shape[0])                                                  
        self.input_label.setPixmap(QPixmap.fromImage(self.QtImg))
        
    
    
    def on_button_load_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.imgName, _= QFileDialog.getOpenFileName(self, "openpicture", "1", "*.*")
        self.bo=1
        '''
        self.jpg = QPixmap(self.imgName).scaled(self.label.width(), self.label.height()) 
        self.label.setPixmap(self.jpg)
        '''
        self.opencv_img=cv2.imread(self.imgName)
        if self.opencv_img is  not None:
            print("already")
            self.show_pic()
    
    
    
    
    def tailor(self):
        print(self.input_label.Rectangle_list[0],self.input_label.Rectangle_list[1],self.input_label.Rectangle_list[2]+self.input_label.Rectangle_list[0],self.input_label.Rectangle_list[3]+self.input_label.Rectangle_list[1])
        #cropImg = self.opencv_img[self.input_label.Rectangle_list[1]:self.input_label.Rectangle_list[0],self.input_label.Rectangle_list[1]+self.input_label.Rectangle_list[3]:self.input_label.Rectangle_list[0]+self.input_label.Rectangle_list[2]]
        #cropImg = self.opencv_img[138:299,228:521]
        cropImg = self.opencv_img[self.input_label.Rectangle_list[1]:self.input_label.Rectangle_list[3]+self.input_label.Rectangle_list[1],self.input_label.Rectangle_list[0]:self.input_label.Rectangle_list[2]+self.input_label.Rectangle_list[0]]
        
        
        
        
        a=os.getcwd()
        print(a)

        a=a+'\\new floder'

        if not os.path.exists(a):
            os.mkdir(a)
            print(a)

        self.i=0
        print(a)
        b=a+'\\'+str(self.i)+".png" 
        while os.path.exists(b):
            self.i=self.i+1
            b=a+'\\'+str(self.i)+".png"
        cropImg = cv2.cvtColor(cropImg, cv2.COLOR_BGR2RGB)
        cv2.imwrite(b,cropImg)
        #cropImg = cv2.cvtColor(cropImg, cv2.COLOR_BGR2RGB)
        cv2.imshow("img2",cropImg)
    
    def black(self):
        triangle = np.array([[self.input_label.Rectangle_list[0],self.input_label.Rectangle_list[1]] , [self.input_label.Rectangle_list[0],self.input_label.Rectangle_list[1]+self.input_label.Rectangle_list[3]] , [self.input_label.Rectangle_list[0]+self.input_label.Rectangle_list[2],self.input_label.Rectangle_list[1]+self.input_label.Rectangle_list[3]] , [self.input_label.Rectangle_list[0]+self.input_label.Rectangle_list[2],self.input_label.Rectangle_list[1]] ])        
        cv2.fillPoly(self.opencv_img,[triangle],1)    
        self.show_pic()
    
    def white(self):
        triangle = np.array([[self.input_label.Rectangle_list[0],self.input_label.Rectangle_list[1]] , [self.input_label.Rectangle_list[0],self.input_label.Rectangle_list[1]+self.input_label.Rectangle_list[3]] , [self.input_label.Rectangle_list[0]+self.input_label.Rectangle_list[2],self.input_label.Rectangle_list[1]+self.input_label.Rectangle_list[3]] , [self.input_label.Rectangle_list[0]+self.input_label.Rectangle_list[2],self.input_label.Rectangle_list[1]] ])        
        cv2.fillPoly(self.opencv_img,[triangle],(255,255,255))    
        self.show_pic()
    '''
    def on_Button_test_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
 
     
        #self.timer_camera.start(10) 

        
        self.opencv_img=cv2.imread("111.png", 1)
        self.bo=1
        if self.opencv_img is None:
            print ('None')
        else:

            
            size = (int(self.input_label.width()),int(self.input_label.height()))  
            
            #print (self.label.width(),self.label.height())
            square = np.array([ [(0, 0), (200, 100), (200, 300), (0, 100)] ])
            #cv2.fillPoly(opencv_img, square, (169,169,169,0.2))
            
            cv2.line(opencv_img, tuple(square[0][0]), tuple(square[0][1]), (0, 0, 255), 1)
            cv2.line(opencv_img, tuple(square[0][1]), tuple(square[0][2]), (0, 0, 255), 2)
            cv2.line(opencv_img, tuple(square[0][2]), tuple(square[0][3]), (0, 0, 255), 3)
            cv2.line(opencv_img, tuple(square[0][3]), tuple(square[0][0]), (0, 0, 255), 4)
            
            
            cv2.polylines(self.opencv_img,[square],True,(0,0,255),3)
            
            self.opencv_img = cv2.resize(self.opencv_img, size, interpolation=cv2.INTER_AREA)  
            
            if self.bo:
                self.opencv_img = cv2.cvtColor(self.opencv_img, cv2.COLOR_BGR2RGB) 
                self.bo=0
            #cv2.imshow('img', self.opencv_img)
            self.QtImg = QImage(self.opencv_img.data, 
                                                    self.opencv_img.shape[1], 
                                                    self.opencv_img.shape[0],
                                                    self.opencv_img.shape[1]*3, 
                                                    QImage.Format_RGB888)
                                                        
            self.input_label.setPixmap(QPixmap.fromImage(self.QtImg))
            
            a=os.getcwd()
            print(a)

            a=a+'\\new floder'

            if not os.path.exists(a):
                os.mkdir(a)
                print(a)

            self.i=0
            b=a+'\\'+str(self.i)+".png" 
            while os.path.exists(b):
                self.i=self.i+1
                b=a+'\\'+str(self.i)+".png"
            
            self.opencv_img = cv2.cvtColor(self.opencv_img, cv2.COLOR_BGR2RGB) 
            cv2.imwrite(b,self.opencv_img)
            self.opencv_img = cv2.cvtColor(self.opencv_img, cv2.COLOR_BGR2RGB) 
            
    
 
        '''
    def on_button_save_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        a=os.getcwd()
        print(a)

        a=a+'\\new floder'

        if not os.path.exists(a):
            os.mkdir(a)
            print(a)

        self.i=0
        print(a)
        b=a+'\\'+str(self.i)+".png" 
        while os.path.exists(b):
            self.i=self.i+1
            b=a+'\\'+str(self.i)+".png"
        self.opencv_img = cv2.cvtColor(self.opencv_img, cv2.COLOR_BGR2RGB) 
        cv2.imwrite(b,self.opencv_img)
        self.opencv_img = cv2.cvtColor(self.opencv_img, cv2.COLOR_BGR2RGB) 
    
    
    def on_button_edit_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.a=Dialog()
        self.a.x=self.a.y=self.a.xl=self.a.yl=0
        self.a.exec_()
        
        
        square = np.array([ [(self.a.x, self.a.y), (self.a.x+self.a.xl, self.a.y), (self.a.x+self.a.xl, self.a.y+self.a.yl), (self.a.x, self.a.y+self.a.yl)] ])
        if self.a.radioButton.isChecked():
            cv2.fillPoly(self.opencv_img,[square],1)
        else:
            cv2.fillPoly(self.opencv_img,[square],(255,255,255))
        
        
        '''    
        square = np.array([ [(self.a.x, self.a.y), (self.a.x+self.a.xl, self.a.y), (self.a.x+self.a.xl, self.a.y+self.a.yl), (self.a.x, self.a.y+self.a.yl)] ])
        cv2.polylines(self.opencv_img,[square],True,(0,0,255),3)
        self.a.close()
        '''
        self.show_pic()
        
    
    
    def draw_sqr(self):
        square = np.array([ [(self.input_label.Rectangle_list[0],self.input_label.Rectangle_list[1]),(self.input_label.Rectangle_list[0],self.input_label.Rectangle_list[1]+self.input_label.Rectangle_list[3]),(self.input_label.Rectangle_list[0]+self.input_label.Rectangle_list[2],self.input_label.Rectangle_list[3]+self.input_label.Rectangle_list[1]),(self.input_label.Rectangle_list[0]+self.input_label.Rectangle_list[2],self.input_label.Rectangle_list[1]) ] ])
        cv2.polylines(self.opencv_img,[square],True,(0,0,255),3)
        self.show_pic()
        
           

    
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 376)
        self.label = QLabel(Dialog)
        self.label.setGeometry(QRect(30, 30, 81, 21))
        self.label.setObjectName("label")
        self.label_2 = QLabel(Dialog)
        self.label_2.setGeometry(QRect(150, 50, 16, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QLabel(Dialog)
        self.label_3.setGeometry(QRect(150, 90, 16, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QLabel(Dialog)
        self.label_4.setGeometry(QRect(103, 150, 71, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QLabel(Dialog)
        self.label_5.setGeometry(QRect(30, 120, 101, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QLabel(Dialog)
        self.label_6.setGeometry(QRect(103, 180, 71, 20))
        self.label_6.setObjectName("label_6")
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setGeometry(QRect(210, 50, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QRect(210, 90, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QRect(210, 140, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QRect(210, 180, 113, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setGeometry(QRect(150, 310, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.radioButton = QRadioButton(Dialog)
        self.radioButton.setGeometry(QRect(120, 220, 115, 19))
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QRadioButton(Dialog)
        self.radioButton_2.setGeometry(QRect(120, 260, 115, 19))
        self.radioButton_2.setObjectName("radioButton_2")

        self.retranslateUi(Dialog)
        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "start location"))
        self.label_2.setText(_translate("Dialog", "x:"))
        self.label_3.setText(_translate("Dialog", "y:"))
        self.label_4.setText(_translate("Dialog", "x length:"))
        self.label_5.setText(_translate("Dialog", "rectangle size"))
        self.label_6.setText(_translate("Dialog", "y length:"))
        self.lineEdit.setText(_translate("Dialog", "0"))
        self.lineEdit_2.setText(_translate("Dialog", "0"))
        self.lineEdit_3.setText(_translate("Dialog", "0"))
        self.lineEdit_4.setText(_translate("Dialog", "0"))
        self.pushButton.setText(_translate("Dialog", "ok"))
        self.radioButton.setText(_translate("Dialog", "black"))
        self.radioButton_2.setText(_translate("Dialog", "white"))

class Dialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.x=eval(str(self.lineEdit.text()))
        self.y=eval(str(self.lineEdit_2.text()))
        self.xl=eval(str(self.lineEdit_3.text()))
        self.yl=eval(str(self.lineEdit_4.text()))
        self.close()
 
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = MainDialog()
    ui.show()
    sys.exit(app.exec_())