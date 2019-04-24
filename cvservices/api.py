import StringIO
from collections import OrderedDict
import csv
from django.http.response import HttpResponse
from tastypie.api import Api
from tastypie.resources import ModelResource
from tastypie.serializers import Serializer
from tastypie.utils.mime import build_content_type

from rdfserializer.api import ModelRdfResource

from models import AggregationStatistic, ApplicableResourceType,CoordinateMethod,MethodType,CropType, DataQualityValue,EPSGCode, GNISFeatureName, IrrigationMethod, LegalStatus, NAICSCode, NHDNetworkStatus, NHDProduct, RegulatoryStatus, ReportYear, ReportingUnitType, ReportYearType, SiteType,States,\
     Units,USGSCategory,Variable,VariableSpecific,WaterAllocationBasis,WaterQualityIndicator,WaterAllocationType,WaterSourceType	


class CSVSerializer(Serializer):
    formats = ['csv']
    content_types = {
        'csv': 'text/plain'
    }

    def to_csv(self, data, options=None, writer=None):
        options = options or {}
        data = self.to_simple(data, options)
        excluded_fields = [u'resource_uri']

        raw_data = StringIO.StringIO()
        first = True

        if "meta" in data.keys():
            objects = data.get("objects")

            for value in objects:
                test = {}
                for excluded_field in excluded_fields:
                    del value[excluded_field]
                self.flatten(value, test)

                odict = OrderedDict()
                odict['Term'] = test['term']
                del test['term']
                odict['UnitsLink'] = test['link']
                del test['link']

                if first:
                    writer = csv.DictWriter(raw_data, odict.keys())
                    writer.writeheader()
                    writer.writerow(odict)
                    first = False
                else:
                    writer.writerow({k: (v.encode('utf-8') if isinstance(v, int) is not True and isinstance(v, type(
                        None)) is not True else v) for k, v in odict.items()})
        else:
            test = {}
            for excluded_field in excluded_fields:
                del data[excluded_field]
            self.flatten(data, test)
            odict = OrderedDict()
            odict['Term'] = test['term']
            del test['term']
            odict['UnitsLink'] = test['link']
            del test['link']

            if first:
                writer = csv.DictWriter(raw_data, odict.keys())
                writer.writeheader()
                writer.writerow(odict)
                first = False
            else:
                writer.writerow(odict)
        CSVContent = raw_data.getvalue()
        return CSVContent

    def flatten(self, data, odict={}):
        if isinstance(data, list):
            for value in data:
                self.flatten(value, odict)
        elif isinstance(data, dict):
            for (key, value) in data.items():
                if not isinstance(value, (dict, list)):
                    odict[key] = value
                else:
                    self.flatten(value, odict)


class AggregationStatisticResource(ModelRdfResource):
    scheme = 'aggregationStatistic'

    class Meta(ModelRdfResource.Meta):
        queryset = AggregationStatistic.objects.filter(ModelRdfResource.vocabulary_filter)
        resource_name = 'aggregationstatistic'


class ApplicableResourceTypeResource(ModelRdfResource):
    scheme = 'applicableResourcetype'

    class Meta(ModelRdfResource.Meta):
        queryset = ApplicableResourceType.objects.filter(ModelRdfResource.vocabulary_filter)
        resource_name = 'applicableresourcetype'
          

class CoordinateMethodResource(ModelRdfResource):
    scheme = 'coordinateMethod'

    class Meta(ModelRdfResource.Meta):
        queryset = CoordinateMethod.objects.filter(ModelRdfResource.vocabulary_filter)
        resource_name = 'coordinatemethod'
                  
          
          
class CropTypeResource(ModelRdfResource):
    scheme = 'cropType'

    class Meta(ModelRdfResource.Meta):
        queryset = CropType.objects.filter(ModelRdfResource.vocabulary_filter)
        resource_name = 'croptype'

class DataQualityValueResource(ModelRdfResource):
    scheme = 'dataQualityvalue'

    class Meta(ModelRdfResource.Meta):
        queryset = DataQualityValue.objects.filter(ModelRdfResource.vocabulary_filter)
        resource_name = 'dataqualityvalue'  

          
          
class EPSGCodeResource(ModelRdfResource):
    scheme = 'epsgCode'

    class Meta(ModelRdfResource.Meta):
        queryset = EPSGCode.objects.filter(ModelRdfResource.vocabulary_filter)
        resource_name = 'epsgcode'          
          
          
class GNISFeatureNameResource(ModelRdfResource):
    scheme = 'gnisFeaturename'

    class Meta(ModelRdfResource.Meta):
        queryset = GNISFeatureName.objects.filter(ModelRdfResource.vocabulary_filter)
        resource_name = 'gnisfeaturename'

          
          
          
class IrrigationMethodResource(ModelRdfResource):
    scheme = 'irrigationMethod'

    class Meta(ModelRdfResource.Meta):
        queryset = IrrigationMethod.objects.filter(ModelRdfResource.vocabulary_filter)
        resource_name = 'irrigationmethod'

          
          
class LegalStatusResource(ModelRdfResource):
    scheme = 'legalStatus'

    class Meta(ModelRdfResource.Meta):
        queryset = LegalStatus.objects.filter(ModelRdfResource.vocabulary_filter)
        resource_name = 'legalstatus'

          
          
class MethodTypeResource(ModelRdfResource):
    scheme = 'methodType'

    class Meta(ModelRdfResource.Meta):
        queryset = MethodType.objects.filter(ModelRdfResource.vocabulary_filter)
        resource_name = 'methodtype'

          
          
class NAICSCodeResource(ModelRdfResource):
    scheme = 'naicsCode'

    class Meta(ModelRdfResource.Meta):
        queryset = NAICSCode.objects.filter(ModelRdfResource.vocabulary_filter)
        resource_name = 'naicscode'

          
          
class NHDNetworkStatusResource(ModelRdfResource):
    scheme = 'nhdNetorkstatus'

    class Meta(ModelRdfResource.Meta):
        queryset = NHDNetworkStatus.objects.filter(ModelRdfResource.vocabulary_filter)
        resource_name = 'nhdnetworkstatus'

          
          
class NHDProductResource(ModelRdfResource):
    scheme = 'nhdProduct'

    class Meta(ModelRdfResource.Meta):
        queryset = NHDProduct.objects.filter(ModelRdfResource.vocabulary_filter)
        resource_name = 'nhdproduct'

          

class RegulatoryStatusResource(ModelRdfResource):
    scheme = 'regulatoryStatus'

    class Meta(ModelRdfResource.Meta):
        queryset = RegulatoryStatus.objects.filter(ModelRdfResource.vocabulary_filter)
        resource_name = 'regulatorystatus'

          
          
class ReportingUnitTypeResource(ModelRdfResource):
    scheme = 'reportingUnittype'

    class Meta(ModelRdfResource.Meta):
        queryset = ReportingUnitType.objects.filter(ModelRdfResource.vocabulary_filter)
        resource_name = 'reportingunittype'

          
          
          
class ReportYearResource(ModelRdfResource):
    scheme = 'reportYear'

    class Meta(ModelRdfResource.Meta):
        queryset = ReportYear.objects.filter(ModelRdfResource.vocabulary_filter)
        resource_name = 'reportyear'

          
          

class ReportYearTypeResource(ModelRdfResource):
    scheme = 'reportYeartype'

    class Meta(ModelRdfResource.Meta):
        queryset = ReportYearType.objects.filter(ModelRdfResource.vocabulary_filter)
        resource_name = 'reportyeartype'

class SiteTypeResource(ModelRdfResource):
    scheme = 'siteType'

    class Meta(ModelRdfResource.Meta):
        queryset = SiteType.objects.filter(ModelRdfResource.vocabulary_filter)
        resource_name = 'sitetype'          


class StatesResource(ModelRdfResource):
    scheme = 'states'

    class Meta(ModelRdfResource.Meta):
        queryset = States.objects.filter(ModelRdfResource.vocabulary_filter)
        resource_name = 'states'            
          
          
          
class UnitsResource(ModelRdfResource):
    scheme = 'units'

    class Meta(ModelRdfResource.Meta):
        queryset = Units.objects.filter(ModelRdfResource.vocabulary_filter)
        resource_name = 'units'          
          
          
class USGSCategoryResource(ModelRdfResource):
    scheme = 'usgsCategory'

    class Meta(ModelRdfResource.Meta):
        queryset = USGSCategory.objects.filter(ModelRdfResource.vocabulary_filter)
        resource_name = 'usgscategory'          
 

class VariableResource(ModelRdfResource):
    scheme = 'variable'

    class Meta(ModelRdfResource.Meta):
        queryset = Variable.objects.filter(ModelRdfResource.vocabulary_filter)
        resource_name = 'variable'          
          
          
class VariableSpecificResource(ModelRdfResource):
    scheme = 'variableSpecific'

    class Meta(ModelRdfResource.Meta):
        queryset = VariableSpecific.objects.filter(ModelRdfResource.vocabulary_filter)
        resource_name = 'variablespecific'            
    


class WaterAllocationBasisResource(ModelRdfResource):
    scheme = 'waterAllocationbasis'

    class Meta(ModelRdfResource.Meta):
        queryset = WaterAllocationBasis.objects.filter(ModelRdfResource.vocabulary_filter)
        resource_name = 'waterallocationbasis'            
          
          
          
class WaterQualityIndicatorResource(ModelRdfResource):
    scheme = 'waterQualityindicator'

    class Meta(ModelRdfResource.Meta):
        queryset = WaterQualityIndicator.objects.filter(ModelRdfResource.vocabulary_filter)
        resource_name = 'waterqualityindicator'   
          
          
class WaterAllocationTypeResource(ModelRdfResource):
    scheme = 'waterAllocationtype'

    class Meta(ModelRdfResource.Meta):
        queryset = WaterAllocationType.objects.filter(ModelRdfResource.vocabulary_filter)
        resource_name = 'waterallocationtype'   
          
          
class WaterSourceTypeResource(ModelRdfResource):
    scheme = 'waterSourcetype'

    class Meta(ModelRdfResource.Meta):
        queryset = WaterSourceType.objects.filter(ModelRdfResource.vocabulary_filter)
        resource_name = 'watersourcetype'             
          
          
          
          
          
          
v1_api = Api(api_name='v1')

v1_api.register(AggregationStatisticResource())
v1_api.register(ApplicableResourceTypeResource())

v1_api.register(CoordinateMethodResource())
v1_api.register(CropTypeResource())

v1_api.register(UnitsResource())
v1_api.register(VariableSpecificResource())

v1_api.register(DataQualityValueResource())


v1_api.register(EPSGCodeResource())
v1_api.register(GNISFeatureNameResource())

v1_api.register(IrrigationMethodResource())
v1_api.register(LegalStatusResource())

v1_api.register(MethodTypeResource())
v1_api.register(NAICSCodeResource())

v1_api.register(NHDNetworkStatusResource())
v1_api.register(NHDProductResource())

v1_api.register(RegulatoryStatusResource())
v1_api.register(ReportYearResource())

v1_api.register(ReportYearTypeResource())
v1_api.register(StatesResource())

v1_api.register(SiteTypeResource())

v1_api.register(ReportingUnitTypeResource())

v1_api.register(USGSCategoryResource())
v1_api.register(VariableResource())

v1_api.register(WaterAllocationBasisResource())
v1_api.register(WaterQualityIndicatorResource())

v1_api.register(WaterAllocationTypeResource())
v1_api.register(WaterSourceTypeResource())
