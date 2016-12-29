
class Request:

    def __init__(self, path, method):
        self.path = path

        if method is None:
            method = 'GET'
        else:
            method = method.upper()

        self.method = method

    def __str__(self):
        return '{method}: {path}'.format(
            method=self.method,
            path=self.path
        )
