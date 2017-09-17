import arcpy

point = arcpy.Point(5000, 2000)
ptGeo = arcpy.PointGeometry(point)

print(ptGeo)