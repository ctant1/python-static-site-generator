from os import mkdir
from pathlib import Path 


class Site:
    def __init__(self, source, dest):
        self.source=path(source)
        self.dest=path(dest)


    def create_dir(self, path):
        directory = self.dest / relative_to(self.source)
        mkdir(directory, parents=True, exist_ok=True)


    def build(self):
        mkdir(self.dest, parents=True, exist_ok=True)
        for path in self.source.rglob("*"):
            if isdir(path):
                create_dir(self, path)
