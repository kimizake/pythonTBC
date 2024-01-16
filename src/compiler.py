from .io import fileReader
from .lexer import LexicalAnalyser

class Compiler:
    def __init__(self, filePath: str):
        self.fileContents = fileReader(filePath)
        self.lexer = LexicalAnalyser()

    def compile(self):
        tokens = self.lexer.analyse(self.fileContents)
        print(tokens)
