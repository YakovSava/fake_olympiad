from aiohttp.web import Application, RouteTableDef, Response, Request, run_app
from components.static import routes as static
from components.api import routes as api
from components.binder import Binder

binder = Binder()
app = Application()
routes = RouteTableDef()


@routes.get('/')
async def main_handler(request: Request):
    return Response(**(await binder.get_page('index.html')))


@routes.get('/check')
async def search_handler(request: Request):
    return Response(**(await binder.get_page('search.html')))


@routes.get('/sertificates/{sertificatesheet}')
async def sertificate_handler(request: Request):
    return Response(**(await binder.get_page(f'sertificates/{str(request.url).split("/")[-1]}')))


if __name__ == '__main__':
    app.add_routes(routes)
    app.add_routes(static)
    app.add_routes(api)
    run_app(app, host='192.168.100.12', port=80)
