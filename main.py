from aiohttp.web import Application, RouteTableDef, Response, Request, run_app
from components.static import routes
from components.binder import Binder

binder = Binder()
app = Application()
main_routes = RouteTableDef()


@main_routes.get('/')
async def main_handler(request: Request):
    return Response(body=await binder.get_page('index.html'))


if __name__ == '__main__':
    app.add_routes(routes)
    app.add_routes(main_routes)
    run_app(app, host='192.168.100.9', port=80)
