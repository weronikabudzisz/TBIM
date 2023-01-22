import ifcopenshell.util.element
import pprint as pp

m = ifcopenshell.open("AC-20-Smiley-West-10-Bldg.ifc")
walls = m.by_type("IfcWall")

ext_walls = []

for w in walls:
    psets = ifcopenshell.util.element.get_psets(w)
    if psets.get("Pset_WallCommon"):
        if bool(psets.get("Pset_WallCommon").get("IsExternal")):
            ext_walls.append(w)

totalvolume = 0

for w in ext_walls:
    psets = ifcopenshell.util.element.get_psets(w)
    for psetname, pset_dict in psets.items():
        for name, value in pset_dict.items():
            # print (f"{name}: {value}")
            if name == "NetVolume":
                totalvolume += float(value)
print(f'TotalVolume: {totalvolume:.2f}')