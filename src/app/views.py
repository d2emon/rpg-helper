from flask import render_template
from app import app, cache

import requests


DEV_SERVER = 'http://localhost:43057/'

@app.context_processor
def template_globals():
    return {
        'appname': "RPG-Helper"
    }


@app.errorhandler(403)
@cache.cached()
def forbidden(error):
    return render_template('errors/403.html', title='Forbidden'), 403


@app.errorhandler(404)
@cache.cached()
def page_not_found(e):
    return render_template('error/404.html'), 404


@app.errorhandler(500)
@cache.cached()
def internal_server_error(error):
    return render_template('errors/500.html', title='Server Error'), 500


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_route(path):
    if app.debug:
        return requests.get('{}{}'.format(DEV_SERVER, path)).text
    return render_template('vue/router.html')
