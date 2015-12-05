from os import path, pardir
from sys import stderr, exit

# Default Values
CSRF_ENABLED = True
MONGODB_SETTINGS = {
    'DB': 'eventum'
}
EVENTUM_GOOGLE_AUTH_ENABLED = False
EVENTUM_APP_LOG_NAME = 'app.log'
EVENTUM_WERKZEUG_LOG_NAME = 'werkzeug.log'
EVENTUM_LOG_FILE_MAX_SIZE = 256
EVENTUM_URL_PREFIX = '/admin'
EVENTUM_ALLOWED_UPLOAD_EXTENSIONS = set(['.png', '.jpg', '.jpeg', '.gif'])

EVENTUM_BASEDIR = path.abspath(path.join(path.dirname(__file__),
                                         pardir,
                                         pardir))

# Eventum folder
EVENTUM_RELATIVE_EVENTUM_FOLDER = 'eventum'
EVENTUM_EVENTUM_FOLDER = path.join(EVENTUM_BASEDIR, 'eventum/')

# Static folder
EVENTUM_RELATIVE_STATIC_FOLDER = path.join(EVENTUM_RELATIVE_EVENTUM_FOLDER,
                                           'static/')
EVENTUM_STATIC_FOLDER = path.join(EVENTUM_BASEDIR,
                                  EVENTUM_RELATIVE_STATIC_FOLDER)
# Upload folder
EVENTUM_RELATIVE_UPLOAD_FOLDER = path.join(EVENTUM_RELATIVE_STATIC_FOLDER,
                                           'img/uploaded/')
EVENTUM_UPLOAD_FOLDER = path.join(EVENTUM_BASEDIR,
                                  EVENTUM_RELATIVE_UPLOAD_FOLDER)
# Delete Folder
EVENTUM_RELATIVE_DELETE_FOLDER = path.join(EVENTUM_RELATIVE_STATIC_FOLDER,
                                           'img/uploaded/deleted/')
EVENTUM_DELETE_FOLDER = path.join(EVENTUM_BASEDIR,
                                  EVENTUM_RELATIVE_DELETE_FOLDER)

# SCSS folder
EVENTUM_RELATIVE_SCSS_FOLDER = path.join(EVENTUM_RELATIVE_STATIC_FOLDER,
                                         'scss/')
EVENTUM_SCSS_FOLDER = path.join(EVENTUM_BASEDIR,
                                EVENTUM_RELATIVE_SCSS_FOLDER)
# Template folder
EVENTUM_RELATIVE_TEMPLATE_FOLDER = path.join(EVENTUM_RELATIVE_EVENTUM_FOLDER,
                                             'templates/')
EVENTUM_TEMPLATE_FOLDER = path.join(EVENTUM_BASEDIR,
                                    EVENTUM_RELATIVE_TEMPLATE_FOLDER)


######################
# Must be overridden #
######################

EVENTUM_INSTALLED_APP_CLIENT_SECRET_PATH = None
EVENTUM_INSTALLED_APP_CREDENTIALS_PATH = None
EVENTUM_CLIENT_SECRETS_PATH = None
EVENTUM_PRIVATE_CALENDAR_ID = None
EVENTUM_PUBLIC_CALENDAR_ID = None
EVENTUM_SINGLE_EVENT_ROUTE = None
EVENTUM_RECURRING_EVENT_ROUTE = None


def assert_necessary_configs_are_provided(app):
    manditory = [
        'EVENTUM_INSTALLED_APP_CLIENT_SECRET_PATH',
        'EVENTUM_INSTALLED_APP_CREDENTIALS_PATH',
        'EVENTUM_CLIENT_SECRETS_PATH',
        'EVENTUM_PRIVATE_CALENDAR_ID',
        'EVENTUM_PUBLIC_CALENDAR_ID',
        'EVENTUM_SINGLE_EVENT_ROUTE',
        'EVENTUM_RECURRING_EVENT_ROUTE'
    ]

    for key in manditory:
        if app.config.get(key) is None:
            print >> stderr, ('Flask configuration variable {} must be '
                              'set.'.format(key))
            exit(1)


# Will be set elsewhere, do not set directly
EVENTUM_GOOGLE_CLIENT_ID = None
