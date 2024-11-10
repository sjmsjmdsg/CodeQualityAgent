import requests
import json
import re
import ast


def get_osv_info(adv_id):
    """
    Get software advisory info from OSV
    :param adv_id: advisory entry id
    :return: json of OSV advisory info
    """
    url = f"https://api.osv.dev/v1/vulns/{adv_id}"
    response = requests.get(url)
    if response.status_code == 200:
        adv_info = response.json()
        return adv_info
    else:
        return None


def transfer_to_dict(resp):
    """
    Transfer string model returns to dict format
    Args:
        resp (str): The model returns.
    Return:
        resp_dict (dict): The transferred dict.
    """
    try:
        return json.loads(resp)
    except Exception as e:
        regex = r'"([A-Za-z _]+?)"\s*:\s*(\[[^\]]*\]|\d+|".*?[^\\]"|\'.*?[^\\]\')|\'([A-Za-z _]+?)\'\s*:\s*(\[[^\]]*\]|\d+|\'.*?[^\\]\'|".*?[^\\]")'
        attributes = re.findall(regex, resp)
        resp_dict = {}
        for match in attributes:
            key = match[0].strip('"').strip("'") if match[0] else match[2].strip('"').strip(
                "'")  # Select the correct group for the key
            value = match[1].strip('"').strip("'") if match[1] else match[3].strip('"').strip(
                "'")  # Select the correct group for the value

            # Check if value is a list
            if value.startswith('[') and value.endswith(']'):
                try:
                    value = ast.literal_eval(value)
                except Exception:
                    pass

            resp_dict[key] = value
        return resp_dict
