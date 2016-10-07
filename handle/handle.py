import ramlfications


class Handle:

    def __init__(self, source):
        self.source = source
        self.root_node = ramlfications.parse(source)

    def build(self):
        pass
