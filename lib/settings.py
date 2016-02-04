"""
settings for MelshoXblog project.
By : Mahmoud Elshobaky (mahmoud.elshobaky@gmail.com).
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
MAIN_DIR  = os.path.dirname(os.path.dirname(__file__))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'mpjn+z)t_w0%nttcu$web9*@*br)^5qzgb@(gy$v%es23rs(%a'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# www.mywebsite.com/[[urls_prefix]]
#url prefix to easily integerate app in other project as
#using url prefix as '/blog' will make the app url in this form
#www.mywebsite.com/blog it should start with '/' and not end with '/'
URLS_PREFIX = ''   # ex. '/blog'


# Template Files path
DEFAULT_TEMPLATE = 'default' # default template folder
TEMPLATES_DIR = os.path.join(MAIN_DIR,"style","templates")
TEMPLATE_DIR = os.path.join(TEMPLATES_DIR, DEFAULT_TEMPLATE)

# Internationalization

LOCALE = 'ar_EG'

TIME_ZONE = 'UTC'

INTERNATIONAL_CFG = {'webapp2_extras.jinja2': {
              'template_path': 'style/templates',
              'environment_args': { 'extensions': ['jinja2.ext.i18n'] }
            }
           }
