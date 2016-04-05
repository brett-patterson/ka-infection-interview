from PySide.QtGui import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, QSpinBox,
                          QPushButton)
from PySide.QtSvg import QSvgWidget

from ka_infection.infection import limited_infection
from ka_infection.user import UserGraph
from .renderer import render_graph


OUT_NAME = '_out_'
OUT_FILE = OUT_NAME + '.gv.svg'


class SimulationWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super(SimulationWidget, self).__init__(*args, **kwargs)
        self._setup_ui()

    def load_graph(self):
        """ Render the graph to disk and load it into the image viewer.
        """
        render_graph(self.graph, name=OUT_NAME)
        self.image_widget.load(OUT_FILE)

    def generate(self):
        """ Generate a graph with the specified nodes and edges and render it.
        """
        nodes = self.nodes_edit.value()
        edges = self.edges_edit.value()

        self.graph = UserGraph.random(nodes, edges)
        self.load_graph()

    def infect(self):
        """ Infect the graph with the specified parameters and render it.
        """
        start = self.start_edit.value()
        target = self.target_edit.value()
        delta = self.delta_edit.value()

        if hasattr(self, 'graph') and self.graph is not None:
            # Clear all infected nodes
            for node in self.graph.users():
                node.metadata['infected'] = False

            limited_infection(self.graph.get_user(start), self.graph, target,
                              delta=delta)
            self.load_graph()

    def _setup_ui(self):
        layout = QVBoxLayout()

        top_layout = QHBoxLayout()

        top_layout.addWidget(QLabel('Nodes:'))
        self.nodes_edit = QSpinBox(self)
        self.nodes_edit.setValue(50)
        top_layout.addWidget(self.nodes_edit)

        top_layout.addWidget(QLabel('Edges:'))
        self.edges_edit = QSpinBox(self)
        self.edges_edit.setValue(50)
        top_layout.addWidget(self.edges_edit)

        generate_button = QPushButton('Generate')
        generate_button.clicked.connect(self.generate)
        top_layout.addWidget(generate_button)

        top_layout.addWidget(QLabel('Start node:'))
        self.start_edit = QSpinBox(self)
        self.start_edit.setValue(0)
        top_layout.addWidget(self.start_edit)

        top_layout.addWidget(QLabel('Target:'))
        self.target_edit = QSpinBox(self)
        self.target_edit.setValue(25)
        top_layout.addWidget(self.target_edit)

        top_layout.addWidget(QLabel('Delta:'))
        self.delta_edit = QSpinBox(self)
        self.delta_edit.setValue(0)
        top_layout.addWidget(self.delta_edit)

        infect_button = QPushButton('Infect')
        infect_button.clicked.connect(self.infect)
        top_layout.addWidget(infect_button)

        layout.addLayout(top_layout)

        self.image_widget = QSvgWidget(self)
        layout.addWidget(self.image_widget)

        self.setLayout(layout)
