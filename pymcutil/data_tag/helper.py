from pymcutil.data_tag import DataTag


def data_taggify(obj):
    # Note that we are using local imports due to circular dependencies.
    if isinstance(obj, DataTag):
        return obj
    elif isinstance(obj, dict):
        from pymcutil.data_tag.compound_data_tag import CompoundDataTag
        return CompoundDataTag(obj)
    elif isinstance(obj, bool):
        from pymcutil.data_tag.byte_data_tag import ByteDataTag
        return ByteDataTag(obj)
    elif isinstance(obj, str):
        from pymcutil.data_tag.string_data_tag import StringDataTag
        return StringDataTag(obj)
    else:
        raise TypeError(f'Object cannot be converted into a data tag: {obj}')
