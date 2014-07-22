"""
A dummy kalite_staticfiles for the central server so that the templates we share
between KA Lite and the Hub don't break on central. 
"""

from django.conf import settings
from django.template import Library
if 'django.contrib.staticfiles' in settings.INSTALLED_APPS:
    from django.contrib.staticfiles.templatetags.staticfiles import static as static_lib
else:
    from django.templatetags.static import static as static_lib

register = Library()

@register.simple_tag
def static(path):
    return static_lib(path)