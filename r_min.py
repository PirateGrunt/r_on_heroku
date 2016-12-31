import sys
import os

from django.conf import settings

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

settings.configure(
    DEBUG=True,
    SECRET_KEY='thisisthesecretkey',
    ROOT_URLCONF=__name__,
    MIDDLEWARE_CLASSES=(
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ),
    ALLOWED_HOSTS = [ 'r-on-heroku.herokuapp.com',
                      'localhost'],
    BASE_DIR = BASE_DIR,
    STATIC_URL = '/static/',
    STATIC_ROOT = os.path.join(BASE_DIR, 'static'),
    TEMPLATES = [{
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [ os.path.join(BASE_DIR, 'templates'), ],
        }],
    INSTALLED_APPS = [ 'django.contrib.staticfiles', ],
)

from django.conf.urls import url
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, loader

import subprocess

# import rpy2.robjects as robjects

def index(request):
    # subprocess.call("R CMD BATCH ./myPlot.R", shell=True)
    subprocess.call("fakechroot fakeroot chroot /app/.root /usr/bin/R CMD BATCH ./myPlot.R", shell=True)
    # robjects.r('source("./myPlot.R"')

    return render(request, 'index.html')

    # return HttpResponse(robjects.r('getwd()'))

urlpatterns = (
    url(r'^$', index),
)

if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
