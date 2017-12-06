from pymcutil.resource.resource_reference.function_resource_reference import FunctionResourceReference


class StringSplitFunctionResourceReference(FunctionResourceReference):
    def __init__(self, message: str, indent: int):
        super().__init__(message, indent)


string_split = StringSplitFunctionResourceReference
