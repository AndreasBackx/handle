
class Example:

    def __init__(self, request):
        self.request = request

    def __str__(self):
        return 'Example: {request}'.format(
            request=self.request
        )
