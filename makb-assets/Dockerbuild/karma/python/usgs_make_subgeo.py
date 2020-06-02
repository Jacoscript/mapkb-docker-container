import math 

"This function is supposed to get the first half of a poly and prepare"
"       it for WKT format. Essentially, this is just a swapped lat, "
"       long of the gml format. "
def get_wkt_poly_3d_1(gmlpos):
        nums = gmlpos.split()
        count = 0
	coordCount = 0
	coordNum = len(nums)/3
        x = ''
        y = ''
        coordinates = ''
        for i in nums:
                if count%3 == 0:
                        x = i
                elif count%3 == 1:
                        y = i
                elif count%3 == 2:
                        z = i
	                if coordCount < math.floor(coordNum/4):
				if coordCount != 0:
                                        coordinates += ', '+y+' '+x+' '+z
                                else:
                                        coordinates += ''+y+' '+x+' '+z
			coordCount += 1
                count += 1
        wkt = 'MULTILINESTRING(('+coordinates+'))'
        return wkt

"This function is supposed to get the first half of a poly and prepare"
"       it for WKT format. Essentially, this is just a swapped lat, "
"       long of the gml format. "
def get_wkt_poly_3d_2(gmlpos):
        nums = gmlpos.split()
        count = 0
	coordCount = 0
	coordNum = len(nums)/3
        x = ''
        y = ''
        coordinates = ''
        for i in nums:
                if count%3 == 0:
                        x = i
                elif count%3 == 1:
                        y = i
		elif count%3 == 2:
			z = i
			if  coordCount >= math.floor(coordNum/4) and coordCount < 2*math.floor(coordNum/4):		
				if coordCount != math.floor(coordNum/4):
					coordinates += ', '+y+' '+x+' '+z
				else:
					coordinates += ''+y+' '+x+' '+z
			coordCount += 1
		count += 1
	wkt = 'MULTILINESTRING(('+coordinates+'))'
        return wkt

"This function is supposed to get the first half of a poly and prepare"
"       it for WKT format. Essentially, this is just a swapped lat, "
"       long of the gml format. "
def get_wkt_poly_3d_3(gmlpos):
        nums = gmlpos.split()
        count = 0
        coordCount = 0
        coordNum = len(nums)/3
        x = ''
        y = ''
        coordinates = ''
        for i in nums:
                if count%3 == 0:
                        x = i
                elif count%3 == 1:
                        y = i
                elif count%3 == 2:
                        z = i
                        if  coordCount >= 2*math.floor(coordNum/4) and coordCount < 3*math.floor(coordNum/4):
                                if coordCount != 2*math.floor(coordNum/4):
                                        coordinates += ', '+y+' '+x+' '+z
                                else:
                                        coordinates += ''+y+' '+x+' '+z
                        coordCount += 1
                count += 1
        wkt = 'MULTILINESTRING(('+coordinates+'))'
        return wkt

"This function is supposed to get the first half of a poly and prepare"
"       it for WKT format. Essentially, this is just a swapped lat, "
"       long of the gml format. "
def get_wkt_poly_3d_4(gmlpos):
        nums = gmlpos.split()
        count = 0
        coordCount = 0
        coordNum = len(nums)/3
        x = ''
        y = ''
        coordinates = ''
        for i in nums:
                if count%3 == 0:
                        x = i
                elif count%3 == 1:
                        y = i
                elif count%3 == 2:
                        z = i
                        if  coordCount >= 3*math.floor(coordNum/4):
                                if coordCount != 3*math.floor(coordNum/4):
                                        coordinates += ', '+y+' '+x+' '+z
                                else:
                                        coordinates += ''+y+' '+x+' '+z
                        coordCount += 1
                count += 1
        wkt = 'MULTILINESTRING(('+coordinates+'))'
	return wkt

"This function is supposed to get the first half of a poly and prepare"
"       it for WKT format. Essentially, this is just a swapped lat, "
"       long of the gml format. "
def get_wkt_poly_2d_1(gmlpos):
        nums = gmlpos.split()
        count = 0
        coordCount = 0
        coordNum = len(nums)/2
        x = ''
        y = ''
        coordinates = ''
        for i in nums:
                if count%2 == 0:
                        x = i
                elif count%2 == 1:
                        y = i
                        if coordCount < math.floor(coordNum/4):
                                if coordCount != 0:
                                        coordinates += ', '+y+' '+x
                                else:
                                        coordinates += ''+y+' '+x
                        coordCount += 1
                count += 1
        wkt = 'MULTILINESTRING(('+coordinates+'))'
        return wkt

"This function is supposed to get the first half of a poly and prepare"
"       it for WKT format. Essentially, this is just a swapped lat, "
"       long of the gml format. "
def get_wkt_poly_2d_2(gmlpos):
        nums = gmlpos.split()
        count = 0
        coordCount = 0
        coordNum = len(nums)/2
        x = ''
        y = ''
        coordinates = ''
        for i in nums:
                if count%2 == 0:
                        x = i
                elif count%2 == 1:
                        y = i
                        if  coordCount >= math.floor(coordNum/4) and coordCount < 2*math.floor(coordNum/4):
                                if coordCount != math.floor(coordNum/4):
                                        coordinates += ', '+y+' '+x
                                else:
                                        coordinates += ''+y+' '+x
                        coordCount += 1
                count += 1
        wkt = 'MULTILINESTRING(('+coordinates+'))'
        return wkt

"This function is supposed to get the first half of a poly and prepare"
"       it for WKT format. Essentially, this is just a swapped lat, "
"       long of the gml format. "
def get_wkt_poly_2d_3(gmlpos):
        nums = gmlpos.split()
        count = 0
        coordCount = 0
        coordNum = len(nums)/2
        x = ''
        y = ''
        coordinates = ''
        for i in nums:
                if count%2 == 0:
                        x = i
                elif count%2 == 1:
                        y = i
                        if  coordCount >= 2*math.floor(coordNum/4) and coordCount < 3*math.floor(coordNum/4):
                                if coordCount != 2*math.floor(coordNum/4):
                                        coordinates += ', '+y+' '+x
                                else:
                                        coordinates += ''+y+' '+x
                        coordCount += 1
                count += 1
        wkt = 'MULTILINESTRING(('+coordinates+'))'
        return wkt

"This function is supposed to get the first half of a poly and prepare"
"       it for WKT format. Essentially, this is just a swapped lat, "
"       long of the gml format. "
def get_wkt_poly_2d_4(gmlpos):
        nums = gmlpos.split()
        count = 0
        coordCount = 0
        coordNum = len(nums)/2
        x = ''
        y = ''
        coordinates = ''
        for i in nums:
                if count%2 == 0:
                        x = i
                elif count%2 == 1:
                        y = i
                        if  coordCount >= 3*math.floor(coordNum/4):
                                if coordCount != 3*math.floor(coordNum/4):
                                        coordinates += ', '+y+' '+x
                                else:
                                        coordinates += ''+y+' '+x
                        coordCount += 1
                count += 1
        wkt = 'MULTILINESTRING(('+coordinates+'))'
        return wkt

"This function creates URIs for the subgeometries"
def make_uri_subgeom(gmlid,subid):
	return gmlid+"_"+subid

def get_gml_poly_3d_1(pos):
    	srsDmn = 'srsDimension=\"' + getValue("srsDimension") + '\" '
    	srsVal = getValue("srsName")
    	if srsVal == "urn:ogc:def:crs:EPSG::4326":
        	srsVal = 'http://www.opengis.net/def/crs/EPSG/0/4326'
    	srsNm = 'srsName=\"' + srsVal + '\" '
    	gml = 'xmlns:gml=\"' + getValue("xmlns:gml") + '\"> '
	nums = pos.split()
        count = 0
        coordCount = 0
        coordNum = len(nums)/3
        x = ''
        y = ''
        coordinates = ''
        for i in nums:
                if count%3 == 0:
                        x = i
                elif count%3 == 1:
                        y = i
                elif count%3 == 2:
                        z = i
                        if coordCount < math.floor(coordNum/4):
                                if  coordCount != 0:
                                        coordinates += ' '+x+' '+y+' '+z
                                else:
                                        coordinates += ''+x+' '+y+' '+z
                        coordCount += 1
                count += 1

    	pos = '<gml:posList>' + coordinates + '</gml:posList> '
    	return '<gml:LineString ' + srsDmn + srsNm + gml + pos + '</gml:LineString>'

def get_gml_poly_3d_2(pos):
        srsDmn = 'srsDimension=\"' + getValue("srsDimension") + '\" '
        srsVal = getValue("srsName")
        if srsVal == "urn:ogc:def:crs:EPSG::4326":
                srsVal = 'http://www.opengis.net/def/crs/EPSG/0/4326'
        srsNm = 'srsName=\"' + srsVal + '\" '
        gml = 'xmlns:gml=\"' + getValue("xmlns:gml") + '\"> '
        nums = pos.split()
        count = 0
        coordCount = 0
        coordNum = len(nums)/3
        x = ''
        y = ''
        coordinates = ''
        for i in nums:
                if count%3 == 0:
                        x = i
                elif count%3 == 1:
                        y = i
                elif count%3 == 2:
                        z = i
                        if coordCount >= math.floor(coordNum/4) and coordCount < 2*math.floor(coordNum/4):
                                if coordCount != math.floor(coordNum/4):
                                        coordinates += ' '+x+' '+y+' '+z
                                else:
                                        coordinates += ''+x+' '+y+' '+z
                        coordCount += 1
                count += 1

        pos = '<gml:posList>' + coordinates + '</gml:posList> '
        return '<gml:LineString ' + srsDmn + srsNm + gml + pos + '</gml:LineString>'

def get_gml_poly_3d_3(pos):
        srsDmn = 'srsDimension=\"' + getValue("srsDimension") + '\" '
        srsVal = getValue("srsName")
        if srsVal == "urn:ogc:def:crs:EPSG::4326":
                srsVal = 'http://www.opengis.net/def/crs/EPSG/0/4326'
        srsNm = 'srsName=\"' + srsVal + '\" '
        gml = 'xmlns:gml=\"' + getValue("xmlns:gml") + '\"> '
        nums = pos.split()
        count = 0
        coordCount = 0
        coordNum = len(nums)/3
        x = ''
        y = ''
        coordinates = ''
        for i in nums:
                if count%3 == 0:
                        x = i
                elif count%3 == 1:
                        y = i
                elif count%3 == 2:
                        z = i
                        if coordCount >= 2*math.floor(coordNum/4) and coordCount < 3*math.floor(coordNum/4):
                                if coordCount != 2*math.floor(coordNum/4):
                                        coordinates += ' '+x+' '+y+' '+z
                                else:
                                        coordinates += ''+x+' '+y+' '+z
                        coordCount += 1
                count += 1

        pos = '<gml:posList>' + coordinates + '</gml:posList> '
        return '<gml:LineString ' + srsDmn + srsNm + gml + pos + '</gml:LineString>'

def get_gml_poly_3d_4(pos):
        srsDmn = 'srsDimension=\"' + getValue("srsDimension") + '\" '
        srsVal = getValue("srsName")
        if srsVal == "urn:ogc:def:crs:EPSG::4326":
                srsVal = 'http://www.opengis.net/def/crs/EPSG/0/4326'
        srsNm = 'srsName=\"' + srsVal + '\" '
        gml = 'xmlns:gml=\"' + getValue("xmlns:gml") + '\"> '
        nums = pos.split()
        count = 0
        coordCount = 0
        coordNum = len(nums)/3
        x = ''
        y = ''
        coordinates = ''
        for i in nums:
                if count%3 == 0:
                        x = i
                elif count%3 == 1:
                        y = i
                elif count%3 == 2:
                        z = i
                        if coordCount >= 3*math.floor(coordNum/4):
                                if coordCount != 3*math.floor(coordNum/4):
                                        coordinates += ' '+x+' '+y+' '+z
                                else:
                                        coordinates += ''+x+' '+y+' '+z
                        coordCount += 1
                count += 1

        pos = '<gml:posList>' + coordinates + '</gml:posList> '
        return '<gml:LineString ' + srsDmn + srsNm + gml + pos + '</gml:LineString>'

def get_gml_poly_2d_1(pos):
        srsDmn = 'srsDimension=\"' + getValue("srsDimension") + '\" '
        srsVal = getValue("srsName")
        if srsVal == "urn:ogc:def:crs:EPSG::4326":
                srsVal = 'http://www.opengis.net/def/crs/EPSG/0/4326'
        srsNm = 'srsName=\"' + srsVal + '\" '
        gml = 'xmlns:gml=\"' + getValue("xmlns:gml") + '\"> '
        nums = pos.split()
        count = 0
        coordCount = 0
        coordNum = len(nums)/2
        x = ''
        y = ''
        coordinates = ''
        for i in nums:
                if count%2 == 0:
                        x = i
                elif count%2 == 1:
                        y = i
                        if coordCount < math.floor(coordNum/4):
                                if  coordCount != 0:
                                        coordinates += ' '+x+' '+y
                                else:
                                        coordinates += ''+x+' '+y
                        coordCount += 1
                count += 1

        pos = '<gml:posList>' + coordinates + '</gml:posList> '
        return '<gml:LineString ' + srsDmn + srsNm + gml + pos + '</gml:LineString>'

def get_gml_poly_2d_2(pos):
        srsDmn = 'srsDimension=\"' + getValue("srsDimension") + '\" '
        srsVal = getValue("srsName")
        if srsVal == "urn:ogc:def:crs:EPSG::4326":
                srsVal = 'http://www.opengis.net/def/crs/EPSG/0/4326'
        srsNm = 'srsName=\"' + srsVal + '\" '
        gml = 'xmlns:gml=\"' + getValue("xmlns:gml") + '\"> '
        nums = pos.split()
        count = 0
        coordCount = 0
        coordNum = len(nums)/2
        x = ''
        y = ''
        coordinates = ''
        for i in nums:
                if count%2 == 0:
                        x = i
                elif count%2 == 1:
                        y = i
                        if coordCount >= math.floor(coordNum/4) and coordCount < 2*math.floor(coordNum/4):
                                if coordCount != math.floor(coordNum/4):
                                        coordinates += ' '+x+' '+y
                                else:
                                        coordinates += ''+x+' '+y
                        coordCount += 1
                count += 1

        pos = '<gml:posList>' + coordinates + '</gml:posList> '
        return '<gml:LineString ' + srsDmn + srsNm + gml + pos + '</gml:LineString>'

def get_gml_poly_2d_3(pos):
        srsDmn = 'srsDimension=\"' + getValue("srsDimension") + '\" '
        srsVal = getValue("srsName")
        if srsVal == "urn:ogc:def:crs:EPSG::4326":
                srsVal = 'http://www.opengis.net/def/crs/EPSG/0/4326'
        srsNm = 'srsName=\"' + srsVal + '\" '
        gml = 'xmlns:gml=\"' + getValue("xmlns:gml") + '\"> '
        nums = pos.split()
        count = 0
        coordCount = 0
        coordNum = len(nums)/2
        x = ''
        y = ''
        coordinates = ''
        for i in nums:
                if count%2 == 0:
                        x = i
                elif count%2 == 1:
                        y = i
                        if coordCount >= 2*math.floor(coordNum/4) and coordCount < 3*math.floor(coordNum/4):
                                if coordCount != 2*math.floor(coordNum/4):
                                        coordinates += ' '+x+' '+y
                                else:
                                        coordinates += ''+x+' '+y
                        coordCount += 1
                count += 1

        pos = '<gml:posList>' + coordinates + '</gml:posList> '
        return '<gml:LineString ' + srsDmn + srsNm + gml + pos + '</gml:LineString>'

def get_gml_poly_2d_4(pos):
        srsDmn = 'srsDimension=\"' + getValue("srsDimension") + '\" '
        srsVal = getValue("srsName")
        if srsVal == "urn:ogc:def:crs:EPSG::4326":
                srsVal = 'http://www.opengis.net/def/crs/EPSG/0/4326'
        srsNm = 'srsName=\"' + srsVal + '\" '
        gml = 'xmlns:gml=\"' + getValue("xmlns:gml") + '\"> '
        nums = pos.split()
        count = 0
        coordCount = 0
        coordNum = len(nums)/2
        x = ''
        y = ''
        coordinates = ''
        for i in nums:
                if count%2 == 0:
                        x = i
                elif count%2 == 1:
                        y = i
                        if coordCount >= 3*math.floor(coordNum/4):
                                if coordCount != 3*math.floor(coordNum/4):
                                        coordinates += ' '+x+' '+y
                                else:
                                        coordinates += ''+x+' '+y
                        coordCount += 1
                count += 1

        pos = '<gml:posList>' + coordinates + '</gml:posList> '
        return '<gml:LineString ' + srsDmn + srsNm + gml + pos + '</gml:LineString>'
	
