import arcpy
from arcpy import env

env.workspace = r'C:\Student\AS.430.606\Assignment3\Assignment3\LasVegas.gdb'
schools = 'High_Schools'
schLyr = 'Schools_Layer'
streets = 'Streets'
strLyr = 'Streets_Layer'
copyStr = 'School_Streets'

print("Making Schools Feature Layer...")
arcpy.MakeFeatureLayer_management(schools, schLyr)

print("Making Streets Layer...")
arcpy.MakeFeatureLayer_management(streets, strLyr)

print("Selecting by street proximity to school...")
arcpy.SelectLayerByLocation_management(strLyr, "WITHIN_A_DISTANCE", schLyr, "3000 Feet")

matchcount = int(arcpy.GetCount_management(strLyr)[0])

print('{0} Features will be copied to {1}'.format(str(matchcount), copyStr))
arcpy.CopyFeatures_management(strLyr, copyStr)
