from pymcutil.resource.resource_reference.function_reference import FunctionReference


class StringSplitFunctionReference(FunctionReference):
    def __init__(self, message: str, indent: int):
        super().__init__(message, indent)


string_split = StringSplitFunctionReference
