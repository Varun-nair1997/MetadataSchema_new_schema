"""
A novel metadata schema is introduced to address the sparsity of microstructure-sensitive mechanical data.
The schema design followed the material modeling workflow, as each run of this workflow results in the definition of
unique data objects.  It includes various categorical elements to ensure the Findability, Accessibility,
Interoperability, and Reusability (FAIR) of these data objects.

This script checks for the existence of mandatory elements in the metadata schema and reports any missing elements.

Author: Ronak Shoghi
ICAMS, Ruhr University Bochum, Germany
August 2024
"""



import json

with open('template.json') as f:
    Dict_Test = json.load(f)

list_of_mandatory_without_sub_fields = ["identifier", "title", "creator"]
list_of_mandatory_with_sub_fields = {"material": ["material_identifier"],
                                     "mechanical_BC": ["vertex_list", "constraints"]
                                     }

list_of_mandatory_with_sub_sub_fields = {"mechanical_BC": {"applied_load": ["magnitude"]},
                                         "material": {"constitutive_model": ["elastic_parameters"],
                                                      "orientation": ["euler_angles", "grain_count"]
                                                      }
                                         }
for key in Dict_Test:

    if key in list_of_mandatory_without_sub_fields:
        if Dict_Test[key] is None:
            print ("Error without sub: {}".format(key))

    if key in list_of_mandatory_with_sub_fields.keys():
        for sf in list_of_mandatory_with_sub_fields[key]:
            if isinstance(Dict_Test.get(key), list):
                for case_index, case in enumerate(Dict_Test.get(key)):
                    if case[sf] is None:
                        print("Error with sub: {} -> {} -> List_Postion {}".format(key, sf, case_index))
            else:
                if Dict_Test.get(key).get(sf) is None:
                    print("Error with sub: {} -> {}".format(key, sf))

    if key in list_of_mandatory_with_sub_sub_fields.keys():
        for sf_key in list_of_mandatory_with_sub_sub_fields[key].keys():
            for ssf in list_of_mandatory_with_sub_sub_fields[key][sf_key]:

                if ssf == "magnitude":
                    for case_index, case in enumerate(Dict_Test.get(key)):
                        if "loaded" in case.get("constraints"):
                            if case.get(sf_key).get(ssf) is None:
                                print("Error with sub: {} -> {} -> {} -> List_Postion {}".format(key, sf, ssf, case_index))

                else:
                    if isinstance(Dict_Test.get(key), list):
                        for case_index, case in enumerate(Dict_Test.get(key)):
                            if case.get(sf_key).get(ssf) is None:
                                print("Error with sub: {} -> {} -> {} -> List_Postion {}".format(key, sf, ssf, case_index))
                    else:
                        if Dict_Test.get(key).get(sf_key).get(ssf) is None:
                            print("Error with sub: {} -> {} -> {}".format(key, sf, ssf))
