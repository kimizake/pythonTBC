from .grammar import Grammar
from ..lexer import Tokens
from typing import List


class AST:
    def __init__(self, ctx, val=None):
        self.children: List[AST] = []
        self.ctx = ctx
        self.val = val

    def addChild(self, child):
        self.children.append(child)

    def flatten(self) -> List:
        self.children = [_child for child in self.children for _child in child.flatten()]
        if self.ctx in {Grammar.LINELIST, Grammar.BASEXPR, Grammar.TERM, Grammar.FACTOR, Tokens.NL}:
            return self.children
        return [self]

    def __repr__(self):
        return "AST node: " + repr(self.ctx)
    
    def __str__(self, markerStr="+- ", levelMarkers=[]):
        emptyStr = " "*len(markerStr)
        connectionStr = "|" + emptyStr[:-1]
        level = len(levelMarkers)
        mapper = lambda draw: connectionStr if draw else emptyStr
        markers = "".join(map(mapper, levelMarkers[:-1]))
        markers += markerStr if level > 0 else ""
        out = f"{markers}{self.ctx}{'' if self.val == None else f': {self.val}'}"
        for i, child in enumerate(self.children):
            isLast = i == len(self.children) - 1
            out += "\n" + child.__str__(markerStr, [*levelMarkers, not isLast])
        return out
