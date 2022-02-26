from typing import Dict, List


def model_to_dict(obj) -> Dict:
    res = obj.__dict__
    del res['_sa_instance_state']
    return res


def model_to_list(obj_list) -> List:
    res_list = []
    for i in obj_list:
        res_list.append(model_to_dict(i[0]))
    return res_list
