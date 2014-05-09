date_field = {'type': 'datetime'}
string_field = {'type': 'string'}
float_field = {'type': 'float'}

waterpoint_schema = {
    'date_recorded': date_field,
    'company': string_field,
    'region': string_field,
    'district': string_field,
    'lga_name': string_field,
    'ward': string_field,
    'village': string_field,
    'village_po': string_field,
    'village_re': string_field,
    'village_ph': string_field,
    'subvillage': string_field,
    'wpt_name': string_field,
    'wpt_code': {
        'type': 'string',
        # FIXME: waterpoint codes should be unique, but are not in the dataset
        # 'unique': True,
    },
    'population': {
        'type': 'integer',
    },
    'scheme_name': string_field,
    'water_perm': string_field,
    'catchment': string_field,
    'funder': string_field,
    'installer': string_field,
    'construction_year': date_field,
    'source_type': string_field,
    'extraction': string_field,
    'waterpoint': string_field,
    'status_detail': string_field,
    'status': {
        'type': 'string',
        'allowed': ['Functional', 'Not functional'],
    },
    'breakdown_year': date_field,
    'hardware_defect': string_field,
    'reason_wpt': string_field,
    'water_quantity': string_field,
    'water_quality': string_field,
    'scheme_management': string_field,
    'wp_management': string_field,
    'water_payment': string_field,
    'amount_tsh': float_field,
    'public_meeting': string_field,
    'comment': string_field,
    'gps_height': float_field,
    'latitude': float_field,
    'longitude': float_field,
    'sensors': {
        'type': 'list',
    },
}

facility_schema = {'facility_code': "wp001",
                   'facility_name': "Waterpoint",
                   'fields': waterpoint_schema,
                   'description': "A waterpoint in Tanzania",
                   'keywords': ["location", "water", "infrastructure"],
                   'group': "water",
                   'endpoint': "waterpoints"}

service_schema = {
    "service_name": "Communal Water Point",
    "attributes": [
        {"variable": True,
         "code": "waterpoint_id",
         "datatype": "string",
         "required": True,
         "datatype_description": "Give a valid Waterpoint id",
         "order": 1,
         "description": "Unique id of this waterpoint"},
        {"variable": True,
         "code": "status",
         "datatype": "singlevaluelist",
         "required": True,
         "datatype_description": "Select an option from the list",
         "order": 2,
         "description": "Status of this waterpoint (functional, broken)",
         "values": [{"key": "functional",
                     "name": "This waterpoint is functional"},
                    {"key": "not functional",
                     "name": "This waterpoint is broken"}]}
    ],
    "description": "Location and functionality of a waterpoint",
    "keywords": ["location", "infrastructure", "water"],
    "group": "water",
    "service_code": "wp001"
}
