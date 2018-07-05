import os
import yaml

data_path = os.path.expanduser('~/.foxbot/data')


def load(module_name):
    file_name = f'{module_name}.yml'
    full_path = '/'.join((data_path, file_name))

    if os.path.exists(full_path):
        with open(full_path, 'r') as stream:
            return yaml.load(stream)

    return {}


def save(module_name, data):
    create_data_dir()

    file_name = f'{module_name}.yml'
    full_path = '/'.join((data_path, file_name))

    with open(full_path, 'w') as stream:
        yaml.dump(data, stream)


def create_data_dir():
    if not os.path.exists(data_path):
        os.makedirs(data_path)
