import re


class Handle:
    def __getattr__(self, regular, content):
        attr = re.compile(regular).findall(content)
        if len(attr) > 0:
            return attr[0]
        else:
            return ""
