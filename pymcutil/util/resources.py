import os
from typing import Iterable

from pymcutil.constants.resources import *


def get_resource_name(namespace: str, path_components: Iterable) -> str:
    return '{}:{}'.format(namespace, '/'.join(path_components))


def get_resource_path(
        root: str, resource_dir: str, namespace: str, resource_subdir: str, resource_ext: str,
        path_components: Iterable) -> str:
    return '{}.{}'.format(os.sep.join((root, resource_dir, namespace, resource_subdir, *path_components)), resource_ext)


def get_advancement_path(root: str, namespace: str, path_components: Iterable) -> str:
    return get_resource_path(
        root=root, resource_dir=DATA_DIRECTORY, namespace=namespace, resource_subdir=ADVANCEMENTS_DIRECTORY,
        resource_ext=ADVANCEMENTS_EXTENSION, path_components=path_components)


def get_function_path(root: str, namespace: str, path_components: Iterable) -> str:
    return get_resource_path(
        root=root, resource_dir=DATA_DIRECTORY, namespace=namespace, resource_subdir=FUNCTIONS_DIRECTORY,
        resource_ext=FUNCTIONS_EXTENSION, path_components=path_components)


def get_loot_table_path(root: str, namespace: str, path_components: Iterable) -> str:
    return get_resource_path(
        root=root, resource_dir=DATA_DIRECTORY, namespace=namespace, resource_subdir=LOOT_TABLES_DIRECTORY,
        resource_ext=LOOT_TABLES_EXTENSION, path_components=path_components)
