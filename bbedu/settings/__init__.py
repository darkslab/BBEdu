from split_settings.tools import optional, include
import os
from pathlib import Path

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = Path(__file__).resolve().parent.parent.parent
BASE_DIR_PATH = Path(BASE_DIR).resolve()

# ENV = os.environ.get('DJANGO_ENV') or 'development'

base_settings = [
    'components/common.py',  # standard django settings
    'components/database.py', 
    'components/administration.py', 

    'components/auth.py',  # standard django settings
    'components/captcha.py', 
    'components/internationalization.py', 
    'components/loggers.py',  # standard django settings
    'components/ssl.py', 
    'components/staticfiles.py', 

    # You can even use glob:
    # 'components/*.py'

    # Select the right env:
    # 'environments/{0}.py'.format(ENV),
    # Optionally override some settings:
    # optional('environments/local.py'),
]

# Include settings:
include(*base_settings)