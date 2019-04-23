from cvservices.models import *
from cvinterface.views.base_views import *

vocabulary_list_view = DefaultVocabularyListView
vocabulary_detail_view = DefaultVocabularyDetailView
vocabulary_list_template = 'cvinterface/vocabularies/default_list.html'
vocabulary_detail_template = 'cvinterface/vocabularies/default_detail.html'

request_list_view = DefaultRequestListView
request_create_view = DefaultRequestCreateView
request_update_view = DefaultRequestUpdateView
request_list_template = 'cvinterface/requests/default_list.html'
request_create_template = 'cvinterface/requests/default_form.html'
request_update_template = 'cvinterface/requests/default_update_form.html'

vocabularies = {
    # optional keys:
    # list_view, detail_view, list_template, detail_template

    'aggregationstatistic': {
        'name': AggregationStatistic._meta.verbose_name,
        'definition': 'A term for describing the statistical action used to calculate over recorded time series values within a time interval. For example, 100 cfs of delivery target to a demand site is a "cumulative" aggregation statistic calculated over a time interval like a month.',
        'model': AggregationStatistic,
    },
    
    'coordinatemethod': {
    'name': CoordinateMethod._meta.verbose_name,
    'definition': 'A term that indicates the coordinate method used to estimate the longitude and latitude for a site such as GPS, decree',
    'model': CoordinateMethod,
    },    
    
    'croptype': {
    'name': CropType._meta.verbose_name,
    'definition': 'A term that indicates the Crop type for the place of use, if the VariableSpecificCV is SiteSpecificConsumptive Use, Irrigation or SiteSpecificWithdrawal, Irrigation',
    'model': CropType,
    },
    
    'epsgcode': {
        'name': EPSGCode._meta.verbose_name,
        'definition': 'A term to indicate the European Petroleum Survey Group (EPSG) Code for projection, with a preference for WGS_1984, EPSG of 4326',
        'model': EPSGCode,
    },
    'gnisfeaturename': {
        'name': GNISFeatureName._meta.verbose_name,
        'definition': 'A term that describes the most appropriate Geographic Names Information System (GNIS) identifier for the source location.',
        'model': GNISFeatureName,
    },
    'irrigationmethod': {
        'name': IrrigationMethod._meta.verbose_name,
        'definition': 'A term to describe the irrigation method for the place of use, if the VariableSpecificCV is SiteSpecificConsumptive Use, Irrigation or SiteSpecificWithdrawal, Irrigation',
        'model': IrrigationMethod,
    },
    'legalstatus': {
        'name': LegalStatus._meta.verbose_name,
        'definition': 'A term that describes the legal status of the water right (e.g., proven, approved, perfected, adjudicated, etc.)',
        'model': LegalStatus,
    },
    'methodtype': {
        'name': MethodType._meta.verbose_name,
        'definition': 'A term to describe how the actual amount was determined (i.e. calculated, measured, estimated, or reported).',
        'model': MethodType,
    },
    'naicscode': {
        'name': NAICSCode._meta.verbose_name,
        'definition': 'A term for a Six-digit (North American Industry Classification System) NAICs Code associated with the primary beneficial use category',
        'model': NAICSCode,
    },
    'nhdnetworkstatus': {
        'name': NHDNetworkStatus._meta.verbose_name,
        'definition': 'A term to describe whether the point location is indexed to a USGS National Hydrography Dataset (NHD) product',
        'model': NHDNetworkStatus,
    },
    'nhdproduct': {
        'name': NHDProduct._meta.verbose_name,
        'definition': 'A term that indicates the National Hydrography Dataset (NHD) Product that is used for the indexing. Should be NHDPlus V1, NHDPlus V2, NHD Med Res, or NHD High Res.',
        'model': NHDProduct,
    },
    'regulatorystatus': {
        'name': RegulatoryStatus._meta.verbose_name,
        'definition': 'A term to indicate the status of the regulation (i.e., whether it is currently initiated/in effect)',
        'model': RegulatoryStatus,
    },
    'reportingunittype': {
        'name': ReportingUnitType._meta.verbose_name,
        'definition': 'A term to describe the type of reporting unit - county, HUC, or a custom delineation.',
        'model': ReportingUnitType,
    },
    'reportyear': {
        'name': ReportYear._meta.verbose_name,
        'definition': 'A term to indicate the annual reporting period that this data are valid. There is a need to ensure the annual reporting period year matches the type of year used by the data provider. For example, if the data are valid for November 2018, the annual reporting period could be 2018 or 2019 depending on whether the data provider uses a calendar or water year.',
        'model': ReportYear,
    },
    'reportyeartype': {
        'name': ReportYearType._meta.verbose_name,
        'definition': 'A term that describes the annual reporting period for this datatype. Could be a "water year," "irrigation year," a calendar year, or other variant.',
        'model': ReportYearType,
    },
    
    'states': {
        'name': States._meta.verbose_name,
        'definition': 'A two digit code for each US state',
        'model': States,
    },
    
    
    'sitetype': {
        'name': SiteType._meta.verbose_name,
        'definition': 'A term that describes the site type "irrigation field", City',
        'model': SiteType,
    },
    
    'units': {
        'name': Units._meta.verbose_name,
        'definition': 'A term that describes the unit of the amount',
        'model': Units,
    },
    
    'usgscategory': {
        'name': USGSCategory._meta.verbose_name,
        'definition': 'A term that assign a USGS water use category from the USGS controlled vocabulary (e.g. irrigation, groundwater, fresh)',
        'model': USGSCategory,
    },    
    
    'variable': {
        'name': Variable._meta.verbose_name,
        'definition': 'A term that describes the high-level variable used for aggregated water data to support water planning and water balances. The general categories available are for water supply, water withdrawal, consumptive use, and return flows: [AggregatedWaterSupply], [AggregatedWithdrawal], [AggregatedConsumptiveUse], [AggregatedReturnFlow]',
        'model': Variable,
    },    

    'variablespecific': {
        'name': VariableSpecific._meta.verbose_name,
        'definition': 'A term that describes a subcategorization of the site-specific variable. This allows the user to specify not only the general category of water data, but also a more specific categorization. For example, for a subcategorization of water withdrawal, the variable would be [SiteSpecificWithdrawal, Irrigation]. Other examples: [SiteSpecificConsumptiveUse, Irrigation], [SiteSpecificReturnFlow, Discharge], etc.',
        'model': VariableSpecific,
    }, 

    'waterallocationbasis': {
        'name': WaterAllocationBasis._meta.verbose_name,
        'definition': 'A Term to specify whether this water right is based on water withdrawals/diversion or consumptive use/depletion amount',
        'model': WaterAllocationBasis,
    }, 

    'waterqualityindicator': {
        'name': WaterQualityIndicator._meta.verbose_name,
        'definition': 'A term to describe water quality fresh, saline, or mixed quality',
        'model': WaterQualityIndicator,
    },     
    
    'waterallocationtype': {
        'name': WaterAllocationType._meta.verbose_name,
        'definition': 'A term that describes the water right type in each state such as Federal Reserved Water Right, Temporary Application, Water Company Shares',
        'model': WaterAllocationType,
    },     
    
    'watersourcetype': {
        'name': WaterSourceType._meta.verbose_name,
        'definition': 'A term that describes the source type of the water allocation (e.g., surface water, groundwater, mixed sources, reuse, etc.)',
        'model': WaterSourceType,
    }   
    

}


requests = {
    # optional keys:
    # list_view, create_view, update_view, list_template, create_template, update_template

    'aggregationstatisticrequest': {
        'vocabulary': 'aggregationstatistic',
        'vocabulary_model': AggregationStatistic,
        'name': AggregationStatisticRequest._meta.verbose_name,
        'model': AggregationStatisticRequest,
    },
    
    'coordinatemethodrequest': {
    'vocabulary': 'coordinatemethod',
    'vocabulary_model': CoordinateMethod,
    'name': CoordinateMethodRequest._meta.verbose_name,
    'model': CoordinateMethodRequest, 
     },
       
    'croptyperequest': {
    'vocabulary': 'croptype',
    'vocabulary_model': CropType,
    'name': CropTypeRequest._meta.verbose_name,
    'model': CropTypeRequest, 
     },
      
    'epsgcoderequest': {
        'vocabulary': 'epsgcode',
        'vocabulary_model': EPSGCode,
        'name': EPSGCodeRequest._meta.verbose_name,
        'model': EPSGCodeRequest,
    },
    'gnisfeaturenamerequest': {
        'vocabulary': 'gnisfeaturename',
        'vocabulary_model': GNISFeatureName,
        'name': GNISFeatureNameRequest._meta.verbose_name,
        'model': GNISFeatureNameRequest,
    },
    'irrigationmethodrequest': {
        'vocabulary': 'irrigationmethod',
        'vocabulary_model': IrrigationMethod,
        'name': IrrigationMethodRequest._meta.verbose_name,
        'model': IrrigationMethodRequest,
    },
    'legalstatusrequest': {
        'vocabulary': 'legalstatus',
        'vocabulary_model': LegalStatus,
        'name': LegalStatusRequest._meta.verbose_name,
        'model': LegalStatusRequest,
    },
    'methodtyperequest': {
        'vocabulary': 'methodtype',
        'vocabulary_model': MethodType,
        'name': MethodTypeRequest._meta.verbose_name,
        'model': MethodTypeRequest,
    },
    'naicscoderequest': {
        'vocabulary': 'naicscode',
        'vocabulary_model': NAICSCode,
        'name': NAICSCodeRequest._meta.verbose_name,
        'model': NAICSCodeRequest,
    },
    'nhdnetworkstatusrequest': {
        'vocabulary': 'nhdnetworkstatus',
        'vocabulary_model': NHDNetworkStatus,
        'name': NHDNetworkStatusRequest._meta.verbose_name,
        'model': NHDNetworkStatusRequest,
    },
    'nhdproductrequest': {
        'vocabulary': 'nhdproduct',
        'vocabulary_model': NHDProduct,
        'name': NHDProductRequest._meta.verbose_name,
        'model': NHDProductRequest,
    },
    'regulatorystatusrequest': {
        'vocabulary': 'regulatorystatus',
        'vocabulary_model': RegulatoryStatus,
        'name': RegulatoryStatusRequest._meta.verbose_name,
        'model': RegulatoryStatusRequest,
    },
    'reportingunittyperequest': {
        'vocabulary': 'reportingunittype',
        'vocabulary_model': ReportingUnitType,
        'name': ReportingUnitTypeRequest._meta.verbose_name,
        'model': ReportingUnitTypeRequest,
    },
    'reportyearrequest': {
        'vocabulary': 'reportyear',
        'vocabulary_model': ReportYear,
        'name': ReportYearRequest._meta.verbose_name,
        'model': ReportYearRequest,
    },
    'reportyeartyperequest': {
        'vocabulary': 'reportyeartype',
        'vocabulary_model': ReportYearType,
        'name': ReportYearTypeRequest._meta.verbose_name,
        'model': ReportYearTypeRequest,
    },
    
    'statesrequest': {
        'vocabulary': 'states',
        'vocabulary_model': States,
        'name': StatesRequest._meta.verbose_name,
        'model': StatesRequest,
    },
    
    'sitetyperequest': {
        'vocabulary': 'sitetype',
        'vocabulary_model': SiteType,
        'name': SiteTypeRequest._meta.verbose_name,
        'model': SiteTypeRequest,
    },
    
    
    'unitsrequest': {
        'vocabulary': 'units',
        'vocabulary_model': Units,
        'name': UnitsRequest._meta.verbose_name,
        'model': UnitsRequest,
    },
    'usgscategoryrequest': {
        'vocabulary': 'usgscategory',
        'vocabulary_model': USGSCategory,
        'name': USGSCategoryRequest._meta.verbose_name,
        'model': USGSCategoryRequest,
    },
    'variablerequest': {
        'vocabulary': 'variable',
        'vocabulary_model': Variable,
        'name': VariableRequest._meta.verbose_name,
        'model': VariableRequest,
    },
    'variablespecificrequest': {
        'vocabulary': 'variablespecific',
        'vocabulary_model': VariableSpecific,
        'name': VariableSpecificRequest._meta.verbose_name,
        'model': VariableSpecificRequest,
    },
    'waterallocationbasisrequest': {
        'vocabulary': 'waterallocationbasis',
        'vocabulary_model': WaterAllocationBasis,
        'name': WaterAllocationBasisRequest._meta.verbose_name,
        'model': WaterAllocationBasisRequest,
    },
    'waterqualityindicatorrequest': {
        'vocabulary': 'waterqualityindicator',
        'vocabulary_model': WaterQualityIndicator,
        'name': WaterQualityIndicatorRequest._meta.verbose_name,
        'model': WaterQualityIndicatorRequest,
    },
    'waterallocationtyperequest': {
        'vocabulary': 'waterallocationtype',
        'vocabulary_model': WaterAllocationType,
        'name': WaterAllocationTypeRequest._meta.verbose_name,
        'model': WaterAllocationTypeRequest,
    },
    'watersourcetyperequest': {
        'vocabulary': 'watersourcetype',
        'vocabulary_model': WaterSourceType,
        'name': WaterSourceTypeRequest._meta.verbose_name,
        'model': WaterSourceTypeRequest,
    }
}

