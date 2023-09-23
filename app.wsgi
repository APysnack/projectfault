import sys
import os

FLASK_APP_PATH = '/var/www/html/ProjectFault'
VENV_PATH = '/home/ec2-user/projectFaultVenv'

activate_this = os.path.join(VENV_PATH, 'bin', 'activate')
exec(open(activate_this).read(), dict(__file__=activate_this))

sys.path.insert(0, FLASK_APP_PATH)

from app import app as application
