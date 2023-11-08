import aiohttp
from aiohttp import web
import json
from datetime import datetime
import requests

app = web.Application()

lab_schedule = {}  # Словарь для хранения данных о лабораторных работах

# Запрос для внесения лабораторной работы в расписание
async def create_lab(request):
    data = await request.json()
    lab_name = data.get('name')
    deadline_str = data.get('deadline')
    description = data.get('description')
    lab_schedule[lab_name] = {
        'name': lab_name,
        'deadline': deadline_str,
        'description': description,
        'students': []
    }
    return web.Response(text=f"Lab {lab_name} created. URL: /labs/{lab_name}")

# Запрос для изменения полей лабораторной работы
async def update_lab(request):
    lab_name = request.match_info['name']
    if lab_name in lab_schedule:
        data = await request.json()
        lab_schedule[lab_name].update(data)
        return web.Response(text=f"Lab {lab_name} updated")
    else:
        return web.Response(text=f"Lab {lab_name} not found", status=404)

# Запрос для удаления лабораторной работы
async def delete_lab(request):
    lab_name = request.match_info['name']
    if lab_name in lab_schedule:
        del lab_schedule[lab_name]
        return web.Response(text=f"Lab {lab_name} deleted")
    else:
        return web.Response(text=f"Lab {lab_name} not found", status=404)

# Запрос для получения данных о лабораторной работе
async def get_lab(request):
    lab_name = request.match_info['name']
    if lab_name in lab_schedule:
        lab_data = lab_schedule[lab_name]
        return web.Response(text=json.dumps(lab_data))
    else:
        return web.Response(text=f"Lab {lab_name} not found", status=404)

# Запрос для получения данных обо всех лабораторных работах
async def get_all_labs(request):
    labs_data = list(lab_schedule.values())
    return web.Response(text=json.dumps(labs_data))

app.router.add_post('/labs', create_lab)
app.router.add_patch('/labs/{name}', update_lab)
app.router.add_delete('/labs/{name}', delete_lab)
app.router.add_get('/labs/{name}', get_lab)
app.router.add_get('/labs', get_all_labs)

if __name__ == '__main__':
    web.run_app(app, host='localhost', port=8080)
