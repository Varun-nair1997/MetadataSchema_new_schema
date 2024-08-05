"""

The JSON template with all the mandatory and optional elements for the metadata schema. Once created, the existence of
all the mandatory elements can be checked using Check_Mandatory_Fields.py. Any missing mandatory elements will be
reported.

Author: Ronak Shoghi
ICAMS, Ruhr University Bochum, Germany
August 2024
"""



import json

Dict_Test = {
    "identifier": None,
    "title": None,
    "creator": [None],
    "creator_ORCID": [None],
    "creator_affiliation": [None],
    "creator_institute": [None],
    "creator_group": [None],
    "contributor": [None],
    "contributor_ORCID": [None],
    "contributor_affiliation": [None],
    "contributor_institute": [None],
    "contributor_group": [None],
    "date": None,
    "shared_with": [None],
    "description": None,
    "rights": None,
    "rights_holder": [None],
    "funder_name": None,
    "fund_identifier": None,
    "publisher": None,
    "relation": [None],
    "user_extra_information": None,
    "keywords": [None],
    "software": None,
    "software_version": None,
    "system": None,
    "system_version": None,
    "CPU_specifications": None,
    "input_path": None,
    "results_path": None,
    "system_extra_information": None,
    "RVE_size": [None, None, None],
    "RVE_continuity": True,
    "discretization_type": None,
    "discretization_unit_size": [None, None, None],
    "discretization_count": None,
    "origin": {
        "software": None,
        "software Version": None,
        "system": None,
        "system Version": None,
        "Input Path": None,
        "Results Path": None
        },
    "global_temperature": None,
    "mechanical_BC": [
        {"vertex_list": [None],
         "constraints": [None, None, None],
         "loading_type": None,
         "loading_mode": None,
         "applied_load": [{"magnitude": None,
                           "frequency": None,
                           "duration": None,
                           "R": None}]
         }
    ],
    "thermal_BC": [
        {"vertices_list": [None],
        "constraints": [None, None, None],
        "loading_mode": None,
         "applied_load": [{"magnitude": None,
                           "frequency": None,
                           "duration": None}]
        }
    ],
    "material": [{
        "material_identifier": None,
        "constitutive_model": {
            "elastic_parameters": None,
            "plastic_model_name": None,
            "plastic_parameters": {None},
            "hardening_model_name": None,
            "hardening_parameters": {None}
        },
        "orientation": {
            "euler_angles": {None},
            "grain_count": None,
            "orientation_identifier": None,
            "texture_type": None,
            "software": None,
            "software_version": None
        }}
    ],
    "stress": {},
    "total_strain": {},
    "plastic_strain": {}
}

with open('template.json', 'w') as fp:
    json.dump(Dict_Test, fp)