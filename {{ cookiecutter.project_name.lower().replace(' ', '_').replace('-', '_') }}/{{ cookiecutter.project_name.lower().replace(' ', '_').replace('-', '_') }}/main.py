from typing import Any, NoReturn

import sys
from collections.abc import Callable

from loguru import logger
from PyQt5.QtWidgets import QApplication
from workflow_manager.action_script import ActionScript
from workflow_manager.config import Config
from workflow_manager.workflow_manager import WorkflowManager

from {{ cookiecutter.project_name.lower().replace(' ', '_').replace('-', '_') }} import version
from {{ cookiecutter.project_name.lower().replace(' ', '_').replace('-', '_') }}.pyqt5_ui import Ui_MainWindow

logger.add("log.log", level="TRACE", rotation="50 MB")

CONFIG = Config(
    app_name=f"WorkflowManagerExample v{version}",
    statusbar_text="App designed by v3services",
    about_text="App designed by v3services.",
    pos_x=0,
    pos_y=0,
    height=1200,
    width=800,
)


class {{ cookiecutter.project_name.title().replace('_', '').replace('-', '') }}ActionScript(ActionScript):
    def script(self, **kwargs: object) -> str:
        logger.info(f"Starting: {self.__class__.__name__}.script()")

        return f"Hello World. {kwargs=}"


class {{ cookiecutter.project_name.title().replace('_', '').replace('-', '') }}WorkflowManager(WorkflowManager):
    def __init__(self) -> None:
        self.ui = Ui_MainWindow()  # type: ignore # Imports QtDesigner UI
        self.config: Config = CONFIG
        super().__init__()

    # Line 1 Callbacks
    def line1_browse_button_clicked(self):
        self.ui.line1_line_edit.setText(self._get_file_name())

    def line2_browse_button_clicked(self):
        self.ui.line2_line_edit.setText(self._get_file_name())

    def run_script_button_clicked(self):
        # Define Script & Input
        script_cls: Callable[..., Any] = {{ cookiecutter.project_name.title().replace('_', '').replace('-', '') }}ActionScript
        input1 = self.ui.line1_line_edit.text()
        input2 = self.ui.line2_line_edit.text()

        # Validate & Run Script
        if self.inputs_are_valid(input1=input1, input2=input2):
            self.run_action_script(script_cls=script_cls, input1=input1, input2=input2)

    # Connections
    def connect_buttons(self):
        """Connects UI buttons the the callback function."""
        super().connect_buttons()

        # Setup Action 1
        self.ui.line1_browse_button.clicked.connect(self.line1_browse_button_clicked)
        self.ui.line2_browse_button.clicked.connect(self.line2_browse_button_clicked)
        self.ui.run_script_button.clicked.connect(self.run_script_button_clicked)

    # Input Validations
    def validate_inputs(self, **kwargs: object) -> str | None:
        """
        Validation on required inputs. ie. Ensure file exists, ensure value is int, etc.

        Return None if passes all validations.
        Return str with error if does NOT pass validation.
        """
        if not kwargs.get("input1"):
            return "Input 1 can not be empty."
        if not kwargs.get("input2"):
            return "Input 2 can not be empty."
        return None


def main() -> NoReturn:
    app = QApplication(sys.argv)
    _ = {{ cookiecutter.project_name.title().replace('_', '').replace('-', '') }}WorkflowManager()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
