from flask import render_template
from app import app, cache


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
