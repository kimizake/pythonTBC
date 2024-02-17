from .io import fileReader
from .lexer import LexicalAnalyser
from .parser import Parser

class Compiler:
    def __init__(self, filePath: str):
        self.fileContents = fileReader(filePath)
        self.lexer = LexicalAnalyser()
        self.parser = Parser(self.fileContents, self.lexer)

    def compile(self):
        ast =self.parser.generateTree()
        print(ast)
