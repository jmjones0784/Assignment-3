import arcpy

fc = r'C:\Student\AS.430.606\Assignment3\Assignment3\Newark.gdb\Schools'

fields = arcpy.ListFields(fc)

for f in fields:
    print("Field Name: " + str(f))
    print("Field Type:" + str(f.type()))
    print("Field Length: " + str(f.length()))