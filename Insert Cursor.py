import arcpy

fc = r'C:\Student\AS.430.606\Assignment3\Assignment3\Newark.gdb\Schools'

x = 557940.077
y = 612696.986

name = "South Park School"
ELEV_METER = 43

point = arcpy.Point(x, y)
ptGeo = arcpy.PointGeometry(point)

cursor = arcpy.da.InsertCursor(fc, ["SHAPE@XY", "NAME", "ELEV_METER"])

for row in range(0,1):
    iRow = [ptGeo, name, ELEV_METER]
    cursor.insertRow(iRow)

del cursor