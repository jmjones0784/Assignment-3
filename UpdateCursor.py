import arcpy

fc = r'C:\Student\AS.430.606\Assignment3\Assignment3\LasVegas.gdb\Hospitals'

print("Adding 'Full Address' field...")
arcpy.AddField_management(fc, "Full_Address", "TEXT", "", "", 75)
fields = ["ADDRESS", "CITY", "ST_ABREV", "Full_Address"]

print("Updating Full Address field...")
with arcpy.da.UpdateCursor(fc, fields) as cursor:
    for row in cursor:
        row[3] = row[0] + " " + row[1] + ", " + row[2]
        cursor.updateRow(row)

del cursor