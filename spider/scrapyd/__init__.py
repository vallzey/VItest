def get_scrapyd_request(*args, **kwargs):
    """
    Connect to the database; see connections.Connection.__init__() for
    more information.
    """
    from .scrapyd_request import Requests
    return Requests(*args, **kwargs)


def get_http(*args, **kwargs):
    """
    Connect to the database; see connections.Connection.__init__() for
    more information.
    """
    from .http import Http
    return Http(*args, **kwargs)