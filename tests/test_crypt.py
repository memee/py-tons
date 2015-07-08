# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import pytest

from pytons import crypt


@pytest.mark.parametrize('uuid_str', [
    '00000000-0000-4000-a000-000000000000',
    'd71fab67-680f-464c-ae41-3f526e249c0d',
    'd71fab67680f464cae413f526e249c0d'
])
def test_validating_uid4(uuid_str):
    """Test it validates valid uuid4"""

    assert crypt.validate_uuid4(uuid_str)


@pytest.mark.parametrize('uuid_str', [
    '00000000-0000-4000-f000-000000000000',
    '00000000-0000-b000-a000-000000000000',
    '00000000-0000-4ghi-a000-000000000000',
])
def test_invalidating_uid4(uuid_str):
    """Test it doesn't validate invalid uuid4."""

    assert not crypt.validate_uuid4(uuid_str)
