# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\img_test\AoprChk_app\MPRtest.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.splitter_4 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName("splitter_4")
        self.splitter_3 = QtWidgets.QSplitter(self.splitter_4)
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName("splitter_3")
        self.splitter = QtWidgets.QSplitter(self.splitter_3)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.Axial_widget = QtWidgets.QWidget(self.splitter)
        self.Axial_widget.setMinimumSize(QtCore.QSize(0, 200))
        self.Axial_widget.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.Axial_widget.setObjectName("Axial_widget")
        self.Axial_horizontalLayout = QtWidgets.QVBoxLayout(self.Axial_widget)
        self.Axial_horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.Axial_horizontalLayout.setSpacing(0)
        self.Axial_horizontalLayout.setObjectName("Axial_horizontalLayout")
        self.Sagittal_widget = QtWidgets.QWidget(self.splitter)
        self.Sagittal_widget.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.Sagittal_widget.setObjectName("Sagittal_widget")
        self.Sagittal_horizontalLayout = QtWidgets.QVBoxLayout(self.Sagittal_widget)
        self.Sagittal_horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.Sagittal_horizontalLayout.setSpacing(0)
        self.Sagittal_horizontalLayout.setObjectName("Sagittal_horizontalLayout")
        self.splitter_2 = QtWidgets.QSplitter(self.splitter_3)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.Coronal_widget = QtWidgets.QWidget(self.splitter_2)
        self.Coronal_widget.setMinimumSize(QtCore.QSize(0, 200))
        self.Coronal_widget.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.Coronal_widget.setObjectName("Coronal_widget")
        self.Coronal_horizontalLayout = QtWidgets.QVBoxLayout(self.Coronal_widget)
        self.Coronal_horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.Coronal_horizontalLayout.setSpacing(0)
        self.Coronal_horizontalLayout.setObjectName("Coronal_horizontalLayout")
        self.Slicer3D_widget = QtWidgets.QWidget(self.splitter_2)
        self.Slicer3D_widget.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.Slicer3D_widget.setObjectName("Slicer3D_widget")
        self.Slicer3D_horizontalLayout = QtWidgets.QVBoxLayout(self.Slicer3D_widget)
        self.Slicer3D_horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.Slicer3D_horizontalLayout.setSpacing(0)
        self.Slicer3D_horizontalLayout.setObjectName("Slicer3D_horizontalLayout")
        self.WL_widget = QtWidgets.QWidget(self.splitter_4)
        self.WL_widget.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.WL_widget.setObjectName("WL_widget")
        self.WL_verticalLayout = QtWidgets.QVBoxLayout(self.WL_widget)
        self.WL_verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.WL_verticalLayout.setSpacing(0)
        self.WL_verticalLayout.setObjectName("WL_verticalLayout")
        self.verticalLayout_6.addWidget(self.splitter_4)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.test1 = QtWidgets.QPushButton(self.centralwidget)
        self.test1.setObjectName("test1")
        self.horizontalLayout.addWidget(self.test1)
        self.test2 = QtWidgets.QPushButton(self.centralwidget)
        self.test2.setObjectName("test2")
        self.horizontalLayout.addWidget(self.test2)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.test1.setText(_translate("MainWindow", "test1"))
        self.test2.setText(_translate("MainWindow", "test2"))
