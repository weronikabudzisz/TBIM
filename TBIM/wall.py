import ifcopenshell.util.element
import pprint as pp

m = ifcopenshell.open("231110AC-11-Smiley-West-04-07-2007.ifc")
walls = m.by_type("IfcWall")

