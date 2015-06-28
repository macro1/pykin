from pyramid.renderers import render_to_response
from pyramid.view import view_config

from . import models


@view_config(route_name='home')
def home(request):
    if not request.user:
        return render_to_response('templates/landing.jinja2', {}, request=request)
    return render_to_response('templates/app.jinja2', {}, request=request)


@view_config(route_name='whoami', renderer='json')
def whoami(request):
    """View returning the authenticated user's credentials."""
    return {
        'username': request.user.username,
        'email': request.user.email,
    }
