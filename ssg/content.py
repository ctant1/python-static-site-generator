import re
from typing import Mapping
from yaml import load, FullLoader
from collections.abc import Mapping

class Content(Mapping):
    __delimiter = "^(?:-|\+){3}\s*$"
    __regex = re.compile(__delimiter, re.MULTILINE)

    @classmethod
    def load(cls, string):
        _, fm, content = Content.__regex.split(string, 2)
        load(fm, Loader=FullLoader)
        return(cls(metadata, content))


    def __init__(self, metadata, content):
        self.data = metadata
        self.data["content"] = content


    @property
    def body():
        return(Content.data["content"])


    @property
    def type():
        return (Content.data["type"] if Content.data.has_key("type") else None)
