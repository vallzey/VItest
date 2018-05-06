import sys
import os
import django
# 当不运行Django时运行Django的包

sys.path.append('/Users/vallzey/Projects/PycharmProjects/DataMining/VI_test') # 具体路径
os.environ['DJANGO_SETTINGS_MODULE'] = 'VI_test.settings'
django.setup()