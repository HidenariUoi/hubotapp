# -*- coding:utf-8 -*-

from bottle import route, run, request, response, static_file
import json, os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

@route('/api/first', method='GET')
def get_json():
    result = {'a': 'hoge'}

    response.content_type = 'application/json'
    return json.dumps(result)

@route('/app', method='GET')
def static():
	print BASE_DIR
	return static_file('index.html', root=os.path.join(BASE_DIR, 'hubotapp'))


run(host='localhost', port=8080, debug=True, reloader=True)
