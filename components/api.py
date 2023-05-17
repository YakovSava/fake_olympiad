from os import listdir
from urllib.parse import unquote
from json import loads
from aiofiles import open as aiopen
from aiohttp.web import json_response, Request, RouteTableDef

routes = RouteTableDef()


@routes.get('/api')
async def api_page(request: Request):
    '''
	/api?method=test&data={"request": 1}
	'''

    def _split(string: str) -> dict:
        string = (string
                  .replace('=', '=\'')
                  .replace('&', '\', ')
                  )
        _temp = unquote(string) + "\'"
        _temp = eval(f'dict({_temp})')
        _temp['data'] = loads(_temp['data'])
        return _temp

    data = _split(str(request.url).split('?')[-1])
    try:
        if data['method'] == 'checkSertificate':
            return json_response(data={
                'response': f"{data['data']['number']}.html" in listdir('html/sertificates/'),
                'sertificate': f"/sertificates/{data['data']['number']}"
            })
    except:
        return json_response(data={'response': 0})