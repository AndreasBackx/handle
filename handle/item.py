import logging

from ramlfications.models.root import Documentation

from .example import Example
from .request import Request


class Item:

    def __init__(self, resources=[], title=None, docs=None):
        logging.debug('resources')
        logging.debug(resources)

        self.resources = resources
        self.resource = None

        if len(resources) > 0:
            self.resource = resources[0]

        if title is None:
            title = self.resource.display_name

        if title is None:
            raise ValueError(
                'A title or resource must be given.'
            )

        if docs is None:
            docs = [resource.description.html for resource in resources]
        for i, doc in enumerate(docs):
            if isinstance(doc, Documentation):
                docs[i] = doc.content.html

        self.title = title
        self.docs = docs
        if self.resource is not None:
            self.example = Example(
                Request(
                    self.resource.path,
                    self.resource.method
                )
            )

    def __str__(self):
        return self.title
