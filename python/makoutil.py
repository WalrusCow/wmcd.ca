import os
import functools

from mako.lookup import TemplateLookup

DIR = os.path.dirname(os.path.abspath(__file__))

templateDirs = [os.path.join(DIR, 'templates')]
templateLookup = TemplateLookup(directories=templateDirs)

def serveTemplate(path):
    def deco(func):
        @functools.wraps(func)
        def _serve(*args, **kwargs):
            templ = templateLookup.get_template(path)
            return templ.render(**func(*args, **kwargs))
        return _serve
    return deco
