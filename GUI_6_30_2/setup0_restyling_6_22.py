# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setup0_restyling_continued.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_Dialog(object):
    def __init__(self, TDC_inst):
        self.TDC_inst = TDC_inst


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1118, 657)

        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(20, 540, 1071, 101))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")


        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_6)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_6.addWidget(self.pushButton)
        self.pushButton.clicked.connect(Dialog.reject)

        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_6)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_6.addWidget(self.pushButton_2)
        self.pushButton_2.clicked.connect(Dialog.reject)

        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget_6)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_6.addWidget(self.pushButton_3)
        self.pushButton_3.clicked.connect(Dialog.reject)


        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 20, 1071, 261))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.checkBox_84 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_84.setObjectName("checkBox_84")
        self.gridLayout.addWidget(self.checkBox_84, 6, 1, 1, 1)
        self.checkBox_85 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_85.setObjectName("checkBox_85")
        self.gridLayout.addWidget(self.checkBox_85, 0, 2, 1, 1)
        self.checkBox_89 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_89.setObjectName("checkBox_89")
        self.gridLayout.addWidget(self.checkBox_89, 5, 2, 1, 1)
        self.checkBox_87 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_87.setObjectName("checkBox_87")
        self.gridLayout.addWidget(self.checkBox_87, 2, 2, 1, 1)
        self.checkBox_7 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_7.setObjectName("checkBox_7")
        self.gridLayout.addWidget(self.checkBox_7, 1, 1, 1, 1)
        self.checkBox_6 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_6.setObjectName("checkBox_6")
        self.gridLayout.addWidget(self.checkBox_6, 0, 1, 1, 1)
        self.checkBox_3 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout.addWidget(self.checkBox_3, 2, 0, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 0, 0, 1, 1)
        self.checkBox_93 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_93.setObjectName("checkBox_93")
        self.gridLayout.addWidget(self.checkBox_93, 3, 2, 1, 1)
        self.checkBox_92 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_92.setObjectName("checkBox_92")
        self.gridLayout.addWidget(self.checkBox_92, 4, 0, 1, 1)
        self.checkBox_5 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_5.setObjectName("checkBox_5")
        self.gridLayout.addWidget(self.checkBox_5, 6, 0, 1, 1)
        self.checkBox_4 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout.addWidget(self.checkBox_4, 5, 0, 1, 1)
        self.checkBox_83 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_83.setObjectName("checkBox_83")
        self.gridLayout.addWidget(self.checkBox_83, 5, 1, 1, 1)
        self.checkBox_9 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_9.setObjectName("checkBox_9")
        self.gridLayout.addWidget(self.checkBox_9, 3, 1, 1, 1)
        self.checkBox_8 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_8.setObjectName("checkBox_8")
        self.gridLayout.addWidget(self.checkBox_8, 2, 1, 1, 1)
        self.checkBox_88 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_88.setObjectName("checkBox_88")
        self.gridLayout.addWidget(self.checkBox_88, 4, 2, 1, 1)
        self.checkBox_10 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_10.setObjectName("checkBox_10")
        self.gridLayout.addWidget(self.checkBox_10, 4, 1, 1, 1)
        self.checkBox_90 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_90.setObjectName("checkBox_90")
        self.gridLayout.addWidget(self.checkBox_90, 6, 2, 1, 1)
        self.checkBox_86 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_86.setObjectName("checkBox_86")
        self.gridLayout.addWidget(self.checkBox_86, 1, 2, 1, 1)
        self.checkBox_91 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_91.setObjectName("checkBox_91")
        self.gridLayout.addWidget(self.checkBox_91, 3, 0, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout.addWidget(self.checkBox_2, 1, 0, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(20, 310, 891, 121))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.checkBox_26 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_26.setText("")
        self.checkBox_26.setObjectName("checkBox_26")
        self.gridLayout_2.addWidget(self.checkBox_26, 1, 16, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_15.setObjectName("label_15")
        self.gridLayout_2.addWidget(self.label_15, 0, 13, 1, 1)
        self.checkBox_29 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_29.setText("")
        self.checkBox_29.setObjectName("checkBox_29")
        self.gridLayout_2.addWidget(self.checkBox_29, 1, 19, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_29.setObjectName("label_29")
        self.gridLayout_2.addWidget(self.label_29, 2, 0, 1, 1)
        self.checkBox_28 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_28.setText("")
        self.checkBox_28.setObjectName("checkBox_28")
        self.gridLayout_2.addWidget(self.checkBox_28, 1, 18, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_19.setObjectName("label_19")
        self.gridLayout_2.addWidget(self.label_19, 0, 17, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 2, 1, 1)
        self.checkBox_30 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_30.setText("")
        self.checkBox_30.setObjectName("checkBox_30")
        self.gridLayout_2.addWidget(self.checkBox_30, 1, 20, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 3, 1, 1)
        self.checkBox_17 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_17.setText("")
        self.checkBox_17.setObjectName("checkBox_17")
        self.gridLayout_2.addWidget(self.checkBox_17, 1, 7, 1, 1)
        self.checkBox_37 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_37.setText("")
        self.checkBox_37.setObjectName("checkBox_37")
        self.gridLayout_2.addWidget(self.checkBox_37, 2, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 0, 9, 1, 1)
        self.checkBox_38 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_38.setText("")
        self.checkBox_38.setObjectName("checkBox_38")
        self.gridLayout_2.addWidget(self.checkBox_38, 2, 2, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_30.setObjectName("label_30")
        self.gridLayout_2.addWidget(self.label_30, 3, 0, 1, 1)
        self.checkBox_39 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_39.setText("")
        self.checkBox_39.setObjectName("checkBox_39")
        self.gridLayout_2.addWidget(self.checkBox_39, 2, 3, 1, 1)
        self.checkBox_15 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_15.setText("")
        self.checkBox_15.setObjectName("checkBox_15")
        self.gridLayout_2.addWidget(self.checkBox_15, 1, 5, 1, 1)
        self.checkBox_20 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_20.setText("")
        self.checkBox_20.setObjectName("checkBox_20")
        self.gridLayout_2.addWidget(self.checkBox_20, 1, 10, 1, 1)
        self.checkBox_16 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_16.setText("")
        self.checkBox_16.setObjectName("checkBox_16")
        self.gridLayout_2.addWidget(self.checkBox_16, 1, 6, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.checkBox_11 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_11.setText("")
        self.checkBox_11.setObjectName("checkBox_11")
        self.gridLayout_2.addWidget(self.checkBox_11, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 1, 1, 1)
        self.checkBox_22 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_22.setText("")
        self.checkBox_22.setObjectName("checkBox_22")
        self.gridLayout_2.addWidget(self.checkBox_22, 1, 12, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 0, 7, 1, 1)
        self.checkBox_12 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_12.setText("")
        self.checkBox_12.setObjectName("checkBox_12")
        self.gridLayout_2.addWidget(self.checkBox_12, 1, 2, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_18.setObjectName("label_18")
        self.gridLayout_2.addWidget(self.label_18, 0, 16, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 0, 4, 1, 1)
        self.checkBox_19 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_19.setText("")
        self.checkBox_19.setObjectName("checkBox_19")
        self.gridLayout_2.addWidget(self.checkBox_19, 1, 9, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 5, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 0, 6, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 0, 8, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_22.setObjectName("label_22")
        self.gridLayout_2.addWidget(self.label_22, 0, 20, 1, 1)
        self.checkBox_33 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_33.setText("")
        self.checkBox_33.setObjectName("checkBox_33")
        self.gridLayout_2.addWidget(self.checkBox_33, 1, 23, 1, 1)
        self.checkBox_32 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_32.setText("")
        self.checkBox_32.setObjectName("checkBox_32")
        self.gridLayout_2.addWidget(self.checkBox_32, 1, 22, 1, 1)
        self.checkBox_14 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_14.setText("")
        self.checkBox_14.setObjectName("checkBox_14")
        self.gridLayout_2.addWidget(self.checkBox_14, 1, 4, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_23.setObjectName("label_23")
        self.gridLayout_2.addWidget(self.label_23, 0, 21, 1, 1)
        self.checkBox_34 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_34.setText("")
        self.checkBox_34.setObjectName("checkBox_34")
        self.gridLayout_2.addWidget(self.checkBox_34, 1, 24, 1, 1)
        self.checkBox_31 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_31.setText("")
        self.checkBox_31.setObjectName("checkBox_31")
        self.gridLayout_2.addWidget(self.checkBox_31, 1, 21, 1, 1)
        self.checkBox_13 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_13.setText("")
        self.checkBox_13.setObjectName("checkBox_13")
        self.gridLayout_2.addWidget(self.checkBox_13, 1, 3, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_25.setObjectName("label_25")
        self.gridLayout_2.addWidget(self.label_25, 0, 23, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_26.setObjectName("label_26")
        self.gridLayout_2.addWidget(self.label_26, 0, 24, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_24.setObjectName("label_24")
        self.gridLayout_2.addWidget(self.label_24, 0, 22, 1, 1)
        self.checkBox_21 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_21.setText("")
        self.checkBox_21.setObjectName("checkBox_21")
        self.gridLayout_2.addWidget(self.checkBox_21, 1, 11, 1, 1)
        self.checkBox_18 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_18.setText("")
        self.checkBox_18.setObjectName("checkBox_18")
        self.gridLayout_2.addWidget(self.checkBox_18, 1, 8, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_21.setObjectName("label_21")
        self.gridLayout_2.addWidget(self.label_21, 0, 19, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_20.setObjectName("label_20")
        self.gridLayout_2.addWidget(self.label_20, 0, 18, 1, 1)
        self.checkBox_23 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_23.setText("")
        self.checkBox_23.setObjectName("checkBox_23")
        self.gridLayout_2.addWidget(self.checkBox_23, 1, 13, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 0, 11, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_16.setObjectName("label_16")
        self.gridLayout_2.addWidget(self.label_16, 0, 14, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_17.setObjectName("label_17")
        self.gridLayout_2.addWidget(self.label_17, 0, 15, 1, 1)
        self.checkBox_25 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_25.setText("")
        self.checkBox_25.setObjectName("checkBox_25")
        self.gridLayout_2.addWidget(self.checkBox_25, 1, 15, 1, 1)
        self.checkBox_27 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_27.setText("")
        self.checkBox_27.setObjectName("checkBox_27")
        self.gridLayout_2.addWidget(self.checkBox_27, 1, 17, 1, 1)
        self.checkBox_24 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_24.setText("")
        self.checkBox_24.setObjectName("checkBox_24")
        self.gridLayout_2.addWidget(self.checkBox_24, 1, 14, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 0, 12, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 0, 10, 1, 1)
        self.checkBox_41 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_41.setText("")
        self.checkBox_41.setObjectName("checkBox_41")
        self.gridLayout_2.addWidget(self.checkBox_41, 2, 5, 1, 1)
        self.checkBox_44 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_44.setText("")
        self.checkBox_44.setObjectName("checkBox_44")
        self.gridLayout_2.addWidget(self.checkBox_44, 2, 8, 1, 1)
        self.checkBox_42 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_42.setText("")
        self.checkBox_42.setObjectName("checkBox_42")
        self.gridLayout_2.addWidget(self.checkBox_42, 2, 6, 1, 1)
        self.checkBox_40 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_40.setText("")
        self.checkBox_40.setObjectName("checkBox_40")
        self.gridLayout_2.addWidget(self.checkBox_40, 2, 4, 1, 1)
        self.checkBox_43 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_43.setText("")
        self.checkBox_43.setObjectName("checkBox_43")
        self.gridLayout_2.addWidget(self.checkBox_43, 2, 7, 1, 1)
        self.checkBox_49 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_49.setText("")
        self.checkBox_49.setObjectName("checkBox_49")
        self.gridLayout_2.addWidget(self.checkBox_49, 2, 13, 1, 1)
        self.checkBox_46 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_46.setText("")
        self.checkBox_46.setObjectName("checkBox_46")
        self.gridLayout_2.addWidget(self.checkBox_46, 2, 10, 1, 1)
        self.checkBox_50 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_50.setText("")
        self.checkBox_50.setObjectName("checkBox_50")
        self.gridLayout_2.addWidget(self.checkBox_50, 2, 14, 1, 1)
        self.checkBox_48 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_48.setText("")
        self.checkBox_48.setObjectName("checkBox_48")
        self.gridLayout_2.addWidget(self.checkBox_48, 2, 12, 1, 1)
        self.checkBox_47 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_47.setText("")
        self.checkBox_47.setObjectName("checkBox_47")
        self.gridLayout_2.addWidget(self.checkBox_47, 2, 11, 1, 1)
        self.checkBox_45 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_45.setText("")
        self.checkBox_45.setObjectName("checkBox_45")
        self.gridLayout_2.addWidget(self.checkBox_45, 2, 9, 1, 1)
        self.checkBox_55 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_55.setText("")
        self.checkBox_55.setObjectName("checkBox_55")
        self.gridLayout_2.addWidget(self.checkBox_55, 2, 19, 1, 1)
        self.checkBox_51 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_51.setText("")
        self.checkBox_51.setObjectName("checkBox_51")
        self.gridLayout_2.addWidget(self.checkBox_51, 2, 15, 1, 1)
        self.checkBox_53 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_53.setText("")
        self.checkBox_53.setObjectName("checkBox_53")
        self.gridLayout_2.addWidget(self.checkBox_53, 2, 17, 1, 1)
        self.checkBox_52 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_52.setText("")
        self.checkBox_52.setObjectName("checkBox_52")
        self.gridLayout_2.addWidget(self.checkBox_52, 2, 16, 1, 1)
        self.checkBox_54 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_54.setText("")
        self.checkBox_54.setObjectName("checkBox_54")
        self.gridLayout_2.addWidget(self.checkBox_54, 2, 18, 1, 1)
        self.checkBox_60 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_60.setText("")
        self.checkBox_60.setObjectName("checkBox_60")
        self.gridLayout_2.addWidget(self.checkBox_60, 2, 24, 1, 1)
        self.checkBox_58 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_58.setText("")
        self.checkBox_58.setObjectName("checkBox_58")
        self.gridLayout_2.addWidget(self.checkBox_58, 2, 22, 1, 1)
        self.checkBox_57 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_57.setText("")
        self.checkBox_57.setObjectName("checkBox_57")
        self.gridLayout_2.addWidget(self.checkBox_57, 2, 21, 1, 1)
        self.checkBox_59 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_59.setText("")
        self.checkBox_59.setObjectName("checkBox_59")
        self.gridLayout_2.addWidget(self.checkBox_59, 2, 23, 1, 1)
        self.checkBox_56 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_56.setText("")
        self.checkBox_56.setObjectName("checkBox_56")
        self.gridLayout_2.addWidget(self.checkBox_56, 2, 20, 1, 1)
        self.checkBox_65 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_65.setText("")
        self.checkBox_65.setObjectName("checkBox_65")
        self.gridLayout_2.addWidget(self.checkBox_65, 3, 5, 1, 1)
        self.checkBox_64 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_64.setText("")
        self.checkBox_64.setObjectName("checkBox_64")
        self.gridLayout_2.addWidget(self.checkBox_64, 3, 7, 1, 1)
        self.checkBox_66 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_66.setText("")
        self.checkBox_66.setObjectName("checkBox_66")
        self.gridLayout_2.addWidget(self.checkBox_66, 3, 4, 1, 1)
        self.checkBox_63 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_63.setText("")
        self.checkBox_63.setObjectName("checkBox_63")
        self.gridLayout_2.addWidget(self.checkBox_63, 3, 6, 1, 1)
        self.checkBox_69 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_69.setText("")
        self.checkBox_69.setObjectName("checkBox_69")
        self.gridLayout_2.addWidget(self.checkBox_69, 3, 1, 1, 1)
        self.checkBox_70 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_70.setText("")
        self.checkBox_70.setObjectName("checkBox_70")
        self.gridLayout_2.addWidget(self.checkBox_70, 3, 8, 1, 1)
        self.checkBox_71 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_71.setText("")
        self.checkBox_71.setObjectName("checkBox_71")
        self.gridLayout_2.addWidget(self.checkBox_71, 3, 9, 1, 1)
        self.checkBox_67 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_67.setText("")
        self.checkBox_67.setObjectName("checkBox_67")
        self.gridLayout_2.addWidget(self.checkBox_67, 3, 3, 1, 1)
        self.checkBox_68 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_68.setText("")
        self.checkBox_68.setObjectName("checkBox_68")
        self.gridLayout_2.addWidget(self.checkBox_68, 3, 2, 1, 1)
        self.checkBox_75 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_75.setText("")
        self.checkBox_75.setObjectName("checkBox_75")
        self.gridLayout_2.addWidget(self.checkBox_75, 3, 13, 1, 1)
        self.checkBox_73 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_73.setText("")
        self.checkBox_73.setObjectName("checkBox_73")
        self.gridLayout_2.addWidget(self.checkBox_73, 3, 11, 1, 1)
        self.checkBox_72 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_72.setText("")
        self.checkBox_72.setObjectName("checkBox_72")
        self.gridLayout_2.addWidget(self.checkBox_72, 3, 10, 1, 1)
        self.checkBox_76 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_76.setText("")
        self.checkBox_76.setObjectName("checkBox_76")
        self.gridLayout_2.addWidget(self.checkBox_76, 3, 14, 1, 1)
        self.checkBox_74 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_74.setText("")
        self.checkBox_74.setObjectName("checkBox_74")
        self.gridLayout_2.addWidget(self.checkBox_74, 3, 12, 1, 1)
        self.checkBox_77 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_77.setText("")
        self.checkBox_77.setObjectName("checkBox_77")
        self.gridLayout_2.addWidget(self.checkBox_77, 3, 15, 1, 1)
        self.checkBox_78 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_78.setText("")
        self.checkBox_78.setObjectName("checkBox_78")
        self.gridLayout_2.addWidget(self.checkBox_78, 3, 16, 1, 1)
        self.checkBox_81 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_81.setText("")
        self.checkBox_81.setObjectName("checkBox_81")
        self.gridLayout_2.addWidget(self.checkBox_81, 3, 19, 1, 1)
        self.checkBox_80 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_80.setText("")
        self.checkBox_80.setObjectName("checkBox_80")
        self.gridLayout_2.addWidget(self.checkBox_80, 3, 18, 1, 1)
        self.checkBox_82 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_82.setText("")
        self.checkBox_82.setObjectName("checkBox_82")
        self.gridLayout_2.addWidget(self.checkBox_82, 3, 20, 1, 1)
        self.checkBox_79 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_79.setText("")
        self.checkBox_79.setObjectName("checkBox_79")
        self.gridLayout_2.addWidget(self.checkBox_79, 3, 17, 1, 1)
        self.checkBox_95 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_95.setText("")
        self.checkBox_95.setObjectName("checkBox_95")
        self.gridLayout_2.addWidget(self.checkBox_95, 3, 22, 1, 1)
        self.checkBox_94 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_94.setText("")
        self.checkBox_94.setObjectName("checkBox_94")
        self.gridLayout_2.addWidget(self.checkBox_94, 3, 21, 1, 1)
        self.checkBox_97 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_97.setText("")
        self.checkBox_97.setObjectName("checkBox_97")
        self.gridLayout_2.addWidget(self.checkBox_97, 3, 24, 1, 1)
        self.checkBox_96 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_96.setText("")
        self.checkBox_96.setObjectName("checkBox_96")
        self.gridLayout_2.addWidget(self.checkBox_96, 3, 23, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 450, 761, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_31 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_31.setObjectName("label_31")
        self.horizontalLayout.addWidget(self.label_31)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(800, 450, 291, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_32 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_32.setObjectName("label_32")
        self.horizontalLayout_2.addWidget(self.label_32)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(930, 310, 161, 121))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.checkBox_61 = QtWidgets.QCheckBox(self.gridLayoutWidget_3)
        self.checkBox_61.setText("")
        self.checkBox_61.setObjectName("checkBox_61")
        self.horizontalLayout_5.addWidget(self.checkBox_61)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.gridLayout_3.addLayout(self.horizontalLayout_5, 3, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.checkBox_36 = QtWidgets.QCheckBox(self.gridLayoutWidget_3)
        self.checkBox_36.setText("")
        self.checkBox_36.setObjectName("checkBox_36")
        self.horizontalLayout_4.addWidget(self.checkBox_36)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.gridLayout_3.addLayout(self.horizontalLayout_4, 2, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem4)
        self.checkBox_62 = QtWidgets.QCheckBox(self.gridLayoutWidget_3)
        self.checkBox_62.setText("")
        self.checkBox_62.setObjectName("checkBox_62")
        self.horizontalLayout_7.addWidget(self.checkBox_62)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem5)
        self.gridLayout_3.addLayout(self.horizontalLayout_7, 1, 1, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.checkBox_35 = QtWidgets.QCheckBox(self.gridLayoutWidget_3)
        self.checkBox_35.setText("")
        self.checkBox_35.setObjectName("checkBox_35")
        self.horizontalLayout_3.addWidget(self.checkBox_35)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.gridLayout_3.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_27.setObjectName("label_27")
        self.gridLayout_3.addWidget(self.label_27, 0, 0, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_28.setObjectName("label_28")
        self.gridLayout_3.addWidget(self.label_28, 0, 1, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem8)
        self.checkBox_98 = QtWidgets.QCheckBox(self.gridLayoutWidget_3)
        self.checkBox_98.setText("")
        self.checkBox_98.setObjectName("checkBox_98")
        self.horizontalLayout_8.addWidget(self.checkBox_98)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem9)
        self.gridLayout_3.addLayout(self.horizontalLayout_8, 2, 1, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem10)
        self.checkBox_99 = QtWidgets.QCheckBox(self.gridLayoutWidget_3)
        self.checkBox_99.setText("")
        self.checkBox_99.setObjectName("checkBox_99")
        self.horizontalLayout_9.addWidget(self.checkBox_99)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem11)
        self.gridLayout_3.addLayout(self.horizontalLayout_9, 3, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Save"))
        self.pushButton_2.setText(_translate("Dialog", "Cancel"))
        self.pushButton_3.setText(_translate("Dialog", "Reset"))
        self.checkBox_84.setText(_translate("Dialog", "enable_high_speed"))
        self.checkBox_85.setText(_translate("Dialog", "enable_legacy"))
        self.checkBox_89.setText(_translate("Dialog", "enable_TDC_ID"))
        self.checkBox_87.setText(_translate("Dialog", "enable_8b10b"))
        self.checkBox_7.setText(_translate("Dialog", "channel_data_debug"))
        self.checkBox_6.setText(_translate("Dialog", "enable_trigger"))
        self.checkBox_3.setText(_translate("Dialog", "enable_direct_bunch_reset"))
        self.checkBox.setText(_translate("Dialog", "enable_new_ttc"))
        self.checkBox_93.setText(_translate("Dialog", "enable_insert"))
        self.checkBox_92.setText(_translate("Dialog", "enable_direct_trigger"))
        self.checkBox_5.setText(_translate("Dialog", "bypass_bcr_distribution"))
        self.checkBox_4.setText(_translate("Dialog", "auto_roll_over"))
        self.checkBox_83.setText(_translate("Dialog", "enable_trigger_timeout"))
        self.checkBox_9.setText(_translate("Dialog", "enable_pair"))
        self.checkBox_8.setText(_translate("Dialog", "enable_leading"))
        self.checkBox_88.setText(_translate("Dialog", "enable_errror_packet"))
        self.checkBox_10.setText(_translate("Dialog", "enable_fake_hit"))
        self.checkBox_90.setText(_translate("Dialog", "enable_error_notify"))
        self.checkBox_86.setText(_translate("Dialog", "full_width_res"))
        self.checkBox_91.setText(_translate("Dialog", "enable_direct_event_reset"))
        self.checkBox_2.setText(_translate("Dialog", "enable_master_reset_code"))
        self.label_15.setText(_translate("Dialog", "12"))
        self.label_29.setText(_translate("Dialog", "channel_enable_r:"))
        self.label_19.setText(_translate("Dialog", "16"))
        self.label_4.setText(_translate("Dialog", "1"))
        self.label_5.setText(_translate("Dialog", "2"))
        self.label_11.setText(_translate("Dialog", "8"))
        self.label_30.setText(_translate("Dialog", "channel_enable_f:"))
        self.label_2.setText(_translate("Dialog", "Channel Options: "))
        self.label_3.setText(_translate("Dialog", "0"))
        self.label_9.setText(_translate("Dialog", "6"))
        self.label_18.setText(_translate("Dialog", "15"))
        self.label_6.setText(_translate("Dialog", "3"))
        self.label_7.setText(_translate("Dialog", "4"))
        self.label_8.setText(_translate("Dialog", "5"))
        self.label_10.setText(_translate("Dialog", "7"))
        self.label_22.setText(_translate("Dialog", "19"))
        self.label_23.setText(_translate("Dialog", "20"))
        self.label_25.setText(_translate("Dialog", "22"))
        self.label_26.setText(_translate("Dialog", "23"))
        self.label_24.setText(_translate("Dialog", "21"))
        self.label_21.setText(_translate("Dialog", "18"))
        self.label.setText(_translate("Dialog", "rising_is_leading:"))
        self.label_20.setText(_translate("Dialog", "17"))
        self.label_13.setText(_translate("Dialog", "10"))
        self.label_16.setText(_translate("Dialog", "13"))
        self.label_17.setText(_translate("Dialog", "14"))
        self.label_14.setText(_translate("Dialog", "11"))
        self.label_12.setText(_translate("Dialog", "9"))
        self.label_31.setText(_translate("Dialog", "TDC_ID:"))
        self.label_32.setText(_translate("Dialog", "Width_select:"))
        self.label_27.setText(_translate("Dialog", "Select All"))
        self.label_28.setText(_translate("Dialog", "Deselect All"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())