def get_csdn_exploer(*args, **kwargs):
    """
    Connect to the database; see connections.Connection.__init__() for
    more information.
    """
    from .csdn import CsdnExplorer
    return CsdnExplorer(*args, **kwargs)


def get_csdn_saver(*args, **kwargs):
    """
    Connect to the database; see connections.Connection.__init__() for
    more information.
    """
    from .csdn import PostSave
    return PostSave(*args, **kwargs)