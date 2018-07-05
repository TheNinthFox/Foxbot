import data as dnd_data
from dnd import utils as dnd_utils

doodle_data = dnd_data.load(__name__)


def doodle(args):
    return dnd_utils.get_module_function(__name__, args, default_function='__get')


def __get(args):
    doodle_url = _get_data('url')
    return f"Bark bork! Das Doodle findest du hier: {doodle_url}"


def __set(args):
    if len(args) <= 0:
        return "Bark bork! Keine neue Doodle URL angegeben!"

    _set_data('url', args[0], True)

    return f"Bark bork! Neue Doodle URL gesetzt: {args[0]}"


def _set_data(key, data, save=False):
    global doodle_data
    doodle_data[key] = data

    if save:
        dnd_data.save(__name__, doodle_data)


def _get_data(key):
    global doodle_data
    if key in doodle_data:
        return doodle_data[key]

    return "Keine Daten gesetzt!"
