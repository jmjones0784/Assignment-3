import arcpy, os
from arcpy import env

env.workspace = r'C:\Student\AS.430.606\Assignment3\Assignment3\Newark.gdb'

rasters = arcpy.ListRasters("*")

for ras in rasters:
    if ras.startswith("N"):
        raster = os.path.join(env.workspace, ras)
        print(ras)
        arcpy.Delete_management(raster)

print("Complete")