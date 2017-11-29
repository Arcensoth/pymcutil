import os
from typing import Iterable

from pymcutil.constants.resources import *


def get_resource_trail(*components) -> str:
    return '/'.join(str(c) for c in components if c is not None)


def get_resource_name(namespace: str, components: Iterable) -> str:
    return '{}:{}'.format(namespace, get_resource_trail(*components))


def get_resource_path(
        root: str, resource_dir: str, namespace: str, resource_subdir: str, resource_ext: str,
        components: Iterable) -> str:
    return '{}.{}'.format(os.path.join(root, resource_dir, namespace, resource_subdir, *components), resource_ext)


def get_advancement_path(root: str, namespace: str, components: Iterable) -> str:
    return get_resource_path(
        root=root, resource_dir=DATA_DIRECTORY, namespace=namespace, resource_subdir=ADVANCEMENTS_DIRECTORY,
        resource_ext=ADVANCEMENTS_EXTENSION, components=components)


def get_function_path(root: str, namespace: str, components: Iterable) -> str:
    return get_resource_path(
        root=root, resource_dir=DATA_DIRECTORY, namespace=namespace, resource_subdir=FUNCTIONS_DIRECTORY,
        resource_ext=FUNCTIONS_EXTENSION, components=components)


def get_loot_table_path(root: str, namespace: str, components: Iterable) -> str:
    return get_resource_path(
        root=root, resource_dir=DATA_DIRECTORY, namespace=namespace, resource_subdir=LOOT_TABLES_DIRECTORY,
        resource_ext=LOOT_TABLES_EXTENSION, components=components)
