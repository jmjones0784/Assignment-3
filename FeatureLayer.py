import arcpy
from arcpy import env

env.workspace = r'C:\Student\AS.430.606\Assignment3\Assignment3\LasVegas.gdb'
schools = 'Schools'
schLyr = 'Schools_Layer'

print("Making Feature Layer...")
arcpy.MakeFeatureLayer_management(schools, schLyr, "ELEV_METER > 700")

lyrCount = arcpy.GetCount_management(schLyr)
result = int(lyrCount.getOutput(0))

print("Number of Records:   " + str(result))

print("Copying features...")

arcpy.CopyFeatures_management(schLyr, "High_Schools")