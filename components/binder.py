from os import mkdir, listdir, getcwd
from os.path import isdir, join
from sass import compile
from aiofiles import open as aiopen


def _split_a_string(string: str) -> dict:
    raw_path_parameters = string.rsplit('-', 4)
    path_parameters = {
        'initials': raw_path_parameters[0],
        'floors': eval(raw_path_parameters[1].replace(',', '.')),
        'size': list(map(
            float,
            (raw_path_parameters[2].replace(',', '.').replace('х', 'x').split('x')))),
        'area': eval(raw_path_parameters[3].replace(',', '.')),
        'surname': raw_path_parameters[4]
    }

    return path_parameters


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