import os

_here = os.path.abspath(os.path.join(os.path.dirname(__file__)))


def apps_dir():
    """Returns the directory where user applications are stored."""
    apps_dir = os.environ.get('AIFY_APPS_DIR', None)
    return apps_dir if apps_dir else '.'


def webui_dir():
    "Returns the directory where webuid resources ared stored."
    return os.path.join(_here, '../webui')
