import arcpy

fc = r'C:\Student\AS.430.606\Assignment3\Assignment3\Newark.gdb\Schools'

fields = arcpy.ListFields(fc)

for f in fields:
    print("Field Name:      {0}".format(f.name))
    print("Field Type:      {0}".format(f.type))
    print("Field Length:    {0}".format(f.length))
    print("\n")