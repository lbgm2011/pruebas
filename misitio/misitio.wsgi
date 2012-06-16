#!/usr/bin/python
import sys
import os
import site
#la ruta al site-packages del virtualenv
BASE_DIR = os.path.join(os.path.dirname(__file__))
site.addsitedir(os.path.join(BASE_DIR,'env','lib','python2.7','site-packages'))
sys.path.append(BASE_DIR)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
