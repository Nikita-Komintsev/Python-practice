import urllib.parse
from aiohttp import web
import datetime

labs = dict()


def validate_deadline_format(deadline):
    try:
        datetime.datetime.strptime(deadline, '%d.%m.%Y').date()
        return None
    except ValueError:
        return 'Invalid deadline format. Use day.month.year (e.g., 01.01.2023)'


def create_lab_url(lab_name):
    return f'http://0.0.0.0:8080/labs/{urllib.parse.quote(lab_name)}'


async def add_lab(request):
    lab_data = await request.json()

    lab_name = lab_data.get('name')
    deadline = lab_data.get('deadline')
    description = lab_data.get('description', '')

    if not lab_name or lab_name in labs:
        return web.json_response({'error': 'Lab name is required and must be unique'}, status=400)

    if not deadline:
        return web.json_response({'error': 'Deadline is required'}, status=400)

    error_date_format = validate_deadline_format(deadline)
    if error_date_format:
        return web.json_response({'error': error_date_format}, status=400)

    labs[lab_name] = {
        'name': lab_name,
        'deadline': deadline,
        'description': description,
        'students': ""
    }
    url = create_lab_url(lab_name)
    return web.json_response({'url': url})


async def update_lab(request):
    lab_name = request.match_info['name']

    if lab_name not in labs:
        return web.json_response({'error': 'Lab not found'}, status=404)

    existing_lab_data = labs[lab_name]
    new_lab_data = await request.json()

    allowed_fields = {'name', 'deadline', 'description', 'students'}
    invalid_fields = set(new_lab_data.keys()) - allowed_fields
    if invalid_fields:
        return web.json_response({'error': f'Invalid field(s): {", ".join(invalid_fields)}'}, status=400)

    if 'name' in new_lab_data and new_lab_data['name'] != lab_name:
        return web.json_response({'error': 'Lab name cannot be changed'}, status=400)

    new_lab_data.setdefault('name', lab_name)
    new_lab_data.setdefault('deadline', existing_lab_data['deadline'])
    new_lab_data.setdefault('description', existing_lab_data['description'])
    new_lab_data.setdefault('students', existing_lab_data['students'])

    error_date_format = validate_deadline_format(new_lab_data['deadline'])
    if error_date_format:
        return web.json_response({'error': error_date_format}, status=400)

    labs[lab_name] = new_lab_data
    url = create_lab_url(lab_name)
    return web.json_response({'url': url})


async def delete_lab(request):
    lab_name = request.match_info['name']

    if lab_name not in labs:
        return web.json_response({'error': 'Lab not found'}, status=404)

    del labs[lab_name]
    return web.json_response({'message': f'Laboratory {lab_name} deleted'})


async def get_lab(request):
    lab_name = request.match_info['name']

    if lab_name not in labs:
        return web.json_response({'error': 'Lab not found'}, status=404)

    return web.json_response(labs[lab_name])


async def get_all_labs(request):
    return web.json_response(list(labs.values()))


app = web.Application()

app.router.add_post('/labs', add_lab)
app.router.add_patch('/labs/{name}', update_lab)
app.router.add_delete('/labs/{name}', delete_lab)
app.router.add_get('/labs/{name}', get_lab)
app.router.add_get('/labs', get_all_labs)

web.run_app(app)
