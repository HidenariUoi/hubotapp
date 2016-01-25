# -*- coding:utf-8 -*-

from bottle import route, run, request, response
import json



@route('/api/first', method='GET')
def get_json():
    result = {'a': 'hoge'}

    response.content_type = 'application/json'
    return json.dumps(result)

run(host='localhost', port=8080, debug=True, reloader=True)
