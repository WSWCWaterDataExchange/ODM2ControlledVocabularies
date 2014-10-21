
import sys
import os

from ODM2.Core.services import readCore as CSread
from ODM2.Core.services import CoreServices
from ODM2.SamplingFeatures.services import readSamplingFeatures as SFread
from ODM2.Results.services import readResults as Rread

from ODMconnection import dbconnection

this_file = os.path.realpath(__file__)
directory = os.path.dirname(this_file)
sys.path.insert(0, directory)


# Create a connection to the ODM2 database
# ----------------------------------------
conn = dbconnection.createConnection('mysql', 'localhost', 'odm2', 'ODM', 'ODM123!!')
#conn = dbconnection.createConnection('mysql', 'jws.uwrl.usu.edu', 'odm2', 'ODM', 'ODM123!!')
#conn = dbconnection.createConnection('postgresql', 'arroyo.uwrl.usu.edu:5432', 'TestODM', 'stephanie', 'odm')


# Create a connection for each of the schemas. Currently the schemas each have a different
# connection but it will be changed to all the services sharing a connection
# ----------------------------------------------------------------------------------------
core_read = CSread(conn)
core = CoreServices(conn)
result_read = Rread(conn)
sampfeat_read = SFread(conn)



# Run some basic sample queries.
# ------------------------------
# Get all of the variables from the database
allVars = core.read.getAllVariables()
print "Get all Variables result: ", allVars

numVars = allVars.count()




# Get all of the people from the database
people = core_read.getAllPersons()
print "Get all People result: ", people

# Get all of the SamplingFeatures
sfs = core_read.getAllSamplingFeatures()
print "Get all SamplingFeatures result: ", sfs
if len(sfs) > 0:
    # Get the first SamplingFeature and print it's SamplingFeatureCode
    temp = sfs[0]
    print "The SamplingFeatureCode of the first SamplingFeature is: " + temp.SamplingFeatureCode


# Now get the SamplingFeature object for a SamplingFeature code
sf = core_read.getSamplingFeatureByCode('USU-LBR-Mendon')
print "Get SamplingFeatureByCode result: ", sf






# You can drill down into the code and get object linked by foreign keys
print "\n\n------------Foreign Key sample--------- \n",

# Call getAllResult, but return only the first result
firstResult = core_read.getAllResult()[0]
print "FeatureAction: ", firstResult.FeatureActionObj
print "Action: ", firstResult.FeatureActionObj.ActionObj
print "Action Attribute: ", firstResult.FeatureActionObj.ActionObj.ActionTypeCV


# Now get a particular Result using a ResultID
TSResult = result_read.getTimeSeriesResultsByResultId(19)
print "TSResult: ", TSResult

# Get the values for a particular Result - in this case time series values from a time series result
TSValues = result_read.getTimeSeriesValuesByResultId(19)
print "Values: ", TSValues
#print dir(result)







from ODM2.LikeODM1.services import SeriesService
#### LIKE ODM1 ####
conn2 = dbconnection.createConnection('mssql', 'localhost', 'odm2', 'root', 'nlcd34GIS')
odm1service = SeriesService(conn2)
#print odm1service.get_all_units()
#print odm1service.get_all_sites()











#The following query shows that you can manipulate geometries within the code
#I can get back a union of two geometries
#and convert from a string to Geometry type if it is in WKT

#Code that is being run:
#Geom = self._session.query(Samplingfeature).first()
#GeomText = self._session.query(func.ST_Union(Geom.FeatureGeometry,func.ST_GeomFromText(TestGeom)).ST_AsText()).first()


#print "\n\n------------GeometryTest--------- \n",
#TestGeom = "POINT (30 10)"
#print "Static Test Geometry:", TestGeom
#print core_read.getGeometryTest(TestGeom)



#geomsf = core_read.getSamplingFeatureByGeometry('POINT(111.781944 41.743333)')
#print "Get Sampling Feature by Geometry: ", geomsf

