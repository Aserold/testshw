import requests

def create_folder(token, folder_name):
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    params = {
        'path': folder_name
    }
    headers = {
        "Authorization" : token
    }
    response = requests.put(url, headers=headers, params=params)
    return response.status_code
    
    