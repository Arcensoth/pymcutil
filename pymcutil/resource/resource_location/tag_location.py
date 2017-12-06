from pymcutil.resource.resource_location.standard_resource_location import StandardResourceLocation


class TagLocation(StandardResourceLocation):
    def __init__(self, namespace: str, trail: str):
        super().__init__(namespace=namespace, trail=trail, subfolder='tags')
