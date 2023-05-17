from json import loads
from aiohttp.web import json_response, Request, RouteTableDef

routes = RouteTableDef()

@routes.get('/api')
async def api_page(request:Request):
	'''
	/api?method=test&data={"request": 1}
	'''
	def _split(string:str) -> dict:
		string = '"' + (string.replace('&', ',')
				.replace('=', '"="')
				.replace('')
			)
	data = str(request.url).split('?')[-1]