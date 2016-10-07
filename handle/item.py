
class Item:

    def __init__(self, resource_type=None, title=None, docs=None, example=None):
        print('resource_type', resource_type)
        if resource_type is not None:
            if title is None:
                title = resource_type.name
            if docs is None:
                docs = [resource_type.description]

        if title is None:
            raise ValueError(
                'A title or resource_type must be given.'
            )

        self.title = title
        self.docs = docs
        self.example = example

    def __str__(self):
        return self.title
