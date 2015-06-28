from pyramid import security

from . import models


def login_user(backend, user, user_social_auth):
    backend.strategy.session_set('auth.userid', user.id)


def login_required(request):
    return getattr(request, 'user', None) is not None


def get_user(request):
    """Get user instance for this request."""
    connection = models.DBSession()
    user_id = request.authenticated_userid
    if user_id is None:
        return
    return connection.query(models.User).get(user_id)
