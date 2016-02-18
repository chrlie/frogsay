import contextlib
import os
import random

try:
    # OS X apparently lacks gdbm and will fail unless we monkey-patch it
    import anydbm
    anydbm.__defaultmod = __import__('dumbdbm')
except:
    pass

import shelve

from RIBBIT.client import RIBBITClient


@contextlib.contextmanager
def open_client(cache_file):
    """\
    Open and return a FROG tips client backed by a cache.
    """
    with Cache(cache_file) as cache:
        yield Client(cache)


class Cache(object):
    """\
    This is a more Pythonic wrapper around shelve's open/close functions.
    """
    def __init__(self, cache_file):
        self._cache_file = cache_file
        self._cache = None

    def __enter__(self):
        # Create the parent directories if they don't exist
        try:
            parent = os.path.dirname(self._cache_file)
            os.makedirs(parent)
        except OSError:
            pass

        self._cache = shelve.open(self._cache_file)

        return self._cache

    def __exit__(self, *ex_info):
        self._cache.close()


class Client(object):
    """\
    This client wraps RIBBIT's FROG tips client and returns FROG tips either
    from a cache or from the client when the cache is empty.
    """

    def __init__(self, cache):
        self._client = RIBBITClient()
        self._cache = cache

    @property
    def should_refresh(self):
        return len(self._cache) == 0

    def frog_tip(self):
        """\
        Return a single FROG tip.
        """
        cache = self._cache
        client = self._client

        if self.should_refresh:
            tips = client.croak()
            for number, tip in tips.items():
                cache[str(number)] = tip

        choice = random.choice(list(cache.keys()))
        return cache.pop(choice)
