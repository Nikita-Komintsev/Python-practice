import urllib.parse
import aiohttp
from aiohttp import web

# Хранилище данных о лабораторных работах
labs = {}


# Обработчик запроса для внесения лабораторной работы в расписание
async def add_lab(request):
    lab_data = await request.json()
    lab_name = lab_data['name']

    if lab_name in labs:
        return web.json_response({'error': 'Lab with the same name already exists'}, status=400)

    labs[lab_name] = lab_data
    # encoded_lab_name = urllib.parse.quote_plus(lab_name)
    # return web.json_response({'url': f'http://0.0.0.0:8080/labs/{encoded_lab_name}'})
    url = f'http://0.0.0.0:8080/labs/{lab_name.replace(" ", "%20")}'
    return web.json_response({'url': url})


# Обработчик запроса для изменения лабораторной работы
async def update_lab(request):
    lab_name = request.match_info['name']

    if lab_name not in labs:
        return web.json_response({'error': 'Lab not found'}, status=404)

    lab_data = await request.json()
    lab_data['name'] = lab_name

    labs[lab_name] = lab_data
    # encoded_lab_name = urllib.parse.quote_plus(lab_name)
    # return web.json_response({'url': f'http://0.0.0.0:8080/labs/{encoded_lab_name}'})
    url = f'http://0.0.0.0:8080/labs/{lab_name.replace(" ", "%20")}'
    return web.json_response({'url': url})


# Обработчик запроса для удаления лабораторной работы
async def delete_lab(request):
    lab_name = request.match_info['name']

    if lab_name not in labs:
        return web.json_response({'error': 'Lab not found'}, status=404)

    del labs[lab_name]
    return web.json_response({'message': 'Lab deleted'})


# Обработчик запроса для получения данных о лабораторной работе
async def get_lab(request):
    lab_name = request.match_info['name']

    if lab_name not in labs:
        return web.json_response({'error': 'Lab not found'}, status=404)

    return web.json_response(labs[lab_name])


# Обработчик запроса для получения данных обо всех лабораторных работах
async def get_all_labs(request):
    return web.json_response(list(labs.values()))


# Создание и запуск приложения
app = web.Application()

app.router.add_post('/labs', add_lab)
app.router.add_patch('/labs/{name}', update_lab)
app.router.add_delete('/labs/{name}', delete_lab)
app.router.add_get('/labs/{name}', get_lab)
app.router.add_get('/labs', get_all_labs)

web.run_app(app)
