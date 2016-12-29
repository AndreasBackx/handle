from ramlfications.models.root import Documentation


class Item:

    def __init__(self, resources=[]):
        self.resources = resources
        self.resource = None

        if len(resources) > 0:
            self.resource = resources[0]

        title = getattr(self.resource, 'title', None)
        title = title if title is not None else getattr(self.resource, 'display_name', '')

        if title is None:
            raise ValueError(
                'A title or resource must be given.'
            )

        documentation = getattr(self.resource, 'documentation', None)
        if documentation is None:
            documentation = [resource.description.html for resource in resources if hasattr(resource, 'description')]
        for i, doc in enumerate(documentation):
            if isinstance(doc, Documentation):
                documentation[i] = doc.content.html

        self.title = title
        self.documentation = documentation

    def __str__(self):
        return self.title
