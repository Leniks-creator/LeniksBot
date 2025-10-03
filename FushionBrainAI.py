import requests
import json
import asyncio

API_KEY = "A95C7130AB56D0D9D469010E9C49F433"
SECRET_KEY = "FBB07EC1D52819309848CE7C88D3D0CE"

HEADERS = {
    "X-Key" : f'Key {API_KEY}',
    "X-Secret" : f"Secret {SECRET_KEY}"
}

URL = 'https://api-key.fusionbrain.ai/'

async def generate(prompt):
    """

    :rtype: object
    """
    params = {
        "type" : "GENERATE",
        "style" : "UHD",
        "numImages" : 1,
        "width" : 1024,
        "height" : 1024,
        "generateParams" : {"query": prompt}
    }
    files = {
        'model_id' : (None, 4),
        'params' : (None, json.dumps(params), 'application/json')
    }
    response = requests.post(URL + 'key/api/v1/text2image/run', headers=HEADERS, files=files)
    data = response.json()
    atempts = 0
    while atempts < 40:
        response = requests.get(URL + 'key/api/v1/text2image/status/' + data['uuid'], headers=HEADERS)
        data = response.json()
        if data['status'] == 'DONE':
            return data['images']
        atempts+=1
        await asyncio.sleep(3)