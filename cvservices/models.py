from __future__ import unicode_literals
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone

from django.db import models


class ControlledVocabulary(models.Model):
    CURRENT = 'Current'
    ARCHIVED = 'Archived'

    STATUS_CHOICES = (
        (CURRENT, 'Current'),
        (ARCHIVED, 'Archived')
    )

    vocabulary_id = models.AutoField(primary_key=True)
    term = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    state = models.CharField(max_length=255, blank=True)

    definition = models.TextField()
    category = models.CharField(max_length=255, blank=True)
    provenance = models.TextField(blank=True)
    provenance_uri = models.URLField(db_column='provenanceUri', blank=True)
    note = models.TextField(blank=True, null=True)
    vocabulary_status = models.CharField(max_length=255, db_column='status', choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0])
    previous_version = models.OneToOneField('self', null=True, related_name='revised_version')

    def has_revision(self):
        revision = None
        try:
            revision = self.revised_version
        except ObjectDoesNotExist:
            pass
        return revision is not None

    def get_latest_version(self):
        term = self
        while term.has_revision():
            term = term.revised_version
        return term

    class Meta:
        db_table = 'controlledvocabularies'
        ordering = ["-name"]


class ControlledVocabularyRequest(models.Model):
    PENDING = 'Pending'
    REJECTED = 'Rejected'
    ACCEPTED = 'Accepted'
    ARCHIVED = 'Archived'

    STATUS_CHOICES = (
        (PENDING, 'Pending'),
        (REJECTED, 'Rejected'),
        (ACCEPTED, 'Accepted'),
        (ARCHIVED, 'Archived'),
    )

    request_id = models.AutoField(max_length=255, db_column='requestId', primary_key=True)

    term = models.CharField(max_length=255, help_text="Please enter a URI-friendly version of your term with no spaces, special characters, etc.")
    name = models.CharField(max_length=255, help_text="Please enter the term as you would expect it to appear in a sentence.")
    state = models.CharField(max_length=255, blank=False, help_text="Please enter a state (or All) for the term.")
    definition = models.TextField(help_text="Please enter a detailed definition of the term.", blank=True)
    provenance = models.TextField(blank=True, help_text="Enter a note about where the term came from. If you retrieved the definition of the term from a website or other source, note that here.")
    provenance_uri = models.URLField(db_column='provenanceUri', blank=True, max_length=1024, help_text="If you retrieved the term from another formal vocabulary system, enter the URI of the term from the other system here.")
    note = models.TextField(blank=True, null=True, help_text="Please enter any additional notes you may have about the term.")
    category = models.CharField(max_length=255, blank=True, help_text="You may suggest a category for the term. Refer to the vocabulary to see which categories have been used. You may also suggest a new category.")

    status = models.CharField(max_length=255, db_column='status', choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0])
    date_submitted = models.DateField(db_column='dateSubmitted', default=timezone.now)
    date_status_changed = models.DateField(db_column='dateStatusChanged', default=timezone.now)
    request_notes = models.TextField(db_column='requestNotes', blank=True)
    submitter_name = models.CharField(max_length=255, db_column='submitterName', help_text="Enter your name.")
    submitter_email = models.CharField(max_length=255, db_column='submitterEmail', help_text="Enter your email address.")
    request_reason = models.TextField(db_column='requestReason', help_text="Please enter a brief description of the reason for your submission (e.g., Term does not exist yet, Term is needed for my data use case, etc.)")

    request_for = models.ForeignKey('ControlledVocabulary', db_column='requestFor', blank=True, null=True)
    original_request = models.ForeignKey('self', db_column='originalRequestId', null=True)

    class Meta:
        db_table = 'requests'
        ordering = ["date_submitted", "-request_id"]


class AggregationStatistic(ControlledVocabulary):
    class Meta:
        db_table = 'aggregationstatisticcv'
        verbose_name = 'Aggregation Statistic'
        ordering = ["name"]


class AggregationStatisticRequest(ControlledVocabularyRequest):
    class Meta:
        db_table = 'aggregationstatisticrequests'
        verbose_name = 'Aggregation Statistic Request'

        
        
class CropType(ControlledVocabulary):
    class Meta:
        db_table = 'croptypecv'
        verbose_name = 'Crop Type'
        ordering = ["name"]


class CropTypeRequest(ControlledVocabularyRequest):
    class Meta:
        db_table = 'croptyperequests'
        verbose_name = 'Crop Type Request'        
        
        
        

class EPSGCode(ControlledVocabulary):
    class Meta:
        db_table = 'epsgcodecv'
        verbose_name = 'EPSG Code'


class EPSGCodeRequest(ControlledVocabularyRequest):
    class Meta:
        db_table = 'epsgcoderequests'
        verbose_name = 'EPSG Code Request'


class GNISFeatureName(ControlledVocabulary):
    class Meta:
        db_table = 'gnisfeaturenamecv'
        verbose_name = 'GNIS Feature Name'


class GNISFeatureNameRequest(ControlledVocabularyRequest):
    class Meta:
        db_table = 'gnisfeaturenamerequests'
        verbose_name = 'GNIS Feature Name Request'


class IrrigationMethod(ControlledVocabulary):
    class Meta:
        db_table = 'irrigationmethodcv'
        verbose_name = 'Irrigation Method'


class IrrigationMethodRequest(ControlledVocabularyRequest):
    class Meta:
        db_table = 'irrigationmethodrequests'
        verbose_name = 'Irrigation Method Request'


class LegalStatus(ControlledVocabulary):
    class Meta:
        db_table = 'legalstatuscv'
        verbose_name = 'Legal Status'


class LegalStatusRequest(ControlledVocabularyRequest):
    class Meta:
        db_table = 'legalstatusrequests'
        verbose_name = 'Legal Status Request'



class MethodType(ControlledVocabulary):
    class Meta:
        db_table = 'methodtypecv'
        verbose_name = 'Method Type'


class MethodTypeRequest(ControlledVocabularyRequest):
    class Meta:
        db_table = 'methodtyperequests'
        verbose_name = 'Method Type Request'


class NAICSCode(ControlledVocabulary):
    class Meta:
        db_table = 'naicscodecv'
        verbose_name = 'NAICS Code'


class NAICSCodeRequest(ControlledVocabularyRequest):
    class Meta:
        db_table = 'naicscoderequests'
        verbose_name = 'NAICS Code Request'


class NHDNetworkStatus(ControlledVocabulary):
    class Meta:
        db_table = 'nhdnetworkstatuscv'
        verbose_name = 'NHD Network Status'


class NHDNetworkStatusRequest(ControlledVocabularyRequest):
    class Meta:
        db_table = 'nhdnetworkstatusrequests'
        verbose_name = 'NHDNetwork Status Request'


class NHDProduct(ControlledVocabulary):
    class Meta:
        db_table = 'nhdproductcv'
        verbose_name = 'NHD Product'


class NHDProductRequest(ControlledVocabularyRequest):
    class Meta:
        db_table = 'nhdproductrequests'
        verbose_name = 'NHD Product Request'


class RegulatoryStatus(ControlledVocabulary):
    class Meta:
        db_table = 'regulatorystatuscv'
        verbose_name = 'Regulatory Status'


class RegulatoryStatusRequest(ControlledVocabularyRequest):
    class Meta:
        db_table = 'regulatorystatusrequests'
        verbose_name = 'Regulatory Status Request'


class ReportingUnitType(ControlledVocabulary):
    class Meta:
        db_table = 'reportingunittypecv'
        verbose_name = 'Reporting Unit Type'


class ReportingUnitTypeRequest(ControlledVocabularyRequest):
    class Meta:
        db_table = 'reportingunittyperequests'
        verbose_name = 'Reporting Unit TypeRequest'
        
        
        
class ReportYear(ControlledVocabulary):
    class Meta:
        db_table = 'reportyearcv'
        verbose_name = 'Report Year'


class ReportYearRequest(ControlledVocabularyRequest):
    class Meta:
        db_table = 'reportyearrequests'
        verbose_name = 'Report Year Request'        

        
class ReportYearType(ControlledVocabulary):
    class Meta:
        db_table = 'reportyeartypecv'
        verbose_name = 'Report Year Type'

               
        
class ReportYearTypeRequest(ControlledVocabularyRequest):
    class Meta:
        db_table = 'reportyeartyperequests'
        verbose_name = 'Report Year Request'           
  

        
class SiteType(ControlledVocabulary):
    class Meta:
        db_table = 'sitetypecv'
        verbose_name = 'Site Type'
 


class SiteTypeRequest(ControlledVocabularyRequest):
    class Meta:
        db_table = 'sitetyperequests'
        verbose_name = 'Site Type Request'         
        
    
    
class Units(ControlledVocabulary):
    class Meta:
        db_table = 'unitscv'
        verbose_name = 'Units'


class UnitsRequest(ControlledVocabularyRequest):
    class Meta:
        db_table = 'unitsrequests'
        verbose_name = 'Units Request'             
        
        
        
class USGSCategory(ControlledVocabulary):
    class Meta:
        db_table = 'usgscategorycv'
        verbose_name = 'USGSCategory'


class USGSCategoryRequest(ControlledVocabularyRequest):
    class Meta:
        db_table = 'usgscategoryrequests'
        verbose_name = 'USGS Category Request'             
                

            
            
class Variable(ControlledVocabulary):
    class Meta:
        db_table = 'variablecv'
        verbose_name = 'Variable'


class VariableRequest(ControlledVocabularyRequest):
    class Meta:
        db_table = 'variablerequests'
        verbose_name = 'Variable Request'                 

        
        
        
        
class VariableSpecific(ControlledVocabulary):
    class Meta:
        db_table = 'variablespecificcv'
        verbose_name = 'VariableSpecific'

        
class VariableSpecificRequest(ControlledVocabularyRequest):
    class Meta:
        db_table = 'variablespecificrequests'
        verbose_name = 'Variable Specific Request'         
        

class WaterAllocationBasis(ControlledVocabulary):
    class Meta:
        db_table = 'waterallocationbasiscv'
        verbose_name = 'Water Allocation Basis'


class WaterAllocationBasisRequest(ControlledVocabularyRequest):
    class Meta:
        db_table = 'waterallocationbasisrequests'
        verbose_name = 'Water Allocation Basis Request'         
  

class WaterQualityIndicator(ControlledVocabulary):
    class Meta:
        db_table = 'waterqualityindicatorcv'
        verbose_name = 'Water Quality Indicator'


class WaterQualityIndicatorRequest(ControlledVocabularyRequest):
    class Meta:
        db_table = 'waterqualityindicatorrequests'
        verbose_name = 'Water Quality Indicator Request'        

        
        
class WaterRightType(ControlledVocabulary):
    class Meta:
        db_table = 'waterrighttypecv'
        verbose_name = 'Water Right Type'

        
        

class WaterRightTypeRequest(ControlledVocabularyRequest):
    class Meta:
        db_table = 'waterrighttyperequests'
        verbose_name = 'Water Right Type Request'             
        

        
        
class WaterSourceType(ControlledVocabulary):
    class Meta:
        db_table = 'watersourcetypecv'
        verbose_name = 'Water Source Type'



class WaterSourceTypeRequest(ControlledVocabularyRequest):
    class Meta:
        db_table = 'watersourcetyperequests'
        verbose_name = 'Water Source Type Request'             
                
