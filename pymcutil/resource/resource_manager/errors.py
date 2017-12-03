class ResourceManagerError(Exception):
    pass


class ReferenceNotRegisteredError(ResourceManagerError):
    pass


class ResourceDidNotGenerateError(ResourceManagerError):
    pass
