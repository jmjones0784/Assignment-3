import arcpy, os

gdb = r'C:\Student\AS.430.606\Assignment3\Assignment3\Newark.gdb'
ras = os.path.join(gdb, 'studyarea')
clipRas = os.path.join(gdb, 'Newark')
outRas = os.path.join(gdb, "MyArea")

desc = arcpy.Describe(ras)
clipArea = str(desc.extent)

print("Raster Extent:  " + clipArea)
arcpy.Clip_management(clipRas, clipArea, outRas)

print("Complete")