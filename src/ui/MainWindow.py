# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QGroupBox, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPlainTextEdit, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QStatusBar, QTabWidget,
    QToolButton, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 750)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_file_mode = QWidget()
        self.tab_file_mode.setObjectName(u"tab_file_mode")
        self.verticalLayout_2 = QVBoxLayout(self.tab_file_mode)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.pb_save_file_as = QPushButton(self.tab_file_mode)
        self.pb_save_file_as.setObjectName(u"pb_save_file_as")
        font = QFont()
        font.setBold(True)
        self.pb_save_file_as.setFont(font)

        self.gridLayout.addWidget(self.pb_save_file_as, 5, 1, 1, 2)

        self.vs_functions_2 = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.vs_functions_2, 6, 1, 1, 2)

        self.pb_save_file = QPushButton(self.tab_file_mode)
        self.pb_save_file.setObjectName(u"pb_save_file")
        self.pb_save_file.setFont(font)

        self.gridLayout.addWidget(self.pb_save_file, 4, 1, 1, 2)

        self.pte_file_preview = QPlainTextEdit(self.tab_file_mode)
        self.pte_file_preview.setObjectName(u"pte_file_preview")
        font1 = QFont()
        font1.setFamilies([u"Cascadia Mono Light"])
        font1.setPointSize(10)
        self.pte_file_preview.setFont(font1)
        self.pte_file_preview.setLineWrapMode(QPlainTextEdit.NoWrap)
        self.pte_file_preview.setTabStopDistance(40.000000000000000)

        self.gridLayout.addWidget(self.pte_file_preview, 1, 0, 6, 1)

        self.le_file_path = QLineEdit(self.tab_file_mode)
        self.le_file_path.setObjectName(u"le_file_path")
        font2 = QFont()
        font2.setFamilies([u"Cascadia Mono Light"])
        self.le_file_path.setFont(font2)
        self.le_file_path.setReadOnly(True)

        self.gridLayout.addWidget(self.le_file_path, 0, 0, 1, 1)

        self.tb_reload_file = QToolButton(self.tab_file_mode)
        self.tb_reload_file.setObjectName(u"tb_reload_file")
        font3 = QFont()
        font3.setPointSize(10)
        self.tb_reload_file.setFont(font3)

        self.gridLayout.addWidget(self.tb_reload_file, 0, 1, 1, 1)

        self.vs_functions_1 = QSpacerItem(0, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.vs_functions_1, 3, 1, 1, 2)

        self.gb_functions = QGroupBox(self.tab_file_mode)
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

        self.pb_open_file = QPushButton(self.tab_file_mode)
        self.pb_open_file.setObjectName(u"pb_open_file")
        self.pb_open_file.setFont(font)

        self.gridLayout.addWidget(self.pb_open_file, 0, 2, 1, 1)

        self.gb_options = QGroupBox(self.tab_file_mode)
        self.gb_options.setObjectName(u"gb_options")
        self.verticalLayout_4 = QVBoxLayout(self.gb_options)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.cb_ignore_comments = QCheckBox(self.gb_options)
        self.cb_ignore_comments.setObjectName(u"cb_ignore_comments")

        self.verticalLayout_4.addWidget(self.cb_ignore_comments)


        self.gridLayout.addWidget(self.gb_options, 2, 1, 1, 2)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.tabWidget.addTab(self.tab_file_mode, "")
        self.tab_folder_mode = QWidget()
        self.tab_folder_mode.setObjectName(u"tab_folder_mode")
        self.verticalLayout_3 = QVBoxLayout(self.tab_folder_mode)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.pte_folder_preview = QPlainTextEdit(self.tab_folder_mode)
        self.pte_folder_preview.setObjectName(u"pte_folder_preview")
        self.pte_folder_preview.setFont(font1)
        self.pte_folder_preview.setLineWrapMode(QPlainTextEdit.NoWrap)
        self.pte_folder_preview.setReadOnly(True)
        self.pte_folder_preview.setTabStopDistance(40.000000000000000)

        self.gridLayout_3.addWidget(self.pte_folder_preview, 1, 0, 3, 1)

        self.le_folder_path = QLineEdit(self.tab_folder_mode)
        self.le_folder_path.setObjectName(u"le_folder_path")
        self.le_folder_path.setFont(font2)
        self.le_folder_path.setReadOnly(True)

        self.gridLayout_3.addWidget(self.le_folder_path, 0, 0, 1, 1)

        self.gb_functions_2 = QGroupBox(self.tab_folder_mode)
        self.gb_functions_2.setObjectName(u"gb_functions_2")
        sizePolicy.setHeightForWidth(self.gb_functions_2.sizePolicy().hasHeightForWidth())
        self.gb_functions_2.setSizePolicy(sizePolicy)
        self.gridLayout_4 = QGridLayout(self.gb_functions_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.ln_functions_4 = QFrame(self.gb_functions_2)
        self.ln_functions_4.setObjectName(u"ln_functions_4")
        self.ln_functions_4.setFrameShadow(QFrame.Plain)
        self.ln_functions_4.setFrameShape(QFrame.HLine)

        self.gridLayout_4.addWidget(self.ln_functions_4, 9, 0, 1, 2)

        self.sb_number_lines_start_2 = QSpinBox(self.gb_functions_2)
        self.sb_number_lines_start_2.setObjectName(u"sb_number_lines_start_2")
        self.sb_number_lines_start_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.sb_number_lines_start_2.setMaximum(100000)
        self.sb_number_lines_start_2.setSingleStep(100)
        self.sb_number_lines_start_2.setValue(1000)

        self.gridLayout_4.addWidget(self.sb_number_lines_start_2, 1, 1, 1, 1)

        self.lb_number_ids_step_2 = QLabel(self.gb_functions_2)
        self.lb_number_ids_step_2.setObjectName(u"lb_number_ids_step_2")

        self.gridLayout_4.addWidget(self.lb_number_ids_step_2, 7, 0, 1, 1)

        self.lb_number_lines_step_2 = QLabel(self.gb_functions_2)
        self.lb_number_lines_step_2.setObjectName(u"lb_number_lines_step_2")

        self.gridLayout_4.addWidget(self.lb_number_lines_step_2, 2, 0, 1, 1)

        self.ln_functions_5 = QFrame(self.gb_functions_2)
        self.ln_functions_5.setObjectName(u"ln_functions_5")
        self.ln_functions_5.setFrameShadow(QFrame.Plain)
        self.ln_functions_5.setFrameShape(QFrame.HLine)

        self.gridLayout_4.addWidget(self.ln_functions_5, 4, 0, 1, 2)

        self.lb_number_lines_start_2 = QLabel(self.gb_functions_2)
        self.lb_number_lines_start_2.setObjectName(u"lb_number_lines_start_2")

        self.gridLayout_4.addWidget(self.lb_number_lines_start_2, 1, 0, 1, 1)

        self.lb_number_ids_start_2 = QLabel(self.gb_functions_2)
        self.lb_number_ids_start_2.setObjectName(u"lb_number_ids_start_2")

        self.gridLayout_4.addWidget(self.lb_number_ids_start_2, 6, 0, 1, 1)

        self.pb_number_ids_2 = QPushButton(self.gb_functions_2)
        self.pb_number_ids_2.setObjectName(u"pb_number_ids_2")

        self.gridLayout_4.addWidget(self.pb_number_ids_2, 8, 0, 1, 2)

        self.sb_number_ids_start_2 = QSpinBox(self.gb_functions_2)
        self.sb_number_ids_start_2.setObjectName(u"sb_number_ids_start_2")
        self.sb_number_ids_start_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.sb_number_ids_start_2.setMaximum(10000)
        self.sb_number_ids_start_2.setSingleStep(10)
        self.sb_number_ids_start_2.setValue(100)

        self.gridLayout_4.addWidget(self.sb_number_ids_start_2, 6, 1, 1, 1)

        self.pb_convert_tabs_to_spaces_2 = QPushButton(self.gb_functions_2)
        self.pb_convert_tabs_to_spaces_2.setObjectName(u"pb_convert_tabs_to_spaces_2")

        self.gridLayout_4.addWidget(self.pb_convert_tabs_to_spaces_2, 13, 0, 1, 2)

        self.lb_tab_width_2 = QLabel(self.gb_functions_2)
        self.lb_tab_width_2.setObjectName(u"lb_tab_width_2")

        self.gridLayout_4.addWidget(self.lb_tab_width_2, 12, 0, 1, 1)

        self.sb_tab_width_2 = QSpinBox(self.gb_functions_2)
        self.sb_tab_width_2.setObjectName(u"sb_tab_width_2")
        self.sb_tab_width_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.sb_tab_width_2.setMinimum(2)
        self.sb_tab_width_2.setMaximum(8)
        self.sb_tab_width_2.setSingleStep(2)
        self.sb_tab_width_2.setValue(4)

        self.gridLayout_4.addWidget(self.sb_tab_width_2, 12, 1, 1, 1)

        self.sb_number_lines_step_2 = QSpinBox(self.gb_functions_2)
        self.sb_number_lines_step_2.setObjectName(u"sb_number_lines_step_2")
        self.sb_number_lines_step_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.sb_number_lines_step_2.setMaximum(10000)
        self.sb_number_lines_step_2.setSingleStep(10)
        self.sb_number_lines_step_2.setValue(10)

        self.gridLayout_4.addWidget(self.sb_number_lines_step_2, 2, 1, 1, 1)

        self.sb_number_ids_step_2 = QSpinBox(self.gb_functions_2)
        self.sb_number_ids_step_2.setObjectName(u"sb_number_ids_step_2")
        self.sb_number_ids_step_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.sb_number_ids_step_2.setMaximum(100)
        self.sb_number_ids_step_2.setValue(1)

        self.gridLayout_4.addWidget(self.sb_number_ids_step_2, 7, 1, 1, 1)

        self.pb_number_lines_2 = QPushButton(self.gb_functions_2)
        self.pb_number_lines_2.setObjectName(u"pb_number_lines_2")

        self.gridLayout_4.addWidget(self.pb_number_lines_2, 3, 0, 1, 2)

        self.pb_remove_trailing_whitespace_2 = QPushButton(self.gb_functions_2)
        self.pb_remove_trailing_whitespace_2.setObjectName(u"pb_remove_trailing_whitespace_2")

        self.gridLayout_4.addWidget(self.pb_remove_trailing_whitespace_2, 15, 0, 1, 2)

        self.ln_functions_6 = QFrame(self.gb_functions_2)
        self.ln_functions_6.setObjectName(u"ln_functions_6")
        self.ln_functions_6.setFrameShadow(QFrame.Plain)
        self.ln_functions_6.setFrameShape(QFrame.HLine)

        self.gridLayout_4.addWidget(self.ln_functions_6, 14, 0, 1, 2)


        self.gridLayout_3.addWidget(self.gb_functions_2, 1, 1, 1, 2)

        self.verticalSpacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 3, 1, 1, 2)

        self.tb_reload_folder = QToolButton(self.tab_folder_mode)
        self.tb_reload_folder.setObjectName(u"tb_reload_folder")
        self.tb_reload_folder.setFont(font3)

        self.gridLayout_3.addWidget(self.tb_reload_folder, 0, 1, 1, 1)

        self.pb_open_folder = QPushButton(self.tab_folder_mode)
        self.pb_open_folder.setObjectName(u"pb_open_folder")
        self.pb_open_folder.setFont(font)

        self.gridLayout_3.addWidget(self.pb_open_folder, 0, 2, 1, 1)

        self.gb_options_2 = QGroupBox(self.tab_folder_mode)
        self.gb_options_2.setObjectName(u"gb_options_2")
        self.verticalLayout_5 = QVBoxLayout(self.gb_options_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.cb_ignore_comments_2 = QCheckBox(self.gb_options_2)
        self.cb_ignore_comments_2.setObjectName(u"cb_ignore_comments_2")

        self.verticalLayout_5.addWidget(self.cb_ignore_comments_2)


        self.gridLayout_3.addWidget(self.gb_options_2, 2, 1, 1, 2)


        self.verticalLayout_3.addLayout(self.gridLayout_3)

        self.tabWidget.addTab(self.tab_folder_mode, "")

        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1000, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"CNC Tool", None))
        self.pb_save_file_as.setText(QCoreApplication.translate("MainWindow", u"Save File As", None))
        self.pb_save_file.setText(QCoreApplication.translate("MainWindow", u"Save File", None))
        self.pte_file_preview.setPlaceholderText(QCoreApplication.translate("MainWindow", u"File Preview / Manual Input", None))
        self.le_file_path.setPlaceholderText(QCoreApplication.translate("MainWindow", u"File Path", None))
#if QT_CONFIG(tooltip)
        self.tb_reload_file.setToolTip(QCoreApplication.translate("MainWindow", u"Reload File", None))
#endif // QT_CONFIG(tooltip)
        self.tb_reload_file.setText(QCoreApplication.translate("MainWindow", u"\u2b6e", None))
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
        self.pb_open_file.setText(QCoreApplication.translate("MainWindow", u"Open File", None))
        self.gb_options.setTitle(QCoreApplication.translate("MainWindow", u"Options", None))
        self.cb_ignore_comments.setText(QCoreApplication.translate("MainWindow", u"Ignore Comments", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_file_mode), QCoreApplication.translate("MainWindow", u"File Mode", None))
        self.pte_folder_preview.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Folder Preview", None))
        self.le_folder_path.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Folder Path", None))
        self.gb_functions_2.setTitle(QCoreApplication.translate("MainWindow", u"Functions", None))
        self.sb_number_lines_start_2.setPrefix(QCoreApplication.translate("MainWindow", u"N", None))
        self.lb_number_ids_step_2.setText(QCoreApplication.translate("MainWindow", u"Step:", None))
        self.lb_number_lines_step_2.setText(QCoreApplication.translate("MainWindow", u"Step:", None))
        self.lb_number_lines_start_2.setText(QCoreApplication.translate("MainWindow", u"Start:", None))
        self.lb_number_ids_start_2.setText(QCoreApplication.translate("MainWindow", u"Start:", None))
        self.pb_number_ids_2.setText(QCoreApplication.translate("MainWindow", u"Number IDS", None))
        self.sb_number_ids_start_2.setPrefix(QCoreApplication.translate("MainWindow", u"IDS=", None))
        self.pb_convert_tabs_to_spaces_2.setText(QCoreApplication.translate("MainWindow", u"Convert Tabs To Spaces", None))
        self.lb_tab_width_2.setText(QCoreApplication.translate("MainWindow", u"Tab Width", None))
        self.pb_number_lines_2.setText(QCoreApplication.translate("MainWindow", u"Number Lines", None))
        self.pb_remove_trailing_whitespace_2.setText(QCoreApplication.translate("MainWindow", u"Remove Trailing Whitespace", None))
#if QT_CONFIG(tooltip)
        self.tb_reload_folder.setToolTip(QCoreApplication.translate("MainWindow", u"Reload Folder", None))
#endif // QT_CONFIG(tooltip)
        self.tb_reload_folder.setText(QCoreApplication.translate("MainWindow", u"\u2b6e", None))
        self.pb_open_folder.setText(QCoreApplication.translate("MainWindow", u"Open Folder", None))
        self.gb_options_2.setTitle(QCoreApplication.translate("MainWindow", u"Options", None))
        self.cb_ignore_comments_2.setText(QCoreApplication.translate("MainWindow", u"Ignore Comments", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_folder_mode), QCoreApplication.translate("MainWindow", u"Folder Mode", None))
    # retranslateUi

