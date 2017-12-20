from typing import Callable, Optional


def nullable(obj: object, converter: Callable):
    return converter(obj) if obj is not None else None


def nullable_float(obj: object) -> Optional[float]:
    return nullable(obj, float)


def nullable_int(obj: object) -> Optional[int]:
    return nullable(obj, int)


def nullable_bool(obj: object) -> Optional[bool]:
    return nullable(obj, bool)


def nullable_str(obj: object) -> Optional[str]:
    return nullable(obj, str)


def nullable_tuple(obj: object, converter: Callable) -> Optional[tuple]:
    t = nullable(obj, tuple)
    return None if t is None else tuple(converter(item) for item in t)
