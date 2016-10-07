
class Request:

    def __init__(self, path, method):
        self.path = path
        self.method = method

    def __str__(self):
        return '{method}: {path}'.format(
            method=self.method,
            path=self.path
        )
