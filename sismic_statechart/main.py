from sismic.io import import_from_yaml, export_to_plantuml
from sismic.model import Statechart
from sismic.interpreter import Interpreter

# Open YAML with the representation of Statechart
with open('blockchain_agriculture_statechart.yaml') as f:
    statechart = import_from_yaml(f)
    assert isinstance(statechart, Statechart)

# Create an interpreter for the statechart
interpreter = Interpreter(statechart)

# Present statechart config
print('Before:', interpreter.configuration)

step = interpreter.execute_once()

print('After:', interpreter.configuration)