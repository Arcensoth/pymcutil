from pymcutil.resource.resource_location.tag_location import TagLocation


class ItemTagLocation(TagLocation):
    def __init__(self, namespace: str, trail: str):
        super().__init__(namespace=namespace, trail='/'.join(('items', trail)))
