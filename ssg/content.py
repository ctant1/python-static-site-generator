import re
from typing import Mapping
from yaml import load, FullLoader
from collections.abc import Mapping

class Content(Mapping):
    __delimiter = r"^(?:-|\+){3}\s*$"
    __regex = re.compile(__delimiter, re.MULTILINE)

    @classmethod
    def load(cls, string):
        _, fm, content = cls.__regex.split(string, 2)
        metadata = load(fm, Loader=FullLoader)
        return(cls(self, metadata, content))


    def __init__(self, metadata, content):
        self.data = metadata
        self.data["content"] = content


    @property
    def body(self):
        return(Content.data["content"])


    @property
    def type(self):
        return (Content.data["type"] if Content.data.has_key("type") else None)


    @property
    def setter(self:
        )
