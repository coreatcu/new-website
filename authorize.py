import argparse
from oauth2client.file import Storage
from oauth2client.client import flow_from_clientsecrets
from oauth2client.tools import run_flow
from oauth2client import tools

from config.flask_config import config

parser = argparse.ArgumentParser(parents=[tools.argparser])
FLAGS = parser.parse_args()
SCOPE = 'https://www.googleapis.com/auth/calendar'

FLOW = flow_from_clientsecrets(
    config['EVENTUM_INSTALLED_APP_CLIENT_SECRET_PATH'],
    scope=SCOPE)

# Save the credentials file here for use by the app
storage = Storage(config['EVENTUM_INSTALLED_APP_CREDENTIALS_PATH'])
run_flow(FLOW, storage, FLAGS)
