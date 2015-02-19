# coding=utf-8
from __future__ import unicode_literals

import pytest

from pytons.strings import camelcase_to_underscore, underscore_to_camelcase


@pytest.mark.parametrize("input_,expected", [
    ("CamelcaseToUnderscore", "camelcase_to_underscore"),
    ("PythonCMDForWindows", "python_cmd_for_windows"),
    ("DRYIsCool", "dry_is_cool"),
])
def test_camelcase_to_underscore(input_, expected):
    assert camelcase_to_underscore(input_) == expected


@pytest.mark.parametrize("input_,expected", [
    ("camelcase_to_underscore", "CamelcaseToUnderscore"),
    ("python_cmd_for_windows", "PythonCmdForWindows"),
    ("dry_is_cool", "DryIsCool"),
])
def test_underscore_to_camelcase(input_, expected):
    assert underscore_to_camelcase(input_) == expected
