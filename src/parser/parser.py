from .ast import AST
from .grammar import Grammar, BNF
from ..lexer import LexicalAnalyser
from typing import Tuple

class Parser:
    def __init__(self, data: str, lexer: LexicalAnalyser):
        self.stream = list(lexer.analyse(data))
        self.currentScope = [Grammar.PROGRAM]
        self.ctx = []

    def generateTree(self) -> AST:
        truth, ptr, tree = self.parse(Grammar.PROGRAM, 0)
        if truth and ptr == len(self.stream):
            tree.flatten()
            return tree
        raise SyntaxError()

    def parse(self, context: Grammar, ptr) -> Tuple[bool, int, AST | None]:
        # See what patterns the current token matches
        for pattern in BNF[context]:
            root = AST(context)
            offset = 0
            for part in pattern:
                # Sanity check
                if ptr + offset >= len(self.stream):
                    break

                token, lexeme = self.stream[ptr + offset]

                if type(part) == Grammar:
                    # Try to keep parsing with the current pattern
                    truth, subOffset, child = self.parse(part, ptr + offset)
                    if truth: 
                        root.addChild(child)
                        offset += subOffset
                    else: break
                elif part == token:
                    # Token matches this pattern
                    root.addChild(
                        AST(token, lexeme)
                    )
                    offset += 1
                # token wasn't expected for this pattern, try next
                else: break
            else:
                # Full pattern was matched
                return True, offset, root
        # No matching pattern found
        return False, 0, None
