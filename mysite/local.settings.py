import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SECRET_KEY = 'django-insecure-m8hwmju52%n%qo=_a*%fjc#x#8#p4gf#@q4z182cfa3fz!3u*#'

#settings.pyからそのままコピー
DATABASES = {
 'default': {
 'ENGINE': 'django.db.backends.sqlite3',
 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
 }
}
DEBUG = True

