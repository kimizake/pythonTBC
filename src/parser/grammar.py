import enum
from ..lexer import Tokens

class Grammar(enum.Enum):
    LINE = 1
    STATEMENT = 2
    EXPRLIST = 3
    VARLIST = 4
    EXPR = 5
    BASEXPR = 6
    TERM = 7
    FACTOR = 8
    NUMBER = 9
    RELOP = 10

m = {
    Grammar.LINE: [
        [Tokens.NUMBER, Grammar.STATEMENT, Tokens.NL],
        [Grammar.STATEMENT, Tokens.NL]
    ],
    Grammar.STATEMENT: [
        [Tokens.PRINT, Grammar.EXPRLIST],
        [Tokens.IF, Grammar.EXPR, Grammar.RELOP, Grammar.EXPR, Tokens.THEN, Grammar.STATEMENT],
        [Tokens.GOTO, Grammar.EXPR],
        [Tokens.INPUT, Grammar.VARLIST],
        [Tokens.LET, Grammar.VAR, Tokens.EQ, Grammar.EXPR],
        [Tokens.GOSUB, Grammar.EXPR],
        [Tokens.RETURN],
        [Tokens.CLEAR],
        [Tokens.LIST],
        [Tokens.RUN],
        [Tokens.END],
    ],
    Grammar.EXPRLIST: [
        [Tokens.STRING],
        [Grammar.EXPR],
        [Tokens.STRING, Tokens.COMMA, Grammar.EXPRLIST],
        [Grammar.EXPR, Tokens.COMMA, Grammar.EXPRLIST],
    ],
    Grammar.VARLIST: [
        [Tokens.IDENTIFIER],
        [Tokens.IDENTIFIER, Tokens.COMMA, Grammar.VARLIST]
    ],
    Grammar.BASEXPR: [
        [Grammar.TERM],
        [Grammar.TERM, Tokens.PLUS, Grammar.BASEXPR],
        [Grammar.TERM, Tokens.MINUS, Grammar.BASEXPR],
    ],
    Grammar.EXPR: [
        [Grammar.BASEXPR],
        [Tokens.PLUS, Grammar.TERM],
        [Tokens.MINUS, Grammar.TERM],
        [Tokens.PLUS, Grammar.TERM, Grammar.BASEXPR],
        [Tokens.MINUS, Grammar.TERM, Grammar.BASEXPR],
    ],
    Grammar.TERM: [
        [Grammar.FACTOR],
        [Grammar.FACTOR, Tokens.MULTIPLY, Grammar.TERM],
        [Grammar.FACTOR, Tokens.DIVIDE, Grammar.TERM],
    ],
    Grammar.FACTOR: [
        [Tokens.IDENTIFIER],
        [Tokens.NUMBER],
        [Grammar.EXPR]
    ],
    Grammar.RELOP: [
        [Tokens.EQ],
        [Tokens.LT],
        [Tokens.LEQ],
        [Tokens.GT],
        [Tokens.GEQ],
    ]
}