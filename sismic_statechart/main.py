from sismic.io import import_from_yaml, export_to_plantuml
from sismic.model import Statechart
from sismic.interpreter import Interpreter
from plantuml import PlantUML

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

# Generate PlantUML text 
plantuml_text = export_to_plantuml(statechart)

# Insert scale directive
plantuml_text = plantuml_text.replace('@startuml', '@startuml\nscale 0.5')

# Write PlantUML file
with open('statechart_visualization.puml', 'w') as f:
  f.write(plantuml_text)
  
# Create a PlantUML object and generate the diagram
puml = PlantUML(url='http://www.plantuml.com/plantuml/img/')
puml.processes_file('statechart_visualization.puml')