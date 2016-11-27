import logging

from ramlfications.models.root import Documentation
from markdown import markdown


class Item:

    def __init__(self, resource=None, title=None, docs=None, example=None):
        logging.debug('resource')
        logging.debug(resource)

        self.resource = resource

        if resource is not None:
            if title is None:
                title = resource.display_name
            if docs is None:
                docs = [
                    markdown(resource.description.raw.strip())
                ]

        if title is None:
            raise ValueError(
                'A title or resource must be given.'
            )

        for i, doc in enumerate(docs):
            if isinstance(doc, Documentation):
                docs[i] = markdown(doc.content.raw.strip())

        self.title = title
        self.docs = docs
        self.example = example

    def __str__(self):
        return self.title
