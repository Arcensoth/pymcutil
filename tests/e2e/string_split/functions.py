from pymcutil.resource.resource_reference.function_reference import FunctionReference


class StringSplitFunctionReference(FunctionReference):
    def __init__(self, s: str):
        super().__init__(s)


string_split = StringSplitFunctionReference
