# "This function creates a wkt representation of a point"
# def get_wkt_pt(gmlpos):
#     x = gmlpos.split()[0]
#     y = gmlpos.split()[1]
#     wkt = 'POINT(' + ' '.join([y,x]) + ')'
#     return wkt

# "This function ws create to get the wkt point of the GNIS data"
# "This function should be depreciated since all data now gets output"
# "	in the EPSG 4326 coordinate system."
# def get_wkt_pt_GNIS(gmlpos):
# # We swap the coordiantes since the data is in ESPG:404000 in default and Geoserver
# #	Will not let us reproject it for some reason.
#     	x = gmlpos.split()[0]
#     	y = gmlpos.split()[1]
#     	wkt = 'POINT(' + ' '.join([y,x]) + ')'
#     	return wkt

# "This function creates a wkt representation of a polyline"
# def get_wkt_line(gmlpos):
# 	nums = gmlpos.split()
# 	count = 0
# 	x = ''
# 	y = ''
# 	coordinates = ''
# 	for i in nums:
# 		if count%2 == 0:
# 			x = i
# 			count += 1	
# 		elif count%2 == 1:
# 			y = i
# 			if count != 1:
# 				coordinates += ', '+y+' '+x
# 			else:
# 				coordinates += ''+y+' '+x
# 			count += 1
# 	wkt = 'MULTILINESTRING(('+coordinates+ '))'
# 	return wkt

"This function get creates a wkt representation of a polygon"
def get_wkt_polygon():
    exterior = getValue("gml:exterior")
    if exterior != '':
        exterior = exterior.split("\"")
        exteriorPos =  exterior[5]
        nums = exteriorPos.split()
        count = 0
        x = ''
        y = ''
        exteriorCoordinates = ''
        for i in nums:
                if count%2 == 0:
                        x = i
                        count += 1
                elif count%2 == 1:
                        y = i
                        if count != 1:
                                exteriorCoordinates += ', '+y+' '+x
                        else:
                                exteriorCoordinates += ''+y+' '+x
                        count += 1
        exteriorCoordinates = '(' + exteriorCoordinates + ')'
    interior = getValue("gml:interior")
    if interior != '':
        interior = interior.split("\"")
        interiorPos = interior[5]
        nums = interiorPos.split()
        count = 0
        x = ''
        y = ''
        interiorCoordinates = ''
        for i in nums:
                if count%2 == 0:
                        x = i
                        count += 1
                elif count%2 == 1:
                        y = i
                        if count != 1:
                                interiorCoordinates += ', '+y+' '+x
                        else:
                                interiorCoordinates += ''+y+' '+x
                        count += 1
        interiorCoordinates = ',(' + interiorCoordinates + ')'
        wkt = 'MULTIPOLYGON(('+exteriorCoordinates + interiorCoordinates +'))'
        return wkt