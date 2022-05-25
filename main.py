import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QGuiApplication
from PySide6.QtWidgets import QApplication, QFileDialog, QLabel, QMainWindow

import file_functions
from MainWindow import Ui_MainWindow

VERSION = "0.1.0"


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.display_statusbar_info()
        self.connect_signals_slots()

        self.file_path = ""
        self.file_contents = ""

    def display_statusbar_info(self):
        self.statusbar.addPermanentWidget(QLabel(f" v{VERSION} "))

    def connect_signals_slots(self):
        self.pb_convert_tabs_to_spaces.clicked.connect(self.convert_tabs_to_spaces)
        self.pb_number_ids.clicked.connect(self.number_ids)
        self.pb_number_lines.clicked.connect(self.number_lines)
        self.pb_open_file.clicked.connect(self.open_file)
        self.pb_remove_trailing_whitespace.clicked.connect(
            self.remove_trailing_whitespace
        )
        self.pb_save_file_as.clicked.connect(self.save_file_as)
        self.pb_save_file.clicked.connect(self.save_file)
        self.tb_reload_file.clicked.connect(self.load_file)

    def open_file(self):
        opened_file_path, _ = QFileDialog.getOpenFileName(self)
        if not opened_file_path:
            return
        self.file_path = opened_file_path
        self.le_file_path.setText(self.file_path)
        self.load_file()

    def load_file(self):
        if not self.file_path:
            return
        with open(self.file_path, encoding="utf-8") as file:
            self.pte_file_preview.setPlainText(file.read())

    def number_lines(self):
        current_text = self.pte_file_preview.toPlainText()
        start_number = self.sb_number_lines_start.value()
        step = self.sb_number_lines_step.value()
        new_text = file_functions.number_lines(current_text, start_number, step)
        self.pte_file_preview.setPlainText(new_text)

    def number_ids(self):
        current_text = self.pte_file_preview.toPlainText()
        start_number = self.sb_number_ids_start.value()
        step = self.sb_number_ids_step.value()
        new_text = file_functions.number_ids(current_text, start_number, step, ";")
        self.pte_file_preview.setPlainText(new_text)

    def convert_tabs_to_spaces(self):
        current_text = self.pte_file_preview.toPlainText()
        tab_width = self.sb_tab_width.value()
        new_text = file_functions.convert_tabs_to_spaces(current_text, tab_width)
        self.pte_file_preview.setPlainText(new_text)

    def remove_trailing_whitespace(self):
        current_text = self.pte_file_preview.toPlainText()
        new_text = file_functions.remove_trailing_whitespace(current_text)
        self.pte_file_preview.setPlainText(new_text)

    def save_file(self):
        save_file_path = self.file_path
        if not save_file_path:
            self.save_file_as()
            return
        current_text = self.pte_file_preview.toPlainText()
        with open(save_file_path, "w", encoding="utf-8") as file:
            file.write(current_text)

    def save_file_as(self):
        save_file_path, _ = QFileDialog.getSaveFileName(self)
        if not save_file_path:
            return
        current_text = self.pte_file_preview.toPlainText()
        with open(save_file_path, "w", encoding="utf-8") as file:
            file.write(current_text)
        self.file_path = save_file_path
        self.le_file_path.setText(self.file_path)


def main():
    QGuiApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.Round
    )
    app = QApplication()
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()