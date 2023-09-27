# Define custom exceptions
class IPDetailsError(Exception):
    pass

class GeolocationError(IPDetailsError):
    pass

class RequestError(IPDetailsError):
    pass