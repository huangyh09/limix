import os
import sys
import warnings
from .._display import timer_text

PY2 = sys.version_info < (3,)


# TODO: document it
def download(url, dest=None, verbose=True, force=False):
    if PY2:
        from urllib import urlretrieve
    else:
        from urllib.request import urlretrieve

    if dest is None:
        dest = os.getcwd()

    filepath = os.path.join(dest, _filename(url))
    if not force and os.path.exists(filepath):
        warnings.warn("File {} already exists.".format(filepath))
        print("Set `force` to `True` in order to overwrite the existing file.")
        return

    with timer_text("Downloading {}... ".format(url), disable=not verbose):
        urlretrieve(url, filepath)


def _filename(url):
    if PY2:
        from urlparse import urlparse
    else:
        from urllib.parse import urlparse

    a = urlparse(url)
    return os.path.basename(a.path)
