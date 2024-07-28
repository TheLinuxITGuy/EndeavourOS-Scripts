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
        self.setFixedSize(400, 300)  # Adjust the width and height as needed

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

        self.install_checkboxes = {}
        self.remove_checkboxes = {}

        # Add checkboxes for install scripts
        for script_name in self.install_scripts:
            checkbox = QCheckBox(script_name)
            checkbox.stateChanged.connect(self.on_checkbox_state_changed)
            self.install_checkboxes[script_name] = checkbox
            install_layout.addWidget(checkbox)

        # Add checkboxes for remove scripts
        for script_name in self.remove_scripts:
            checkbox = QCheckBox(script_name)
            checkbox.stateChanged.connect(self.on_checkbox_state_changed)
            self.remove_checkboxes[script_name] = checkbox
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
        script_name = checkbox.text()
        if state == 2:  # Checked state
            print(f"{script_name} checked.")
            if script_name in self.install_checkboxes:
                self.remove_checkboxes[script_name].setEnabled(False)
            elif script_name in self.remove_checkboxes:
                self.install_checkboxes[script_name].setEnabled(False)
        elif state == 0:  # Unchecked state
            print(f"{script_name} unchecked.")
            if script_name in self.install_checkboxes:
                self.remove_checkboxes[script_name].setEnabled(True)
            elif script_name in self.remove_checkboxes:
                self.install_checkboxes[script_name].setEnabled(True)

    def run_scripts(self):
        for script_name, checkbox in {**self.install_checkboxes, **self.remove_checkboxes}.items():
            if checkbox.isChecked():
                script_path = self.install_scripts.get(script_name) or self.remove_scripts.get(script_name)
                if script_path:
                    try:
                        subprocess.run(['bash', script_path], check=True)
                        QMessageBox.information(self, "Success", f"{script_name} executed successfully.")
                    except subprocess.CalledProcessError as e:
                        QMessageBox.critical(self, "Error", f"Failed to execute {script_name}.\n{e}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScriptRunner()
    ex.show()
    sys.exit(app.exec_())
