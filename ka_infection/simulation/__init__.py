def main():
    import sys

    from PySide.QtGui import QApplication, QMainWindow
    from .simulation_widget import SimulationWidget

    app = QApplication(sys.argv)

    window = QMainWindow()
    window.setCentralWidget(SimulationWidget())
    window.show()

    sys.exit(app.exec_())
