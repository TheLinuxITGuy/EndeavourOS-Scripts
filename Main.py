import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QCheckBox, QMessageBox, QGroupBox

class ScriptRunner(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('The Linux IT Guy - EndeavourOS Scripts')

        # Set fixed size for the window
        self.setFixedSize(400, 400)  # Adjust the width and height as needed

        # Layouts
        main_layout = QVBoxLayout()

        # Group boxes for Install and Remove scripts
        install_group = QGroupBox("Install")
        remove_group = QGroupBox("Remove")

        install_layout = QVBoxLayout()
        remove_layout = QVBoxLayout()

        # Scripts categorized into Install and Remove
        self.install_scripts = {
            "Brave Browser": "./install-brave.sh",
            "Google Chrome": "./install-chrome.sh",
            "Lutris": "./install-lutris.sh",
            "Microsoft Edge": "./install-edge.sh",
            "Firefox": "./install-firefox.sh",
            "Neofetch": "./install-neofetch.sh"

        }
        self.remove_scripts = {
            "Brave Browser": "./remove-brave.sh",
            "Google Chrome": "./remove-chrome.sh",
            "Microsoft Edge": "./remove-edge.sh",
            "Firefox": "./remove-firefox.sh",
            "Neofetch": "./remove-neofetch.sh"
        }

        self.checkboxes = []

        # Add checkboxes for install scripts
        for script_name in self.install_scripts:
            checkbox = QCheckBox(script_name)
            checkbox.stateChanged.connect(self.on_checkbox_state_changed)
            self.checkboxes.append(checkbox)
            install_layout.addWidget(checkbox)

        # Add checkboxes for remove scripts
        for script_name in self.remove_scripts:
            checkbox = QCheckBox(script_name)
            checkbox.stateChanged.connect(self.on_checkbox_state_changed)
            self.checkboxes.append(checkbox)
            remove_layout.addWidget(checkbox)

        install_group.setLayout(install_layout)
        remove_group.setLayout(remove_layout)

        main_layout.addWidget(install_group)
        main_layout.addWidget(remove_group)

        # Run and Quit buttons
        button_layout = QHBoxLayout()
        run_button = QPushButton('Run', self)
        quit_button = QPushButton('Quit', self)

        run_button.clicked.connect(self.run_scripts)
        quit_button.clicked.connect(self.close)

        button_layout.addWidget(run_button)
        button_layout.addWidget(quit_button)

        main_layout.addLayout(button_layout)
        self.setLayout(main_layout)

    def on_checkbox_state_changed(self, state):
        checkbox = self.sender()
        if state == 2:  # Checked state
            print(f"{checkbox.text()} checked.")
        elif state == 0:  # Unchecked state
            print(f"{checkbox.text()} unchecked.")

    def run_scripts(self):
        for checkbox in self.checkboxes:
            if checkbox.isChecked():
                script_path = self.install_scripts.get(checkbox.text()) or self.remove_scripts.get(checkbox.text())
                if script_path:
                    try:
                        subprocess.run(['bash', script_path], check=True)
                        QMessageBox.information(self, "Success", f"{checkbox.text()} executed successfully.")
                    except subprocess.CalledProcessError as e:
                        QMessageBox.critical(self, "Error", f"Failed to execute {checkbox.text()}.\n{e}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScriptRunner()
    ex.show()
    sys.exit(app.exec_())
