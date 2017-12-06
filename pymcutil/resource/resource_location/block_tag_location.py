from pymcutil.resource.resource_location.tag_location import TagLocation


class BlockTagLocation(TagLocation):
    def __init__(self, namespace: str, trail: str):
        super().__init__(namespace=namespace, trail='/'.join(('blocks', trail)))
