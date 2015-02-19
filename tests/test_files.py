# coding=utf-8
from __future__ import unicode_literals
import pytest
from six import StringIO, PY3
from pytons import files


py2 = pytest.mark.skipif(PY3, reason="requires python2.*")


def prepare_file_object(contents):
    if not PY3:
        contents = contents.encode('utf-8')
    fobj = \
        StringIO(contents)
    return fobj


@py2
def test_reading_unicode_csv():
    contents = 'id,name,address\n1,Łukasz Łękotka,Łódź'
    csvfile = prepare_file_object(contents)
    reader = files.UnicodeReader(csvfile)

    rows = [row for row in reader]

    assert rows[1][1] == 'Łukasz Łękotka'
    assert rows[1][2] == 'Łódź'


@py2
def test_writing_unicode_csv():
    csvfile = prepare_file_object('')

    writer = files.UnicodeWriter(csvfile)

    writer.writerow(['id', 'name', 'address'])
    writer.writerow(['1', 'Łukasz Łękotka', 'Łódź'])

    csvfile.seek(0)

    assert 'Łukasz Łękotka'.encode('utf-8') in csvfile.read()
