from pymcutil.data_tag import DataTag


def data_taggify(obj):
    # Note that we are using local imports due to circular dependencies.
    if isinstance(obj, DataTag):
        return obj
    elif isinstance(obj, bool):
        from pymcutil.data_tag.byte_data_tag import ByteDataTag
        return ByteDataTag(obj)
    elif isinstance(obj, int):
        from pymcutil.data_tag.int_data_tag import IntDataTag
        return IntDataTag(obj)
    elif isinstance(obj, float):
        from pymcutil.data_tag.float_data_tag import FloatDataTag
        return FloatDataTag(obj)
    elif isinstance(obj, str):
        from pymcutil.data_tag.string_data_tag import StringDataTag
        return StringDataTag(obj)
    elif isinstance(obj, list):
        from pymcutil.data_tag.list_data_tag import ListDataTag
        return ListDataTag(obj)
    elif isinstance(obj, dict):
        from pymcutil.data_tag.compound_data_tag import CompoundDataTag
        return CompoundDataTag(obj)
    else:
        raise TypeError(f'Object cannot be converted into a data tag: {obj}')
