import arcpy

fc = r'C:\Student\AS.430.606\Assignment3\Assignment3\LasVegas.gdb\Hospitals'
fields = ['NAME', "ADDRESS", "CITY", "ST_ABREV", "ZIP_CODE"]

with arcpy.da.SearchCursor(fc, fields) as cursor:
    for row in cursor:
        print(row[0])
        print(row[1])
        print(row[2] + " " + row[3])
        print("\n")