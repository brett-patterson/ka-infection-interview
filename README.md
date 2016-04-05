# ka-infection-interview

An implementation of the Limited Infection interview project for Khan Academy.
This project requires:

* Python 2.x
* GraphViz
* Qt 4.8.x

as well as the following Python packages:

* PySide
* graphviz
* nose (for tests only)

Use `python setup.py install` to install as a library. Run
`python simulation.py` to start the simulator. The simulator demonstrates
the partial infection algorithm. The total infection algorithm is available
under the subpackage `ka_infection.infection`.

Tests can be run with `nosetests tests/`.
