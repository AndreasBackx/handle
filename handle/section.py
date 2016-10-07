from .item import Item


class Section(Item):

    def __init__(self, *args, items=[], **kwargs):
        super().__init__(*args, **kwargs)
        self.items = items
