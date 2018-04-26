import sys
import os
import django
# 当不运行Django时运行Django的包

sys.path.append('../../VI_test') # 具体路径
os.environ['DJANGO_SETTINGS_MODULE'] = 'VI_test.settings'
django.setup()


def explorer(*args, **kwargs):
    """
    Connect to the database; see connections.Connection.__init__() for
    more information.
    """
    from .resource_explorer import ResourceExplorer
    return ResourceExplorer(*args, **kwargs)