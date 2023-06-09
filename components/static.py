from urllib.parse import unquote
from aiohttp.web import Response, RouteTableDef, Request
from components.binder import Binder

routes = RouteTableDef()
get = Binder()


@routes.get('/styles/{stylesheet}')
async def styles_handler(request: Request):
    url = str(request.url)
    if url.endswith(('.scss', '.sass')):
        data = await get.get_sass(url.split('/')[-1])
    else:
        data = await get.get_css(url.split('/')[-1])
    return Response(**data)


@routes.get('/scripts/{scriptsheet}')
async def script_handler(request: Request):
    data = await get.get_js(str(request.url).split('/')[-1])
    return Response(**data)


@routes.get('/png/{a}/{b}/{c}')
async def image_handler(request: Request):
    path = unquote(str(request.url)).split('/')
    data = await get.get_pic(path[-3], path[-2], path[-1])
    return Response(**data)

@routes.get('/images/{imagesheet}')
async def imagehandler(request:Request):
    data = await get.get_image(str(request.url).split('/')[-1])
    return Response(**data)