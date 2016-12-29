from collections import defaultdict

from .item import Item


class Section(Item):

    def __init__(self, resource=None, *args, items=None, **kwargs):
        resources = [] if resource is None else [resource]
        super().__init__(*args, resources=resources, **kwargs)

        if items is None:
            self.items = []
            child_resources = []

            if self.resource is not None:
                child_resources = [
                    resource for resource in self.resource.root.resources
                    if resource.parent == self.resource
                ]

            resources_by_path = defaultdict(list)
            for resource in child_resources:
                resources_by_path[resource.path].append(resource)

            for path, resources in resources_by_path.items():
                self.items.append(
                    Item(resources=resources)
                )
