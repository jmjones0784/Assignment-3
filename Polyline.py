import arcpy

feature_info = [[[260,320], [450,420], [360, 680], [600, 1000], [900,190]]]

features = []

for feature in feature_info:
    features.append(
        arcpy.Polyline(
            arcpy.Array([arcpy.Point(*coords) for coords in feature])))

print("Number of Points:   {0}".format(features[0].pointCount))