"""
Builder pattern example: API Request Builder
It is used to build complex objects step by step.

Is kind of a creational pattern because it is used to create complex objects.
In this case, the API request is built step by step.
"""


class APIRequestBuilder:
    """ API Request Builder class """
    def __init__(self):
        self.request = {}

    def set_url(self, url):
        self.request["url"] = url
        return self

    def set_method(self, method):
        self.request["method"] = method
        return self

    def set_headers(self, headers):
        self.request["headers"] = headers
        return self

    def set_body(self, body):
        self.request["body"] = body
        return self

    def build(self):
        return self.request


if __name__ == "__main__":
    builder = APIRequestBuilder()
    builder.set_url("https://api.example.com")
    builder.set_method("GET")
    builder.set_headers({"Authorization": "Bearer 1234567890"})
    builder.set_body({"name": "John Doe"})
    print(builder.build())