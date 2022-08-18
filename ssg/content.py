import re
from typing import Mapping
from yaml import load, FullLoader
from collections.abc import Mapping

class Content(Mapping):
    __delimiter = "^(?:-|\+){3}\s*$"
    __regex = re.compile(__delimiter, re.MULTILINE)

    def load(self, cls, string):
        _, fm, content = self.__regex.split(string, 2)
        load(fm, Loader=FullLoader)
        cls(metadata, content)


    def __init__(self, metadata, content):
        self.data = metadata
        self.data["content"] = content