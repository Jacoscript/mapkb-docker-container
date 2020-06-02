def adminType_uri(x):
    "Return a URI for an adminType."
    if x != '':
        return 'http://data.usgs.gov/lod/topo/OwnerClass_Domain/' + x 

def data_Security_uri(x):
    "Return a URI for a data_Security."
    if x != '':
        return 'http://data.usgs.gov/lod/topo/Sec_Classification_Domain/' + x

def distribution_Policy_uri(x):
    "Return a URI for a distribution_Policy."
    if x != '':
        return 'http://data.usgs.gov/lod/topo/Distribution_Policy_Domain/' + x

def fCode_uri(x):
    "Return a URI for a fCode."
    if x != '':
        return 'http://data.usgs.gov/lod/topo/' + x

def fType_uri(x):
    "Return a URI for a fType."
    if x != '':
        return 'http://data.usgs.gov/lod/topo/' + x

def isLandmark_uri(x):
    "Return a URI for an isLandmark."
    if x != '':
        return 'http://data.usgs.gov/lod/topo/YesNo_Domain/' + x

def pointLocationType_uri(x):
    "Return a URI for a pointLocationType."
    if x != '':
        return 'http://data.usgs.gov/lod/topo/PointLocationType_Domain/' + x

def runway_Status_uri(x):
    "Return a URI for a runway_Status."
    if x != '':
       return 'http://data.usgs.gov/lod/topo/UseStatus_Domain/' + x

def surface_Material_uri(x):
    "Return a URI for a surface_Material."
    if x != '':
        return 'http://data.usgs.gov/lod/topo/SurfaceType_Domain/' + x

def railClassification_uri(x):
    "Return a URI for railClassification."
    if x != '':
        return 'http://data.usgs.gov/lod/topo/RailClassificationFRA_Domain/' + x

def railUsage_uri(x):
    "Return a URI for railUsage."
    if x != '':
        return 'http://data.usgs.gov/lod/topo/RailUsageFRA_Domain/' + x

def tnmFRC_uri(x):
    "Return a URI for TNMFRC."
    if x != '':
        return 'http://data.usgs.gov/lod/topo/FunctionalRoadClassification/' + x

def trailYesNo_uri(x):
    "Return a URI for TrailYesNo."
    if x != '':
        return 'http://data.usgs.gov/lod/topo/TrailYesNoDomain/' + x

def nationTrailDesignation_uri(x):
    "Return a URI for nationalTrailDesignation."
    if x != '':
        return 'http://data.usgs.gov/lod/topo/NationalTrailDesignation_Domain/' + x

def primaryTrailMaintainer_uri(x):
    "Return a URI for primaryTrailMaintainer."
    if x != '':
        return 'http://data.usgs.gov/lod/topo/PrimaryTrailMaintainer_Domain/' + x

def trailType_uri(x):
    "Return a URI for trailType."
    if x != '':
        x = x.replace(" ","_")
        return 'http://data.usgs.gov/lod/topo/TrailType_Domain/' + x

def tnmFRC_uri(x):
    "Return a URI for TNMFRC."
    if x != '':
        return 'http://data.usgs.gov/lod/topo/FunctionalRoadClassification/' + x

def airport_Class_uri(x):
    "Return a URI for Airport_Class."
    if x != '':
        return 'http://data.usgs.gov/lod/topo/AirportClass_Domain/' + x

def resolution_uri(x):
    "Return a URI for Resolution."
    if x != '':
        return 'http://data.usgs.gov/lod/topo/Resolution/' +x

def flowdir_uri(x):
    "Return a URI for FlowDir."
    if x != '':
        return 'http://data.usgs.gov/lod/topo/HydroFlowDirections/' +x

def statusflag_uri(x):
    "Return a URI for StatusFlag."
    if x != '':
        return 'http://data.usgs.gov/lod/topo/StatusFlag_Domain/' +x

def humod_uri(x):
    "Return a URI for HUMod."
    if x != '':
        return 'http://data.usgs.gov/lod/topo/HUModFeatureType_Domain/' +x

def ownerormanagingagency_uri(x):
    "Return a URI for OwnerOrManagingAgency."
    if x != '':
        return 'http://data.usgs.gov/lod/topo/OwnerOrManagingAgency_Domain/' +x 

def feature_class_uri(x):
    "Return a URI for Feature_Class."
    if x != '':
        return 'http://data.usgs.gov/lod/topo/GNIS_Feature_Class/' +x

def census_code_uri(x):
    "Return a URI for Census_Class_Code."
    return 'http://data.usgs.gov/lod/topo/Census_Class_Code/' +x

def _uri(x):
    "Return a URI for ."
    return 'http://data.usgs.gov/lod/topo//' +x