from classes import writer
from classes import pen
from classes import writing_machine
writer = writer('Arthur')
pen = pen('Strauss')
machine = writing_machine()
writer.tool = pen # Pen or Writing Machine
writer.tool.write()