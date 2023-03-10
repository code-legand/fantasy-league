# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'evaluate_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import dbaccess
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(609, 354)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        Form.setFont(font)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label1 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setBold(True)
        font.setWeight(75)
        self.label1.setFont(font)
        self.label1.setAlignment(QtCore.Qt.AlignCenter)
        self.label1.setObjectName("label1")
        self.verticalLayout.addWidget(self.label1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.combo1 = QtWidgets.QComboBox(Form)
        self.combo1.setObjectName("combo1")
        
        self.load_teams()
        self.combo1.currentIndexChanged.connect(self.load_list)
        
        self.horizontalLayout.addWidget(self.combo1)
        self.combo2 = QtWidgets.QComboBox(Form)
        self.combo2.setObjectName("combo2")
        
        self.load_matches()
         
        self.horizontalLayout.addWidget(self.combo2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label2 = QtWidgets.QLabel(Form)
        self.label2.setObjectName("label2")
        self.verticalLayout_2.addWidget(self.label2)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.listWidget1 = QtWidgets.QListWidget(Form)
        self.listWidget1.setObjectName("listWidget1")
        self.horizontalLayout_11.addWidget(self.listWidget1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label3 = QtWidgets.QLabel(Form)
        self.label3.setObjectName("label3")
        self.horizontalLayout_4.addWidget(self.label3)
        self.line1 = QtWidgets.QLineEdit(Form)
        self.line1.setReadOnly(True)
        self.line1.setObjectName("line1")
        self.horizontalLayout_4.addWidget(self.line1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.listWidget2 = QtWidgets.QListWidget(Form)
        self.listWidget2.setObjectName("listWidget2")
        self.horizontalLayout_6.addWidget(self.listWidget2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_12.addLayout(self.verticalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout_12)
        self.pushButton1 = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton1.setFont(font)
        self.pushButton1.setObjectName("pushButton1")
        
        self.pushButton1.clicked.connect(self.display_score)
        
        self.verticalLayout.addWidget(self.pushButton1)
        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
        
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Evaluate"))
        self.label1.setText(_translate("Form", "Evaluate the Performance of your Fantasy Team"))
        self.label2.setText(_translate("Form", "Players"))
        self.label3.setText(_translate("Form", "Points"))
        self.pushButton1.setText(_translate("Form", "Calculate Score"))
    
    team_names=[]
    points=[]

    #------------loading items to combo box 1---------------
    def load_teams(self):
        command="SELECT name FROM teams;"
        data=dbaccess.read_data(command)
        #print(data)
        for i in data:
            if i[0] not in self.team_names:
                self.team_names.append(i[0])
        self.add_combo1()
      
    #-------------------called by load_teams function------------      
    def add_combo1(self):
        self.combo1.addItem('<Select Team>')
        for name in self.team_names:
            self.combo1.addItem(name)
    
    #------------------loading combo box 2-------------------------
    def load_matches(self):
        self.combo2.addItem('<Select Match>')
        for i in range(10):
            self.combo2.addItem("Match {}".format(i+1))
    
    #------------------filling list 1 with player names and list 2 with points--------------
    def load_list(self):
        team_name=self.combo1.currentText()
        command="SELECT players, value FROM teams WHERE name='{}'".format(team_name)
        data=dbaccess.read_data(command)
        #self.team_names=[x[0] for x in data]
        self.points=[x[1] for x in data]
        for x in data:
           self.listWidget1.addItem(x[0])
           self.listWidget2.addItem(str(x[1]))
    
    #-----------------------displaying the total points scored by the team----------       
    def display_score(self):
        self.line1.setText(str(sum(self.points)))
        

        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
