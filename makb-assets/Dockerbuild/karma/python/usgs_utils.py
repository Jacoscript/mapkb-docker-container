# Python functions for modeling USGS related data sources

def get_hash_uri(identifier):
    return getTextHash(identifier)

def clean_name(name):
    return name.strip().replace('.','')

"This functions gets the latitude of a point geometry"
def get_lat(gmlpos):
    return gmlpos.split()[0]

"This function gets the longitude of a point geometry"
def get_lon(gmlpos):
    return gmlpos.split()[1]

"This function creates a wkt representation of a point"
def get_wkt_pt(gmlpos):
    x = gmlpos.split()[0]
    y = gmlpos.split()[1]
    wkt = 'POINT(' + ' '.join([y,x]) + ')'
    return wkt

"This function ws create to get the wkt point of the GNIS data"
"This function should be depreciated since all data now gets output"
"	in the EPSG 4326 coordinate system."
def get_wkt_pt_GNIS(gmlpos):
# We swap the coordiantes since the data is in ESPG:404000 in default and Geoserver
#	Will not let us reproject it for some reason.
    	x = gmlpos.split()[0]
    	y = gmlpos.split()[1]
    	wkt = 'POINT(' + ' '.join([y,x]) + ')'
    	return wkt

"This function creates a wkt representation of a polyline"
def get_wkt_line(gmlpos):
	nums = gmlpos.split()
	count = 0
	x = ''
	y = ''
	coordinates = ''
	for i in nums:
		if count%2 == 0:
			x = i
			count += 1	
		elif count%2 == 1:
			y = i
			if count != 1:
				coordinates += ', '+y+' '+x
			else:
				coordinates += ''+y+' '+x
			count += 1
	wkt = 'MULTILINESTRING(('+coordinates+ '))'
	return wkt

"This function get creates a wkt representation of a polygon"
def get_wkt_poly(gmlpos):
        nums = gmlpos.split()
        count = 0
        x = ''
        y = ''
        coordinates = ''
        for i in nums:
                if count%2 == 0:
                        x = i
                        count += 1
                elif count%2 == 1:
                        y = i
                        if count != 1:
                                coordinates += ', '+y+' '+x
                        else:
                                coordinates += ''+y+' '+x
                        count += 1
        wkt = 'MULTIPOLYGON((('+coordinates+ ')))'
        return wkt

"I have no idea what this does."
# truncate wgs84 latitude or longitude value to 3 places after decimal
def get_coord3(coord):
    decpos = coord.find('.')
    return coord[:decpos+4]

"This function converts a gml point to a wkt point."
def conv_coor_to_wkt(gmlpos):
	x = gmlpos.split(",")[0]
	y = gmlpos.split(",")[1]
	wkt = 'POINT(' + ' '.join([y,x]) + ')'
	return wkt

"This function splits a polygon in half and collects the second half."
def get_gml_poly_2half(gmlpos):
	nums = gmlpos.split()
	count = 1
        x = ''
        y = ''
        coordinates = ''
        for i in nums:
		if count >= (len(nums)/2):
                	if count%2 == 0:
                        	y = i
				if count != ((len(nums)/2) + 1):
					coordinates += ' '+x+' '+y
				else:
					coordinates += ''+x+' '+y
                	elif count%2 == 1:
                        	x = i
		count+=1
        return coordinates

"This function split a polygon in half and collects the first half."
def get_gml_poly_1half(gmlpos):
        nums = gmlpos.split()
        count = 1
        x = ''
        y = ''
        coordinates = ''
        for i in nums:
                if count < (len(nums)/2):
                        if count%2 == 0:
                                y = i
				if count != 2:
					coordinates += ' '+x+' '+y
				else:
					coordinates += ''+x+' '+y
                        elif count%2 == 1:
                                x = i
		count += 1
        return coordinates

"This function is supposed to get the first half of a poly and prepare"
"       it for WKT format. Essentially, this is just a swapped lat, "
"       long of the gml format. "
def get_wkt_poly_1half(gmlpos):
	nums = gmlpos.split()
	count = 1
	x = ''
	y = ''
	coordinates = ''
	for i in nums:
		if count >= (len(nums)/2)-2:
			if count%2 == 0:
                                y = i
                                if count != ((len(nums)/2)-1):
                                        coordinates += ' '+y+' '+x
                                else:
                                        coordinates += ''+y+' '+x
                        elif count%2 == 1:
                                x = i
		count += 1
        return coordinates

"This function is supposed to get the first half of a poly and prepare"
"	it for WKT format. Essentially, this is just a swapped lat, "
"	long of the gml format. "
def get_wkt_poly_2half(gmlpos):
	nums = gmlpos.split()
	count = 1
	x = ''
	y = ''
	coordinates = ''
	for i in nums:
		if count < (len(nums)/2):
			if count%2 == 0:
                                y = i
                                if count != 2:
                                        coordinates += ' '+y+' '+x
                                else:
                                        coordinates += ''+y+' '+x
                        elif count%2 == 1:
                                x = i
		count += 1
        return coordinates

"This function does nothing. It was never finished."
def make_multipoly(gmlpos):
	gmlList = getValue("gml:posList")
	
	return len(gmlList)

"This function creates a wkt representation of a 3d polygon."
def make_poly_3d(gmlpos):
	nums = gmlpos.split()
	count = 0
	x = ''
	y = ''
	z = ''
	coordinates = ''
	for i in nums:
                if count%3 == 0:
                        x = i
                        count += 1
                elif count%3 == 1:
                        y = i
			count += 1
		elif count%3 == 2:
			z = i
                        if count != 2:
                                coordinates += ', '+y+' '+x+' '+z
				#if count%(len(nums)/6) == (len(nums)/6 - 1):
                                #        coordinates += '@'
                        else:
                                coordinates += ''+y+' '+x+' '+z
                        count += 1
        wkt = 'MULTIPOLYGON((('+coordinates+ ')))'#+str(len(nums))
        return wkt

"This function creates a wkt representation of a 3d polyline."
def make_line_3d(gmlpos):
        nums = gmlpos.split()
        count = 0
        x = ''
        y = ''
        z = ''
        coordinates = ''
        for i in nums:
                if count%3 == 0:
                        x = i
                        count += 1
                elif count%3 == 1:
                        y = i
                        count += 1
                elif count%3 == 2:
                        z = i
                        if count != 2:
                                coordinates += ', '+y+' '+x+' '+z
                                #if count%(len(nums)/6) == (len(nums)/6 - 1):
                                #        coordinates += '@'
                        else:
                                coordinates += ''+y+' '+x+' '+z
                        count += 1
        wkt = 'MULTILINESTRING(('+coordinates+ '))'#+str(len(nums))
        return wkt

"This function creates a wkt representation of a 3d point."
def make_point_3d(gmlpos):
        nums = gmlpos.split()
        count = 0
        x = ''
        y = ''
        z = ''
        coordinates = ''
        for i in nums:
                if count%3 == 0:
                        x = i
                        count += 1
                elif count%3 == 1:
                        y = i
                        count += 1
                elif count%3 == 2:
                        z = i
                        if count != 2:
                                coordinates += ', '+y+' '+x+' '+z
                                #if count%(len(nums)/6) == (len(nums)/6 - 1):
                                #        coordinates += '@'
                        else:
                                coordinates += ''+y+' '+x+' '+z
                        count += 1
        wkt = 'POINT('+coordinates+ ')'#+str(len(nums))
        return wkt

