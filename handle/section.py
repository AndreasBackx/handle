from .item import Item


class Section(Item):

    def __init__(self, *args, items=None, **kwargs):
        super().__init__(*args, **kwargs)

        if items is None:
            self.items = []

            if self.resource is not None:
                for resource in self.resource.root.resources:
                    if resource.parent == self.resource:
                        self.items.append(
                            Item(resource=resource)
                        )
