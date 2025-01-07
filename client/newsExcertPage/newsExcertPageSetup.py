# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newsExcertPageSetup.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1222, 937)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(0, 0))
        Form.setMaximumSize(QtCore.QSize(1920, 1098))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        Form.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("asset/ack3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setLayoutDirection(QtCore.Qt.LeftToRight)
        Form.setStyleSheet("")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalWidget = QtWidgets.QWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalWidget.sizePolicy().hasHeightForWidth())
        self.verticalWidget.setSizePolicy(sizePolicy)
        self.verticalWidget.setMaximumSize(QtCore.QSize(1920, 1080))
        self.verticalWidget.setStyleSheet("background-color:#F5F5F5")
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalWidget = QtWidgets.QWidget(self.verticalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalWidget.sizePolicy().hasHeightForWidth())
        self.horizontalWidget.setSizePolicy(sizePolicy)
        self.horizontalWidget.setMinimumSize(QtCore.QSize(1186, 0))
        self.horizontalWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.horizontalWidget.setStyleSheet("background-color:#616161;\n"
"border-style:solid;\n"
"border-bottom-width:2px;\n"
"border-radius:3px;\n"
"border-color:#BDBDBD;")
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout_4.setContentsMargins(2, 10, 0, 10)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalWidget_3 = QtWidgets.QWidget(self.horizontalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalWidget_3.sizePolicy().hasHeightForWidth())
        self.horizontalWidget_3.setSizePolicy(sizePolicy)
        self.horizontalWidget_3.setMinimumSize(QtCore.QSize(0, 0))
        self.horizontalWidget_3.setMaximumSize(QtCore.QSize(270, 1080))
        self.horizontalWidget_3.setAutoFillBackground(False)
        self.horizontalWidget_3.setStyleSheet("border:none\n"
"")
        self.horizontalWidget_3.setObjectName("horizontalWidget_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalWidget_3)
        self.horizontalLayout_6.setContentsMargins(8, 0, 8, 0)
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.main_page = QtWidgets.QPushButton(self.horizontalWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_page.sizePolicy().hasHeightForWidth())
        self.main_page.setSizePolicy(sizePolicy)
        self.main_page.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.main_page.setStyleSheet("background-color:#607D8B;\n"
"border:solid;\n"
"border-radius:3px;\n"
"border-color:#616161;\n"
"padding:10px\n"
"\n"
"")
        self.main_page.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("asset/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.main_page.setIcon(icon1)
        self.main_page.setIconSize(QtCore.QSize(32, 32))
        self.main_page.setObjectName("main_page")
        self.horizontalLayout_6.addWidget(self.main_page)
        self.news_excert = QtWidgets.QPushButton(self.horizontalWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.news_excert.sizePolicy().hasHeightForWidth())
        self.news_excert.setSizePolicy(sizePolicy)
        self.news_excert.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.news_excert.setStyleSheet("background-color:#607D8B;\n"
"border:solid;\n"
"border-radius:3px;\n"
"border-color:#616161;\n"
"padding:10px\n"
"\n"
"")
        self.news_excert.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("asset/news.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.news_excert.setIcon(icon2)
        self.news_excert.setIconSize(QtCore.QSize(32, 32))
        self.news_excert.setObjectName("news_excert")
        self.horizontalLayout_6.addWidget(self.news_excert)
        self.setting = QtWidgets.QPushButton(self.horizontalWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.setting.sizePolicy().hasHeightForWidth())
        self.setting.setSizePolicy(sizePolicy)
        self.setting.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.setting.setStyleSheet("background-color:#607D8B;\n"
"border:solid;\n"
"border-radius:3px;\n"
"border-color:#616161;\n"
"padding:10px\n"
"\n"
"")
        self.setting.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("asset/setting.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setting.setIcon(icon3)
        self.setting.setIconSize(QtCore.QSize(32, 32))
        self.setting.setObjectName("setting")
        self.horizontalLayout_6.addWidget(self.setting)
        self.horizontalLayout_4.addWidget(self.horizontalWidget_3)
        self.verticalWidget1 = QtWidgets.QWidget(self.horizontalWidget)
        self.verticalWidget1.setStyleSheet("border:none\n"
"")
        self.verticalWidget1.setObjectName("verticalWidget1")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.verticalWidget1)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_4.addWidget(self.verticalWidget1)
        self.verticalLayout_9.addWidget(self.horizontalWidget, 0, QtCore.Qt.AlignLeft)
        self.horizontalWidget_2 = QtWidgets.QWidget(self.verticalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalWidget_2.sizePolicy().hasHeightForWidth())
        self.horizontalWidget_2.setSizePolicy(sizePolicy)
        self.horizontalWidget_2.setMaximumSize(QtCore.QSize(1920, 1080))
        self.horizontalWidget_2.setStyleSheet("")
        self.horizontalWidget_2.setObjectName("horizontalWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalWidget_4 = QtWidgets.QWidget(self.horizontalWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalWidget_4.sizePolicy().hasHeightForWidth())
        self.verticalWidget_4.setSizePolicy(sizePolicy)
        self.verticalWidget_4.setMinimumSize(QtCore.QSize(400, 0))
        self.verticalWidget_4.setStyleSheet("border:solid;\n"
"border-radius:3px;\n"
"border-color:rgb(185, 185, 185);\n"
"border-width:2px")
        self.verticalWidget_4.setObjectName("verticalWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalWidget_4)
        self.verticalLayout_4.setContentsMargins(15, 15, 15, 15)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalWidget1 = QtWidgets.QWidget(self.verticalWidget_4)
        self.horizontalWidget1.setStyleSheet("border:none")
        self.horizontalWidget1.setObjectName("horizontalWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalWidget1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.horizontalWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 648))
        self.scrollArea.setStyleSheet("border:none")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1138, 648))
        self.scrollAreaWidgetContents.setStyleSheet("""border:solid;
                                                    border-radius:5px;
                                                    background-color:#F5F5F5;
                                                    border-color:#BDBDBD;
                                                    border-width:2px;""")
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.scrollArea)
        self.verticalLayout_4.addWidget(self.horizontalWidget1)
        self.horizontalWidget_21 = QtWidgets.QWidget(self.verticalWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalWidget_21.sizePolicy().hasHeightForWidth())
        self.horizontalWidget_21.setSizePolicy(sizePolicy)
        self.horizontalWidget_21.setStyleSheet("border:none")
        self.horizontalWidget_21.setObjectName("horizontalWidget_21")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalWidget_21)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.AckButton = QtWidgets.QPushButton(self.horizontalWidget_21)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AckButton.sizePolicy().hasHeightForWidth())
        self.AckButton.setSizePolicy(sizePolicy)
        self.AckButton.setMinimumSize(QtCore.QSize(0, 103))
        self.AckButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.AckButton.setMouseTracking(False)
        self.AckButton.setStyleSheet("border:solid;\n"
"border-radius:3px;\n"
"border-color:#BDBDBD;\n"
"border-width:2px;\n"
"background-color:#607D8B;\n"
"\n"
"margin-bottom:18px")
        self.AckButton.setText("")
        self.AckButton.setIcon(icon)
        self.AckButton.setIconSize(QtCore.QSize(48, 48))
        self.AckButton.setObjectName("AckButton")
        self.horizontalLayout_3.addWidget(self.AckButton)
        self.verticalLayout_4.addWidget(self.horizontalWidget_21)
        self.horizontalLayout_2.addWidget(self.verticalWidget_4)
        self.verticalLayout_9.addWidget(self.horizontalWidget_2)
        self.verticalLayout.addWidget(self.verticalWidget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "文本摘要器"))
