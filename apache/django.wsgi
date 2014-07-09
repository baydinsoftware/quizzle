import os
import sys
 
path = '/srv/project/quizzle'
if path not in sys.path:
    sys.path.insert(0, '/srv/project/quizzle')
 
os.environ['DJANGO_SETTINGS_MODULE'] = 'quizzle.settings'
 
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

