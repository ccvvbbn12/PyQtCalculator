# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 21:14:50 2018

@author: LiangChih
"""

import sys 	
from PyQt5.QtWidgets import QApplication , QMainWindow
from PyQtCalculator import Ui_MainWindow

class MyMainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self, parent=None):
		super(MyMainWindow, self).__init__(parent)
		self.setupUi(self)
		
		self.pushButton_0.clicked.connect(self.fnBut0_clecked)
		self.pushButton_1.clicked.connect(self.fnBut1_clecked)
		self.pushButton_2.clicked.connect(self.fnBut2_clecked)
		self.pushButton_3.clicked.connect(self.fnBut3_clecked)
		self.pushButton_4.clicked.connect(self.fnBut4_clecked)
		self.pushButton_5.clicked.connect(self.fnBut5_clecked)
		self.pushButton_6.clicked.connect(self.fnBut6_clecked)
		self.pushButton_7.clicked.connect(self.fnBut7_clecked)
		self.pushButton_8.clicked.connect(self.fnBut8_clecked)
		self.pushButton_9.clicked.connect(self.fnBut9_clecked)
		self.pushButton_dot.clicked.connect(self.fnButDot_clecked)
		self.pushButton_sq.clicked.connect(self.fnButHat_clecked)
		self.pushButton_over.clicked.connect(self.fnButOver_clecked)
		self.pushButton_mul.clicked.connect(self.fnButMu_clecked)
		self.pushButton_sub.clicked.connect(self.fnButSub_clecked)
		self.pushButton_plus.clicked.connect(self.fnButPlus_clecked)
		self.pushButton_left.clicked.connect(self.fnButLeft_clecked)
		self.pushButton_right.clicked.connect(self.fnButRight_clecked)
		self.pushButton_equal.clicked.connect(self.fnButEqual_clecked)
		self.pushButton_cancel.clicked.connect(self.fnButCancel_clecked)
		
		
	def fnBut0_clecked(self):
		Text = self.label.text()
		Text += "0"
		self.label.setText(Text)
		
	def fnBut1_clecked(self):
		Text = self.label.text()
		Text += "1"
		self.label.setText(Text)
		
	def fnBut2_clecked(self):
		Text = self.label.text()
		Text += "2"
		self.label.setText(Text)
		
	def fnBut3_clecked(self):
		Text = self.label.text()
		Text += "3"
		self.label.setText(Text)
		
	def fnBut4_clecked(self):
		Text = self.label.text()
		Text += "4"
		self.label.setText(Text)
		
	def fnBut5_clecked(self):
		Text = self.label.text()
		Text += "5"
		self.label.setText(Text)
		
	def fnBut6_clecked(self):
		Text = self.label.text()
		Text += "6"
		self.label.setText(Text)
		
	def fnBut7_clecked(self):
		Text = self.label.text()
		Text += "7"
		self.label.setText(Text)
		
	def fnBut8_clecked(self):
		Text = self.label.text()
		Text += "8"
		self.label.setText(Text)
		
	def fnBut9_clecked(self):
		Text = self.label.text()
		Text += "9"
		self.label.setText(Text)
		
	def fnButHat_clecked(self):
		Text = self.label.text()
		Text += "^"
		self.label.setText(Text)
		
	def fnButDot_clecked(self):
		Text = self.label.text()
		Text += "."
		self.label.setText(Text)
		
	def fnButOver_clecked(self):
		Text = self.label.text()
		Text += "/"
		self.label.setText(Text)
		
	def fnButMu_clecked(self):
		Text = self.label.text()
		Text += "*"
		self.label.setText(Text)
		
	def fnButSub_clecked(self):
		Text = self.label.text()
		Text += "-"
		self.label.setText(Text)
		
	def fnButPlus_clecked(self):
		Text = self.label.text()
		Text += "+"
		self.label.setText(Text)
		
	def fnButLeft_clecked(self):
		Text = self.label.text()
		Text += "("
		self.label.setText(Text)
		
	def fnButRight_clecked(self):
		Text = self.label.text()
		Text += ")"
		self.label.setText(Text)
		
	def fnButEqual_clecked(self):
		Text = self.label.text()
		Text = Text.replace("^","**")
		
		try:
			result = eval(Text)
		except :
			self.label.setText("Error!")
		else:
			self.label.setText(str(result))
		
	def fnButCancel_clecked(self):
		self.label.setText("")
		
		
if __name__=="__main__":
	app = QApplication(sys.argv)
	myWin = MyMainWindow()
	myWin.show()
	sys.exit(app.exec_())
	
	
	
	
	 
