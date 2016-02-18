import tempfile

from nose.tools import raises

from frogsay.client import Cache


def test_cache_opens_with_a_contextmanager_like_guido_intended():
    key = '1'
    value = 'DO NOT CACHE FROG.'

    with tempfile.NamedTemporaryFile() as file:
        with Cache(file.name) as cache:
            cache[key] = value

        with Cache(file.name) as cache:
            assert cache[key] == value


@raises(KeyError)
def test_cache_can_delete():
    key = '1'
    value = 'DO NOT DELETE FROG.'

    with tempfile.NamedTemporaryFile() as file:
        with Cache(file.name) as cache:
            del cache[key]

        with Cache(file.name) as cache:
            cache[key]
