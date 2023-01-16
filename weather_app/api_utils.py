from typing import Dict, Tuple

def json_to_latitude_longitude(response_body: Dict) -> Tuple[float,]:
    try:
        return response_body['geocoding_results']['RESULTS'][0]['COORDINATES']
    except KeyError as e:
        raise e("Couldn't parse json response.")