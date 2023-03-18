from typing import List


class ConverterData:

    @staticmethod
    def converter_data_json(data):
        if data:
            json_response = {
                key: value for key, value in data.__dict__.items()
                if key != '_sa_instance_state'
            }
            return json_response
        return dict()

    @staticmethod
    def paginate_json(list_data: List, page: int = 1, size: int = 100) -> dict:
        list_response = list()
        response = dict()
        for data in list_data:
            list_response.append(ConverterData.converter_data_json(data=data).copy())
        response['items'] = list_response
        response['size'] = size
        response['page'] = page
        response['total'] = len(list_data)
        return response
