import os
import sys
import transaction

from sqlalchemy import engine_from_config

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

from pyramid.scripts.common import parse_vars
from social.apps.pyramid_app.models import init_social

from .. import models


def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri> [var=value]\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def main(argv=sys.argv):
    if len(argv) < 2:
        usage(argv)
    config_uri = argv[1]
    options = parse_vars(argv[2:])
    setup_logging(config_uri)
    settings = {
        'SOCIAL_AUTH_USER_MODEL': 'pykin.models.User',
    }
    settings.update(get_appsettings(config_uri, options=options))
    init_social(settings, models.Base, models.DBSession)
    engine = engine_from_config(settings, 'sqlalchemy.')
    models.DBSession.configure(bind=engine)
    models.Base.metadata.create_all(engine)

    with transaction.manager:
        pass  # put fixture models here
