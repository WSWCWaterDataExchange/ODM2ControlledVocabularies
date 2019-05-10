# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


def forwards(apps, schema_editor):
    namespace = apps.get_model('rdfserializer', 'Namespace')
    node = apps.get_model('rdfserializer', 'Node')
    field_relation = apps.get_model('rdfserializer', 'FieldRelation')
    scheme = apps.get_model('rdfserializer', 'Scheme')

    db_alias = schema_editor.connection.alias

    namespace.objects.using(db_alias).bulk_create([
        namespace(alias='skos', reference='http://www.w3.org/2004/02/skos/core'),
        namespace(alias='wade', reference='http://vocabulary.wade.org/WADE/WADETerms'),
        namespace(alias='dc', reference='http://purl.org/dc/elements/1.1/'),
    ])

    node.objects.using(db_alias).bulk_create([
        node(name='prefLabel', namespace_id='skos'),
        node(name='definition', namespace_id='skos'),
        node(name='note', namespace_id='skos'),
        node(name='historyNote', namespace_id='skos'),
        node(name='exactMatch', namespace_id='skos'),
        node(name='category', namespace_id='wade'),
        node(name='state', namespace_id='wade'),
		node(name='abbreviation', namespace_id='wade'),

        node(name='producesResult', namespace_id='wade'),
        node(name='Concept', namespace_id='skos'),
        node(name='inScheme', namespace_id='skos'),
        node(name='offset1', namespace_id='wade'),
        node(name='offset2', namespace_id='wade'),
        node(name='offset3', namespace_id='wade'),
        node(name='defaultUnit', namespace_id='wade'),
        node(name='dimensionSymbol', namespace_id='wade'),
        node(name='dimensionLength', namespace_id='wade'),
        node(name='dimensionMass', namespace_id='wade'),
        node(name='dimensionTime', namespace_id='wade'),
        node(name='dimensionCurrent', namespace_id='wade'),
        node(name='dimensionTemperature', namespace_id='wade'),
        node(name='dimensionAmount', namespace_id='wade'),
        node(name='dimensionLight', namespace_id='wade'),
    ])

    field_relation.objects.using(db_alias).bulk_create([
        field_relation(field_name='name',
                       node=node.objects.using(db_alias).get(name='prefLabel', namespace_id='skos')),
        field_relation(field_name='definition',
                       node=node.objects.using(db_alias).get(name='definition', namespace_id='skos')),
        field_relation(field_name='note',
                       node=node.objects.using(db_alias).get(name='note', namespace_id='skos')),
        field_relation(field_name='provenance',
                       node=node.objects.using(db_alias).get(name='historyNote', namespace_id='skos')),
        field_relation(field_name='provenance_uri',
                       node=node.objects.using(db_alias).get(name='exactMatch', namespace_id='skos')),
        field_relation(field_name='state',
                       node=node.objects.using(db_alias).get(name='state', namespace_id='wade')),
        
        field_relation(field_name='abbreviation',
                       node=node.objects.using(db_alias).get(name='abbreviation', namespace_id='wade')),		
		
		
		field_relation(field_name='category',
                       node=node.objects.using(db_alias).get(name='category', namespace_id='wade')),
        field_relation(field_name='produces_result',
                       node=node.objects.using(db_alias).get(name='producesResult', namespace_id='wade')),
        field_relation(field_name='term',
                       node=node.objects.using(db_alias).get(name='Concept', namespace_id='skos')),
        field_relation(field_name='offset1',
                       node=node.objects.using(db_alias).get(name='offset1', namespace_id='wade')),
        field_relation(field_name='offset2',
                       node=node.objects.using(db_alias).get(name='offset2', namespace_id='wade')),
        field_relation(field_name='offset3',
                       node=node.objects.using(db_alias).get(name='offset3', namespace_id='wade')),
        field_relation(field_name='default_unit',
                       node=node.objects.using(db_alias).get(name='defaultUnit', namespace_id='wade')),
        field_relation(field_name='dimension_symbol',
                       node=node.objects.using(db_alias).get(name='dimensionSymbol', namespace_id='wade')),
        field_relation(field_name='dimension_length',
                       node=node.objects.using(db_alias).get(name='dimensionLength', namespace_id='wade')),
        field_relation(field_name='dimension_mass',
                       node=node.objects.using(db_alias).get(name='dimensionMass', namespace_id='wade')),
        field_relation(field_name='dimension_time',
                       node=node.objects.using(db_alias).get(name='dimensionTime', namespace_id='wade')),
        field_relation(field_name='dimension_current',
                       node=node.objects.using(db_alias).get(name='dimensionCurrent', namespace_id='wade')),
        field_relation(field_name='dimension_temperature',
                       node=node.objects.using(db_alias).get(name='dimensionTemperature', namespace_id='wade')),
        field_relation(field_name='dimension_amount',
                       node=node.objects.using(db_alias).get(name='dimensionAmount', namespace_id='wade')),
        field_relation(field_name='dimension_light',
                       node=node.objects.using(db_alias).get(name='dimensionLight', namespace_id='wade')),
    ])

    scheme.objects.using(db_alias).bulk_create([
        scheme(name='aggregationStatistic', title='Wade Aggregation Statistic Controlled Vocabulary',
               creator='WaDE Working Group',
               description='A vocabulary for describing the calculated statistic associated with recorded observations.'
                           ' The aggregation statistic is calculated over the time aggregation interval associated '
                           'with the recorded observation. ',
               uri='http://vocabulary.westernstateswater.org/aggregationstatistic'
               ),
        
        scheme(name='applicableResourcetype', title='WaDE applicableResourcetype', creator='WaDE Working Group',
               description='A term that indicates the types of water supply or water use for which the method is used (e.g. surface water, groundwater, storage, consumptive use, withdrawal)	',
               uri='http://vocabulary.westernstateswater.org/applicableresourcetype'
               ),

        scheme(name='beneficialUse', title='WaDE beneficialUse', creator='WaDE Working Group',
               description='A term that indicates the beneficial Use for water',
               uri='http://vocabulary.westernstateswater.org/beneficialuse'
               ),
			   
			   
			   
        scheme(name='coordinateMethod', title='WaDE coordinateMethod', creator='WaDE Working Group',
               description='A term that indicates coordinate method used to report the longitude and latitude of a site',
               uri='http://vocabulary.westernstateswater.org/coordinatemethod'
               ),
        
        
        scheme(name='cropType', title='WaDE Elevation Datum Controlled Vocabulary', creator='WaDE Working Group',
               description='A term that indicates the Crop type for the place of use, if the VariableSpecificCV is SiteSpecificConsumptive Use,'
                           'Irrigation or SiteSpecificWithdrawal, Irrigation.',
               uri='http://vocabulary.westernstateswater.org/croptype'
               ),      
        
        scheme(name='dataQualityvalue', title='WaDE DataQualityValue Controlled Vocabulary', creator='WADE Working Group',
               description='A term to indicate the data quality or grading (e.g. fair, good, best, unreported), or using the NEMS data quality grading system.	',    
               uri='http://vocabulary.westernstateswater.org/dataqualityvalue'
               ),        


        scheme(name='epsgCode', title='WaDE MethodType Controlled Vocabulary', creator='WADE Working Group',
               description='A term to indicate the European Petroleum Survey Group (EPSG) Code for projection, with a preference for WGS_1984, EPSG of 4326',    
               uri='http://vocabulary.westernstateswater.org/epsgcode'
               ),
        
        scheme(name='gnisFeaturename', title='WaDE ResourceType Controlled Vocabulary', creator='WADE Working Group',
               description='A term that describes the most appropriate Geographic Names Information System (GNIS) identifier for the source location.',
               uri='http://vocabulary.westernstateswater.org/gnisfeaturename'
               ),
        
             
     
        scheme(name='irrigationMethod', title='WaDE irrigation Method Controlled Vocabulary', creator='WaDE Working Group',
               description='A term to describe the irrigation method for the place of use, if the VariableSpecificCV is SiteSpecificConsumptive Use, Irrigation or SiteSpecificWithdrawal, Irrigation',
               uri='http://vocabulary.westernstateswater.org/irrigationmethod'
               ),
        
        scheme(name='legalStatus', title='WaDE Object Topology Vocabulary', creator='WaDE Working Group',
               description='A term that describes the legal status of the water right (e.g., proven, approved, perfected, adjudicated, etc.)',
               uri='http://vocabulary.westernstateswater.org/legalstatus'
               ),
        
        
        scheme(name='methodType', title='WaDE Attribute Name Vocabulary', creator='WaDE Working Group',
               description='A term to describe how the actual amount was determined (i.e. calculated, measured, estimated, or reported).',
               uri='http://vocabulary.westernstateswater.org/methodtype'
               ),
        
        scheme(name='naicsCode', title='WaDE Attribute Data Type Controlled Vocabulary', creator='WaDE Working Group',
               description='A term for a Six-digit (North American Industry Classification System) NAICs Code associated with the primary beneficial use category',
               uri='http://vocabulary.westernstateswater.org/naicscode'
               ),
        
        scheme(name='nhdNetworkstatus', title='WaDE File Format Controlled Vocabulary', creator='WaDE Working Group',
               description='A term to describe whether the point location is indexed to a USGS National Hydrography Dataset (NHD) product',
               uri='http://vocabulary.westernstateswater.org/nhdnetworkstatus'
               ),
        
        scheme(name='nhdProduct', title='WaDE Season Name Vocabulary', creator='WaDE Working Group',
               description='A term that indicates the National Hydrography Dataset (NHD) Product that is used for the indexing. Should be NHDPlus V1, NHDPlus V2, NHD Med Res, or NHD High Res.',
               uri='http://vocabulary.westernstateswater.org/nhdproduct'
               ),
        
        scheme(name='regulatoryStatus', title='WaDE Instance Name Controlled Vocabulary', creator='WaDE Working Group',
               description='A term to indicate the status of the regulation (i.e., whether it is currently initiated/in effect)',
               uri='http://vocabulary.westernstateswater.org/regulatorystatus'
               ),
        
        
        scheme(name='reportingUnittype', title='WaDE Text Controlled Value Controlled Vocabulary', creator='WaDE Working Group',
               description='A term to describe the type of reporting unit - county, HUC, or a custom delineation.',
               uri='http://vocabulary.westernstateswater/reportingunittype'
               ),
        
        scheme(name='reportYear', title='WaDE Text Controlled Value Controlled Vocabulary', creator='WaDE Working Group',
               description='A term to indicate the annual reporting period that this data are valid. There is a need to ensure the annual reporting period year matches the type of year used by the data provider. For example, if the data are valid for November 2018, the annual reporting period could be 2018 or 2019 depending on whether the data provider uses a calendar or water year.',
               uri='http://vocabulary.westernstateswater.org/reportyear'
               ),        
        
        scheme(name='reportYeartype', title='WaDE Text Controlled Value Controlled Vocabulary', creator='WaDE Working Group',
               description='A term that describes the annual reporting period for this datatype. Could be a "water year," "irrigation year," a calendar year, or other variant. "Utah".',
               uri='http://vocabulary.westernstateswater.org/reportyeartype'
               ), 
        
        scheme(name='siteType', title='WaDE Text Controlled Value Controlled Vocabulary', creator='WaDE Working Group',
               description='A term that describes the site type',
               uri='http://vocabulary.westernstateswater.org/sitetype'
               ), 
        
        scheme(name='states', title='WaDE Text Controlled Value Controlled Vocabulary', creator='WaDE Working Group',
               description='A term that describes the state',
               uri='http://vocabulary.westernstateswater.org/state'
               ),         
        
        scheme(name='units', title='WaDE units Controlled Value Controlled Vocabulary', creator='WaDE Working Group',
               description='A term that describes the unit of the amount',
               uri='http://vocabulary.westernstateswater.org/units'
               ),
        
        scheme(name='usgsCategory', title='WaDE Text Controlled Value Controlled Vocabulary', creator='WaDE Working Group',
               description='A term that assign a USGS water use category from the USGS controlled vocabulary (e.g. irrigation, groundwater, fresh)',
               uri='http://vocabulary.westernstateswater.org/usgscategory'
               ), 
        
       scheme(name='variable', title='WaDE Text Controlled Value Controlled Vocabulary', creator='WaDE Working Group',
           description='A term that describes the high-level variable used for aggregated water data to support water planning and water balances. The general categories available are for water supply, water withdrawal, consumptive use, and return flows: [AggregatedWaterSupply], [AggregatedWithdrawal], [AggregatedConsumptiveUse], [AggregatedReturnFlow]',
           uri='http://vocabulary.westernstateswater.org/variable'
           ),
        
       scheme(name='variableSpecific', title='WaDE Text Controlled Value Controlled Vocabulary', creator='WaDE Working Group',
               description='A term that describes a subcategorization of the site-specific variable. This allows the user to specify not only the general category of water data, but also a more specific categorization. For example, for a subcategorization of water withdrawal, the variable would be [SiteSpecificWithdrawal, Irrigation]. Other examples: [SiteSpecificConsumptiveUse, Irrigation], [SiteSpecificReturnFlow, Discharge], etc.',
               uri='http://vocabulary.westernstateswater.org/variablespecific'
               ),        
        
       scheme(name='waterAllocationbasis', title='WaDE Text Controlled Value Controlled Vocabulary', creator='WaDE Working Group',
               description='A Term to specify whether this water right is based on water withdrawals/diversion or consumptive use/depletion amount.',
               uri='http://vocabulary.westernstateswater.org/waterallocationbasis'
               ),         
        
       scheme(name='waterQualityindicator', title='WaDE Text Controlled Value Controlled Vocabulary', creator='WaDE Working Group',
               description='A term to describe water quality fresh, saline, or mixed quality',
               uri='http://vocabulary.westernstateswater.org/waterqualityindicator'
               ), 
       scheme(name='waterAllocationtype', title='WaDE Text Controlled Value Controlled Vocabulary', creator='WaDE Working Group',
               description='A term that describes the water right type in each state such as Federal Reserved Water Right, Temporary Application, Water Company Shares',
               uri='http://vocabulary.westernstateswater.org/waterallocationtype'
               ),     
    
       scheme(name='waterSourcetype', title='WaDE Text Controlled Value Controlled Vocabulary', creator='WaDE Working Group',
               description='A term that describes the source type of the water allocation (e.g., surface water, groundwater, mixed sources, reuse, etc.)',
               uri='http://vocabulary.westernstateswater.org/watersourcetype'
               ),    
    ])


class Migration(migrations.Migration):
    initial = False

    dependencies = [
        ('rdfserializer', 'schema_migration'),
    ]

    operations = [
        migrations.RunPython(
            forwards,
            hints={'target_db': 'default'}
        ),
    ]

