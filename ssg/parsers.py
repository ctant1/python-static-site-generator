from typing import List 
from pathlib import Path 
import shutil

class Parser:
    extensions = List[str]

    def valid_extension(extension):
        if extension in self.extensions:
            return True
        else:
            return False


    def parse(Path: path, source, dest):
        raise NotImplementedError


    def read(path):
        with open(path) as file:
            return(file.read())


    def write (path, dest, content, ext="html"):
        full_path = self.dest / with_suffix(ext).name
        with open(full_path, 'w') as file:
            file.write(content)


    def copy(path, source, dest):
        shutil.copy2(path, dest / source)


class ResourceParser(Parser):
        extensions = [".jpg", ".png", ".gif", ".css", ".html"]
        def parse(Path: path, source, dest):
            self.copy(path, source, dest)