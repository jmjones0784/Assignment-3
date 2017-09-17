import arcpy

fc = r'C:\Student\AS.430.606\Assignment3\Assignment3\Newark.gdb\NewarkStreets'

desc = arcpy.Describe(fc)

print("Feature Class Shape Type:  " + desc.shapeType)
print("Feature Class Feature Type:  " + desc.featureType)
print("Feature Class has Spatial Index:  " + str(desc.hasSpatialIndex))
print("Feature Class Extent:  " + str(desc.extent))
print("Complete")