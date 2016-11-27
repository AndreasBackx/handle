import logging

from ramlfications.models.root import Documentation


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
                    resource.description.html
                ]

        if title is None:
            raise ValueError(
                'A title or resource must be given.'
            )

        if docs is not None:
            for i, doc in enumerate(docs):
                if isinstance(doc, Documentation):
                    docs[i] = doc.content.html

        self.title = title
        self.docs = docs
        self.example = example

    def __str__(self):
        return self.title
