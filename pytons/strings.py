from __future__ import unicode_literals
import re

from six import PY3


camelcase_patt1 = re.compile('(.)([A-Z][a-z]+)')
camelcase_patt2 = re.compile('([a-z0-9])([A-Z])')


def camelcase_to_underscore(name):
    """
    http://stackoverflow.com/questions/1175208/elegant-python-function-to-convert-camelcase-to-camel-case
    :param name:
    :return:
    """
    s1 = camelcase_patt1.sub(r'\1_\2', name)
    return camelcase_patt2.sub(r'\1_\2', s1).lower()


def underscore_to_camelcase(name):
    """
    http://stackoverflow.com/a/4306777/1145954
    :param name:
    :return:
    """
    if not PY3:
        name = name.decode('utf-8')
    return "".join([n.capitalize() for n in name.split('_')])

