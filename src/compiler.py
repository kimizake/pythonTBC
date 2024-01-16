from .io import fileReader

class Compiler:
    def __init__(self, filePath: str):
        print(fileReader(filePath))
