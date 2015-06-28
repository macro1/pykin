import pyramid_beaker
from pyramid import authentication, authorization, config
from social.apps.pyramid_app.models import init_social
from sqlalchemy import engine_from_config

from . import auth, models


def main(global_config, **env_settings):
    """Provides a Pyramid WSGI instance and acts as the entry point to the application."""
    settings = {
        'SOCIAL_AUTH_USER_MODEL': 'pykin.models.User',
        'SOCIAL_AUTH_AUTHENTICATION_BACKENDS': ('social.backends.twitter.TwitterOAuth',),
        'SOCIAL_AUTH_LOGIN_URL': '/',
        'SOCIAL_AUTH_LOGIN_REDIRECT_URL': '/',
        'SOCIAL_AUTH_LOGIN_FUNCTION': 'pykin.login_user',
        'SOCIAL_AUTH_LOGGEDIN_FUNCTION': 'pykin.login_required',
    }
    settings.update(env_settings)

    engine = engine_from_config(settings, 'sqlalchemy.')
    models.DBSession.configure(bind=engine)
    models.Base.metadata.bind = engine

    session_factory = pyramid_beaker.BeakerSessionFactoryConfig(
        type='ext:database',
        url=settings['sqlalchemy.url'],
    )

    app_config = config.Configurator(settings=settings)
    app_config.set_session_factory(session_factory)
    app_config.set_authentication_policy(authentication.SessionAuthenticationPolicy())
    app_config.set_authorization_policy(authorization.ACLAuthorizationPolicy())

    app_config.include('pyramid_jinja2')
    app_config.include('social.apps.pyramid_app')
    app_config.include('pyramid_beaker')

    app_config.add_static_view('static', 'static', cache_max_age=3600)
    app_config.add_route('home', '/')
    app_config.add_route('whoami', '/api/user')
    app_config.add_request_method(auth.get_user, 'user', reify=True)

    init_social(settings, models.Base, models.DBSession)
    app_config.scan('social.apps.pyramid_app')

    app_config.scan()

    return app_config.make_wsgi_app()
