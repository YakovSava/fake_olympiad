from os import mkdir
from os.path import isdir, join
from sass import compile
from aiofiles import open as aiopen

class Binder:

    def __init__(self):
        if not isdir('html/'):
            mkdir('html')
        self._path = 'html'

    async def get_page(self, page_name: str) -> dict:
        async with aiopen(join(self._path, page_name), 'r', encoding='utf-8') as file:
            return {
                'body': await file.read(),
                'content_type': 'text/html'
            }

    async def get_css(self, css_filename: str) -> dict:
        async with aiopen(join(self._path, 'styles', css_filename), 'r', encoding='utf-8') as file:
            return {
                'body': await file.read(),
                'content_type': 'text/css'
            }

    async def get_sass(self, scss_filename: str) -> dict:
        async with aiopen(join(self._path, 'styles', scss_filename), 'r', encoding='utf-8') as file:
            return {
                'body': compile(string=await file.read()),
                'content_type': 'text/css'
            }

    async def get_js(self, js_filename: str) -> dict:
        async with aiopen(join(self._path, 'scripts', js_filename), 'r', encoding='utf-8') as file:
            return {
                'body': await file.read(),
                'content_type': 'text/javascript'
            }

    async def get_image(self, picture:str='') -> dict:
        type_ = self.type(picture)
        async with aiopen(join(self._path, 'images', picture), ('rb' if type_['binary'] else 'r')) as file:
            return {
                'body': await file.read(),
                'content_type': type_['content_type']
            }

    def type(self, filename:str) -> dict:
        if filename.endswith('.png'):
            return {
                'binary': True,
                'content_type': 'image/png'
            }
        elif filename.endswith(('.jpg', '.jpeg')):
            return {
                'binary': True,
                'content_type': 'image/jpeg'
            }
        elif filename.endswith('.svg'):
            return {
                'binary': False,
                'content_type': 'image/svg+xml'
            }