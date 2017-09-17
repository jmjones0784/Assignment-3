import arcpy
from arcpy import env

env.workspace = r'C:\Student\AS.430.606\Assignment3\Assignment3\Newark.gdb'
streets = 'NewarkStreets'
acc = "Accident"
buffOut = "Accident_Buffer"
clipOut = "Closed_Streets"

x = 561200
y = 613205

print("Creating Accident Location")
pt = arcpy.Point(x,y)
ptGeo = arcpy.PointGeometry(pt)
arcpy.CopyFeatures_management(ptGeo, acc)

print("Buffering...")
arcpy.Buffer_analysis(acc, buffOut, "2000 Feet")
print("Clipping...")
arcpy.Clip_analysis(streets, buffOut, clipOut)
print("Complete...")