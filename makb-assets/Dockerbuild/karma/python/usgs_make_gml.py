def get_gml_point(pos):
    srsDmn = 'srsDimension=\"' + getValue("srsDimension") + '\" '
    srsVal = getValue("srsName")
    if srsVal == "urn:ogc:def:crs:EPSG::4326":
        srsVal = 'http://www.opengis.net/def/crs/EPSG/0/4326'
    srsNm = 'srsName=\"' + srsVal + '\" '
    gml = 'xmlns:gml=\"' + getValue("xmlns:gml") + '\"> '
    pos = '<gml:pos>' + pos + '</gml:pos> '
    return '<gml:Point ' + srsDmn + srsNm + gml + pos + '</gml:Point>'

def get_gml_line(pos):
    srsDmn = 'srsDimension=\"' + getValue("srsDimension") + '\" '
    srsVal = getValue("srsName")
    if srsVal == "urn:ogc:def:crs:EPSG::4326":
        srsVal = 'http://www.opengis.net/def/crs/EPSG/0/4326'
    srsNm = 'srsName=\"' + srsVal + '\" '
    gml = 'xmlns:gml=\"' + getValue("xmlns:gml") + '\"> '
    pos = '<gml:posList>' + pos + '</gml:posList> '
    return '<gml:LineString ' + srsDmn + srsNm + gml + pos + '</gml:LineString>'

def get_gml_polygon(pos):
    srsDmn = 'srsDimension=\"' + getValue("srsDimension") + '\" '
    srsVal = getValue("srsName")
    if srsVal == "urn:ogc:def:crs:EPSG::4326":
        srsVal = 'http://www.opengis.net/def/crs/EPSG/0/4326'
    exterior = getValue("gml:exterior")
    if exterior != '':
        exterior = exterior.split("\"")
        exteriorPos = "<gml:exterior>" + "<gml:LinearRing>" + "<gml:posList>" + exterior[5] + "<gml:posList>" + "<gml:LinearRing>" + "</gml:exterior>"
    interior = getValue("gml:interior")
    if interior != '':
        interior = interior.split("\"")
        interiorPos = "<gml:interior>" + "<gml:LinearRing>" + "<gml:posList>" + interior[5] + "<gml:posList>" + "<gml:LinearRing>" + "</gml:interior>"
    srsNm = 'srsName=\"' + srsVal + '\" '
    gml = 'xmlns:gml=\"' + getValue("xmlns:gml") + '\"> '
    pos = '<gml:posList>' + pos + '</gml:posList> '
    return '<gml:Polygon ' + srsDmn + srsNm + gml + exteriorPos + interiorPos + '</gml:Polygon>'



