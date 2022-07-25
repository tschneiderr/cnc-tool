import os
import sys
from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtGui import QFontDatabase, QGuiApplication
from PySide6.QtWidgets import QApplication, QFileDialog, QLabel, QMainWindow

import file_functions
from ui.MainWindow import Ui_MainWindow

VERSION = "0.3.0"
MSG_TIMEOUT = 5000


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setup_fonts()
        self.setupUi(self)
        self.display_statusbar_info()
        self.connect_signals_slots()

        self.file_path = ""
        self.folder_path = ""
        self.folder_contents = []

    def setup_fonts(self):
        QFontDatabase.addApplicationFont("fonts/CascadiaMono-Light.ttf")

    def display_statusbar_info(self):
        self.statusbar.addPermanentWidget(QLabel(" Made by T. Schneider "))
        self.statusbar.addPermanentWidget(QLabel(f" v{VERSION} "))

    def connect_signals_slots(self):
        self.pb_open_file.clicked.connect(self.open_file)
        self.tb_reload_file.clicked.connect(self.load_file)
        self.pb_number_lines.clicked.connect(self.number_lines)
        self.pb_number_ids.clicked.connect(self.number_ids)
        self.pb_convert_tabs_to_spaces.clicked.connect(self.convert_tabs_to_spaces)
        self.pb_remove_trailing_whitespace.clicked.connect(
            self.remove_trailing_whitespace
        )
        self.pb_save_file.clicked.connect(self.save_file)
        self.pb_save_file_as.clicked.connect(self.save_file_as)

        self.pb_open_folder.clicked.connect(self.open_folder)
        self.tb_reload_folder.clicked.connect(self.load_folder)
        self.pb_number_lines_2.clicked.connect(self.number_lines_folder)
        self.pb_number_ids_2.clicked.connect(self.number_ids_folder)
        self.pb_convert_tabs_to_spaces_2.clicked.connect(
            self.convert_tabs_to_spaces_folder
        )
        self.pb_remove_trailing_whitespace_2.clicked.connect(
            self.remove_trailing_whitespace_folder
        )

    def open_folder(self):
        opened_folder_path = QFileDialog.getExistingDirectory(self)
        if not opened_folder_path:
            return
        self.folder_path = os.path.normpath(opened_folder_path)
        self.le_folder_path.setText(self.folder_path)
        self.load_folder()

    def load_folder(self):
        if not self.folder_path:
            return
        self.folder_contents = find_files_in_folder(
            self.folder_path, [".def", ".mpf", ".spf", ".tea"]
        )
        if not self.folder_contents:
            self.pte_folder_preview.setPlainText("No Files Found!")
            self.statusbar.showMessage("Loaded Folder!", MSG_TIMEOUT)
            return
        self.pte_folder_preview.clear()
        for file in self.folder_contents:
            self.pte_folder_preview.appendPlainText(file.name)
        self.statusbar.showMessage("Loaded Folder!", MSG_TIMEOUT)

    def number_lines_folder(self):
        for file in self.folder_contents:
            current_text = file.read_text("utf-8")
            start_number = self.sb_number_lines_start_2.value()
            step = self.sb_number_lines_step_2.value()
            if self.cb_ignore_comments_2.isChecked():
                new_text = file_functions.number_lines_wo_comment(
                    current_text, start_number, step, ";"
                )
            else:
                new_text = file_functions.number_lines(current_text, start_number, step)
            file.write_text(new_text, "utf-8")
        self.statusbar.showMessage("Numbered Lines!", MSG_TIMEOUT)

    def number_ids_folder(self):
        for file in self.folder_contents:
            current_text = file.read_text("utf-8")
            start_number = self.sb_number_ids_start_2.value()
            step = self.sb_number_ids_step_2.value()
            if self.cb_ignore_comments_2.isChecked():
                new_text = file_functions.number_ids_wo_comment(
                    current_text, start_number, step, ";"
                )
            else:
                new_text = file_functions.number_ids(current_text, start_number, step)
            file.write_text(new_text, "utf-8")
        self.statusbar.showMessage("Numbered IDS!", MSG_TIMEOUT)

    def convert_tabs_to_spaces_folder(self):
        for file in self.folder_contents:
            current_text = file.read_text("utf-8")
            tab_width = self.sb_tab_width_2.value()
            new_text = file_functions.convert_tabs_to_spaces(current_text, tab_width)
            file.write_text(new_text, "utf-8")
        self.statusbar.showMessage("Converted Tabs To Spaces!", MSG_TIMEOUT)

    def remove_trailing_whitespace_folder(self):
        for file in self.folder_contents:
            current_text = file.read_text("utf-8")
            new_text = file_functions.remove_trailing_whitespace(current_text)
            file.write_text(new_text, "utf-8")
        self.statusbar.showMessage("Removed Trailing Whitespace!", MSG_TIMEOUT)

    def open_file(self):
        opened_file_path, _ = QFileDialog.getOpenFileName(self)
        if not opened_file_path:
            return
        self.file_path = os.path.normpath(opened_file_path)
        self.le_file_path.setText(self.file_path)
        self.load_file()

    def load_file(self):
        if not self.file_path:
            return
        with open(self.file_path, encoding="utf-8") as file:
            self.pte_file_preview.setPlainText(file.read())
        self.statusbar.showMessage("Loaded File!", MSG_TIMEOUT)

    def number_lines(self):
        current_text = self.pte_file_preview.toPlainText()
        start_number = self.sb_number_lines_start.value()
        step = self.sb_number_lines_step.value()
        if self.cb_ignore_comments.isChecked():
            new_text = file_functions.number_lines_wo_comment(
                current_text, start_number, step, ";"
            )
        else:
            new_text = file_functions.number_lines(current_text, start_number, step)
        self.pte_file_preview.setPlainText(new_text)
        self.statusbar.showMessage("Numbered Lines!", MSG_TIMEOUT)

    def number_ids(self):
        current_text = self.pte_file_preview.toPlainText()
        start_number = self.sb_number_ids_start.value()
        step = self.sb_number_ids_step.value()
        if self.cb_ignore_comments.isChecked():
            new_text = file_functions.number_ids_wo_comment(
                current_text, start_number, step, ";"
            )
        else:
            new_text = file_functions.number_ids(current_text, start_number, step)
        self.pte_file_preview.setPlainText(new_text)
        self.statusbar.showMessage("Numbered IDS!", MSG_TIMEOUT)

    def convert_tabs_to_spaces(self):
        current_text = self.pte_file_preview.toPlainText()
        tab_width = self.sb_tab_width.value()
        new_text = file_functions.convert_tabs_to_spaces(current_text, tab_width)
        self.pte_file_preview.setPlainText(new_text)
        self.statusbar.showMessage("Converted Tabs To Spaces!", MSG_TIMEOUT)

    def remove_trailing_whitespace(self):
        current_text = self.pte_file_preview.toPlainText()
        new_text = file_functions.remove_trailing_whitespace(current_text)
        self.pte_file_preview.setPlainText(new_text)
        self.statusbar.showMessage("Removed Trailing Whitespace!", MSG_TIMEOUT)

    def save_file(self):
        save_file_path = self.file_path
        if not save_file_path:
            self.save_file_as()
            return
        current_text = self.pte_file_preview.toPlainText()
        with open(save_file_path, "w", encoding="utf-8") as file:
            file.write(current_text)
        self.statusbar.showMessage("Saved File!", MSG_TIMEOUT)

    def save_file_as(self):
        save_file_path, _ = QFileDialog.getSaveFileName(self)
        if not save_file_path:
            return
        self.file_path = os.path.normpath(save_file_path)
        self.le_file_path.setText(self.file_path)
        current_text = self.pte_file_preview.toPlainText()
        with open(self.file_path, "w", encoding="utf-8") as file:
            file.write(current_text)
        self.statusbar.showMessage("Saved File!", MSG_TIMEOUT)


def find_files_in_folder(folder_path: str, file_extensions: list[str]) -> list[Path]:
    file_extensions = [ext.lower() for ext in file_extensions]
    files = []
    for item in Path(folder_path).iterdir():
        if item.is_file() and item.suffix.lower() in file_extensions:
            files.append(item)
    return files


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
