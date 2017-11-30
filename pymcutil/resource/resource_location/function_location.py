from pymcutil.resource.resource_location.standard_function_location import StandardResourceLocation


class FunctionLocation(StandardResourceLocation):
    def __init__(self, namespace: str, trail: str):
        super().__init__(namespace=namespace, trail=trail, subfolder='functions', extension='mcfunction')
