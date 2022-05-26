# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPlainTextEdit, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QStatusBar, QToolButton, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 750)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.pte_file_preview = QPlainTextEdit(self.centralwidget)
        self.pte_file_preview.setObjectName(u"pte_file_preview")
        font = QFont()
        font.setFamilies([u"Cascadia Mono Light"])
        font.setPointSize(10)
        self.pte_file_preview.setFont(font)
        self.pte_file_preview.setLineWrapMode(QPlainTextEdit.NoWrap)
        self.pte_file_preview.setTabStopDistance(40.000000000000000)

        self.gridLayout.addWidget(self.pte_file_preview, 1, 0, 5, 1)

        self.vs_functions_2 = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.vs_functions_2, 5, 1, 1, 2)

        self.pb_save_file = QPushButton(self.centralwidget)
        self.pb_save_file.setObjectName(u"pb_save_file")
        font1 = QFont()
        font1.setBold(True)
        self.pb_save_file.setFont(font1)

        self.gridLayout.addWidget(self.pb_save_file, 3, 1, 1, 2)

        self.le_file_path = QLineEdit(self.centralwidget)
        self.le_file_path.setObjectName(u"le_file_path")
        self.le_file_path.setReadOnly(True)

        self.gridLayout.addWidget(self.le_file_path, 0, 0, 1, 1)

        self.tb_reload_file = QToolButton(self.centralwidget)
        self.tb_reload_file.setObjectName(u"tb_reload_file")
        font2 = QFont()
        font2.setPointSize(10)
        self.tb_reload_file.setFont(font2)

        self.gridLayout.addWidget(self.tb_reload_file, 0, 1, 1, 1)

        self.pb_open_file = QPushButton(self.centralwidget)
        self.pb_open_file.setObjectName(u"pb_open_file")
        self.pb_open_file.setFont(font1)

        self.gridLayout.addWidget(self.pb_open_file, 0, 2, 1, 1)

        self.gb_functions = QGroupBox(self.centralwidget)
        self.gb_functions.setObjectName(u"gb_functions")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gb_functions.sizePolicy().hasHeightForWidth())
        self.gb_functions.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QGridLayout(self.gb_functions)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.ln_functions_2 = QFrame(self.gb_functions)
        self.ln_functions_2.setObjectName(u"ln_functions_2")
        self.ln_functions_2.setFrameShadow(QFrame.Plain)
        self.ln_functions_2.setFrameShape(QFrame.HLine)

        self.gridLayout_2.addWidget(self.ln_functions_2, 9, 0, 1, 2)

        self.sb_number_lines_start = QSpinBox(self.gb_functions)
        self.sb_number_lines_start.setObjectName(u"sb_number_lines_start")
        self.sb_number_lines_start.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.sb_number_lines_start.setMaximum(100000)
        self.sb_number_lines_start.setSingleStep(100)
        self.sb_number_lines_start.setValue(1000)

        self.gridLayout_2.addWidget(self.sb_number_lines_start, 1, 1, 1, 1)

        self.lb_number_ids_step = QLabel(self.gb_functions)
        self.lb_number_ids_step.setObjectName(u"lb_number_ids_step")

        self.gridLayout_2.addWidget(self.lb_number_ids_step, 7, 0, 1, 1)

        self.lb_number_lines_step = QLabel(self.gb_functions)
        self.lb_number_lines_step.setObjectName(u"lb_number_lines_step")

        self.gridLayout_2.addWidget(self.lb_number_lines_step, 2, 0, 1, 1)

        self.ln_functions_1 = QFrame(self.gb_functions)
        self.ln_functions_1.setObjectName(u"ln_functions_1")
        self.ln_functions_1.setFrameShadow(QFrame.Plain)
        self.ln_functions_1.setFrameShape(QFrame.HLine)

        self.gridLayout_2.addWidget(self.ln_functions_1, 4, 0, 1, 2)

        self.lb_number_lines_start = QLabel(self.gb_functions)
        self.lb_number_lines_start.setObjectName(u"lb_number_lines_start")

        self.gridLayout_2.addWidget(self.lb_number_lines_start, 1, 0, 1, 1)

        self.lb_number_ids_start = QLabel(self.gb_functions)
        self.lb_number_ids_start.setObjectName(u"lb_number_ids_start")

        self.gridLayout_2.addWidget(self.lb_number_ids_start, 6, 0, 1, 1)

        self.pb_number_ids = QPushButton(self.gb_functions)
        self.pb_number_ids.setObjectName(u"pb_number_ids")

        self.gridLayout_2.addWidget(self.pb_number_ids, 8, 0, 1, 2)

        self.sb_number_ids_start = QSpinBox(self.gb_functions)
        self.sb_number_ids_start.setObjectName(u"sb_number_ids_start")
        self.sb_number_ids_start.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.sb_number_ids_start.setMaximum(10000)
        self.sb_number_ids_start.setSingleStep(10)
        self.sb_number_ids_start.setValue(100)

        self.gridLayout_2.addWidget(self.sb_number_ids_start, 6, 1, 1, 1)

        self.pb_convert_tabs_to_spaces = QPushButton(self.gb_functions)
        self.pb_convert_tabs_to_spaces.setObjectName(u"pb_convert_tabs_to_spaces")

        self.gridLayout_2.addWidget(self.pb_convert_tabs_to_spaces, 13, 0, 1, 2)

        self.lb_tab_width = QLabel(self.gb_functions)
        self.lb_tab_width.setObjectName(u"lb_tab_width")

        self.gridLayout_2.addWidget(self.lb_tab_width, 12, 0, 1, 1)

        self.sb_tab_width = QSpinBox(self.gb_functions)
        self.sb_tab_width.setObjectName(u"sb_tab_width")
        self.sb_tab_width.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.sb_tab_width.setMinimum(2)
        self.sb_tab_width.setMaximum(8)
        self.sb_tab_width.setSingleStep(2)
        self.sb_tab_width.setValue(4)

        self.gridLayout_2.addWidget(self.sb_tab_width, 12, 1, 1, 1)

        self.sb_number_lines_step = QSpinBox(self.gb_functions)
        self.sb_number_lines_step.setObjectName(u"sb_number_lines_step")
        self.sb_number_lines_step.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.sb_number_lines_step.setMaximum(10000)
        self.sb_number_lines_step.setSingleStep(10)
        self.sb_number_lines_step.setValue(10)

        self.gridLayout_2.addWidget(self.sb_number_lines_step, 2, 1, 1, 1)

        self.sb_number_ids_step = QSpinBox(self.gb_functions)
        self.sb_number_ids_step.setObjectName(u"sb_number_ids_step")
        self.sb_number_ids_step.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.sb_number_ids_step.setMaximum(100)
        self.sb_number_ids_step.setValue(1)

        self.gridLayout_2.addWidget(self.sb_number_ids_step, 7, 1, 1, 1)

        self.pb_number_lines = QPushButton(self.gb_functions)
        self.pb_number_lines.setObjectName(u"pb_number_lines")

        self.gridLayout_2.addWidget(self.pb_number_lines, 3, 0, 1, 2)

        self.pb_remove_trailing_whitespace = QPushButton(self.gb_functions)
        self.pb_remove_trailing_whitespace.setObjectName(u"pb_remove_trailing_whitespace")

        self.gridLayout_2.addWidget(self.pb_remove_trailing_whitespace, 15, 0, 1, 2)

        self.ln_functions_3 = QFrame(self.gb_functions)
        self.ln_functions_3.setObjectName(u"ln_functions_3")
        self.ln_functions_3.setFrameShadow(QFrame.Plain)
        self.ln_functions_3.setFrameShape(QFrame.HLine)

        self.gridLayout_2.addWidget(self.ln_functions_3, 14, 0, 1, 2)


        self.gridLayout.addWidget(self.gb_functions, 1, 1, 1, 2)

        self.vs_functions_1 = QSpacerItem(0, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.vs_functions_1, 2, 1, 1, 2)

        self.pb_save_file_as = QPushButton(self.centralwidget)
        self.pb_save_file_as.setObjectName(u"pb_save_file_as")
        self.pb_save_file_as.setFont(font1)

        self.gridLayout.addWidget(self.pb_save_file_as, 4, 1, 1, 2)


        self.verticalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1000, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"CNC Tool", None))
        self.pte_file_preview.setPlaceholderText(QCoreApplication.translate("MainWindow", u"File Preview / Manual Input", None))
        self.pb_save_file.setText(QCoreApplication.translate("MainWindow", u"Save File", None))
        self.le_file_path.setPlaceholderText(QCoreApplication.translate("MainWindow", u"File Path", None))
#if QT_CONFIG(tooltip)
        self.tb_reload_file.setToolTip(QCoreApplication.translate("MainWindow", u"Reload File", None))
#endif // QT_CONFIG(tooltip)
        self.tb_reload_file.setText(QCoreApplication.translate("MainWindow", u"\u2b6e", None))
        self.pb_open_file.setText(QCoreApplication.translate("MainWindow", u"Open File", None))
        self.gb_functions.setTitle(QCoreApplication.translate("MainWindow", u"Functions", None))
        self.sb_number_lines_start.setPrefix(QCoreApplication.translate("MainWindow", u"N", None))
        self.lb_number_ids_step.setText(QCoreApplication.translate("MainWindow", u"Step:", None))
        self.lb_number_lines_step.setText(QCoreApplication.translate("MainWindow", u"Step:", None))
        self.lb_number_lines_start.setText(QCoreApplication.translate("MainWindow", u"Start:", None))
        self.lb_number_ids_start.setText(QCoreApplication.translate("MainWindow", u"Start:", None))
        self.pb_number_ids.setText(QCoreApplication.translate("MainWindow", u"Number IDS", None))
        self.sb_number_ids_start.setPrefix(QCoreApplication.translate("MainWindow", u"IDS=", None))
        self.pb_convert_tabs_to_spaces.setText(QCoreApplication.translate("MainWindow", u"Convert Tabs To Spaces", None))
        self.lb_tab_width.setText(QCoreApplication.translate("MainWindow", u"Tab Width", None))
        self.pb_number_lines.setText(QCoreApplication.translate("MainWindow", u"Number Lines", None))
        self.pb_remove_trailing_whitespace.setText(QCoreApplication.translate("MainWindow", u"Remove Trailing Whitespace", None))
        self.pb_save_file_as.setText(QCoreApplication.translate("MainWindow", u"Save File As", None))
    # retranslateUi

