from flask import render_template, Blueprint

errors = Blueprint('errors', __name__)


@errors.app_errorhandler(404)
def error_404(_):
  return render_template('errors/404.html'), 404


@errors.app_errorhandler(403)
def error_403(_):
  return render_template('errors/403.html'), 404


@errors.app_errorhandler(500)
def error_500(_):
  return render_template('errors/500.html'), 404
